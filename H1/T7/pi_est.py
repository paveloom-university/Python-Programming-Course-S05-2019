def est_pi(N):
    '''
    Метод для вычисления числа pi
    по формуле, перемножающей N членов
    :param N: Число членов в формуле
    '''

    # Начальное значение итератора числителя
    ia = 2

    # Начальное значение итератора знаменателя
    ib = 1

    # Начальные значения числителя и знаменателя
    a = b = 1

    # Вычисление значений числителей и знаменателей при N-членах
    for i in range(N):

        a *= ia

        b *= ib

        if i%2 == 1:
            ia += 2
        else:
            ib += 2

    # Вывод результата
    return a / b * 2