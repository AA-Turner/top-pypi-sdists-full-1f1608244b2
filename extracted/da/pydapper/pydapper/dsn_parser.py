from typing import Dict

import dsnparse

_DEFAULT_DB_API = {
    # if the desired dbapi is not provided in scheme, fall back on sane defaults
    "postgresql": "psycopg2",
    "sqlite": "sqlite3",
    "mssql": "pymssql",
    "mysql": "mysql",
    "oracle": "oracledb",
    "bigquery": "google",
}


class PydapperParseResult(dsnparse.ParseResult):
    # noinspection PyUnresolvedReferences
    def __init__(self, dsn: str, **defaults):
        super().__init__(dsn, **defaults)
        # make linters and editors happy
        self.dsn: str = dsn
        self.scheme: str = self.scheme
        self.path: str = self.path
        self.hostname: str = self.hostname
        self.username: str = self.username
        self.password: str = self.password
        self.query_str: str = self.query
        self.query_params: Dict[str, str] = self.query_params
        self.port: str = self.port
        self.fragment: str = self.fragment

    def __repr__(self):
        result = [f"instance({self.__class__.__name__}):"]
        for k, v in vars(self).items():
            result.append(f"\t{k}: {v!r}")
        return "\n".join(result)

    def __eq__(self, other):
        return self.dsn == other.dsn

    @property
    def dbms(self) -> str:
        return self.schemes[0]

    @property
    def dbapi(self) -> str:
        if len(self.schemes) == 1:
            dbapi = _DEFAULT_DB_API.get(self.dbms)
        else:
            dbapi = "_".join(self.schemes[1:])
        if not dbapi:
            raise ValueError(f"Could not derive dbapi from schemes {self.schemes}")
        return dbapi


parse = PydapperParseResult
