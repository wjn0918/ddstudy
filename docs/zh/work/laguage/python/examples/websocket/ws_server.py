import websockets
import asyncio


async def cs_server(ws, path):
    if path == '/cs':
        async for ms in ws:
            print(f"cs receive: {ms}")
            await ws.send(f"this is cs")


async def cs2_server(ws, path):
    if path == "/cs2":
        async for ms in ws:
            print(f"cs2 receive {ms}")
            await ws.send(f"this is cs2")

async def handle(ws,path):
    if path == "/cs":
        await cs_server(ws,path)
    elif path == "/cs2":
        await cs2_server(ws,path)
    else:
        await ws.send("error")

if __name__ == '__main__':
    start_server = websockets.serve(handle, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

