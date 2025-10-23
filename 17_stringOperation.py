A = input("Enter the string: ")

A = A * 2  # Concatenate with itself

result = ""
for ch in A:
    if ch.islower():
        if ch in "aeiou":
            result += "#"
        else:
            result += ch

print(result)
