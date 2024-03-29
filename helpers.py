def parse_keys():
    keys = []
    with open('data/keys.txt', "r") as f:
        for line in f:
            keys.append(line.rsplit("\n")[0])
    return keys
