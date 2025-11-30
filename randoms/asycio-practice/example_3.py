### Right way to use Asyncio ###
import asyncio
import time


async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    # We are creating a task -> schedule the coroutine to run on the event loop
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    task3 = asyncio.create_task(fetch_data(3))
    # Now when we await that coroutine object -> we scheduling and running it to completion at the same time -> no concurrency
    result1 = await task1
    print("Task 1 fully completed")
    result2 = await task2
    print("Task 2 fully completed")
    result3 = await task3
    print("Task 3 fully completed")
    return [result1, result2, result3]


t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")
