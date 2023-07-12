# example of gather for many coroutines in a list
import asyncio
import time

# coroutine for a task
async def task_coro(value):
    # report a message
    print(f'{time.ctime()} task {value} is executing')
    # block for a moment
    await asyncio.sleep(1)

# coroutine used for the enry point
async def main():
    # report a message
    print(f'{time.ctime()} main strating.')
    # create many coroutines
    coros = [task_coro(i) for i in range (36)]
    # run the tasks
    await asyncio.gather(*coros)
    # repor a message
    print(f'{time.ctime()} main done')

# start the asyncio program
asyncio.run(main())

# Wed Jul 12 14:51:29 2023 main strating.
# Wed Jul 12 14:51:29 2023 task 0 is executing
# Wed Jul 12 14:51:29 2023 task 1 is executing
# Wed Jul 12 14:51:29 2023 task 2 is executing
# Wed Jul 12 14:51:29 2023 task 3 is executing
# Wed Jul 12 14:51:29 2023 task 4 is executing
# Wed Jul 12 14:51:29 2023 task 5 is executing
# Wed Jul 12 14:51:29 2023 task 6 is executing
# Wed Jul 12 14:51:29 2023 task 7 is executing
# Wed Jul 12 14:51:29 2023 task 8 is executing
# Wed Jul 12 14:51:29 2023 task 9 is executing
# Wed Jul 12 14:51:29 2023 task 10 is executing
# Wed Jul 12 14:51:29 2023 task 11 is executing
# Wed Jul 12 14:51:29 2023 task 12 is executing
# Wed Jul 12 14:51:29 2023 task 13 is executing
# Wed Jul 12 14:51:29 2023 task 14 is executing
# Wed Jul 12 14:51:29 2023 task 15 is executing
# Wed Jul 12 14:51:29 2023 task 16 is executing
# Wed Jul 12 14:51:29 2023 task 17 is executing
# Wed Jul 12 14:51:29 2023 task 18 is executing
# Wed Jul 12 14:51:29 2023 task 19 is executing
# Wed Jul 12 14:51:29 2023 task 20 is executing
# Wed Jul 12 14:51:29 2023 task 21 is executing
# Wed Jul 12 14:51:29 2023 task 22 is executing
# Wed Jul 12 14:51:29 2023 task 23 is executing
# Wed Jul 12 14:51:29 2023 task 24 is executing
# Wed Jul 12 14:51:29 2023 task 25 is executing
# Wed Jul 12 14:51:29 2023 task 26 is executing
# Wed Jul 12 14:51:29 2023 task 27 is executing
# Wed Jul 12 14:51:29 2023 task 28 is executing
# Wed Jul 12 14:51:29 2023 task 29 is executing
# Wed Jul 12 14:51:29 2023 task 30 is executing
# Wed Jul 12 14:51:29 2023 task 31 is executing
# Wed Jul 12 14:51:29 2023 task 32 is executing
# Wed Jul 12 14:51:29 2023 task 33 is executing
# Wed Jul 12 14:51:29 2023 task 34 is executing
# Wed Jul 12 14:51:29 2023 task 35 is executing
# Wed Jul 12 14:51:30 2023 main done