import classes

def main():
    """Основная функция"""

    print('Задание Е1')
    print(classes.query1(classes.one_to_many))
    
    print('\nЗадание Е2')
    print(classes.query2(classes.one_to_many))

    print('\nЗадание Е3')
    print(classes.query3(classes.many_to_many))


if __name__ == '__main__':
    main()


