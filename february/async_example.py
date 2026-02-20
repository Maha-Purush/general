# import asyncio 

# async def confusement(delay):
#   await asyncio.sleep(delay)
#   print("i am waiting, so confused bruh..")

# async def func1(delay):
#   print("Fetching data...")
#   await confusement(delay)
#   await asyncio.sleep(delay)
#   print("Data fetched")
#   return {"data":"Some data"}

# async def mainfunc():
#   print("Start of main coroutine: ")
#   task = func1(10)
#   result = await task
#   print(f"The result is:{result}")
#   print("c'est fini")

# asyncio.run(mainfunc())

################################################
# import asyncio 

# async def func1(delay, id):
#   print(f"Fetching data for id{id}...")
#   await asyncio.sleep(delay)
#   print("Data fetched")
#   return {f"data{id}":"Some data"}

# async def mainfunc():
#   print("Start of main coroutine: ")
#   task1 = func1(5, 1)
#   task2 = func1(5, 2)
#   result = await task1
#   print(f"The result is:{result}")

#   result = await task2
#   print(f"The result is:{result}")
  
#   print("c'est fini")

# asyncio.run(mainfunc())

################################################

# import asyncio

# async def fetch_data(id, sleep):
#     print(f"Coroutine {id} starting")
#     await asyncio.sleep(sleep)
#     print(f"Coroutine {id} finished after {sleep} seconds")
#     return {"id": id}


# async def main():
#   task1 = asyncio.create_task(fetch_data(1,5))
#   task2 = asyncio.create_task(fetch_data(2,8))
#   task3 = asyncio.create_task(fetch_data(3,3))

#   result3 = await task3
#   result1 = await task1
#   result2 = await task2

#   print(result1, result2, result3)
# asyncio.run(main())

##########################################################

import asyncio
import time

def now():
    return round(time.time() - START_TIME, 2)

async def worker():
    print(f"{now()}s → Worker: Started")
    await asyncio.sleep(4)
    print(f"{now()}s → Worker: Finished")
    return "Worker Result"

async def main():
    print(f"{now()}s → Main: Starting")

    await asyncio.sleep(1)
    print(f"{now()}s → Main: About to create task")

    task = asyncio.create_task(worker())

    await asyncio.sleep(2)
    print(f"{now()}s → Main: Still doing something else...")

    await asyncio.sleep(2)
    print(f"{now()}s → Main: Now awaiting the worker")

    result = await task
    print(f"{now()}s → Main: Got result -> {result}")

    print(f"{now()}s → Main: Finished")

START_TIME = time.time()
asyncio.run(main())
