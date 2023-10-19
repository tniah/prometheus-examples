# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask import jsonify
from prometheus_flask_exporter.multiprocess import UWsgiPrometheusMetrics

app = Flask(__name__)
metrics = UWsgiPrometheusMetrics(
    app, group_by='url_rule', defaults_prefix='flask')
metrics.start_http_server(os.getenv('METRICS_PORT', 5000))


@app.route('/hello')
def hello():
    return jsonify({'message': 'hello, world!'})


@app.route('/error')
def error():
    raise Exception('An unexpected error has occurred')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
