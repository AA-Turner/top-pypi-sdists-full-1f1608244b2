"""
Submission models hold student responses to problems, scores, and a history of
those scores. It is intended to be a general purpose store that is usable by
different problem types, and is therefore ignorant of ORA workflow.

NOTE: We've switched to migrations, so if you make any edits to this file, you
need to then generate a matching migration for it using:

    ./manage.py makemigrations submissions
"""

import functools
import logging
import os
from datetime import timedelta
from uuid import uuid4

from django.conf import settings
from django.contrib import auth
from django.core.files.storage import default_storage
from django.db import DatabaseError, models, transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import Signal, receiver
from django.utils.module_loading import import_string
from django.utils.timezone import now
from jsonfield import JSONField
from model_utils.models import TimeStampedModel

from submissions.errors import DuplicateTeamSubmissionsError, TeamSubmissionInternalError, TeamSubmissionNotFoundError

logger = logging.getLogger(__name__)
User = auth.get_user_model()

# Signal to inform listeners that a score has been changed
score_set = Signal()

# Signal to inform listeners that a score has been reset
score_reset = Signal()


class AnonymizedUserIDField(models.CharField):
    """
    Field for storing anonymized user ids.
    """
    description = "The anonymized User ID that the XBlock sees"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255
        kwargs['db_index'] = True
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        del kwargs["db_index"]
        return name, path, args, kwargs


class StudentItem(models.Model):
    """
    Represents a single item for a single course for a single user.

    This is typically an XBlock problem, but could be something more generic
    like class participation.

    .. no_pii:
    """
    # The anonymized Student ID that the XBlock sees, not their real ID.
    student_id = AnonymizedUserIDField()

    # Not sure yet whether these are legacy course_ids or new course_ids
    course_id = models.CharField(max_length=255, blank=False, db_index=True)

    # Version independent, course-local content identifier, i.e. the problem
    # This is the block_id for XBlock items.
    item_id = models.CharField(max_length=255, blank=False, db_index=True)

    # What kind of problem is this? The XBlock tag if it's an XBlock
    item_type = models.CharField(max_length=100)

    def __repr__(self):
        return repr(self.student_item_dict)

    @property
    def student_item_dict(self):
        return {
            "student_id": self.student_id,
            "course_id": self.course_id,
            "item_id": self.item_id,
            "item_type": self.item_type,
        }

    def __str__(self):
        return (
            f"({self.student_id}, {self.course_id}, "
            f"{self.item_type}, {self.item_id})"
        )

    class Meta:
        app_label = "submissions"
        unique_together = (
            # For integrity reasons, and looking up all of a student's items
            ("course_id", "student_id", "item_id"),
        )


# Has this submission been soft-deleted? This allows instructors to reset student
# state on an item, while preserving the previous value for potential analytics use.
DELETED = 'D'
ACTIVE = 'A'
STATUS_CHOICES = (
    (DELETED, 'Deleted'),
    (ACTIVE, 'Active'),
)


class TeamSubmission(TimeStampedModel):
    """
    A single response by a team for a given problem (ORA2) in a given course.
    An abstraction layer over Submission used to for teams. Since we create a submission record for every team member,
    there is a need to have a single point to connect the team to the workflows.
    TeamSubmission is a 1 to many with Submission

    .. no_pii:
    """

    uuid = models.UUIDField(db_index=True, default=uuid4, null=False)

    # Which attempt is this? Consecutive Submissions do not necessarily have
    # increasing attempt_number entries -- e.g. re-scoring a buggy problem.
    attempt_number = models.PositiveIntegerField()

    # submitted_at is separate from created_at to support re-scoring and other
    # processes that might create Submission objects for past user actions.
    submitted_at = models.DateTimeField(default=now, db_index=True)

    course_id = models.CharField(max_length=255, null=False, db_index=True)

    item_id = models.CharField(max_length=255, null=False, db_index=True)

    team_id = models.CharField(max_length=255, null=False, db_index=True)

    submitted_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=ACTIVE)

    # Override the default Manager with our custom one to filter out soft-deleted items
    class SoftDeletedManager(models.Manager):
        def get_queryset(self):
            return super(TeamSubmission.SoftDeletedManager, self).get_queryset().exclude(status=DELETED)

    objects = SoftDeletedManager()
    _objects = models.Manager()  # Don't use this unless you know and can explain why objects doesn't work for you

    @staticmethod
    def get_cache_key(sub_uuid):
        return f"submissions.team_submission.{sub_uuid}"

    @staticmethod
    def get_team_submission_by_uuid(team_submission_uuid):
        """
        Given a uuid, return the matching team submission.

        Raises:
            - TeamSubmissionNotFoundError if there is no matching team submission
            - TeamSubmissionInternalError if there is some other error looking up the team submission.
        """
        try:
            return TeamSubmission.objects.prefetch_related('submissions').get(uuid=team_submission_uuid)
        except TeamSubmission.DoesNotExist as error:
            logger.error("Team Submission %s not found.", team_submission_uuid)
            raise TeamSubmissionNotFoundError(
                f"No team submission matching uuid {team_submission_uuid}"
            ) from error
        except Exception as exc:
            err_msg = (
                f"Attempt to get team submission for uuid {team_submission_uuid} "
                f"caused error: {exc}"
            )
            logger.error(err_msg)
            raise TeamSubmissionInternalError(err_msg) from exc

    @staticmethod
    def get_team_submission_by_course_item_team(course_id, item_id, team_id):
        """
        Given a course_id, item_id, and team_id, return team submission for the team assignment

        Raises:
            - TeamSubmissionNotFoundError if there is no matching team submission
            - TeamSubmissionInternalError if there is some other error looking up the team submission.

        """
        model_query_params = {"course_id": course_id, "item_id": item_id, "team_id": team_id}
        query_params_string = "course_id={course_id} item_id={item_id} team_id={team_id}".format(**model_query_params)
        try:
            # In the equivalent non-teams api call, we're filtering on student item and then getting first(),
            # which will get us the most recent active submission due to the sort order of the model.
            # However, for this model, we have a uniqueness constraint (non-db, as a signal handler)
            # that means we can only ever have one submission per team per assignment. I don't fully understand
            # the logic behind the non-teams api, but this shouldn't have to do that filter.
            team_submission = TeamSubmission.objects.prefetch_related(
                'submissions'
            ).get(
                **model_query_params
            )
        except TeamSubmission.DoesNotExist as error:
            logger.error("Team submission for %s not found.", query_params_string)
            raise TeamSubmissionNotFoundError(
                f"No team submission matching {query_params_string}"
            ) from error
        except Exception as exc:
            err_msg = (
                f"Attempt to get team submission for {query_params_string} "
                f"caused error: {exc}"
            )
            logger.error(err_msg)
            raise TeamSubmissionInternalError(err_msg) from exc
        return team_submission

    @staticmethod
    def get_team_submission_by_student_item(student_item):
        """
        Return the team submission that has an individual submission tied to the given StudentItem

        Raises:
            - TeamSubmissionNotFoundError if there is no matching team submission
            - TeamSubmissionInternalError if there is some other error looking up the team submission.

        """
        try:
            return TeamSubmission.objects.prefetch_related('submissions').get(submissions__student_item=student_item)
        except TeamSubmission.DoesNotExist as error:
            logger.error("Team submission for %s not found.", student_item)
            raise TeamSubmissionNotFoundError(
                f"No team submission matching {student_item}"
            ) from error
        except Exception as exc:
            err_msg = (
                f"Attempt to get team submission for {student_item} "
                f"caused error: {exc}"
            )
            logger.error(err_msg)
            raise TeamSubmissionInternalError(err_msg) from exc

    @staticmethod
    def get_all_team_submissions_for_course_item(course_id, item_id):
        """
        Given a course_id and item_id, return all team submissions for the team assignment in the course

        Raises:
            - TeamSubmissionInternalError if there is some error looking up the team submissions.
        """
        try:
            return TeamSubmission.objects.prefetch_related('submissions').filter(
                course_id=course_id,
                item_id=item_id,
            ).all()
        except Exception as exc:
            query_params_string = f"course_id={course_id} item_id={item_id}"
            err_msg = (
                f"Attempt to get team submissions for {query_params_string} "
                f"caused error: {exc}"
            )
            logger.error(err_msg)
            raise TeamSubmissionInternalError(err_msg) from exc

    def __repr__(self):
        return repr({
            "uuid": self.uuid,
            "submitted_by": self.submitted_by,
            "attempt_number": self.attempt_number,
            "submitted_at": self.submitted_at,
            "created": self.created,
            "modified": self.modified,
        })

    def __str__(self):
        return f"Team Submission {self.uuid}"

    class Meta:
        app_label = "submissions"
        ordering = ["-submitted_at", "-id"]


@receiver(pre_save, sender=TeamSubmission)
def validate_only_one_submission_per_team(sender, **kwargs):  # pylint:disable=unused-argument
    """
    Ensures that there is only one active submission per team.
    """
    ts = kwargs['instance']
    if TeamSubmission.objects.filter(
            course_id=ts.course_id,
            item_id=ts.item_id,
            team_id=ts.team_id,
            status='A'
    ).exclude(id=ts.id).exists():
        raise DuplicateTeamSubmissionsError('Can only have one submission per team.')


class Submission(models.Model):
    """
    A single response by a student for a given problem in a given course.

    A student may have multiple submissions for the same problem. Submissions
    should never be mutated. If the student makes another Submission, or if we
    have to make corrective Submissions to fix bugs, those should be new
    objects. We want to keep Submissions immutable both for audit purposes, and
    because it makes caching trivial.

    .. no_pii:
    """
    MAXSIZE = 1024*100  # 100KB

    uuid = models.UUIDField(db_index=True, default=uuid4)

    student_item = models.ForeignKey(StudentItem, on_delete=models.CASCADE)

    # Which attempt is this? Consecutive Submissions do not necessarily have
    # increasing attempt_number entries -- e.g. re-scoring a buggy problem.
    attempt_number = models.PositiveIntegerField()

    # submitted_at is separate from created_at to support re-scoring and other
    # processes that might create Submission objects for past user actions.
    submitted_at = models.DateTimeField(default=now, db_index=True)

    # When this row was created.
    created_at = models.DateTimeField(editable=False, default=now, db_index=True)

    # The answer (JSON-serialized)
    # NOTE: previously, this field was a TextField named `raw_answer`.
    # Since JSONField is a subclass of TextField, we can use it as a drop-in
    # replacement for TextField that performs JSON serialization/deserialization.
    # For backwards compatibility, we override the default database column
    # name so it continues to use `raw_answer`.
    answer = JSONField(blank=True, dump_kwargs={'ensure_ascii': True}, db_column="raw_answer")

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=ACTIVE)

    team_submission = models.ForeignKey(
        TeamSubmission,
        related_name='submissions',
        null=True,
        blank=True,
        db_index=True,
        on_delete=models.SET_NULL
    )

    # Override the default Manager with our custom one to filter out soft-deleted items
    class SoftDeletedManager(models.Manager):
        def get_queryset(self):
            return super(Submission.SoftDeletedManager, self).get_queryset().exclude(status=DELETED)

    objects = SoftDeletedManager()
    _objects = models.Manager()  # Don't use this unless you know and can explain why objects doesn't work for you

    @staticmethod
    def get_cache_key(sub_uuid):
        return f"submissions.submission.{sub_uuid}"

    def __repr__(self):
        return repr({
            "uuid": self.uuid,
            "student_item": self.student_item,
            "attempt_number": self.attempt_number,
            "submitted_at": self.submitted_at,
            "created_at": self.created_at,
            "answer": self.answer,
        })

    def __str__(self):
        return f"Submission {self.uuid}"

    class Meta:
        app_label = "submissions"
        ordering = ["-submitted_at", "-id"]


class Score(models.Model):
    """
    What the user scored for a given StudentItem at a given time.

    Note that while a Score *can* be tied to a Submission, it doesn't *have* to.
    Specifically, if we want to have scores for things that are not a part of
    the courseware (like "class participation"), there would be no corresponding
    Submission.

    .. no_pii:
    """
    student_item = models.ForeignKey(StudentItem, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submission, null=True, on_delete=models.CASCADE)
    points_earned = models.PositiveIntegerField(default=0)
    points_possible = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(editable=False, default=now, db_index=True)

    # Flag to indicate that this score should reset the current "highest" score
    reset = models.BooleanField(default=False)

    class Meta:
        app_label = "submissions"

    @property
    def submission_uuid(self):
        """
        Retrieve the submission UUID associated with this score.
        If the score isn't associated with a submission (for example, if this is
        a "reset" score or a a non-courseware item like "class participation"),
        then this will return None.

        Returns:
            str or None

        """
        if self.submission is not None:
            return str(self.submission.uuid)
        else:
            return None

    def to_float(self):
        """
        Calculate (points earned) / (points possible).
        If points possible is None (e.g. this is a "hidden" score)
        then return None.

        Returns:
            float or None

        """
        if self.points_possible == 0:
            return None
        return float(self.points_earned) / self.points_possible

    def __repr__(self):
        return repr({
            "student_item": self.student_item,
            "submission": self.submission,
            "created_at": self.created_at,
            "points_earned": self.points_earned,
            "points_possible": self.points_possible,
        })

    def is_hidden(self):
        """
        By convention, a score of 0/0 is not displayed to users.
        Hidden scores are filtered by the submissions API.

        Returns:
            bool: Whether the score should be hidden.

        """
        return self.points_possible == 0

    @classmethod
    def create_reset_score(cls, student_item):
        """
        Create a "reset" score (a score with a null submission).

        Only scores created after the most recent "reset" score
        should be used to determine a student's effective score.

        Args:
            student_item (StudentItem): The student item model.

        Returns:
            Score: The newly created "reset" score.

        Raises:
            DatabaseError: An error occurred while creating the score
        """
        # By setting the "reset" flag, we ensure that the "highest"
        # score in the score summary will point to this score.
        # By setting points earned and points possible to 0,
        # we ensure that this score will be hidden from the user.
        return cls.objects.create(
            student_item=student_item,
            submission=None,
            points_earned=0,
            points_possible=0,
            reset=True,
        )

    def __str__(self):
        return f"{self.points_earned}/{self.points_possible}"


class ScoreSummary(models.Model):
    """
    Running store of the highest and most recent Scores for a StudentItem.

    .. no_pii:
    """
    student_item = models.OneToOneField(StudentItem, on_delete=models.CASCADE)

    highest = models.ForeignKey(Score, related_name="+", on_delete=models.CASCADE)
    latest = models.ForeignKey(Score, related_name="+", on_delete=models.CASCADE)

    class Meta:
        app_label = "submissions"
        verbose_name_plural = "Score Summaries"

    @receiver(post_save, sender=Score)
    def update_score_summary(sender, **kwargs):  # pylint: disable=no-self-argument
        """
        Listen for new Scores and update the relevant ScoreSummary.

        Args:
            sender: not used

        Kwargs:
            instance (Score): The score model whose save triggered this receiver.
        """
        score = kwargs['instance']
        try:
            score_summary = ScoreSummary.objects.get(
                student_item=score.student_item
            )
            score_summary.latest = score

            # A score with the "reset" flag set will always replace the current highest score
            if score.reset:
                score_summary.highest = score
            # The conversion to a float may return None if points possible is zero
            elif score_summary.highest.to_float() is None and score.to_float() is not None:
                # Any score with non-null points possible will take precedence if the current
                # highest score is None
                score_summary.highest = score
            elif (
                score.to_float() is not None and
                score_summary.highest.to_float() is not None and
                score.to_float() > score_summary.highest.to_float()
            ):
                # If both scores are non-null we can do a normal comparison
                score_summary.highest = score
            score_summary.save()
        except ScoreSummary.DoesNotExist:
            ScoreSummary.objects.create(
                student_item=score.student_item,
                highest=score,
                latest=score,
            )
        except DatabaseError:
            logger.exception(
                "Error while updating score summary for student item %(item)s",
                {
                    'item': score.student_item,
                }
            )


class ScoreAnnotation(models.Model):
    """
    Annotate individual scores with extra information if necessary.

    .. no_pii:
    """

    class Meta:
        app_label = "submissions"

    score = models.ForeignKey(Score, on_delete=models.CASCADE)
    # A string that will represent the 'type' of annotation,
    # e.g. staff_override, etc.
    annotation_type = models.CharField(max_length=255, blank=False, db_index=True)

    creator = AnonymizedUserIDField()
    reason = models.TextField()


class ExternalGraderDetailManager(models.Manager):
    """
    Manager for handling queue-related operations on Submissions.
    """

    def get_queue_length(self, queue_name):
        """Count pending submissions in a specific queue"""
        return self.time_filter().filter(
            queue_name=queue_name,
            status='pending'
        ).count()

    def get_next_submission(self, queue_name):
        """Safely retrieve the next available submission for processing"""
        return self.time_filter().filter(
            queue_name=queue_name,
            status='pending'
        ).select_related('submission').order_by(
            'created_at'
        ).select_for_update().first()

    def time_filter(self):
        """
        Filter submissions based on processing delay window.
        Ensures we don't process submissions that were recently updated.
        """
        processing_window = now() - timedelta(
            minutes=getattr(settings, 'SUBMISSION_PROCESSING_DELAY', 60)
        )
        return self.filter(status_time__lte=processing_window)


class ExternalGraderDetail(models.Model):
    """
    Tracks queue processing information for a Submission.
    """

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        PULLED = 'pulled', 'Pulled'
        RETIRED = 'retired', 'Retired'
        FAILED = 'failed', 'Failed'

    VALID_TRANSITIONS = {
        'pending': ['pulled', 'failed'],
        'pulled': ['retired', 'failed'],
        'failed': ['pending'],
        'retired': []
    }
    submission = models.OneToOneField(
        Submission,
        on_delete=models.CASCADE,
        related_name='external_grader_detail',
    )

    queue_name = models.CharField(max_length=128)
    grader_file_name = models.CharField(max_length=128, default='')
    points_possible = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    # Secret key generated when a submission is pulled by an external grader.
    # Acts as a security token that must be provided when submitting results,
    # preventing unauthorized grade submissions and ensuring only the service
    # that pulled the submission can grade it.
    pullkey = models.CharField(max_length=128, null=True, blank=True)
    grader_reply = models.TextField(null=True, blank=True)

    # Timestamp of the most recent status change for this submission.
    # Used to track when state transitions occur, determine processing
    # eligibility based on time thresholds, and prioritize submissions
    # in processing queues (oldest first).
    status_time = models.DateTimeField(default=now, db_index=True)
    created_at = models.DateTimeField(default=now, db_index=True)

    num_failures = models.PositiveIntegerField(default=0)

    objects = ExternalGraderDetailManager()

    class Meta:
        indexes = [
            models.Index(fields=['queue_name', 'status', 'status_time']),
        ]
        ordering = ['-created_at']

    @property
    def is_processable(self):
        """
        Indicates if this submission can be processed based on its current state
        and time since last update.
        """
        if self.status not in ['pending', 'failed']:
            return False

        processing_window = now() - timedelta(
            minutes=getattr(settings, 'SUBMISSION_PROCESSING_DELAY', 60)
        )
        return self.status_time <= processing_window

    def can_transition_to(self, new_status, current_status=None):
        """Check if the transition to new_status is valid."""
        from_status = current_status if current_status is not None else self.status
        return new_status in self.VALID_TRANSITIONS.get(from_status, [])

    @transaction.atomic
    def update_status(self, new_status):
        """
        Update status and timestamp atomically
        """
        if not self.can_transition_to(new_status):
            raise ValueError(
                f"Invalid transition from {self.status} to {new_status} for "
                f"ExternalGraderDetail(id={self.id}, "
                f"submission_uuid={self.submission.uuid})")

        self.status = new_status
        self.status_time = now()

        if new_status == 'failed':
            self.num_failures += 1
            self.save(update_fields=['status', 'status_time', 'num_failures'])
        else:
            self.save(update_fields=['status', 'status_time'])

    @classmethod
    def create_from_uuid(cls, submission_uuid, **kwargs):
        submission = Submission.objects.get(uuid=submission_uuid)
        return cls.objects.create(submission=submission, **kwargs)


def submission_file_path(instance, _):
    """
    Generate file path for submission files.
    Format: queue_name/uuid
    The filename is replaced with the UUID to ensure uniqueness without preserving extension.
    """
    return os.path.join(
        instance.external_grader.queue_name,
        f"{instance.uuid}"
    )


@functools.cache
def _get_storage_cached():
    """
    Cached implementation to get the configured storage backend.

    This private function loads storage configuration from settings and
    dynamically instantiates the specified storage backend. It expects
    EDX_SUBMISSIONS['MEDIA'] to be a dict with 'BACKEND' (string path to
    storage class) and optional 'OPTIONS' (dict of parameters).

    This function is for internal use only and is cached to improve performance.
    """
    edx_submissions_config = getattr(settings, 'EDX_SUBMISSIONS', {})
    storage_config = edx_submissions_config.get('MEDIA')

    if storage_config:
        storage_cls = import_string(storage_config['BACKEND'])
        options = storage_config.get('OPTIONS', {})
        return storage_cls(**options)

    return default_storage


def get_storage():
    """
    Get the configured storage backend or fallback to default storage.

    This function checks for a storage configuration in the Django settings.
    It first looks for 'MEDIA' in the 'EDX_SUBMISSIONS' configuration dictionary.

    The function uses an internal cached implementation while remaining
    serializable for Django migrations, avoiding "Cannot serialize" errors.

    Returns:
        Storage instance: Returns the configured storage if found in EDX_SUBMISSIONS['MEDIA'],
                         otherwise returns Django's default_storage.

    Example:
        # In settings.py
        EDX_SUBMISSIONS = {
            'MEDIA': {
                'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
                'OPTIONS': {
                    'bucket_name': 'my-bucket'
                }
            }
        }

        # Then get_storage() will return an S3Boto3Storage instance
    """
    return _get_storage_cached()  # For performance while keeping this function serializable for migrations


class SubmissionFile(models.Model):
    """
    Model to handle files associated with submissions
    """
    uuid = models.UUIDField(default=uuid4, editable=False)  # legacy S3 key
    external_grader = models.ForeignKey(
        'submissions.ExternalGraderDetail',
        on_delete=models.SET_NULL,
        related_name='files',
        null=True,
    )
    file = models.FileField(
        upload_to=submission_file_path,
        max_length=512,
        storage=get_storage
    )
    original_filename = models.CharField(max_length=255)  # This is necessary to send file name to xqueue-watcher
    created_at = models.DateTimeField(default=now)

    class Meta:
        indexes = [
            models.Index(fields=['external_grader', 'uuid']),
        ]

    @property
    def xqueue_url(self):
        """
        Returns a URL in the XQueue-compatible format: /queue_name/uuid

        This format is used for file references in both the legacy XQueue system
        and the new integrated standard. It maintains backward compatibility
        while supporting the migration from the external XQueue API to the
        integrated Open edX solution.

        The URL follows the pattern: /{queue_name}/{submission_uuid}
        where:
        - queue_name: identifies the external grader queue
        - uuid: uniquely identifies this submission (legacy S3 key)

        Returns:
            str: Formatted URL path following XQueue conventions
        """
        return f"/{self.external_grader.queue_name}/{self.uuid}"
