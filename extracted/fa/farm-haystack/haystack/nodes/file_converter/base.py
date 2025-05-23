from typing import List, Optional, Dict, Union, Any

import logging
from abc import abstractmethod
from pathlib import Path

from tqdm import tqdm
from haystack.nodes.base import BaseComponent
from haystack.schema import Document
from haystack.lazy_imports import LazyImport


logger = logging.getLogger(__name__)


with LazyImport("Run 'pip install farm-haystack[preprocessing]' or 'pip install langdetect'") as langdetect_import:
    import langdetect


# https://en.wikipedia.org/wiki/Ligature_(writing)
KNOWN_LIGATURES = {
    # Latin
    "ﬀ": "ff",
    "ﬁ": "fi",
    "ﬂ": "fl",
    "ﬃ": "ffi",
    "ﬄ": "ffl",
    "ﬅ": "ft",
    "ﬆ": "st",
    "Ǳ": "DZ",
    "ǲ": "Dz",
    "ǳ": "dz",
    "Ǆ": "DŽ",
    "ǅ": "Dž",
    "ǆ": "dž",
    "Ꜩ": "Tz",
    "ꜩ": "tz",
    "🙰": "et",
    "℔": "lb",
    "ᵫ": "ue",
    "Ĳ": "IJ",
    "ĳ": "ij",  # They are both capitalized together, so the "Ij" ligature doesn't exist
    "ꝏ": "oo",  # Not the infinite sign but a double-o ligature: https://en.wikipedia.org/wiki/Ligature_(writing)#Massachusett_%EA%9D%8F
    # Armenian
    "ﬓ": "մն",
    "ﬔ": "մե",
    "ﬕ": "մի",
    "ﬖ": "վն",
    "ﬗ": "մխ",
}


class BaseConverter(BaseComponent):
    """
    Base class for implementing file converts to transform input documents to text format for ingestion in DocumentStore.
    """

    outgoing_edges = 1

    def __init__(
        self,
        remove_numeric_tables: bool = False,
        valid_languages: Optional[List[str]] = None,
        id_hash_keys: Optional[List[str]] = None,
        progress_bar: bool = True,
    ):
        """
        :param remove_numeric_tables: This option uses heuristics to remove numeric rows from the tables.
                                      The tabular structures in documents might be noise for the reader model if it
                                      does not have table parsing capability for finding answers. However, tables
                                      may also have long strings that could possible candidate for searching answers.
                                      The rows containing strings are thus retained in this option.
        :param valid_languages: validate languages from a list of languages specified in the ISO 639-1
                                (https://en.wikipedia.org/wiki/ISO_639-1) format.
                                This option can be used to add test for encoding errors. If the extracted text is
                                not one of the valid languages, then it might likely be encoding error resulting
                                in garbled text.
        :param id_hash_keys: Generate the document id from a custom list of strings that refer to the document's
            attributes. If you want to ensure you don't have duplicate documents in your DocumentStore but texts are
            not unique, you can modify the metadata and pass e.g. `"meta"` to this field (e.g. [`"content"`, `"meta"`]).
            In this case the id will be generated by using the content and the defined metadata.
        :param progress_bar: Show a progress bar for the conversion.
        """
        super().__init__()

        self.remove_numeric_tables = remove_numeric_tables
        self.valid_languages = valid_languages
        self.id_hash_keys = id_hash_keys
        self.progress_bar = progress_bar

    @abstractmethod
    def convert(
        self,
        file_path: Path,
        meta: Optional[Dict[str, Any]],
        remove_numeric_tables: Optional[bool] = None,
        valid_languages: Optional[List[str]] = None,
        encoding: Optional[str] = "UTF-8",
        id_hash_keys: Optional[List[str]] = None,
    ) -> List[Document]:
        """
        Convert a file to a dictionary containing the text and any associated meta data.

        File converters may extract file meta like name or size. In addition to it, user
        supplied meta data like author, url, external IDs can be supplied as a dictionary.

        :param file_path: path of the file to convert
        :param meta: dictionary of meta data key-value pairs to append in the returned document.
        :param remove_numeric_tables: This option uses heuristics to remove numeric rows from the tables.
                                      The tabular structures in documents might be noise for the reader model if it
                                      does not have table parsing capability for finding answers. However, tables
                                      may also have long strings that could possible candidate for searching answers.
                                      The rows containing strings are thus retained in this option.
        :param valid_languages: validate languages from a list of languages specified in the ISO 639-1
                                (https://en.wikipedia.org/wiki/ISO_639-1) format.
                                This option can be used to add test for encoding errors. If the extracted text is
                                not one of the valid languages, then it might likely be encoding error resulting
                                in garbled text.
        :param encoding: Select the file encoding (default is `UTF-8`)
        :param id_hash_keys: Generate the document id from a custom list of strings that refer to the document's
            attributes. If you want to ensure you don't have duplicate documents in your DocumentStore but texts are
            not unique, you can modify the metadata and pass e.g. `"meta"` to this field (e.g. [`"content"`, `"meta"`]).
            In this case the id will be generated by using the content and the defined metadata.
        """
        pass

    def validate_language(self, text: str, valid_languages: Optional[List[str]] = None) -> bool:
        """
        Validate if the language of the text is one of valid languages.
        """
        if valid_languages is None:
            valid_languages = self.valid_languages

        if not valid_languages:
            return True

        lang = None
        try:
            langdetect_import.check()
            lang = langdetect.detect(text)
        except langdetect.lang_detect_exception.LangDetectException:
            pass
        except ImportError as exc:
            logger.debug(
                "langdetect could not be imported. Haystack won't try to guess the document language. "
                "Original error: %s",
                exc,
            )

        return lang in valid_languages

    def run(  # type: ignore
        self,
        file_paths: Union[Path, List[Path]],
        meta: Optional[Union[Dict[str, str], List[Optional[Dict[str, str]]]]] = None,
        remove_numeric_tables: Optional[bool] = None,
        known_ligatures: Optional[Dict[str, str]] = None,
        valid_languages: Optional[List[str]] = None,
        encoding: Optional[str] = "UTF-8",
        id_hash_keys: Optional[List[str]] = None,
        raise_on_failure: bool = True,
    ):
        """
        Extract text from a file.

        :param file_paths: Path to the files you want to convert
        :param meta: Optional dictionary with metadata that shall be attached to all resulting documents.
                     Can be any custom keys and values.
        :param remove_numeric_tables: This option uses heuristics to remove numeric rows from the tables.
                                      The tabular structures in documents might be noise for the reader model if it
                                      does not have table parsing capability for finding answers. However, tables
                                      may also have long strings that could possible candidate for searching answers.
                                      The rows containing strings are thus retained in this option.
        :param known_ligatures: Some converters tend to recognize clusters of letters as ligatures, such as "ﬀ" (double f).
                                Such ligatures however make text hard to compare with the content of other files,
                                which are generally ligature free. Therefore we automatically find and replace the most
                                common ligatures with their split counterparts. The default mapping is in
                                `haystack.nodes.file_converter.base.KNOWN_LIGATURES`: it is rather biased towards Latin alphabeths
                                but excludes all ligatures that are known to be used in IPA.
                                If no value is provided, this default is created and used.
                                You can use this parameter to provide your own set of ligatures to clean up from the documents.
        :param valid_languages: validate languages from a list of languages specified in the ISO 639-1
                                (https://en.wikipedia.org/wiki/ISO_639-1) format.
                                This option can be used to add test for encoding errors. If the extracted text is
                                not one of the valid languages, then it might likely be encoding error resulting
                                in garbled text.
        :param encoding: Select the file encoding (default is `UTF-8`)
        :param id_hash_keys: Generate the document id from a custom list of strings that refer to the document's
            attributes. If you want to ensure you don't have duplicate documents in your DocumentStore but texts are
            not unique, you can modify the metadata and pass e.g. `"meta"` to this field (e.g. [`"content"`, `"meta"`]).
            In this case the id will be generated by using the content and the defined metadata.
        :param raise_on_failure: If true, raises an exception if the conversion of a single file fails. If False, skips the file without failing.
        """
        if known_ligatures is None:
            known_ligatures = KNOWN_LIGATURES

        if isinstance(file_paths, Path):
            file_paths = [file_paths]

        if isinstance(meta, dict) or meta is None:
            meta = [meta] * len(file_paths)

        documents: list = []
        failed_paths: list = []
        for file_path, file_meta in tqdm(
            zip(file_paths, meta), total=len(file_paths), disable=not self.progress_bar, desc="Converting files"
        ):
            try:
                documents += self.convert(
                    file_path=file_path,
                    meta=file_meta,
                    remove_numeric_tables=remove_numeric_tables,
                    valid_languages=valid_languages,
                    encoding=encoding,
                    id_hash_keys=id_hash_keys,
                )
            except Exception as e:
                if raise_on_failure:
                    raise e
                failed_paths.append(str(file_path))
                continue

        # Cleanup ligatures
        for document in documents:
            for ligature, letters in known_ligatures.items():
                if document.content is not None:
                    document.content = document.content.replace(ligature, letters)

        if failed_paths:
            logger.warning("Conversion of the following file paths failed: %s", ",".join(failed_paths))

        result = {"documents": documents}
        return result, "output_1"

    def run_batch(  # type: ignore
        self,
        file_paths: Union[Path, List[Path]],
        meta: Optional[Union[Dict[str, str], List[Optional[Dict[str, str]]]]] = None,
        remove_numeric_tables: Optional[bool] = None,
        known_ligatures: Optional[Dict[str, str]] = None,
        valid_languages: Optional[List[str]] = None,
        encoding: Optional[str] = "UTF-8",
        id_hash_keys: Optional[List[str]] = None,
    ):
        return self.run(
            file_paths=file_paths,
            meta=meta,
            remove_numeric_tables=remove_numeric_tables,
            known_ligatures=known_ligatures,
            valid_languages=valid_languages,
            encoding=encoding,
            id_hash_keys=id_hash_keys,
        )
