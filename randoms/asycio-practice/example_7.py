import asyncio
import time


async def fetch_data(param):
    await asyncio.sleep(param)
    return f"Result of {param}"


async def manual_tasks():
    # Create Tasks Manually
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    result2 = await task2
    print(f"Task 1 and 2 awaited results: {[result1, result2]}")

    return "Manual Task runned"


async def gather_coroutines():
    # Gather Coroutines
    coroutines = [fetch_data(i) for i in range(1, 3)]
    # * -> unpacking a list
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    print(f"Corotine Results: {results}")

    return "Coroutines Gather runned"


async def gather_tasks():
    # Gather Tasks
    tasks = [asyncio.create_task(fetch_data(i)) for i in range(1, 3)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Task Results: {results}")

    return "Task Gather runned"


async def task_group():
    # Task Group
    # Async Context Manager -> doing setup and teardown operation asynchronously
    # TaskGroup does a lot of asynchronous work for us when Entering and Exiting:
    # track tasks, wait for compeletions, handles cancelation, handles errors, etc.
    async with asyncio.TaskGroup() as tg:
        # There is no await when we are using TaskGroup -> it await all the tasks that we created for that taskgroup for us when it exit context manager
        # Can be used for network requests, file access, database operations
        results = [tg.create_task(fetch_data(i)) for i in range(1, 3)]
    print(f"Task Group Results: {[result.result() for result in results]}")

    return "Task Group runned"


def runner(functions):
    for func in functions:
        t1 = time.perf_counter()

        results = asyncio.run(func())
        print(results)

        t2 = time.perf_counter()
        print(f"Finished in {t2 - t1:.2f} seconds")
        print()


functions = [manual_tasks, gather_coroutines, gather_tasks, task_group]
runner(functions)
