Status = True
try:
    while Status:
        first_num = int(input("Type in your first number: "))

        if type(first_num) == int:
            Status = False
        else:
            print('Type in a number!')

        second_num = int(input("Type in your second number: "))
        if type(first_num) == int:
            Status = False
        else:
            print('Type in a number!')

        operation = input('Type in add, subtract, multiply, or divide: ')
        if operation.lower() == 'add':
            print('The answer is:' , first_num + second_num)
        elif operation.lower() == 'subtract':
            print('The answer is:' , first_num - second_num)
        elif operation.lower() == 'multiply':
            print('The answer is:' , first_num * second_num)
        elif operation.lower() == 'divide':
            print('The answer is:' ,first_num / second_num)
        else:
            print('Please choose one of the options!')
except:
    print('Something went wrong please try again')