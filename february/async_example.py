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

import asyncio

async def work():
  print("Work started")
  await asyncio.sleep(3)
  print("Work finished")
  return 42

async def main():
  task = asyncio.create_task(work())
  print("Task created")

  await asyncio.sleep(1)
  print("After 1 second")

  result = await task
  print("Result: ", result)

asyncio.run(main())