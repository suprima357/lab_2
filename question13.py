text = input("Enter the text: ")

freq = {}

for char in text:
    if char.isalpha():
        char_lower = char.lower()
        if char_lower in freq:
            freq[char_lower] += 1
        else:
            freq[char_lower] = 1

for char in freq:
    print(char + ":", freq[char])
