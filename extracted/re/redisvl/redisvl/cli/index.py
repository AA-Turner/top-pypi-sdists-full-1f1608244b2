import argparse
import sys
from argparse import Namespace

from redisvl.cli.utils import add_index_parsing_options, create_redis_url
from redisvl.index import SearchIndex
from redisvl.redis.connection import RedisConnectionFactory
from redisvl.redis.utils import convert_bytes, make_dict
from redisvl.schema.schema import IndexSchema
from redisvl.utils.log import get_logger
from redisvl.utils.utils import lazy_import

logger = get_logger("[RedisVL]")


class Index:
    usage = "\n".join(
        [
            "rvl index <command> [<args>]\n",
            "Commands:",
            "\tinfo        Obtain information about an index",
            "\tcreate      Create a new index",
            "\tdelete      Delete an existing index",
            "\tdestroy     Delete an existing index and all of its data",
            "\tlistall     List all indexes",
            "\n",
        ]
    )

    def __init__(self):
        parser = argparse.ArgumentParser(usage=self.usage)

        parser.add_argument("command", help="Subcommand to run")
        parser.add_argument(
            "-f",
            "--format",
            help="Output format for info command",
            type=str,
            default="rounded_outline",
        )
        parser = add_index_parsing_options(parser)

        args = parser.parse_args(sys.argv[2:])
        if not hasattr(self, args.command):
            parser.print_help()
            exit(0)
        try:
            getattr(self, args.command)(args)
        except Exception as e:
            logger.error(e)
            exit(0)

    def create(self, args: Namespace):
        """Create an index.

        Usage:
            rvl index create -i <index_name> | -s <schema_path>
        """
        if not args.schema:
            logger.error("Schema must be provided to create an index")
        index = SearchIndex.from_yaml(args.schema, redis_url=create_redis_url(args))
        index.create()
        logger.info("Index created successfully")

    def info(self, args: Namespace):
        """Obtain information about an index.

        Usage:
            rvl index info -i <index_name> | -s <schema_path>
        """
        index = self._connect_to_index(args)
        _display_in_table(index.info())

    def listall(self, args: Namespace):
        """List all indices.

        Usage:
            rvl index listall
        """
        redis_url = create_redis_url(args)
        conn = RedisConnectionFactory.get_redis_connection(redis_url=redis_url)
        indices = convert_bytes(conn.execute_command("FT._LIST"))
        logger.info("Indices:")
        for i, index in enumerate(indices):
            logger.info(str(i + 1) + ". " + index)

    def delete(self, args: Namespace, drop=False):
        """Delete an index.

        Usage:
            rvl index delete -i <index_name> | -s <schema_path>
        """
        index = self._connect_to_index(args)
        index.delete(drop=drop)
        logger.info("Index deleted successfully")

    def destroy(self, args: Namespace):
        """Delete an index and the documents within it.

        Usage:
            rvl index destroy -i <index_name> | -s <schema_path>
        """
        self.delete(args, drop=True)

    def _connect_to_index(self, args: Namespace) -> SearchIndex:
        # connect to redis
        try:
            redis_url = create_redis_url(args)
            conn = RedisConnectionFactory.get_redis_connection(redis_url=redis_url)
        except ValueError:
            logger.error(
                "Must set REDIS_URL environment variable or provide host and port"
            )
            exit(0)

        if args.index:
            schema = IndexSchema.from_dict({"index": {"name": args.index}})
            index = SearchIndex(schema=schema, redis_url=redis_url)
        elif args.schema:
            index = SearchIndex.from_yaml(args.schema, redis_client=conn)
        else:
            logger.error("Index name or schema must be provided")
            exit(0)

        return index


def _display_in_table(index_info):
    print("\n")
    attributes = index_info.get("attributes", [])
    definition = make_dict(index_info.get("index_definition"))
    index_info = [
        index_info.get("index_name"),
        definition.get("key_type"),
        definition.get("prefixes"),
        index_info.get("index_options"),
        index_info.get("indexing"),
    ]

    # Display the index information in tabular format
    headers = ["Index Name", "Storage Type", "Prefixes", "Index Options", "Indexing"]
    col_width = max(len(str(info)) for info in index_info + headers) + 2

    def print_table_edge(length, col_width, start, mid, stop):
        print(f"{start}", end="")
        for _ in range(length):
            print("─" * col_width, mid, sep="", end="")
        print(f"\b{stop}")

    print("Index Information:")

    print_table_edge(len(index_info), col_width, "╭", "┬", "╮")

    # print header row
    for header in headers:
        print(f"│ {header.ljust(col_width-2)} ", end="")
    print("│")

    print_table_edge(len(index_info), col_width, "├", "┼", "┤")

    # print data row
    for info in index_info:
        print(f"| {str(info).ljust(col_width-2)} ", end="")
    print("|")

    print_table_edge(len(index_info), col_width, "╰", "┴", "╯")

    attr_values = []
    headers = [
        "Name",
        "Attribute",
        "Type",
    ]

    for attrs in attributes:
        attr = make_dict(attrs)

        values = [attr.get("identifier"), attr.get("attribute"), attr.get("type")]
        if len(attrs) > 5:
            options = make_dict(attrs)
            for k, v in options.items():
                if k not in ["identifier", "attribute", "type"]:
                    headers.append("Field Option")
                    headers.append("Option Value")
                    values.append(k)
                    values.append(v)
        attr_values.append(values)

    # Display the attributes in tabular format
    print("Index Fields:")
    headers = headers[
        : max(len(row) for row in attr_values)
    ]  # remove extra headers with no attr values
    col_widths = [max([len(str(attr)) + 2 for attr in row]) for row in attr_values]
    print_table_edge(len(headers), max(col_widths), "╭", "┬", "╮")

    # print header row
    for header in headers:
        print(f"│ {str(header).ljust(max(col_widths)-2)} ", end="")
    print("│")

    print_table_edge(len(headers), max(col_widths), "├", "┼", "┤")

    # print data rows
    num_cols = max(len(row) for row in attr_values)
    for row in attr_values:
        row.extend([""] * (num_cols - len(row)))
        for attr in row:
            print(f"│ {str(attr).ljust(max(col_widths)-2)} ", end="")
        print("│")

    print_table_edge(len(headers), max(col_widths), "╰", "┴", "╯")
