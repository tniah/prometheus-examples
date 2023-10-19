# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app, group_by='url_rule', defaults_prefix='flask')


@app.route('/hello')
def hello():
    return jsonify({'message': 'hello, world!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
