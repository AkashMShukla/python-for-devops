my_list = [1, 4.6, "Apple", "Akash", "DevOps"]
print(my_list)
print(my_list[3])
print(len(my_list))

my_list.append("Great")
print(my_list)

my_list.remove("Apple")
print(my_list)

sublist = my_list[2:4]
print(sublist)

concate_list = sublist + my_list
print(concate_list)

sublist.sort()
print(sublist)

print('DevOps' in sublist)


concate_list = sublist + ["Nice"]
print(concate_list)