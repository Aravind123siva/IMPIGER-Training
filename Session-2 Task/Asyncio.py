# import asyncio
#
# async def task(name, delay):
#     print(f"{name} started...")
#     await asyncio.sleep(delay)
#     print(f"{name} finished!")
#
# async def main():
#     await asyncio.gather(task("Task 1", 2), task("Task 2", 1))
#
# asyncio.run(main())
#
# #
# #

import asyncio
import aiofiles

async def process_file(file_path, output_path):
    try:
        async with aiofiles.open(file_path, mode='r') as file:
            content = await file.read()
            print(f"Read {len(content)} characters from {file_path}")

        async with aiofiles.open(output_path, mode='w') as file:
            await file.write(content)
            print(f"Saved {file_path} content to {output_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

async def main():
    file_paths = ["/home/aravinds/directory_env/PycharmProjects/001 after.txt", "/home/aravinds/directory_env/PycharmProjects/001 before.txt"]  # Only 2 files
    output_paths = ["output1.txt", "output2.txt"]

    tasks = [process_file(file_paths[i], output_paths[i]) for i in range(len(file_paths))]

    await asyncio.gather(*tasks)

asyncio.run(main())
