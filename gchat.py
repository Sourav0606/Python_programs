fd = open("chat.txt")
chat = {}
data = []
for line in fd:
    name, msg = line.split(":")
    chat[name] = 0
    data.append(line)


for i in data:
    name, msg = i.split(':')
    chat[name] += len(msg)
print(chat)
