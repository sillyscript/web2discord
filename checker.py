def checkIfNew(title):
    with open("database.txt", "r") as f:
        lines = f.read().splitlines()
    if title in lines:
        return False
    else:
        with open("database.txt", "a") as f:
            f.write(title + "\n")
        return True
