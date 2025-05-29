import asyncio

import httpx
import time

async def main():
    urls = ["https://api.ipify.org?format=json"] * 20
    async with httpx.AsyncClient() as client:
        responses = []
        for url in urls:
            response = await client.get(url)
            responses.append(response)


if __name__ == "__main__":
    import time

    start = time.time()
    asyncio.run(main())
    print(f"Execution time: {time.time() - start:.2f} seconds")
