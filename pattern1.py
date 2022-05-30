n=int(input("Enter a number of Rows"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
