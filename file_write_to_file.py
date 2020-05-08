# w, a --> it will create you a new file if file is not exist
# r+ --> both can done read and write

# with open('file1.txt', 'r+') as f :
#     f.seek(len(f.read()))
#     f.write('hi')

# read and write to another file

with open('file1.txt', 'r') as rf :
    with open('file2.txt', 'w') as wf :
        wf.write(rf.read())