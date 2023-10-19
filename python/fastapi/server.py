# -*- coding: utf-8 -*-
from typing import Union

from fastapi import FastAPI
from prometheus_fastapi_instrumentator.instrumentation import \
    PrometheusFastApiInstrumentator

app = FastAPI()
PrometheusFastApiInstrumentator(should_group_status_codes=False).instrument(
    app,
).expose(app, should_gzip=True, name='prometheus_metrics')


@app.get('/hello')
async def hello():
    return {'Hello': 'World'}


@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int, q: Union[str, None] = None):
    return {'userId': user_id, 'q': q}
