# example of an asynchronous iterator with async for loop
import asyncio
import time

# define an asynchronous iterator
class AsyncIterator():
    # constructor, define some state
    def __init__(self):
        self.counter = 0

    # create an instance of the iterator
    def __aiter__(self):
        return self
    
    # return the next awaitable 
    async def __anext__(self):
    #  check for no furture items
        if self.counter >= 10:
            raise StopAsyncIteration 
        #increment the counter
        self.counter += 1
        # simulate work
        await asyncio.sleep(1)
        # return the counter value
        return self.counter
    
# main coroutine
async def main():
# loop over async iterator with async for loop 
    async for item in AsyncIterator():
        print (f'{time.ctime()} {item}')
# execute the asyncio program
asyncio.run(main())

# Wed Jul 19 13:55:26 2023 1
# Wed Jul 19 13:55:27 2023 2
# Wed Jul 19 13:55:28 2023 3
# Wed Jul 19 13:55:29 2023 4
# Wed Jul 19 13:55:30 2023 5
# Wed Jul 19 13:55:31 2023 6
# Wed Jul 19 13:55:32 2023 7
# Wed Jul 19 13:55:33 2023 8
# Wed Jul 19 13:55:34 2023 9
# Wed Jul 19 13:55:35 2023 10