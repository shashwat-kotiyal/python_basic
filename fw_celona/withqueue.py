import asyncio

async def worker(queue):
    while True:
        item = await queue.get()
        print(f"🔧 Working on {item}")
        await asyncio.sleep(1)
        print(f"✅ Done with {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()

    # Start worker
    asyncio.create_task(worker(queue))

    # Enqueue items
    for i in range(3):
        await queue.put(f"task-{i}")

    print("⏳ Waiting for all tasks to be done...")
    await queue.join()  # waits for 3 task_done() calls
    print("🎉 All tasks processed.")

asyncio.run(main())
