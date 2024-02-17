a = int(input('Enter first number '))
b = int(input('Enter second number '))
operation = input('Select a math operation: +, -, *, /\n')
if operation == '+':
    print(a,'+',b,'=', a+b)
elif operation == '-':
    print(a,'-',b,'=', a-b)
elif operation == '*':
    print(a,'*',b,'=', a*b)
elif operation == '/':
    if b !=0:
        print(a,'/',b,'=', a/b)
    else:
        print('Error')
else:
    print('You have not typed a valid operator')
