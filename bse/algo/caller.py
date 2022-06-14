import asyncio


async def periodic():
    while True:
        await asyncio.sleep(300)
        print('periodic2 ')

def stop():
    task.cancel()

loop = asyncio.get_event_loop()
loop.call_later(42, stop)
task = loop.create_task(periodic())

try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass
