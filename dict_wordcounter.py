def word_counter(string) :
    count = {}
    for char in string :
        count[char] = string.count(char)
    return count

print(word_counter('sourav'))