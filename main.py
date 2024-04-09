import os
import time
import random
import string

total_size_mb = int(input("Size of the file (in MB): "))

print(f"Folder for the file will be created.")

confirmation = input("process? (y/n): ")

if confirmation.lower() == 'y':
    
    folder_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

    os.mkdir(folder_name)

    os.chdir(folder_name)

    start_time = time.time()

    with open(f'dummy {total_size_mb}mb', 'wb') as f:
        f.write(os.urandom(total_size_mb * 1024 * 1024))

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"{total_size_mb}mb in {elapsed_time} seconds created.")
else:
    print("aborted.")