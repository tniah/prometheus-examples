# -*- coding: utf-8 -*-
import os

from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics


def when_ready(server):
    port = int(os.getenv('METRICS_PORT', 5000))
    GunicornPrometheusMetrics.start_http_server_when_ready(port)


def child_exit(server, worker):
    GunicornPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)
