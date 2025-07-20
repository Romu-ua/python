# run_in_executor:
# 非同期コードの中から同期関数を別スレッドや別プロセスで実行するための仕組み

import asyncio
import time 

def blocking_task(x):
    print(f"start blocking task {x}")
    time.sleep(5)
    print(f"end blocking task {x}")
    return x * 2

async def main():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, blocking_task, 2)
    print(f"Result : {result}")

asyncio.run(main())
