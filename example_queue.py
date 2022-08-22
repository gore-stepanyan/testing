import asyncio
import random
import time

async def worker(queue):
    while True:
        i = await queue.get()
        print(i)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    for i in range(10):
        queue.put_nowait(i)

    task = asyncio.create_task(worker(queue))
    await queue.join()
    task.cancel()

asyncio.run(main())