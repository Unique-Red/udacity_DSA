def make_list(number):
    names = []
    for item in range(number):
        names.append(input("Enter name: "))
    return names

number = int(input("Enter number of names: "))
names = make_list(number)
for name in names:
    if name[0] == "a":
        print("name: ", name)