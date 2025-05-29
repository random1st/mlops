import asyncio

import httpx
import time

async def say(what, delay):
    await asyncio.sleep(delay)
    print(what)

async def main():
    await asyncio.gather(
        say("Hello", 5),
        say("World", 5)
    )

asyncio.run(main()) # prints both words almost instantly


def say_1(what, delay):
    time.sleep(delay)
    print(what)

def main_1():
    say_1("Hello", 5)
    say_1("World", 5)

main_1()
