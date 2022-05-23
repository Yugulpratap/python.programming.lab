f=open('sample.txt','r')
n=int(input('Enter number of lines'))
for i in range(n):
    data=f.readline()
    print(data)
f.close()
