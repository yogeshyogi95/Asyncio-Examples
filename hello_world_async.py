# this asynchronous version runs in 2 secs
import time
import asyncio

async def message():
    print("hello")
    await asyncio.sleep(2)
    print("world")

async def main():
    tasks = []
    for i in range(10):
        tasks.append(message())
    await asyncio.wait(tasks)

loop = asyncio.get_event_loop()

start = time.time()
loop.run_until_complete(main())
end = time.time()
print(end - start)
loop.close()