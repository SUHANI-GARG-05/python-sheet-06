A = input("Enter the main string: ")
B = input("Enter the substring: ")

if B in A:
    print(A.index(B))
else:
    print("Substring not found")
