import asyncio
import time
from concurrent.futures import ProcessPoolExecutor


def fetch_data(param):
    # flush = True -> make sure that print statements come at as the order that we expect --
    # -> running them outside of our current thread cause them to get buffer and come out in wierd order
    print(f"Do something with {param}...", flush=True)
    time.sleep(param)
    print(f"Done with {param}", flush=True)
    return f"Result of {param}"


async def main_thread():
    # Run in Threads
    # asyncio.to_thread  -> wrap synchronous function with future and make it await-able
    # We pass function name and it params separatly so it can execute them later when it is ready
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 2))
    result1 = await task1
    print("Thread 1 fully completed")
    result2 = await task2
    print("Thread 2 fully completed")

    return [result1, result2]


async def main_processes():
    # Run in Process Pool
    # We need to get the running loop for Processes
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as executor:
        # Wrap new process within future that is await-able
        task1 = loop.run_in_executor(executor, fetch_data, 1)
        task2 = loop.run_in_executor(executor, fetch_data, 2)

        result1 = await task1
        print("Process 1 fully completed")
        result2 = await task2
        print("Process 2 fully completed")

    return [result1, result2]


# For multi processing -> When Python spawns multiple processes it needs to rerun our script in that new process --
# -> this check that we don't end up in an infinit loop
if __name__ == "__main__":
    t1 = time.perf_counter()

    results = asyncio.run(main_thread())
    print(results)

    t2 = time.perf_counter()
    print(f"Thread Finished in {t2 - t1:.2f} seconds")
    print()

    t1 = time.perf_counter()

    results = asyncio.run(main_processes())
    print(results)

    t2 = time.perf_counter()
    print(f"Processes Finished in {t2 - t1:.2f} seconds")
