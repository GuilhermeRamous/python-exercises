def in_function_one(value1, value2):
    if type(value1) != type(value2):
        return False
    else:
        for i in range(len(value2)):
            if value1 == value2[i]:
                return True
            elif i == len(value2) - 1:
                return False

print(in_function_one("a", [1, 2, 3]))
print(in_function_one("a", "anta"))
print(in_function_one([1], [1, 2, 3]))
print(in_function_one("jjd", "aaaa"))
print(in_function_one([2], [1, 3, 45]))
