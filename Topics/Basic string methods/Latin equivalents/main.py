name = input()

def normalize(name):

    # put your code here
    num = len(name)
    new_name = name.replace('é', "e", num)
    new_name = new_name.replace('ë', "e", num)
    new_name = new_name.replace('á', "a", num)
    new_name = new_name.replace('å', "aa", num)
    new_name = new_name.replace('œ', "oe", num)
    new_name = new_name.replace('æ', "ae", num)

    return new_name

print(normalize(name))
