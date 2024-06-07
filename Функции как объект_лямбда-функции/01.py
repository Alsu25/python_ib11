def arithmetic_operation(op):
    return eval('lambda x, y: x' + op + 'y')


operation = arithmetic_operation('+')
print(operation(1, 4))