import os
import time
import random
import string

total_size_mb = int(input("Bitte geben Sie ein, wie groß der Ordner werden soll (in MB): "))

print(f"Es wird ein Ordner erstellt.")

confirmation = input("Möchten Sie fortfahren? (j/n): ")

if confirmation.lower() == 'j':
    
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