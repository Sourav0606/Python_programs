square = {f"square if {num} is" : num**2 for num in range(1, 11)}
for k, v in square.items() :
    print(f"{k} : {v}")

string = "sourav"
word_counter = {char : string.count(char) for char in string}
print(word_counter)