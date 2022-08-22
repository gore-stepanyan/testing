import pyshark
import asyncio
import nest_asyncio

nest_asyncio.apply()
  
capture = pyshark.LiveCapture(interface='enp5s0', display_filter="rtcp")

async def listen():
    for packet in capture.sniff_continuously():
        print('new packet sniffed!')
        return packet

async def fun_1():
    await listen()
    loop.create_task(fun_1())

  
async def fun_2():
    print('ice-cream')
    await asyncio.sleep(0.5)
    loop.create_task(fun_2())
  
try:
    loop = asyncio.get_event_loop()
    loop.create_task(fun_1())
    loop.create_task(fun_2())
    loop.run_forever()
except KeyboardInterrupt:
    pass