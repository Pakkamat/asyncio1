# example of starting many tasks and getting acces to all tasks
import asyncio
import time

# coroutine for a task
async def task_coroutine(value):
    # report a message
    print(f'{time.ctime()} task {value} is running')
    # block for a moment
    await asyncio.sleep(1)

# dfine a main coroutine
async def main():
    # report a message
    print(f'{time.ctime()} main coroutine started')
    # start many tasks
    started_tasks = [asyncio.create_task(task_coroutine(i)) for i in range (10)]
    # allow some of the tasks time to start
    await asyncio.sleep(0.1)
    # get all tasks
    tasks = asyncio.all_tasks()
    # reprot all tasks
    for task in tasks:
        print(f'{time.ctime()} > {task.get_name()}, {task.get_coro()}')
    # wait for all tasks to complete
    for task in started_tasks:
        await task

# start the asyncio program
asyncio.run(main())

# Wed Jul 12 14:32:20 2023 main coroutine started
# Wed Jul 12 14:32:20 2023 task 0 is running
# Wed Jul 12 14:32:20 2023 task 1 is running
# Wed Jul 12 14:32:20 2023 task 2 is running
# Wed Jul 12 14:32:20 2023 task 3 is running
# Wed Jul 12 14:32:20 2023 task 4 is running
# Wed Jul 12 14:32:20 2023 task 5 is running
# Wed Jul 12 14:32:20 2023 task 6 is running
# Wed Jul 12 14:32:20 2023 task 7 is running
# Wed Jul 12 14:32:20 2023 task 8 is running
# Wed Jul 12 14:32:20 2023 task 9 is running
# Wed Jul 12 14:32:20 2023 > Task-3, <coroutine object task_coroutine at 0x000001E364B8BAE0>
# Wed Jul 12 14:32:20 2023 > Task-7, <coroutine object task_coroutine at 0x000001E364BEE570>
# Wed Jul 12 14:32:20 2023 > Task-10, <coroutine object task_coroutine at 0x000001E364BEE960>
# Wed Jul 12 14:32:20 2023 > Task-2, <coroutine object task_coroutine at 0x000001E364B88AC0>
# Wed Jul 12 14:32:20 2023 > Task-8, <coroutine object task_coroutine at 0x000001E364BEE880>
# Wed Jul 12 14:32:20 2023 > Task-6, <coroutine object task_coroutine at 0x000001E364BEE500>
# Wed Jul 12 14:32:20 2023 > Task-5, <coroutine object task_coroutine at 0x000001E364B8BE60>
# Wed Jul 12 14:32:20 2023 > Task-1, <coroutine object main at 0x000001E364B88820>
# Wed Jul 12 14:32:20 2023 > Task-11, <coroutine object task_coroutine at 0x000001E364BEE9D0>
# Wed Jul 12 14:32:20 2023 > Task-4, <coroutine object task_coroutine at 0x000001E364B8BCA0>
# Wed Jul 12 14:32:20 2023 > Task-9, <coroutine object task_coroutine at 0x000001E364BEE8F0>