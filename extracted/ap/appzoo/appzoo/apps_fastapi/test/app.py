#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AppZoo.
# @File         : raw_app
# @Time         : 2020/12/28 11:11 上午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :


import time

from datetime import datetime
from typing import Optional
from fastapi import FastAPI, Form, Depends, File, UploadFile
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.responses import \
    RedirectResponse, FileResponse, HTMLResponse, PlainTextResponse
from starlette.status import *

app = FastAPI()


@app.post('/post/{p}')
def read_root(kwargs: dict, p: str, a: int = 0):
    print(kwargs)
    print(type(a), a)
    print(p)
    return kwargs


@app.post('/')
def read_root(kwargs: dict):
    print(kwargs)
    return kwargs


def func(**kwargs):
    print(kwargs)


@app.api_route('/xx/{xx}', methods=['POST', 'GET'])
def get(request: Request, xx):
    kwargs = dict(request.query_params)
    return func(kwargs)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('app:app', reload=True, debug=True, port=8080)
