import threading
import os

base_path = "/home/aravinds/directory_env/acl to databricks before and after/"
output_path = "/home/aravinds/directory_env/acl to databricks before and after/Thread output"

# List of file names
input_files = [os.path.join(base_path, filename) for filename in
               ["001 after.txt", "001 before.txt", "003 after.txt", "24 after.txt", "003 before.txt"]]
output_files = [os.path.join(output_path, "output_" + filename) for filename in
                ["001 after.txt", "001 before.txt", "003 after.txt", "24 after.txt", "003 before.txt"]]

def read_and_save(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            content = infile.read()

        with open(output_file, "w") as outfile:
            outfile.write(content)

        print(f"Successfully processed {input_file} -> {output_file}")

    except Exception as e:
        print(f"Error processing {input_file}: {e}")

# List to store threads
threads = []

# Creating and starting threads
for i in range(len(input_files)):
    thread = threading.Thread(target=read_and_save, args=(input_files[i], output_files[i]))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All files processed successfully!")

