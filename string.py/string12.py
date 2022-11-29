#removing charector from the given string
name='harinarayan'
l=''
b=len(name)
for i in range(b):
    if i!=1:
        l+=name[i]
print(l)