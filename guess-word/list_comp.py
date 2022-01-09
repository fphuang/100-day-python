squares = [n**2 for n in range(20)]
print(squares)

name = "fangping"
new_list = [ch for ch in name]
print(new_list)

my_set = {1, 2, 4, 5}
for n in my_set:
    print(n)

names = ["Alex", "Angela", "Dave", "Eileen", "Fangping"]
A_names = [name for name in names if name.lower().startswith('d')]
print(A_names)
