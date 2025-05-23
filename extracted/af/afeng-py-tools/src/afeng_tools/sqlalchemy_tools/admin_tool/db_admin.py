from typing import Any, Optional
from sqlalchemy import text, Index, Sequence
from sqlalchemy.orm import Session
from afeng_tools.sqlalchemy_tools.core.sqlalchemy_class import SqlalchemyDb
from afeng_tools.sqlalchemy_tools.core.sqlalchemy_items import DatabaseInfoItem
from afeng_tools.sqlalchemy_tools.crdu import sequence_crdu
from sqlalchemy.sql.ddl import CreateIndex, DropSequence, CreateSequence, DropIndex


class DBAdmin:
    """数据库管理"""

    def __init__(self, database_uri: str, echo_sql: bool = False):
        self.database_uri = database_uri
        self.sqlalchemy_db = SqlalchemyDb(DatabaseInfoItem(
            database_uri=database_uri,
            echo_sql=echo_sql
        ))

    def query_more_by_sql(self, sql: str, params: dict = None) -> list[dict[str, Any]]:
        """
        执行sql查询多条结果
        @param sql: sql语句，如： select * from tb_link_info where id=:id
        @param params: sql参数，如：{ 'id':1 }
        @return list: 返回 [{'id':1, 'title':'测试1'}]
        """
        with self.sqlalchemy_db.get_session() as session:
            if params:
                cursor = session.execute(text(sql), params=params)
            else:
                cursor = session.execute(text(sql))
            result_list = []
            for tmp_line in cursor.fetchall():
                result_list.append({tmp_key: tmp_line[index] for index, tmp_key in enumerate(cursor.keys())})
            return result_list

    def query_one_by_sql(self, sql: str, params: dict = None) -> dict[str, Any]:
        """
        执行sql查询单条结果
        @param sql: sql语句，如： select * from tb_link_info where id=:id
        @param params: sql参数，如：{ 'id':1 }
        @return dict: 返回 {'id':1, 'title':'测试1'}
        """
        with self.sqlalchemy_db.get_session() as session:
            if params:
                cursor = session.execute(text(sql), params=params)
            else:
                cursor = session.execute(text(sql))
            sql_result = cursor.fetchone()
            return {tmp_key: sql_result[index] for index, tmp_key in enumerate(cursor.keys())}

    def query_by_sql(self, sql: str, params: dict = None) -> Sequence[tuple]:
        """
        执行sql查询
        @param sql: sql语句，如： select id,title from tb_link_info where id=:id
        @param params: sql参数，如：{ 'id':1 }
        @return dict: 返回 [(1,'测试1')]
        """
        with self.sqlalchemy_db.get_session() as session:
            if params:
                cursor = session.execute(text(sql), params=params)
            else:
                cursor = session.execute(text(sql))
            return cursor.fetchall()

    def exec_by_sql(self, sql: str, params: dict = None) -> int:
        """
        执行sql
        @param sql: sql语句，如： update tb_link_info set title =:title where id=:id
        @param params: sql参数，如：{ 'id':1, 'title':‘测试2’ }
        @return 修改数据条数
        """
        with self.sqlalchemy_db.get_session() as session:
            if params:
                cursor = session.execute(text(sql), params=params)
            else:
                cursor = session.execute(text(sql))
            session.commit()
            return cursor.rowcount

    def insert_by_sql(self, sql: str, params: dict = None) -> int:
        """
        执行插入sql
        @param sql: sql语句，如： INSERT INTO test (title) VALUES (:title) where id=:id
        @param params: sql参数，如：{ 'id':1, 'title':‘测试2’ }
        @return 最后插入一条的id
        """
        with self.sqlalchemy_db.get_session() as session:
            if params:
                cursor = session.execute(text(sql), params=params)
            else:
                cursor = session.execute(text(sql))
            last_row_id = cursor.lastrowid
            session.commit()
            return last_row_id

    def get_session(self) -> Session:
        return self.sqlalchemy_db.get_session()

    def update_sequence_value_to(self, sequence_name: str, max_id: int):
        with self.sqlalchemy_db.get_session() as tmp_session:
            sequence_crdu.update_sequence_value_to(sequence_name, to_value=max_id, db=tmp_session)
            tmp_session.commit()

    def query_max_id(self, table_name: str):
        query_result = self.query_one_by_sql(f'SELECT max(id) FROM {table_name};')
        if query_result:
            return query_result.get('max')
        return 0

    def update_table_sequence_to_new(self, table_name: str):
        self.update_sequence_value_to(sequence_name=f'{table_name}_id_seq',
                                      max_id=self.query_max_id(table_name))

    def create_sequence(self, sequence_name: str, start: Optional[int] = None,
                        increment: Optional[int] = None,
                        min_value: Optional[int] = None,
                        max_value: Optional[int] = None, ):
        with self.sqlalchemy_db.engine.connect() as conn:
            conn.execute(CreateSequence(Sequence(sequence_name,
                                                 start=start, increment=increment,
                                                 minvalue=min_value,
                                                 maxvalue=max_value), if_not_exists=True))

    def drop_sequence(self, sequence_name: str):
        with self.sqlalchemy_db.engine.connect() as conn:
            conn.execute(DropSequence(Sequence(sequence_name), if_exists=True))

    def create_index(self, index_name: str):
        with self.sqlalchemy_db.engine.connect() as conn:
            conn.execute(CreateIndex(Index(index_name), if_not_exists=True))

    def drop_index(self, index_name: str):
        with self.sqlalchemy_db.engine.connect() as conn:
            conn.execute(DropIndex(Index(index_name), if_exists=True))


if __name__ == '__main__':
    db_admin = DBAdmin('postgresql://www_user:123456@127.0.0.1:5432/test_db')
    result = db_admin.query_one_by_sql('SELECT max(id) FROM tb_blacklist_info;')
    # result = db_admin.exec_by_sql('SELECT * FROM tb_blacklist_info;')
    print()
