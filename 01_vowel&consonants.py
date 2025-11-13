T = int(input())
for i in range(T):
    s = input().strip().lower()
    vowels = 0
    consonants = 0
    for ch in s:
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
    print(vowels, consonants)

