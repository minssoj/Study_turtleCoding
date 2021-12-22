

a = [1,2,3,4,5,6]
b = [0] *6

# for i in zip(a,b):
#     print(i)

# print(list(zip(a,b)))
print(list(zip(*list(zip(a,b)))))
