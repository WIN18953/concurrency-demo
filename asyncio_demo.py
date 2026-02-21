import asyncio

async def fetch_data(task_name):
    print(f"Start fetching {task_name}")
    await asyncio.sleep(2)
    print(f"Finished fetching {task_name}")

async def main():
    tasks = [
        fetch_data("Task1"),
        fetch_data("Task2"),
        fetch_data("Task3")
    ]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())