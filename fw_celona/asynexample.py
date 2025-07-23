import asyncio
import random

async def worker(name, succeed=True):
    delay = random.uniform(0.5, 2.0)
    await asyncio.sleep(delay)
    if succeed:
        return f"{name} ✅ succeeded in {delay:.2f}s"
    else:
        raise Exception(f"{name} ❌ failed in {delay:.2f}s")

async def main():
    tasks = [
        asyncio.create_task(worker("A", succeed=True)),
        asyncio.create_task(worker("B", succeed=True)),
        asyncio.create_task(worker("C", succeed=False)),  # Will raise exception
    ]

    completed = set()

    while len(completed) < len(tasks):
        for task in tasks:
            if task in completed:
                continue

            if task.done():
                completed.add(task)

                if task.exception():
                    print(f"❌ Task failed: {task.exception()}")

                    # Cancel other tasks
                    for other in tasks:
                        if other not in completed:
                            other.cancel()
                            print(f"🛑 Cancelled task: {other.get_name()}")
                else:
                    print(f"✅ Result: {task.result()}")

        await asyncio.sleep(0.1)  # prevent tight loop

    # Clean up cancelled tasks
    await asyncio.gather(*tasks, return_exceptions=True)

asyncio.run(main())