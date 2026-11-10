# Task 2 - Simple Key Logger (Safe Lab Version)
# Only what is typed in this program's window will be logged

print("Keylogger started... Type something, type 'exit' to stop")

with open("keylog.txt", "a") as file:
    while True:
        key = input("Type: ")
        if key.lower() == "exit":
            print("Keylogger stopped. Data saved in keylog.txt")
            break
        file.write(key + "\n")
        file.flush()
        print(f"Logged: {key}")
