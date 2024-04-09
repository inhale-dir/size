import os
import time

total_size_mb = int(input("Bitte geben Sie ein, wie groß der Ordner werden soll (in MB): "))

print(f"Es wird ein Ordner erstellt.")

confirmation = input("Möchten Sie fortfahren? (j/n): ")

if confirmation.lower() == 'j':
    start_time = time.time()

    os.mkdir("Ordner")
    os.chdir("Ordner")

    with open('dummy', 'wb') as f:
        f.write(os.urandom(total_size_mb * 1024 * 1024))

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Ordner erstellt in {elapsed_time} Sekunden.")
else:
    print("Vorgang abgebrochen.")