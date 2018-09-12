# -*- coding: utf-8 -*-

import time

import requests


NUM_REQUESTS = 1000
NUM_WORKERS = 100


def request_example(request_number):
    loop_start = time.time()

    try:
        requests.get('http://example.com/')

    except requests.exceptions.ConnectionError:
        pass

    finally:
        execution_time = time.time() - loop_start
        print("request {}: {}s".format(request_number, execution_time))
        return execution_time



