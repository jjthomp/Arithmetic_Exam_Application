camel_case = list(input())
counter = 0
for i in camel_case:
    if i.isupper():
        camel_case.insert(counter, "_")
        camel_case.pop(counter + 1)
        camel_case.insert(counter + 1, i.lower())
    counter += 1
print(''.join(camel_case))

