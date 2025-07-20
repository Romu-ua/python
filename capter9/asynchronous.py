import asyncio

async def task(name):
    print(f"{name} : 開始")
    await asyncio.sleep(1)
    print(f"{name} : 終了")

async def main():
    await asyncio.gather(
        task("A"),
        task("B"),
        task("C"),
    )

# asyncio.run(main())
# 非同期処理(コルーチン)を用いる本質は
# I/O処理待ちが長い処理を効率よく扱いたいとき