# f = open('txt', 'a', encoding='UTF-8')
# print(f)

# file = open('txt', 'a', encoding='utf-8')
# file.write('hello T/n')

# f = open('txt', 'a', encoding='utf-8')
# print(f.read())


while True:
    print('1 - добавить запись/n2 - выйти из программы')
    us1 = int(input('ваш выбор :'))
    if us1 == 1:
        name=input('введите ваше ФИО :') 
        if ' ' in name:
            first_name=name.split()[0]
            second_name=name.split()[1]
            if len(first_name) > 2 and len(second_name) > 3:
                try:
                    nomer=int(input('введите ваш номер телефона :'))
                    if len(str(nomer)) >9 or len(str(nomer)) <=12:
                        try:
                            god_roj=int(input('введите ваш год рождения :'))
                            if god_roj > 1930 and god_roj <2023:
                                address=input('введите ваш адрес проживания :')
                                if len(address) > 3:
                                    lst=[name, nomer, god_roj, address]
                                else:
                                    print('место проживания пиши правильно')
                                    continue
                            else:
                                print('ты шо?')
                                continue
                        except ValueError:  
                            print('пиши цифры :') 
                    else:
                        print('пиши полный номер :')
                    with open ('txt', 'a', encoding=)'ng='utf-8' as f:
                        print(*lst, file=f)
                except ValueError:
                    print(lst)
        elif us1==2:
            break
                        
                    

                    print(lst)
            with open('txt', 'a', encoding='utf-8') as f:
                        print(*lst, file=f)
        elif us1==2:
                        # break
                        


                    