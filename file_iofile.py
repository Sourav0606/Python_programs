# readfile
# open function
# seek method
# tell method
# readline method
# readlines methods
# close method

# f = open('chat.txt')
# print(f"cursor position - {f.tell()}")
# print(f.read())
# print(f"cursor position - {f.tell()}")
# print('before seek method')
# f.seek(0)
# print('after seek method')
# print(f"cursor position - {f.tell()}")
# print(f.read())

# print(f.readline())

# lines = f.readlines()
# print(len(lines))
# for line in lines :
#     print(line, end = '')

# name, closed
print(f.name)

# f = open(r"filepath copy from pc")

f.close()

print(f.closed)