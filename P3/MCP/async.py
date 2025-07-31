import asyncio

async def func(delay, message):
    print(message)
    await asyncio.sleep(delay)
    print(message)

async def main():
    f1 = func(2, "Hello")   # coroutine object f1
    f2 = func(1, "World")   # coroutine object f2
    await asyncio.gather(f1, f2)

asyncio.run(main())
"""
Hello
World
World
Hello
"""