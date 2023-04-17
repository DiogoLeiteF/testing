

def vouel_count(string):
    vowels = ["a", "e", "i", "o", "u"]

    count = 0

    for ch in string:
        if ch.lower() in vowels:
            count +=1
    return count


def shortLong(string):
    list = string.split()
    if len(list) > 0:
        short = list[0]
        long = list[0]
        for i in list:
            if len(i) < len(short):
                short = i
            if len(i) > len(long):
                long = i
        return [short, long]
    return None
