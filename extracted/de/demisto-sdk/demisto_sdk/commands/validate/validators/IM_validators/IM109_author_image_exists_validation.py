from __future__ import annotations

from typing import Iterable, List

from demisto_sdk.commands.common.constants import (
    AUTHOR_IMAGE_FILE_NAME,
    PACKS_FOLDER,
    PARTNER_SUPPORT,
)
from demisto_sdk.commands.content_graph.objects.pack import Pack
from demisto_sdk.commands.content_graph.parsers.related_files import RelatedFileType
from demisto_sdk.commands.validate.validators.base_validator import (
    BaseValidator,
    ValidationResult,
)

ContentTypes = Pack


class AuthorImageExistsValidator(BaseValidator[ContentTypes]):
    error_code = "IM109"
    description = "Checks if the pack has an author image path."
    error_message = "You've created/modified a partner supported pack without providing an author image as a .png file. Please make sure to add an image under the following path"
    related_field = "Author_image"
    rationale = "Author images make it easier to identify the author."
    related_file_type = [RelatedFileType.AUTHOR_IMAGE]

    def obtain_invalid_content_items(
        self, content_items: Iterable[ContentTypes]
    ) -> List[ValidationResult]:
        return [
            ValidationResult(
                validator=self,
                message=f"{self.error_message} {PACKS_FOLDER}/{content_item.name}/{AUTHOR_IMAGE_FILE_NAME}",
                content_object=content_item,
            )
            for content_item in content_items
            if content_item.support == PARTNER_SUPPORT
            and (not content_item.author_image_file.exist)
        ]
