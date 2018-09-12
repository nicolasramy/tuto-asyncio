# -*- coding: utf-8 -*-

import asyncio
import time

from . import NUM_REQUESTS, request_example


async def main():
    loop = asyncio.get_event_loop()

    # run_in_executor(executor, function, *args)
    futures = [
        loop.run_in_executor(
            None,
            request_example,
            _
        ) for _ in range(NUM_REQUESTS)
    ]

    responses = []
    for response in await asyncio.gather(*futures):
        responses.append(response)

    return responses


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()

    start = time.time()
    try:
        results = event_loop.run_until_complete(main())
    finally:
        event_loop.close()

    print("-----")
    print("Min: {}s".format(min(results)))
    print("Max: {}s".format(max(results)))
    print("-----")
    print("Total: {}s".format(time.time() - start))
