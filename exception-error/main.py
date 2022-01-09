# try:
#     file = open('a_file.txt')
#     a_dict = {"key": "value"}
#     print(a_dict['def'])
# except FileNotFoundError as nfe:
#     print(nfe)
#     file = open('a_file.txt', 'w')
#     file.write("hello world")
# except KeyError as error_message:
#     print(error_message)
# else:
#     content = file.read('a_file.txt')
#     print(content)
# finally:
#     raise KeyError("This is an error I made up")


height = float(input("Height: "))
weight = float(input("Weiht: "))

if height >= 3:
    raise ValueError("Human height should not be over 3")

print("here")
bmi = weight / height ** 2