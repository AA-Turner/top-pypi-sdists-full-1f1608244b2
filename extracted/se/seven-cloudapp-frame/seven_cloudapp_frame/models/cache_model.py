# -*- coding: utf-8 -*-
"""
:Author: HuangJianYi
:Date: 2020-03-06 23:17:54
@LastEditTime: 2025-03-28 18:01:33
@LastEditors: HuangJianYi
:Description: 数据缓存业务模型
"""
import json
from copy import deepcopy
from seven_framework.base_model import *
from seven_framework import *
from seven_framework.redis import *
from seven_cloudapp_frame.libs.common import *
from seven_cloudapp_frame.libs.common.frame_db import *
from seven_cloudapp_frame.libs.customize.seven_helper import *

class CacheModel(FrameDbModel):

    def __init__(self, model_class, sub_table):
        """
        :Description: 数据缓存业务模型,用于mysql数据同步到redis，dependency_cache_expire(依赖建缓存时间默认24小时，普通缓存默认30分钟),查询结果是None和0不会被缓存，除非配置文件设置is_cache_empty=True
        :param model_class: 实体对象类
        :param sub_table: 分表标识
        :last_editors: HuangJianYi
        """
        self.cache_prefix = "data_cache"
        super(CacheModel,self).__init__(model_class, sub_table)

    def get_redis_config(self, config_dict=None):
        """
        :Description: redis初始化
        :param config_dict: config_dict
        :return: redis_init
        :last_editors: HuangJianYi
        """
        if hasattr(self, "redis_config_dict"):
            config_dict = self.redis_config_dict if self.redis_config_dict else config_dict
        if not config_dict:
            config_dict = config.get_value("redis_cache")
            if not config_dict:
                config_dict = config.get_value("redis")
        return config_dict

    def __function_init(self, config_dict=None):
        """
        :Description: 方法初始化
        :return: 是否是集群
        :last_editors: HuangJianYi
        """
        check_config_dict = self.get_redis_config(config_dict)
        if check_config_dict and check_config_dict.get("is_cluster", False):
            self.is_cluster = True
        else:
            self.is_cluster = False

    def get_dependency_key(self, dependency_key=''):
        """
        :Description: 获取依赖建
        :param dependencyKey: 依赖键
        :return: 依赖建
        :last_editors: HuangJianYi
        """
        if not dependency_key:
            dependency_key = self.table_name.lower()
        key = self.cache_prefix + ":" + "dependency_" + dependency_key
        if hasattr(self, "is_cluster") and self.is_cluster == True:
            return key + ":db_" + config.get_value('project_name','')
        return key

    def get_cache_key(self, prefix_key, field='*', where='', group_by='', order_by='', limit='', params=None):
        """
        :Description: 获取缓存key
        :param prefix_key: 缓存key前缀[entity、entityone、entitylist、entitypagelist、total、dict、dictone、dictlist、dictpagelist]
        :param field: 查询字段
        :param where: 数据库查询条件语句
        :param group_by: GROUP BY 语句
        :param order_by:  ORDER BY 语句
        :param limit:  LIMIT 语句
        :param params: 参数化查询参数
        :return: 缓存key
        :last_editors: HuangJianYi
        """
        params_str = ""
        if params:
            if isinstance(params,list):
                for param in params:
                    params_str += "_" + str(param)
            else:
                params_str += "_" + str(params)
        suffix_key = CryptoHelper.md5_encrypt(str(field + "_" + where + "_" + group_by + "_" + order_by + "_" + limit + params_str).replace(" ", "").lower())
        return prefix_key + "_" + self.table_name + "_" + suffix_key

    def get_dependency_cache_key(self, dependency_key, cache_key):
        """
        :Description: 获取依赖缓存key
        :param dependency_key: 依赖键
        :param cache_key: 缓存key
        :return: 依赖缓存key
        :last_editors: HuangJianYi
        """
        key = self.cache_prefix + ":" + CryptoHelper.md5_encrypt(dependency_key+cache_key)
        if hasattr(self, "is_cluster") and self.is_cluster == True:
            return key + ":db_" + config.get_value('project_name','')
        return key

    def get_dependency_cache(self, dependency_key, cache_key, redis_config_dict=None):
        """
        :Description: 获取依赖缓存值
        :param dependency_key: 依赖键
        :param cache_key: 缓存key
        :param redis_config_dict: redis_config_dict
        :return: 依赖缓存值
        :last_editors: HuangJianYi
        """
        if share_config.get_value("is_redis_cache",True) == False:
            return None
        self.__function_init(redis_config_dict)
        redis_init = RedisExHelper.init(config_dict=self.get_redis_config(redis_config_dict), decode_responses=True)
        dependency_cache_key = self.get_dependency_cache_key(dependency_key, cache_key)
        cache_savetime_key = dependency_cache_key + "_savetime"
        key_list = [dependency_key, cache_savetime_key, dependency_cache_key]
        cache_value_list = redis_init.mget(key_list)
        dependency_date_value = cache_value_list[0]
        if not dependency_date_value:
            redis_init.delete(dependency_cache_key)
            return None
        dependency_date = TimeHelper.format_time_to_datetime(dependency_date_value)
        cache_savetime_value = cache_value_list[1]
        if not cache_savetime_value:
            delete_keys = [cache_savetime_key, dependency_cache_key]
            redis_init.delete(*delete_keys)
            return None
        cache_savetime_date = TimeHelper.format_time_to_datetime(cache_savetime_value)
        if cache_savetime_date < dependency_date:
            delete_keys = [cache_savetime_key, dependency_cache_key]
            redis_init.delete(*delete_keys)
            return None
        cache_data = cache_value_list[2]
        if not cache_data:
            return None
        elif cache_data in ['null','0']:
            return cache_data
        else:
            size = len(cache_data) / 1024
            limit_size = share_config.get_value("cache_limit_size", 512) # 单位KB
            if size >= limit_size and limit_size > 0:
                if hasattr(self, "db"):
                    if hasattr(self.db, "context"):
                        if hasattr(self.db.context, "logging_link_error"):
                            self.db.context.logging_link_error(f"超过缓存值大小阀值{limit_size}KB,当前值为{size}KB,dependency_key:{dependency_key}")
            cache_data = json.loads(cache_data)
            return cache_data

    def log_cache(self, dependency_key, cache_key, cache_data, sql, params):
        """
        :Description: 记录从缓存取到的数据到日志
        :param dependency_key: dependency_key
        :param cache_key: cache_key
        :param cache_data: 缓存数据
        :param sql: sql
        :param params: params
        :return:
        :last_editors: HuangJianYi
        """
        if hasattr(self, "db") and share_config.get_value("log_redis_cache",True):
            if hasattr(self.db, "context"):
                if hasattr(self.db.context, "logging_link_info"):
                    log_info = {"sql":sql, "params":params, "result":cache_data, "dependency_key":dependency_key, "cache_key":self.get_dependency_cache_key(dependency_key,cache_key)}
                    self.db.context.logging_link_info("data_cache:" + JsonHelper.json_dumps(log_info))

    def set_dependency_cache(self, dependency_key, cache_key, value, cache_expire, redis_config_dict=None):
        """
        :Description: 设置依赖缓存值
        :param dependency_key: 依赖键
        :param cache_key: 缓存key
        :param cache_expire: 缓存时间（单位秒）
        :param redis_config_dict: redis_config_dict
        :return: 
        :last_editors: HuangJianYi
        """
        if share_config.get_value("is_redis_cache",True) == False:
            return
        is_cache_empty = share_config.get_value("is_cache_empty",False)
        if is_cache_empty == False:
            if not value:
                return
        self.__function_init(redis_config_dict)
        redis_init = RedisExHelper.init(config_dict=self.get_redis_config(redis_config_dict), decode_responses=True)
        dependency_date_value = redis_init.get(dependency_key)
        dependency_cache_key = self.get_dependency_cache_key(dependency_key,cache_key)
        if hasattr(self, "is_cluster") and self.is_cluster == True:
            if not dependency_date_value:
                redis_init.set(dependency_key,str(TimeHelper.get_now_format_time()),ex=share_config.get_value("dependency_cache_expire",24*60*60))
            redis_init.set(dependency_cache_key + "_savetime",str(TimeHelper.get_now_format_time()),ex=cache_expire)
            redis_init.set(dependency_cache_key,JsonHelper.json_dumps(value),ex=cache_expire)
        else:
            pipeline = redis_init.pipeline()
            if not dependency_date_value:
                pipeline.set(dependency_key,str(TimeHelper.get_now_format_time()),ex=share_config.get_value("dependency_cache_expire",24*60*60))
            pipeline.set(dependency_cache_key + "_savetime",str(TimeHelper.get_now_format_time()),ex=cache_expire)
            pipeline.set(dependency_cache_key,JsonHelper.json_dumps(value),ex=cache_expire)
            pipeline.execute()

    def delete_dependency_key(self, dependency_key='', delay_delete_time=0.01, redis_config_dict=None):
        """
        :Description: 删除依赖键,支持延迟删除和重试机制，同时删除多个依赖建建议传数组，不要分开多次调用
        :param dependency_key: 依赖键,为空则删除默认依赖建
        :param delay_delete_time: 延迟删除时间，传0则不进行延迟
        :param redis_config_dict: redis_config_dict
        :return: is_success：是否删除成功 True:成功 False:删除失败
        :last_editors: HuangJianYi
        """
        self.__function_init(redis_config_dict)
        is_success = False
        count = 0
        try_count = 2
        if share_config.get_value("is_redis_cache",True) == True:
            while count < try_count:
                count += 1
                try:
                    redis_init = RedisExHelper.init(config_dict=self.get_redis_config(redis_config_dict), decode_responses=True)
                    if delay_delete_time > 0:
                        time.sleep(delay_delete_time)
                    if isinstance(dependency_key,list):
                        dependency_keys = []
                        for key in dependency_key:
                            dependency_keys.append(self.get_dependency_key(key))
                        redis_init.delete(*dependency_keys)
                        is_success = True
                        break
                    else:
                        redis_init.delete(self.get_dependency_key(dependency_key))
                        is_success = True
                        break
                except Exception as ex:
                    if hasattr(self, "db"):
                        if hasattr(self.db, "context") and count == try_count:
                            if hasattr(self.db.context, "logging_link_error"):
                                self.db.context.logging_link_error(f"删除缓存异常,异常信息:{traceback.print_exc()},dependency_key:{json.dumps(dependency_key)}")
                    else:
                        print(traceback.print_exc())
        return is_success
    
    def delete_dependency_keys(self, dependency_keys=[], delay_delete_time=0.01, redis_config_dict=None):
        """
        :Description: 删除依赖键,支持延迟删除和重试机制，同时删除多个依赖建
        :param dependency_keys: 依赖键数组,为空则删除默认依赖建
        :param delay_delete_time: 延迟删除时间，传0则不进行延迟
        :param redis_config_dict: redis_config_dict
        :return: is_success：是否删除成功 True:成功 False:删除失败
        :last_editors: HuangJianYi
        """
        return self.delete_dependency_key(dependency_keys, delay_delete_time, redis_config_dict)

    def delete_dependency_keys_by_pattern(self, pattern, count=100, delay_delete_time=0.01, redis_config_dict=None):
        """
        :Description: 删除依赖键,根据前缀匹配删除
        :param pattern: 前缀
        :param count: 匹配数量
        :param delay_delete_time: 延迟删除时间，传0则不进行延迟
        :param redis_config_dict: redis_config_dict
        :return: is_success：是否删除成功 True:成功 False:删除失败
        :last_editors: HuangJianYi
        """
        self.__function_init(redis_config_dict)
        is_success = False
        dependency_keys = []
        count = 0
        try_count = 2
        if share_config.get_value("is_redis_cache", True) == True:
            redis_init = RedisExHelper.init(config_dict=self.get_redis_config(redis_config_dict), decode_responses=True)
            pattern = self.cache_prefix + ":" + pattern
            cursor = 0
            while True:
                try:
                    cursor, data = redis_init.scan(cursor, match=pattern + "*", count = 100)
                    dependency_keys.extend(data)
                    if cursor == 0:
                        break
                except:
                    break
            if len(dependency_keys) > 0:
                while count < try_count:
                    count += 1
                    try:
                        success_count = 0
                        if delay_delete_time > 0:
                            time.sleep(delay_delete_time)
                        success_count = redis_init.delete(*dependency_keys)
                        if success_count == len(dependency_keys):
                            is_success = True
                            break
                    except:
                        if hasattr(self, "db"):
                            if hasattr(self.db, "context") and count == try_count:
                                if hasattr(self.db.context, "logging_link_error"):
                                    self.db.context.logging_link_error(f"删除缓存异常,异常信息:{traceback.print_exc()},dependency_key:{json.dumps(dependency_keys)}")
                        else:
                            print(traceback.print_exc())
        return is_success

    def get_cache_list(self, where='', group_by='', order_by='', limit='', field="*", params=None,dependency_key='', cache_expire=1800, redis_config_dict=None):
        """
        :Description: 根据条件获取列表
        :param where: 数据库查询条件语句
        :param group_by: GROUP BY 语句
        :param order_by:  ORDER BY 语句
        :param limit:  LIMIT 语句
        :param field: 查询字段 
        :param params: 参数化查询参数
        :param dependencyKey: 依赖键
        :param cache_expire: 缓存时间（单位秒）
        :param redis_config_dict: redis_config_dict
        :return: 模型实体列表
        :last_editors: HuangJianYi
        """
        if where and where.strip() != '':
            where = " WHERE " + where
        if group_by and group_by.strip() != '':
            group_by = " GROUP BY "+group_by
        if order_by and order_by.strip() != '':
            order_by = " ORDER BY " + order_by
        if limit:
            limit = " LIMIT "+str(limit)
        sql = f"SELECT {field} FROM {self.table_name}{where}{group_by}{order_by}{limit};"
        
        self.__function_init(redis_config_dict)
        dependency_key = self.get_dependency_key(str(dependency_key))
        cache_key = self.get_cache_key('entitylist',field,where,group_by,order_by,limit,params)
        list_row = self.get_dependency_cache(dependency_key,cache_key,redis_config_dict)
        if list_row and share_config.get_value("is_redis_cache",True) == True:
            self.log_cache(dependency_key, cache_key, list_row, sql, params)
            if list_row == 'null':
                return []
            return self._BaseModel__row_entity_list(list_row)
        else:
            list_row = self.db.fetch_all_rows(sql, params)
            cache_value = deepcopy(list_row)
            if not cache_value:
                cache_value = []
            config_cache_expire = share_config.get_value("cache_expire",0)
            if config_cache_expire > 0:
                cache_expire = config_cache_expire
            self.set_dependency_cache(dependency_key,cache_key,cache_value,cache_expire,redis_config_dict)
            return self._BaseModel__row_entity_list(list_row)

    def get_cache_page_list(self, field="*", page_index=0, page_size=20, where='', group_by='', order_by='', params=None, dependency_key='', cache_expire=1800, page_count_mode='total', redis_config_dict=None):
        """
        :Description: 分页获取数据
        :param field: 查询字段 
        :param page_index: 分页页码 0为第一页
        :param page_size: 分页返回数据数量
        :param where: 数据库查询条件语句
        :param group_by: GROUP BY 语句
        :param order_by:  ORDER BY 语句
        :param params: 参数化查询参数
        :param dependencyKey: 依赖键
        :param cache_expire: 缓存时间（单位秒）
        :param page_count_mode: 分页计数模式 total-计算总数(默认) next-计算是否有下一页(bool) none-不计算
        :param redis_config_dict: redis_config_dict
        :return: 模型实体列表
        :last_editors: HuangJianYi
        """
        if where and where.strip() != '':
            where = " WHERE " + where
        if group_by and group_by.strip() != '':
            group_by = " GROUP BY " + group_by
        if order_by and order_by.strip() != '':
            order_by = " ORDER BY " + order_by

        limit = f"{str(int(page_index) * int(page_size))},{str(page_size if page_count_mode != 'next' else page_size+1)}"
        sql = f"SELECT {field} FROM {self.table_name}{where}{group_by}{order_by} LIMIT {limit};"
        
        self.__function_init(redis_config_dict)
        dependency_key = self.get_dependency_key(str(dependency_key))
        cache_key = self.get_cache_key('entitypagelist',field,where,group_by,order_by,limit,params)
        page_list = self.get_dependency_cache(dependency_key,cache_key,redis_config_dict)
        if page_list and share_config.get_value("is_redis_cache",True) == True:
            self.log_cache(dependency_key, cache_key, page_list, sql, params)
            if page_count_mode == "total":
                return self._BaseModel__row_entity_list(page_list["data"]),page_list["row_count"]
            elif page_count_mode == "next":
                return self._BaseModel__row_entity_list(page_list["data"]),bool(page_list["is_next_page"])
            else:
                return self._BaseModel__row_entity_list(page_list["data"])
        else:
            page_list = {}
            list_row = self.db.fetch_all_rows(sql, params)
            if not list_row:
                list_row = []
            if page_count_mode == "total":
                sql = f"SELECT COUNT({self.primary_key_field}) AS count FROM {self.table_name}{where}{group_by}"
                if group_by:
                    sql = f"SELECT COUNT(*) as count FROM ({sql}) temp_table;"
                row = self.db.fetch_one_row(sql, params)
                if row and 'count' in row and int(row['count']) > 0:
                    row_count = int(row["count"])
                else:
                    row_count = 0
                page_list["data"] = list_row
                page_list["row_count"] = row_count
                self.set_dependency_cache(dependency_key,cache_key,page_list,cache_expire,redis_config_dict)
                return self._BaseModel__row_entity_list(page_list["data"]), row_count
            elif page_count_mode == "next":
                is_next_page = len(list_row) == page_size+1
                if list_row and len(list_row) > 0:
                    list_row = list_row[:page_size]
                page_list["data"] = list_row
                page_list["is_next_page"] = is_next_page
                self.set_dependency_cache(dependency_key,cache_key,page_list,cache_expire,redis_config_dict)
                return self._BaseModel__row_entity_list(page_list["data"]), is_next_page
            else:
                page_list["data"] = list_row
                self.set_dependency_cache(dependency_key,cache_key,page_list,cache_expire,redis_config_dict)
                return self._BaseModel__row_entity_list(page_list["data"])

    def get_cache_entity(self, where='', group_by='', order_by='',  params=None, dependency_key='', cache_expire=1800, redis_config_dict=None):
        """
        :Description: 根据条件获取实体对象
        :param where: 数据库查询条件语句
        :param group_by: GROUP BY 语句
        :param order_by:  ORDER BY 语句
        :param params: 参数化查询参数
        :param dependency_key: 依赖键
        :param cache_expire: 缓存时间（单位秒）
        :param redis_config_dict: redis_config_dict
        :return: 模型实体
        :last_editors: HuangJianYi
        """
        if where and where.strip() != '':
            where = " WHERE " + where
        if group_by and group_by.strip() != '':
            group_by = " GROUP BY "+group_by
        if order_by and order_by.strip() != '':
            order_by = " ORDER BY " + order_by
        sql = f"SELECT * FROM {self.table_name}{where}{group_by}{order_by} LIMIT 1;"
        
        self.__function_init(redis_config_dict)
        dependency_key = self.get_dependency_key(str(dependency_key))
        cache_key = self.get_cache_key('entity','*',where,group_by,order_by,'1',params)
        one_row = self.get_dependency_cache(dependency_key,cache_key,redis_config_dict)
        if one_row and share_config.get_value("is_redis_cache",True) == True:
            self.log_cache(dependency_key, cache_key, one_row, sql, params)
            if one_row == 'null':
                return None
            return self._BaseModel__row_entity(one_row)
        else:
            one_row = self.db.fetch_one_row(sql, params)
            config_cache_expire = share_config.get_value("cache_expire",0)
            if config_cache_expire > 0:
                cache_expire = config_cache_expire
            self.set_dependency_cache(dependency_key,cache_key,one_row,cache_expire,redis_config_dict)
            return self._BaseModel__row_entity(one_row)

    def get_cache_entity_by_id(self, primary_key_id, dependency_key='', cache_expire=1800, redis_config_dict=None):
        """
        :Description: 根据主键值获取实体对象
        :param primary_key_id: 主键ID值
        :param dependencyKey: 依赖键
        :param cache_expire: 缓存时间（单位秒）
        :param redis_config_dict: redis_config_dict
        :return: 模型实体
        :last_editors: HuangJianYi
        """
        where = f"{self.primary_key_field}=%s"
        params = [primary_key_id]
        sql = f"SELECT * FROM {self.table_name} WHERE {where} LIMIT 1;"
        
        self.__function_init(redis_config_dict)
        dependency_key = self.get_dependency_key(str(dependency_key))
        cache_key = self.get_cache_key('entityone','*',where,'','','',params)
        one_row = self.get_dependency_cache(dependency_key,cache_key,redis_config_dict)
        if one_row and share_config.get_value("is_redis_cache",True) == True:
            self.log_cache(dependency_key, cache_key, one_row, sql, params)
            if one_row == 'null':
                return None
            return self._BaseModel__row_entity(one_row)
        else:
            one_row = self.db.fetch_one_row(sql,params)
            config_cache_expire = share_config.get_value("cache_expire",0)
            if config_cache_expire > 0:
                cache_expire = config_cache_expire
            self.set_dependency_cache(dependency_key,cache_key,one_row,cache_expire,redis_config_dict)
            return self._BaseModel__row_entity(one_row)

    def get_cache_total(self, where='', group_by='', field=None, params=None, dependency_key='', cache_expire=1800, redis_config_dict=None):
        """
        :Description: 根据条件获取数据数量
        :param where: 数据库查询条件语句
        :param group_by: GROUP BY 语句
        :param params: 参数化查询参数
        :param field: count(传参)
        :param dependencyKey: 依赖键
        :param cache_expire: 缓存时间（单位秒）
        :param redis_config_dict: redis_config_dict
        :return: 查询符合条件的行的数量
        :last_editors: HuangJianYi
        """
        if where and where.strip() != '':
            where = " WHERE " + where
        if group_by and group_by.strip() != '':
            group_by = " GROUP BY "+group_by
        if not field:
            field = self.primary_key_field
        sql = f"SELECT COUNT({field}) AS count FROM {self.table_name}{where}{group_by};"
        
        self.__function_init(redis_config_dict)
        dependency_key = self.get_dependency_key(str(dependency_key))
        cache_key = self.get_cache_key('total',field,where,group_by,'','',params)
        total = self.get_dependency_cache(dependency_key,cache_key,redis_config_dict)
        if total and share_config.get_value("is_redis_cache",True) == True:
            self.log_cache(dependency_key, cache_key, total, sql, params)
            if total == '0':
                return 0
            else:
                return total
        else:
            list_row = self.db.fetch_one_row(sql, params)
            if list_row and 'count' in list_row:
                config_cache_expire = share_config.get_value("cache_expire",0)
                if config_cache_expire > 0:
                    cache_expire = config_cache_expire
                self.set_dependency_cache(dependency_key,cache_key,list_row['count'],cache_expire,redis_config_dict)
                return list_row['count']
            return 0

    def get_cache_dict(self, where='', group_by='', order_by='', limit='1', field="*", params=None, dependency_key='', cache_expire=1800, redis_config_dict=None):
        """
        :Description: 返回字典dict
        :param where: 数据库查询条件语句
        :param group_by: GROUP BY 语句
        :param order_by:  ORDER BY 语句
        :param limit:  LIMIT 语句
        :param field: 查询字段 
        :param params: 参数化查询参数
        :param dependency_key: 依赖键
        :param cache_expire: 缓存时间（单位秒）
        :param redis_config_dict: redis_config_dict
        :return: 返回匹配条件的第一行字典数据
        :last_editors: HuangJianYi
        """
        if where and where.strip() != '':
            where = " WHERE " + where
        if group_by and group_by.strip() != '':
            group_by = " GROUP BY "+group_by
        if order_by and order_by.strip() != '':
            order_by = " ORDER BY " + order_by
        if limit:
            limit = " LIMIT "+str(limit)
        sql = f"SELECT {field} FROM {self.table_name}{where}{group_by}{order_by}{limit}"
        
        self.__function_init(redis_config_dict)
        dependency_key = self.get_dependency_key(str(dependency_key))
        cache_key = self.get_cache_key('dict',field,where,group_by,order_by,limit,params)
        one_row = self.get_dependency_cache(dependency_key,cache_key,redis_config_dict)

        if one_row and share_config.get_value("is_redis_cache",True) == True:
            self.log_cache(dependency_key, cache_key, one_row, sql, params)
            if one_row == 'null':
                return None
            return one_row
        else:
            one_row = self.db.fetch_one_row(sql, params)
            config_cache_expire = share_config.get_value("cache_expire",0)
            if config_cache_expire > 0:
                cache_expire = config_cache_expire
            self.set_dependency_cache(dependency_key,cache_key,one_row,cache_expire,redis_config_dict)
            if one_row:
                for field in one_row:
                    one_row[field] = self._BaseModel__convert_field_type(one_row[field])
            return one_row

    def get_cache_dict_by_id(self, primary_key_id, dependency_key='', cache_expire=1800, field="*", redis_config_dict=None):
        """
        :Description: 根据主键ID获取dict
        :param primary_key_id: 主键ID值
        :param dependencyKey: 依赖键
        :param cache_expire: 缓存时间（单位秒）
        :param field: 查询字段
        :param redis_config_dict: redis_config_dict
        :return: 返回匹配id的第一行字典数据
        :last_editors: HuangJianYi
        """
        where = f"{self.primary_key_field}=%s"
        params = [primary_key_id]
        sql = f"SELECT {field} FROM {self.table_name} WHERE {where} LIMIT 1;"
        
        self.__function_init(redis_config_dict)
        dependency_key = self.get_dependency_key(str(dependency_key))
        cache_key = self.get_cache_key('dictone',field,where,'','','',params)
        one_row = self.get_dependency_cache(dependency_key,cache_key,redis_config_dict)
        if one_row and share_config.get_value("is_redis_cache",True) == True:
            self.log_cache(dependency_key, cache_key, one_row, sql, params)
            if one_row == 'null':
                return None
            return one_row
        else:
            one_row = self.db.fetch_one_row(sql,params)
            config_cache_expire = share_config.get_value("cache_expire",0)
            if config_cache_expire > 0:
                cache_expire = config_cache_expire
            self.set_dependency_cache(dependency_key,cache_key,one_row,cache_expire,redis_config_dict)
            if one_row:
                for field in one_row:
                    one_row[field] = self._BaseModel__convert_field_type(one_row[field])
            return one_row

    def get_cache_dict_list(self, where='', group_by='', order_by='', limit='', field="*", params=None, dependency_key='', cache_expire=1800, redis_config_dict=None):
        """
        :Description: 返回字典列表dict list
        :param where: 数据库查询条件语句
        :param group_by: GROUP BY 语句
        :param order_by:  ORDER BY 语句
        :param limit:  LIMIT 语句
        :param field: 查询字段 
        :param params: 参数化查询参数
        :param dependencyKey: 依赖键
        :param cache_expire: 缓存时间（单位秒）
        :param redis_config_dict: redis_config_dict
        :return: 
        :last_editors: HuangJianYi
        """
        if where and where.strip() != '':
            where = " WHERE " + where
        if group_by and group_by.strip() != '':
            group_by = " GROUP BY "+group_by
        if order_by and order_by.strip() != '':
            order_by = " ORDER BY " + order_by
        if limit:
            limit = " LIMIT "+str(limit)
        sql = f"SELECT {field} FROM {self.table_name}{where}{group_by}{order_by}{limit};"

        self.__function_init(redis_config_dict)
        dependency_key = self.get_dependency_key(str(dependency_key))
        cache_key = self.get_cache_key('dictlist',field,where,group_by,order_by,limit,params)
        list = self.get_dependency_cache(dependency_key,cache_key,redis_config_dict)
        if list and share_config.get_value("is_redis_cache",True) == True:
            self.log_cache(dependency_key, cache_key, list, sql, params)
            return list
        else:
            list_row = self.db.fetch_all_rows(sql, params)
            if not list_row:
                list_row = []
            config_cache_expire = share_config.get_value("cache_expire",0)
            if config_cache_expire > 0:
                cache_expire = config_cache_expire
            self.set_dependency_cache(dependency_key,cache_key,list_row,cache_expire,redis_config_dict)
            if list_row and len(list_row) > 0:
                for one_row in list_row:
                    for field in one_row:
                        one_row[field] = self._BaseModel__convert_field_type(one_row[field])
            return list_row

    def get_cache_dict_page_list(self, field="*", page_index=0 ,page_size=20, where='', group_by='' ,order_by='' , params=None, dependency_key='', cache_expire=1800, page_count_mode='total', redis_config_dict=None):
        """
        :Description: 获取分页字典数据
        :param field: 查询字段 
        :param page_index: 分页页码 0为第一页
        :param page_size: 分页返回数据数量
        :param where: 数据库查询条件语句
        :param group_by: GROUP BY 语句
        :param order_by:  ORDER BY 语句
        :param params: 参数化查询参数
        :param dependencyKey: 依赖键
        :param cache_expire: 缓存时间（单位秒）
        :param page_count_mode: 分页计数模式 total-计算总数(默认) next-计算是否有下一页(bool) none-不计算
        :param redis_config_dict: redis_config_dict
        :return: 数据字典数组
        :last_editors: HuangJianYi
        """
        if where and where.strip() != '':
            where = " WHERE " + where
        if group_by and group_by.strip() != '':
            group_by = " GROUP BY " + group_by
        if order_by and order_by.strip() != '':
            order_by = " ORDER BY " + order_by

        limit = f"{str(int(page_index) * int(page_size))},{str(page_size if page_count_mode != 'next' else page_size+1)}"
        sql = f"SELECT {field} FROM {self.table_name}{where}{group_by}{order_by} LIMIT {limit}"
        
        self.__function_init(redis_config_dict)
        dependency_key = self.get_dependency_key(str(dependency_key))
        cache_key = self.get_cache_key('dictpagelist',field,where,group_by,order_by,limit,params)
        page_list = self.get_dependency_cache(dependency_key,cache_key,redis_config_dict)
        if page_list and share_config.get_value("is_redis_cache",True) == True:
            self.log_cache(dependency_key, cache_key, page_list, sql, params)
            if page_count_mode == "total":
                return page_list["data"],page_list["row_count"]
            elif page_count_mode == "next":
                return page_list["data"],bool(page_list["is_next_page"])
            else:
                return page_list["data"]
        else:
            config_cache_expire = share_config.get_value("cache_expire",0)
            if config_cache_expire > 0:
                cache_expire = config_cache_expire
            page_list = {}
            list_row = self.db.fetch_all_rows(sql, params)
            if not list_row:
                list_row = []
            if list_row and len(list_row) > 0:
                for one_row in list_row:
                    for field in one_row:
                        one_row[field] = self._BaseModel__convert_field_type(one_row[field])
            if page_count_mode == "total":
                sql = f"SELECT COUNT({self.primary_key_field}) AS count FROM {self.table_name}{where}{group_by}"
                if group_by:
                    sql = f"SELECT COUNT(*) as count FROM ({sql}) temp_table;"
                row = self.db.fetch_one_row(sql, params)
                if row and 'count' in row and int(row['count']) > 0:
                    row_count = int(row["count"])
                else:
                    row_count = 0
                page_list["data"] = list_row
                page_list["row_count"] = row_count
                self.set_dependency_cache(dependency_key,cache_key,page_list,cache_expire,redis_config_dict)
                return list_row, row_count
            elif page_count_mode == "next":
                is_next_page = len(list_row) == page_size+1
                if list_row and len(list_row) > 0:
                    list_row = list_row[:page_size]
                page_list["data"] = list_row
                page_list["is_next_page"] = is_next_page
                self.set_dependency_cache(dependency_key,cache_key,page_list,cache_expire,redis_config_dict)
                return list_row, is_next_page
            else:
                page_list["data"] = list_row
                self.set_dependency_cache(dependency_key,cache_key,page_list,cache_expire,redis_config_dict)
                return list_row
            
    def set_cache_entity(self, value, where='', group_by='', order_by='', params=None, dependency_key='', cache_expire=1800, redis_config_dict=None):
        """
        :Description: 根据条件缓存数据
        :param value: 要缓存的数据
        :param where: 数据库查询条件语句
        :param group_by: GROUP BY 语句
        :param order_by:  ORDER BY 语句
        :param params: 参数化查询参数
        :param dependency_key: 依赖键
        :param cache_expire: 缓存时间（单位秒）
        :param redis_config_dict: redis_config_dict
        :return:
        :last_editors: HuangJianYi
        """
        if where and where.strip() != '':
            where = " WHERE " + where
        if group_by and group_by.strip() != '':
            group_by = " GROUP BY "+group_by
        if order_by and order_by.strip() != '':
            order_by = " ORDER BY " + order_by
        
        self.__function_init(redis_config_dict)
        dependency_key = self.get_dependency_key(str(dependency_key))
        cache_key = self.get_cache_key('entity','*',where,group_by,order_by,'1',params)
        config_cache_expire = share_config.get_value("cache_expire",0)
        if config_cache_expire > 0:
            cache_expire = config_cache_expire
        self.set_dependency_cache(dependency_key,cache_key,value.__dict__,cache_expire,redis_config_dict)
    
    def set_cache_entity_by_id(self, value, primary_key_id, dependency_key='', cache_expire=1800, redis_config_dict=None):
        """
        :Description: 根据主键值缓存数据
        :param value: 要缓存的数据
        :param primary_key_id: 主键ID值
        :param dependencyKey: 依赖键
        :param cache_expire: 缓存时间（单位秒）
        :param redis_config_dict: redis_config_dict
        :return:
        :last_editors: HuangJianYi
        """
        where = f"{self.primary_key_field}=%s"
        params = [primary_key_id]
        self.__function_init(redis_config_dict)
        dependency_key = self.get_dependency_key(str(dependency_key))
        cache_key = self.get_cache_key('entityone','*',where,'','','',params)
        config_cache_expire = share_config.get_value("cache_expire",0)
        if config_cache_expire > 0:
            cache_expire = config_cache_expire
        self.set_dependency_cache(dependency_key,cache_key,value,cache_expire,redis_config_dict)
    
    def set_cache_dict(self, value, where='', group_by='', order_by='', limit='1', field="*", params=None, dependency_key='', cache_expire=1800, redis_config_dict=None):
        """
        :Description: 根据条件缓存数据
        :param value: 要缓存的数据
        :param where: 数据库查询条件语句
        :param group_by: GROUP BY 语句
        :param order_by:  ORDER BY 语句
        :param limit:  LIMIT 语句
        :param field: 查询字段 
        :param params: 参数化查询参数
        :param dependency_key: 依赖键
        :param cache_expire: 缓存时间（单位秒）
        :param redis_config_dict: redis_config_dict
        :return: 
        :last_editors: HuangJianYi
        """
        if where and where.strip() != '':
            where = " WHERE " + where
        if group_by and group_by.strip() != '':
            group_by = " GROUP BY "+group_by
        if order_by and order_by.strip() != '':
            order_by = " ORDER BY " + order_by
        if limit:
            limit = " LIMIT "+str(limit)
        
        self.__function_init(redis_config_dict)
        dependency_key = self.get_dependency_key(str(dependency_key))
        cache_key = self.get_cache_key('dict',field,where,group_by,order_by,limit,params)

        config_cache_expire = share_config.get_value("cache_expire",0)
        if config_cache_expire > 0:
            cache_expire = config_cache_expire
        self.set_dependency_cache(dependency_key,cache_key,value,cache_expire,redis_config_dict)

    def set_cache_dict_by_id(self, primary_key_id, value, dependency_key='', cache_expire=1800, field="*", redis_config_dict=None):
        """
        :Description: 根据主键ID缓存数据
        :param primary_key_id: 主键ID值
        :param value: 要缓存的数据
        :param dependencyKey: 依赖键
        :param cache_expire: 缓存时间（单位秒）
        :param field: 查询字段
        :param redis_config_dict: redis_config_dict
        :return:
        :last_editors: HuangJianYi
        """
        where = f"{self.primary_key_field}=%s"
        params = [primary_key_id]
        self.__function_init(redis_config_dict)
        dependency_key = self.get_dependency_key(str(dependency_key))
        cache_key = self.get_cache_key('dictone',field,where,'','','',params)
        config_cache_expire = share_config.get_value("cache_expire",0)
        if config_cache_expire > 0:
            cache_expire = config_cache_expire
        self.set_dependency_cache(dependency_key,cache_key,value,cache_expire,redis_config_dict)