from kodexa import get_source


class KodexaProcessingException(Exception):
    """
    This is a specialized exception, if thrown while in the Kodexa Platform we will include the
    additional exception details so that they can be presented back to the user
    """

    def __init__(self, message, description, advice=None, documentation_url=None):
        self.description = description
        """The description of the problem, this is longer description"""
        self.advice = advice
        """Any advice on how to handle the problem, this can also include markdown to help present possible solutions"""
        self.message = message
        """A short message to express the problem"""
        self.documentation_url = documentation_url
        """A link to a URL where the user might find more information on the problem"""
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}  {self.description}"

class TextParser:
    """Parser to load a source file as a text document.  The text from the document may be placed on the root ContentNode or on the root's child nodes (controlled by lines_as_child_nodes)."""

    def __init__(self, encoding="utf-8", lines_as_child_nodes=False):
        self.encoding = encoding
        """The encoding that should be used when attempting to decode data  (default 'utf-8')"""
        self.lines_as_child_nodes = lines_as_child_nodes
        """If True, the lines of the file will be set as children of the root ContentNode; otherwise, the entire file content is set on the root ContentNode.  (default False)"""

    def decode_text(self, data):
        """ """
        try:
            data = data.decode(self.encoding)
        except (UnicodeDecodeError, AttributeError):
            pass
        return data

    def process(self, document):
        """ """
        with get_source(document) as fh:
            if self.lines_as_child_nodes:
                lines = fh.readlines()
                document.content_node = document.create_node(node_type="text")

                for data in lines:
                    text_node = document.create_node(
                        node_type="text", content=self.decode_text(data).strip()
                    )
                    document.content_node.add_child(text_node)
            else:
                data = fh.read()
                text_node = document.create_node(
                    node_type="text", content=self.decode_text(data)
                )
                document.content_node = text_node

            document.add_mixin("text")

        return document


class RollupTransformer:
    """The rollup step allows you to decide how you want to collapse content in a document by removing nodes
    while maintaining content and features as needed
    """

    def __init__(
        self,
        collapse_type_res=None,
        reindex: bool = True,
        selector: str = ".",
        separator_character: str = None,
        get_all_content: bool = False,
    ):
        if collapse_type_res is None:
            collapse_type_res = []
        self.collapse_type_res = collapse_type_res
        self.reindex = reindex
        self.selector = selector
        self.separator_character = separator_character if separator_character else ""
        self.get_all_content = get_all_content

    def process(self, document):
        if document.get_root():
            # Select those nodes that we want to do the 'rollup' in
            selected_nodes = document.select(self.selector)
            for selected_node in selected_nodes:
                for node_type_re in self.collapse_type_res:
                    nodes = selected_node.select(f'//*[typeRegex("{node_type_re}")]')

                    final_nodes = []
                    node_ids = [node.uuid for node in nodes]
                    # Remove any nodes where the parent node is in the list as well
                    for node in nodes:
                        if not self.is_node_in_list(node.get_parent(), node_ids):
                            final_nodes.append(node)

                    for node in final_nodes:
                        if node.get_parent():
                            if node.get_parent().get_content_parts():
                                # We need to insert into the content part that represents the child - then remove the child
                                content_part_index = (
                                    node.get_parent()
                                    .get_content_parts()
                                    .index(node.index)
                                )
                                parts = node.get_parent().get_content_parts()

                                parts.remove(node.index)
                                parts[
                                    content_part_index:content_part_index
                                ] = node.get_content_parts()
                                node.get_parent().set_content_parts(parts)
                                child_node_index = (
                                    node.get_parent().get_children().index(node)
                                )
                                node.get_parent().get_children()[
                                    child_node_index:child_node_index
                                ] = node.get_children()
                                node.get_parent().remove_child(node)

                            else:
                                # We just need to bring the content onto the end of the parent content and remove
                                # this node

                                node.get_parent().get_children().remove(node)

                                if self.get_all_content:
                                    node.get_parent().content = (
                                        node.get_parent().content
                                        + self.separator_character
                                        + node.get_all_content()
                                        if node.get_parent().content
                                        else node.get_all_content()
                                    )
                                else:
                                    node.get_parent().content = (
                                        node.get_parent().content
                                        + self.separator_character
                                        + node.content
                                        if node.get_parent().content
                                        else node.content
                                    )

                            if self.reindex:
                                # Reindex all the children
                                idx = 0
                                for child in node.get_parent().get_children():
                                    child.index = idx
                                    idx += 1
                                # Reindex content parts
                                if node.get_parent().get_content_parts():
                                    idx = 0
                                    final_cps = []
                                    for cp in node.get_parent().get_content_parts():
                                        if not isinstance(cp, str):
                                            final_cps.append(idx)
                                            idx += 1
                                        else:
                                            final_cps.append(cp)
                                    node.get_parent().set_content_parts(final_cps)

        return document

    def is_node_in_list(self, node, node_ids):
        """

        Args:
          node:
          node_ids:

        Returns:

        """
        if node.uuid in node_ids:
            return True

        if node.get_parent():
            return self.is_node_in_list(node.get_parent(), node_ids)

        return False
