math_operation = input('Введіть Операнд - оператор - операнд: ')

if math_operation[1] == '+':
    result_add = int(math_operation[0]) + int(math_operation[2])
    print('Результат операції додавання:', result_add)

elif math_operation[1] == '-':
    result_subtraction = int(math_operation[0]) - int(math_operation[2])
    print('Результат операції віднімання:', result_subtraction)

elif math_operation[1] == '*':
    result_multiplication = int(math_operation[0]) * int(math_operation[2])
    print('Результат операції множення:', result_multiplication)

elif math_operation[1] == '/' and math_operation[2] != 0 :
    result_division = int(math_operation[0]) / int(math_operation[2])
    print('Результат операції ділення:', result_division)
else:
    print("В даній версії інші оператори відсутні")


