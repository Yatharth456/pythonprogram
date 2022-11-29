str='you are a lazy person but your fitness was to good'
l=[]
count=0
for i in str:
    if i in 'aeiouAEIOU':
        l.append(i)
        if i in l:
            count+=1
print(l)
print(count)