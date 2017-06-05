import test12
from datetime import datetime
import time
import random

time_sm = datetime.strftime(datetime.now(), "%d.%m.%Y")
#file = open('\\text\\Python_Project\\Raport_project\\test.txt', 'w')

master_list = ['Гнатюк Д.А', 'Подручный А.Н.', 'Купчишин Е.Е']
control_list = ['Камеристова', 'Захарова', 'Короткова', 'Погожина']


def view_list(list):
    x = 0
    i = 0
    while i < len(list):
        print(list[i] + ' ' * (20 - len(list[i])) + str(i+1))
        i = i + 1
    while True:
        x = input_num('')
        if x >= 1 and x <= len(list):
            break
        else:
            print('Что то тут не так...')
    return x
        
def input_num(name):
    n = 0
    while True:
        n = input(name + ' ' * (30 - len(name)))
        if n.isdigit(): 
            break
        else: print('Введите число')
    return int(n)

def check_blank_unit(blanks, cm):
    if blanks == 0:
        return -1
    
    c = blanks - cm % blanks
    
    if c == blanks:
        return 0
    else:
        return c
    
def effect(time, speed, cm, flag = 'e'):
    
    plain = time * 60 - cm / speed
    
    if flag == 'p':
        return int(plain)
    else:
        x = int(100 - (plain / (time * 60)) * 100 )
        return x

def divide_time_palin_list(plain, line = 2):
    
    if plain > 450:                                 #проверяем на MAX время
        return -1
    
    p_ratio = int(plain / 450 * 25)                      #значение единицы минимального простоя
    print('min ед.', p_ratio)
    #file.write('min ед.'+ ' ' +str(p_ratio) + ' \n')
    
    num_plain1 = [3, 9, 11, 12, 13, 14, 
                  15, 16, 17, 20, 21, 22, 
                  26, 28, 29, 31]
    
    num_plain = ['Замена бухты медной проволоки',
                 'OCSAM - настройка', 'AFB - магазин бланков жести',
                 'AFB - округление', 'AFB - транспортировка',
                 'AFB - перекрытие (нахлест)', 'AFB - форма обечайки', 
                 'AFB - сварной ток', 'AFB - обрыв проволоки', 
                 'CF - подача баллонов', 'CF - выльцовка горловин', 
                 'CF - выльцовка донышек', 'ТЕСТЕР - настройка', 
                 'ПАЛЛЕТАЙЗЕР - настройка', 'ПАЛЛЕТАЙЗЕР - падение баллонов', 
                 'ТС - настройка']
    
    if line == 1:
        num_plain.append('Замена баллона с инертным газом')
        num_plain.append('AFB - лакировка')
        num_plain1.append(4)
        num_plain1.append(18)
    
    count = 0        
    pl = plain
    pl_list = []
    
    
    while True:
        p = pl
        pl_list = []
        #print(p)
        
        while True:
            if p < 30:
                pl_list.append(p)
                break
            else:
                r = int(random.random() * 30)
                if r > p_ratio:
                    pl_list.append(r)
                    p = p - r                       #вычитаем случайное значение из оставшегося простоя
        
        count = count + 1
        
        if len(pl_list) <= len(num_plain):          #проверяем не превышает ли кол-во простоев список наименований
            print('кол-во проходов', count)
            #file.write('кол-во проходов' + ' ' + str(count) + '\n'*2)
            break                                   #все нормально? выходим
    
    num_plain_random = random.sample(num_plain, len(pl_list))
    plain_dict = {num_plain_random[x]: pl_list[x] for x in range(len(pl_list))}
    return plain_dict
    
def for_testing_view():
    tr = divide_time_palin_list(int(time_test_min), 1)
    x1 = 0
    first_string = 'Сварка - ' + str(cm) + 'Ланико - ' + str(cf) + 'Итог - ' + str(pr * 2244 + pr_h)
    
    print(first_string)
    #file.write(first_string + '\n')
    
    for key, value in tr.items():
        v = str(time_sm +' '+ master_list[master-1] +' '+ control_list[control-1]+ ' ' )          #подготовка строк к записи\выводу на экран
        s = ''.join((key,'-' * (50 - len(key)), str(value)))                                      #
        final_string = v + s
        print(final_string)
        #file.write(final_string + '\n')
        x1 = x1 + value
        
    print(x1)
    
    
print(test12.imeg)

    

master = view_list(master_list)
control = view_list(control_list)

blanks = input_num("Бланков на листе")
cm = input_num('Сварка')
cf = input_num("Ланико")
pr = input_num("Кол-во полных паллет")
pr_h = input_num("На неполной")
speed = input_num("Скорость")
time = input_num("Рабочий день в часах")

time_test_min = input_num('Простой в минутах')

#print(' мастер', '     контролер', '\n'*2,master_list[master - 1], 
#control_list[control - 1], cm, cf, pr, pr_h)
#print('Простой', int(plain), ' ', int(effect), ' %')

#print(effect(time, speed, cm), effect(time, speed, cm, 'p'))

#print('Бланков до целого листа ', check_blank_unit(blanks, cm))


for_testing_view()



#test = input('простой - ')
#ttt = time.time()
"""
for x in range(451):
    for_testing_view(x)
    file.write('\n'*3)

"""
#ttt1 = time.time()
#print(ttt1 - ttt)

#file.close()
input()



    
