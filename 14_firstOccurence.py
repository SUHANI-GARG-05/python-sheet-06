A = input("Enter a string: ")
B = int(input("Enter ASCII code: "))

for i in range(len(A)):
    if ord(A[i]) == B:
        print(i)
        break
else:
    print("Character not found")
