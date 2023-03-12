# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы

def print_operation_table(operation,row,column):
    [print(j,end='\t') for j in range(1,column+1)]  # печатаем верхнюю строку
    print('')
    for i in range(2,row+1):  # печатаем остальные строки
        print(i,end='\t')
        [print(operation(j,i),end='\t') for j in range(2,column+1)]
        print('')


print_operation_table(lambda x,y: x*y, 6, 6)

