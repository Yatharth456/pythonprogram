str='my name is yatharth@#$'
l=[]
li=[]
le=[]
for i in str:
    if i.isalpha():
        if i in 'aeiouAEIOU':
            l.append(i)
        else:
            li.append(i)
    else:
        le.append(i)
print(l)
print(li)
print(le)