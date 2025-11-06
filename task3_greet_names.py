while True:
    name = input("Enter a name (type 'done' to stop): ")

    if name.lower() == "done":  # stop when user types 'done'
        print("Goodbye!")
        break

    print(f"Hello, {name}!")