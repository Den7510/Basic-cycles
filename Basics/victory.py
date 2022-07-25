# kolumb = 1451
# enchtein = 1879
# puchkin = 1799
# paster = 1822
# galilei = 1564
str = 'да'
while str == 'да':
    may_list = [1451, 1879, 1799, 1822, 1564]
    i=0
    for i in may_list:
        kolumb = int(input('укажите год рождения  Колумба: '))
        if kolumb != may_list[0]:
            print(kolumb)
            print('Правильный ответ: ')
            print(may_list[0])
        elif kolumb == may_list[0]:
            print(kolumb)
        break

    for i in may_list:
        enchtein = int(input('укажите год рождения  Энштейна: '))
        if enchtein != may_list[1]:
            print(enchtein)
            print('Правильный ответ: ')
            print(may_list[1])
        elif enchtein == may_list[1]:
            print(enchtein)
        break
    for i in may_list:
        puchkin = int(input('укажите год рождения  Пушкин: '))
        if puchkin != may_list[2]:
            print(puchkin)
            print('Правильный ответ: ')
            print(may_list[2])
        elif puchkin == may_list[2]:
            print(puchkin)
        break
    for i in may_list:
        paster = int(input('укажите год рождения  Пастера: '))
        if paster != may_list[3]:
            print(paster)
            print('Правильный ответ: ')
            print(may_list[3])
        elif paster == may_list[3]:
            print(paster)
        break
    for i in may_list:
        galilei = int(input('укажите год рождения  Галлилея: '))
        if galilei != may_list[4]:
            print(galilei)
            print('Правильный ответ: ')
            print(may_list[4])
        elif galilei == may_list[4]:
            print(galilei)
        break
    may_list1 = [kolumb, enchtein, puchkin, paster, galilei]
    ok_list = []
    ko_list = []
    ok_list1 = 0
    ok_list2 = 0
    ok_list3 = 0
    ok_list4 = 0
    ok_list5 = 0
    ko_list1 = 0
    ko_list2 = 0
    ko_list3 = 0
    ko_list4 = 0
    ko_list5 = 0
    for i in may_list1:
        if may_list1[0] == may_list[0]:
            ok_list1 = may_list1[0]

        else:
            may_list1[0] != may_list[0]
            ko_list1 = may_list1[0]

    for i in may_list1:
        if may_list1[1] == may_list[1]:
            ok_list2 = may_list1[1]

        else:
            may_list1[1] != may_list[1]
            ko_list2 = may_list1[1]

    for i in may_list1:
        if may_list1[2] == may_list[2]:
            ok_list3 = may_list1[2]

        else:
            may_list1[2] != may_list[2]
            ko_list3 = may_list1[2]

    for i in may_list1:
        if may_list1[3] == may_list[3]:
            ok_list4 = may_list1[3]

        else:
            may_list1[3] != may_list[3]
            ko_list4 = may_list1[3]

    for i in may_list1:
        if may_list1[4] == may_list[4]:
            ok_list5 = may_list1[4]

        else:
            may_list1[4] != may_list[4]
            ko_list5 = may_list1[4]

    ok_list = [ok_list1, ok_list2, ok_list3, ok_list4, ok_list5]
    ko_list = [ko_list1, ko_list2, ko_list3, ko_list4, ko_list5]
    sum_list = set(ok_list)
    sum_list1 = set(ko_list)
    set.discard(sum_list, 0)
    set.discard(sum_list1, 0)
    # print(sum_list1)
    right = 0
    no_right = 0

    if len(sum_list) < len(ok_list):
        print("Правильных ответов: ")
        pright = len(sum_list)
        print(pright)
    elif len(ok_list) == len(sum_list):
        print(sum_list)
        print("Правильных ответов: ")
        right = len(sum_list)
        print(right)
    if len(sum_list1) < len(ko_list):
        print("Неправильных ответов: ")
        no_pright = len(sum_list1)
        print(no_pright)
    elif len(sum_list1) == len(ko_list):
         print("Неправильных ответов: ")
         no_right = len(sum_list1)
         print(no_right)
    p1 = 0
    p11 = 0
    if len(sum_list) <= 4:
         print('Статистика правильных ответов: ')
         p1 = pright*100/5
         print(p1, '%')
    else:
        len(sum_list) == 5
        print('Статистика правильных ответов: ')
        p11 = right*100/5
        print(p11, '%', type(p11))
    p2 = 0
    p22 = 0
    if len(sum_list1) <= 4:
       print('Статистика неправильных ответов: ')
       p2 = no_pright*100/5
       print(p2, '%')
    else:
        len(sum_list1) == 5
        print('Статистика неправильных ответов: ')
        p22 = no_right*100/5
        print(p22, '%')

    str1 = 'нет'
    print('Хотите продолжить отгадывать векторину? ')
    if input() == str1:
        print('end')
        break
    else:
        continue










