# example of getting the current task from the main coroutine
import asyncio
import time

# define a main coroutine
async def main():
    # report a message
    print('main coroutine sarted')
    # get the current task
    task = asyncio.current_task()
    # report its details
    print(f'{time.ctime()}{task}')

# start the asyncio program
asyncio.run(main())

#
# Wed Jul 12 14:22:03 2023
# <Task pending name='Task-1' coro=<main() 
# running at d:\จารแดง\asyncio_1\2_asyncio.py:12> cb=[_run_until_complete_cb() 
# at C:\Users\NotebookNitro\AppData\Local\Programs\Python\Python310\lib\asyncio\base_events.py:184]>
#
