#5 code
l='ram is my best FRiend $ ##'
b=l.split()
for i in b:
    if i in isalpha():
        print('yes')
    else:
        print('no')