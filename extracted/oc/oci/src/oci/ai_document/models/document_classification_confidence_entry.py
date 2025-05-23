# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221109


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DocumentClassificationConfidenceEntry(object):
    """
    Confidence Entry.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DocumentClassificationConfidenceEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param threshold:
            The value to assign to the threshold property of this DocumentClassificationConfidenceEntry.
        :type threshold: float

        :param precision:
            The value to assign to the precision property of this DocumentClassificationConfidenceEntry.
        :type precision: float

        :param recall:
            The value to assign to the recall property of this DocumentClassificationConfidenceEntry.
        :type recall: float

        :param f1_score:
            The value to assign to the f1_score property of this DocumentClassificationConfidenceEntry.
        :type f1_score: float

        """
        self.swagger_types = {
            'threshold': 'float',
            'precision': 'float',
            'recall': 'float',
            'f1_score': 'float'
        }
        self.attribute_map = {
            'threshold': 'threshold',
            'precision': 'precision',
            'recall': 'recall',
            'f1_score': 'f1Score'
        }
        self._threshold = None
        self._precision = None
        self._recall = None
        self._f1_score = None

    @property
    def threshold(self):
        """
        **[Required]** Gets the threshold of this DocumentClassificationConfidenceEntry.
        Threshold used to calculate precision and recall.


        :return: The threshold of this DocumentClassificationConfidenceEntry.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """
        Sets the threshold of this DocumentClassificationConfidenceEntry.
        Threshold used to calculate precision and recall.


        :param threshold: The threshold of this DocumentClassificationConfidenceEntry.
        :type: float
        """
        self._threshold = threshold

    @property
    def precision(self):
        """
        **[Required]** Gets the precision of this DocumentClassificationConfidenceEntry.
        Precision under the threshold


        :return: The precision of this DocumentClassificationConfidenceEntry.
        :rtype: float
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """
        Sets the precision of this DocumentClassificationConfidenceEntry.
        Precision under the threshold


        :param precision: The precision of this DocumentClassificationConfidenceEntry.
        :type: float
        """
        self._precision = precision

    @property
    def recall(self):
        """
        **[Required]** Gets the recall of this DocumentClassificationConfidenceEntry.
        Recall under the threshold


        :return: The recall of this DocumentClassificationConfidenceEntry.
        :rtype: float
        """
        return self._recall

    @recall.setter
    def recall(self, recall):
        """
        Sets the recall of this DocumentClassificationConfidenceEntry.
        Recall under the threshold


        :param recall: The recall of this DocumentClassificationConfidenceEntry.
        :type: float
        """
        self._recall = recall

    @property
    def f1_score(self):
        """
        **[Required]** Gets the f1_score of this DocumentClassificationConfidenceEntry.
        f1Score under the threshold


        :return: The f1_score of this DocumentClassificationConfidenceEntry.
        :rtype: float
        """
        return self._f1_score

    @f1_score.setter
    def f1_score(self, f1_score):
        """
        Sets the f1_score of this DocumentClassificationConfidenceEntry.
        f1Score under the threshold


        :param f1_score: The f1_score of this DocumentClassificationConfidenceEntry.
        :type: float
        """
        self._f1_score = f1_score

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
