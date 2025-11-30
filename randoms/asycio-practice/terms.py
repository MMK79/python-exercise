import asyncio
import time


# Synchronous Function -> run within main function which is asynchronous
def sync_function(test_param: str) -> str:
    print("This is a synchronous function.")

    time.sleep(0.1)

    return f"Sync Result: {test_param}"


# Corutine Function
async def async_function(test_param: str) -> str:
    print("This is an asynchronous coroutine function.")

    await asyncio.sleep(0.1)

    return f"Async Result: {test_param}"


# Create an Asynchronous Function = async def function_name
async def main():
    ### Start Synchronous Example ###
    # sync_result = sync_function("Test")
    # print(sync_result)
    ### End Synchronous Example ###

    ### Start Awaitable Type = Futures Example ###
    # loop = asyncio.get_running_loop()
    # Created the future
    # future = loop.create_future()
    # print(f"Empty Future: {future}")

    # Set the future result
    # future.set_result("Future Results: Test")
    # future.set_exception(TypeError)
    # You need to be within async function to use await
    # await = __await__() -> telling evnet loop to pause the execution of current function -> yeild control back to event loop --
    # -> run another task + it will stay suspended until the awaitable is complete
    # Got the result by awaiting it
    # future_result = await future
    # print(future_result)
    ### End Awaitable Type = Futures Example ###

    ### Start Awaitable Types : Coroutine Example ###
    # coroutine_obj = async_function("Test")
    # It print the object, but it won't run the function
    # print(coroutine_obj)

    # Now with await it will run the function
    # coroutine_result = await coroutine_obj
    # print(coroutine_result)
    ### End Awaitable Types : Coroutine Example ###

    ### Start Awaitable Types : Tasks Example ###
    task = asyncio.create_task(async_function("Test"))
    print(task)

    task_result = await task
    print(task_result)
    ### End Awaitable Types : Tasks Example ###


if __name__ == "__main__":
    # Calling an Asynchronous Function
    # Event loop = Engine that manages and run asynchronous function -> like scheduler
    # asyncio.run() = Getting the event loop -> running task till they are marked as complete -> close the event loop when they are done
    asyncio.run(main())
