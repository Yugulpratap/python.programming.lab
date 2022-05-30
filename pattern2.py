n=int(input("Enter a rows"))
k=ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
    print()
