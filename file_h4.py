n=int(input())
with open('sample.txt')as f:
    print(list(f)[-n])


