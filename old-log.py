# small utilities, no deps

def flatten(xs):
    return [y for x in xs for y in x]

if __name__ == "__main__":
    print(list(chunks(range(25), 10)))
