import random
import time
import timeit

def question_asker(question):
    print(question)
    response3 = False
    while not response3:
        save = input()
        if save == "yes" or save == "Yes" or save == "y" or save == "YES":
            response3 = True
            return True
        if save == "no" or save == "n" or save == "No" or save == "NO":
            response3 = True
            return False

        else:
            print("Incorrect format")
    return False



def main():
    operations = ["+", "-", "*"]
    n1 = 0
    n2 = 0
    correct_format = False
    correct_format2 = False
    response = 0
    count = 0
    pick = False
    level = 0
    levels_attempt = []
    leveldict = {
        1: "simple operations with numbers 2-9",
        2: "integral squares of 1-12"
    }

    name = UserInterface.name

    while not pick:
        print("""Which level do you want? Enter a number:
        1 - simple operations with numbers 2-9
        2 - integral squares of 1-12""")
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

    start = time.perf_counter()
    if level == 1:
        while count < 5:
            a = random.randint(2, 9)
            b = random.randint(2, 9)
            op = random.choice(operations)
            print(f"{a} {op} {b}")

            while not correct_format:
                try:
                    response = int(input())
                    correct_format = True
                except ValueError:
                    print("Wrong format! Try again")
                    correct_format = False

            if op == "+":
                result = int(a) + int(b)
            if op == "-":
                result = int(a) - int(b)
            if op == "*":
                result = int(a) * int(b)

            if response == result:
                print("Right!")
                n1 += 1
            else:
                print("Wrong!")
            count += 1
            correct_format = False

        levels_attempt.append(1)
        response2 = question_asker("Would you like to try level 2? Enter yes or no:")
        if response2:
            level = 2
            count = 0
        else:
            end = time.perf_counter()


    if level == 2:
        while count < 5:
            a = random.randint(1, 12)
            print(a)
            while not correct_format2:
                try:
                    response = int(input())
                    correct_format2 = True
                except ValueError:
                    print("Wrong format! Try again.")
                    correct_format2 = False

            result = a*a
            if response == result:
                print("Right!")
                n2 += 1
            else:
                print("Wrong!")
            count += 1
            correct_format2 = False

        end = time.perf_counter()
        levels_attempt.append(2)


    if len(levels_attempt) == 2:
        print(f"Your mark is {n1 + n2}/10.")
    elif levels_attempt.__contains__(1):
        print(f"Your mark is {n1}/5.")
    else:
        print(f"Your mark is {n2}/5.")

    total_time = (end - start)/60
    print(f"Total time to complete the exam was: {round(total_time, 2)} minutes")

    response1 = question_asker("Would you like to save your result to the file? Enter yes or no.")

    if response1:
        with open('results.txt', 'a') as f:
            f.write("\nNew attempt:\n")
            if levels_attempt.__contains__(1):
                f.write(f'{name}: {n1}/5 in level 1 ({leveldict[1]}). ')
            if levels_attempt.__contains__(2):
                f.write(f'{name}: {n2}/5 in level 2 ({leveldict[2]}). ')
            if len(levels_attempt) == 2:
                f.write(f"{name}'s total mark was {n1 + n2}/10.\n")
            elif levels_attempt.__contains__(1):
                f.write(f"{name}'s total mark was {n1}/5.\n")
            else:
                f.write(f"{name}'s total mark was {n2}/5.\n")
            f.write(f"{name} took {round(total_time, 2)} minutes to complete the assessment.\n")
            f.close()

        print('The results are saved in "results.txt".')
        print("Exiting Program")
        if not response1:
            print("Exiting program")


#if __name__ == "__main__":
    #main()


