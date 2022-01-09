# with open("main.py") as file:
#     contents = file.read()
#     print(contents)

with open('./clone.py', mode='w') as clone:
    with open("./main.py") as main:
        content = main.read()
        clone.write(content)
