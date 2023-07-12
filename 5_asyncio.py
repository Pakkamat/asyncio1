# example of waiting for all tasks to complete
import random
import asyncio
import time

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random.random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'{time.ctime()} > task {arg} done with {value}')

# main coroutine
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(36)]
    # wait for all tasks to complete # ALL_COMPLETED, FIRST_COMPLETED, FRIST_EXCEPTION
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    # report result
    print(f'{time.ctime()} All done')       

# start the asyncio program
asyncio.run(main())

#ALL_COMPLETED
# Wed Jul 12 15:05:35 2023 > task 32 done with 0.0389431622467199
# Wed Jul 12 15:05:35 2023 > task 31 done with 0.04179050965022002
# Wed Jul 12 15:05:35 2023 > task 20 done with 0.070689784232698
# Wed Jul 12 15:05:35 2023 > task 24 done with 0.0872543409300176
# Wed Jul 12 15:05:35 2023 > task 10 done with 0.09420830144063252
# Wed Jul 12 15:05:35 2023 > task 15 done with 0.0983173950199333
# Wed Jul 12 15:05:35 2023 > task 30 done with 0.09972837398811629
# Wed Jul 12 15:05:35 2023 > task 16 done with 0.13626976190261564
# Wed Jul 12 15:05:35 2023 > task 12 done with 0.1872028047885571
# Wed Jul 12 15:05:35 2023 > task 8 done with 0.21844869066501915
# Wed Jul 12 15:05:35 2023 > task 18 done with 0.24067443570180713
# Wed Jul 12 15:05:35 2023 > task 21 done with 0.25665112381558597
# Wed Jul 12 15:05:35 2023 > task 25 done with 0.32625736728153476
# Wed Jul 12 15:05:35 2023 > task 6 done with 0.3604861061293855
# Wed Jul 12 15:05:35 2023 > task 33 done with 0.3627638846229322
# Wed Jul 12 15:05:36 2023 > task 0 done with 0.40110181815534174
# Wed Jul 12 15:05:36 2023 > task 2 done with 0.4017889937063974
# Wed Jul 12 15:05:36 2023 > task 29 done with 0.403288644476963
# Wed Jul 12 15:05:36 2023 > task 9 done with 0.40707630382269844
# Wed Jul 12 15:05:36 2023 > task 13 done with 0.4662639077573145
# Wed Jul 12 15:05:36 2023 > task 35 done with 0.48898144187792003
# Wed Jul 12 15:05:36 2023 > task 22 done with 0.5574388194310882
# Wed Jul 12 15:05:36 2023 > task 1 done with 0.5678653436310038
# Wed Jul 12 15:05:36 2023 > task 4 done with 0.5978376282971831
# Wed Jul 12 15:05:36 2023 > task 7 done with 0.6215108757903726
# Wed Jul 12 15:05:36 2023 > task 34 done with 0.6283649011710613
# Wed Jul 12 15:05:36 2023 > task 28 done with 0.7094193366354858
# Wed Jul 12 15:05:36 2023 > task 14 done with 0.7181382957920774
# Wed Jul 12 15:05:36 2023 > task 26 done with 0.7475378830421741
# Wed Jul 12 15:05:36 2023 > task 23 done with 0.8832844677133388
# Wed Jul 12 15:05:36 2023 > task 27 done with 0.8960108735375409
# Wed Jul 12 15:05:36 2023 > task 19 done with 0.9048531622195414
# Wed Jul 12 15:05:36 2023 > task 5 done with 0.9394219497558173
# Wed Jul 12 15:05:36 2023 > task 11 done with 0.9454014000006663
# Wed Jul 12 15:05:36 2023 > task 17 done with 0.9486864485668299
# Wed Jul 12 15:05:36 2023 > task 3 done with 0.9997215728719526
# Wed Jul 12 15:05:36 2023 All done

#FIRST_COMPLETED
# Wed Jul 12 15:06:05 2023 > task 18 done with 0.006271113189946442
# Wed Jul 12 15:06:05 2023 > task 29 done with 0.007275268059457329
# Wed Jul 12 15:06:05 2023 > task 34 done with 0.00804201108179703
# Wed Jul 12 15:06:05 2023 > task 30 done with 0.01164458603789642
# Wed Jul 12 15:06:05 2023 All done