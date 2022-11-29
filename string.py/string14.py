#to print odd places charectors from given string
a='my name is harinarayan'
l=[]
for i in range(len(a)):
    if i%2!=0:
        l.append(a[i])
print(l)