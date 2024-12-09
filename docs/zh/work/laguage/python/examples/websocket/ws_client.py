import websockets
import asyncio


async def cs_client():
    while True:
        path = input("please input path: ")
        uri = f"ws://localhost:8765/{path}"
        print(uri)
        async with websockets.connect(uri) as ws:
            ms = input("please input ms: ")
            await ws.send(ms)
            response = await ws.recv()
            print(f"receive is : {response}")


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(cs_client())
    asyncio.get_event_loop().run_forever()
