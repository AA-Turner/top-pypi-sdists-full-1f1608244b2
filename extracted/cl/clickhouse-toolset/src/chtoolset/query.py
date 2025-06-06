from chtoolset._query import replace_tables, \
    format, \
    tables, \
    table_if_is_simple_query, \
    query_get_type, \
    check_compatible_types, \
    check_valid_write_query, \
    get_left_table, \
    rewrite_aggregation_states, \
    parser_cache_info, \
    parser_cache_reset, \
    explain_ast, \
    create_row_binary_encoder, \
    apply_row_binary_encoder, \
    delete_row_binary_encoder


class RowBinaryEncoderError(Exception):
    """Custom exception for RowBinaryEncoder errors"""
    pass


class RowBinaryEncoder():
    def __init__(self, schema: str, legacy_conversion_mode: bool = True):
        if not isinstance(schema, str):
            raise TypeError("Schema must be a string")

        try:
            self._encoder_ptr = create_row_binary_encoder(schema, legacy_conversion_mode)
            if not self._encoder_ptr:
                raise RowBinaryEncoderError("Failed to create encoder")
        except Exception as e:
            raise RowBinaryEncoderError(f"Error initializing encoder: {str(e)}") from e

    def __enter__(self):
        if not self._encoder_ptr:
            raise RowBinaryEncoderError("Encoder was already closed")
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.close()

    def encode(self, block: str) -> bytes:
        if not isinstance(block, str):
            raise TypeError("Block must be a string")

        if not self._encoder_ptr:
            raise RowBinaryEncoderError("Encoder was already closed")

        try:
            result = apply_row_binary_encoder(self._encoder_ptr, block)
            return result
        except Exception as e:
            raise RowBinaryEncoderError(f"Error encoding block: {str(e)}") from e

    def close(self):
        if self._encoder_ptr:
            delete_row_binary_encoder(self._encoder_ptr)
            self._encoder_ptr = None
