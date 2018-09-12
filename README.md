# Tuto asyncio

## Docker

```bash
docker build --force-rm -t tuto.tuto-asyncio .
docker run --rm -i -t -v $PWD:/app tuto.tuto-asyncio
```

## First step

```bash
python -m tuto_asyncio.simple > logs/simple.log
python -m tuto_asyncio.async_simple > logs/async_simple.log
python -m tuto_asyncio.async_uvloop > logs/async_uvloop.log
python -m tuto_asyncio.async_thread_executor > logs/async_thread_executor.log
python -m tuto_asyncio.async_thread_executor_uvloop > logs/async_thread_executor_uvloop.log
```
