"""
This module is used by Docker Compose to find out if Elasticsearch is okay.
"""

import time

from elasticsearch import Elasticsearch
from tests.functional.settings import test_settings


def wait_elasticsearch():
    """
    Wait until Elasticsearch answers to ping(). The function is used to
    check if Elasticsearch is okay.
    """
    hosts = f'http://{test_settings.es_host}:{test_settings.es_port}'
    es_client = Elasticsearch(hosts=hosts, validate_cert=False, use_ssl=False)
    while True:
        if es_client.ping():
            break
        time.sleep(1)


if __name__ == '__main__':
    wait_elasticsearch()
