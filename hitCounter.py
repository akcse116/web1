filename = "hit_log.txt"


def count():
    with open(filename, 'r') as f:
        reader = int(f.read())
    with open(filename, 'w') as x:
        x.write(str(reader + 1))
