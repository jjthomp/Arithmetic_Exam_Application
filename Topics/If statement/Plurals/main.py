number = int(input())
word = input()

# write a condition for plurals
if not(number == 1):
    word += 's'

print(number, word)
