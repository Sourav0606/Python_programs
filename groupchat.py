data="""sourav:hi
guddu:hello
sourav:how are you?
guddu:good
guddu:good morning
sourav:gd mrng"""

data=[i for i in data.split('\n') if len(i)>2]
data={i.split(':')[0].strip():i.split(':')[1].strip() for i in data}

print(data)


print(len(data['sourav']))
#print(len(data['guddu']))
      
