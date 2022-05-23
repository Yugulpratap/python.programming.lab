f=open('sample.txt','r')
data=f.read()
words=data.split()
print(words)
print (len(words))
f.close
