# -*- coding: utf-8 -*-

import time

from . import NUM_REQUESTS, request_example


if __name__ == '__main__':
    start = time.time()
    results = [request_example(_) for _ in range(NUM_REQUESTS)]
    end = time.time()

    print("-----")
    print("Min: {}s".format(min(results)))
    print("Max: {}s".format(max(results)))
    print("-----")
    print("Total: {}s".format(end - start))
