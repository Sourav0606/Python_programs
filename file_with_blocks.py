with open('chat.txt') as f :
    data = f.read()
    print(len(data))

print(f.closed)