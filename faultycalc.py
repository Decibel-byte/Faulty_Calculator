def calculator ():
    operator = input("Enter the operator from the following to be performed : \n + : Addition \n - : Subtraction \n * : Multiplication \n / : Division \n ** : Power \n // : Floor Division \n ")
    num1 = float(input('Enter the first number : '))
    num2 = float(input('Enter the second number : '))
    if (num1==45 and num2==3 and operator=='*'):
        print('45*3 = 555')
    elif (num1==56 and num2==9 and operator=='+'):
        print('56+9 = 77')
    elif (num1==56 and num2==6 and operator=='/'):
        print('56/6 = 4')
    elif (operator == '+'):
        print(num1+num2)
    elif (operator == '-'):
        print(num1-num2)
    elif (operator == '*'):
        print(num1*num2)
    elif (operator == '/'):
        print(num1/num2)
    elif (operator == '**'):
        print(num1**num2)
    elif (operator == '//'):
        print(num1//num2)
    else : 
        print('Error! Enter the correct operator')
calculator()
while (True):
    user = input('Do you want to perform calculations again? Press "Y" for YES or "N" for NO : ')
    if (user == 'Y'):
        calculator()
    else :
        print('Goodbye!')
        break