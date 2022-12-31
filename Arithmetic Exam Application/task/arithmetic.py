import random
operations = ["+", "-", "*"]
n = 0
format = False
response = 0
count = 0
pick = False
level = 0
leveldict = {
  1: "simple operations with numbers 2-9",
  2: "integral squares of 11-29"
}


while not pick:
    print("""Which level do you want? Enter a number:
    1 - simple operations with numbers 2-9
    2 - integral squares of 11-29""")
    try:
        level = int(input())
        pick = True
    except ValueError:
        print("Incorrect format.")
        pick = False
    if pick:
        if level > 2 or level < 1:
            pick = False
            print("Incorrect format.")

if level == 1:
    while count < 5:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        op = random.choice(operations)
        print(f"{a} {op} {b}")

        while not format:
            try:
                response = int(input())
                format = True
            except ValueError:
                print("Wrong format! Try again")
                format = False

        if op == "+":
            result = int(a) + int(b)
        if op == "-":
            result = int(a) - int(b)
        if op == "*":
            result = int(a) * int(b)
        if response == result:
            print("Right!")
            n += 1
        else:
            print("Wrong!")
        count += 1
        format = False

if level == 2:
    while count < 5:
        a = random.randint(11, 29)
        print(a)
        while not format:
            try:
                response = int(input())
                format = True
            except ValueError:
                print("Wrong format! Try again.")
                format = False

        result = a*a
        if response == result:
            print("Right!")
            n += 1
        else:
            print("Wrong!")
        count += 1
        format = False

print(f"Your mark is {n}/5. Would you like to save the result? Enter yes or no.")
save = input()
if save == "yes" or save == "Yes" or save == "y" or save == "yes":
    print("What is your name?")
    name = input()
    with open('results.txt', 'a') as f:
        f.write(f'{name}: {n}/5 in level {level} ({leveldict[level]}). ')
    print('The results are saved in "results.txt".')
