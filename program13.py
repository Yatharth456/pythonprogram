#13 code
l=[1,3,'naman',5,95,'neel',62]
new_l=[]
for i in l:
    if i is not isalpha():
        new_l.append(i)
print(new_l)