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
import asyncio 

async def func1(delay, id):
  print(f"Fetching data for id{id}...")
  await asyncio.sleep(delay)
  print("Data fetched")
  return {f"data{id}":"Some data"}

async def mainfunc():
  print("Start of main coroutine: ")
  task1 = func1(5, 1)
  task2 = func1(5, 2)
  result = await task1
  print(f"The result is:{result}")

  result = await task2
  print(f"The result is:{result}")
  
  print("c'est fini")

asyncio.run(mainfunc())