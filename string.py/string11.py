#code for checking user given string is palindrome or not.
name=input('enter any name to check palindrome')
b=name[::-1]
if b==name:
    print('it is palindrome')
else:
    print('no,its not a palindrome')