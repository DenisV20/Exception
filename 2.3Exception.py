stack = ['+','-', '*', '/']

try:
  c = input('Введите оператор: ')
  assert c in stack, 'Данного оператора нет в списке'
  a = int(input('Введите число a: '))
  b = int(input('Введите число b: '))
  if c == '+':
    print(a + b)
  elif c == '-':
    print(a - b)
  elif c == '/':
    print(a / b)
  elif c == '*':
    print(a * b)

except AssertionError:
  print('Данного оператора нет в списке')
except ZeroDivisionError:
  print('Делить на ноль нельзя')
except ValueError:
  print('Делить строки нельзя')






