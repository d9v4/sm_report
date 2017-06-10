# -*- coding: utf-8 -*- 

from view_cons import prtup as prt

ch = '''
c - изменить
s - сохранить
d - удалить
a - добавить
'''

class profile:
    st = 'none'                                                 # значение строки профиля по умолчанию 
    flag = False                                                # флаг для проверки существует ли value
     
    def __init__(self, path = 'config\\profile.ini'):           # конструктор, путь по умолчанию     
        self.path = path
        self.prof = self.fileToList(self.path)                 
        
    
    def fileToList(self, path):                                 # метод востановления списка из файла
        try:
            f = open(path, 'r')
            st = f.read()
            st = st[:-1]
            f.close()
            return list(st.split(';'))
        except Exception:
            print('ошибка при загрузке файла')
    
    def listToFile(self, plist, path):                          # метод записи списка в файл
        try:
            f = open(path, 'w')
            for a in plist:
                f.write(a + ';')
            f.close()
        except Exception:
            print('ошибка при выгрузке в файл')
    
    def set_value(self, value):
        if value >= len(self.prof) or value < 0:                # здесь устанавливаем 
            return -1                                           # какой профиль используется
        else:                                                   # проверка что бы не выйти за границу кортежа с профилями
            self.value = value
            self.st = self.prof[value]
            self.flag = True
            
    def set_str(self, st):
        self.st = st
    
    def get_str(self):
        return self.st
    
    def get_list(self):
        return self.prof
    
    def save(self):
        if self.flag == True:
            self.prof[self.value] = self.st
            self.listToFile(self.prof, self.path)
            
    def addProf(self):
        if self.st in self.prof:
            return 0
        else:
            if self.flag == True:
                self.prof.append(self.st)
                self.listToFile(self.prof, self.path)
    
    def set_path(self, path):
        if type(path) == str:
            self.path = path  
        else:
            return -1
      
    def delpr(self):
        if self.flag == True:
            self.prof.pop([value])
           
if __name__ == "__main__":
    l = profile()
    
    flag = False
    while True:
        print('Выберите профиль:')
        prt(l.get_list())                       # добавить сюда условие выбора профиля
        l.set_value(int(input('номер профиля - ')))
        print(l.get_str())
        re = input('1 - выбрать другой, 2 - редактировать, enter - продолжить\n')
        if re == '1':
            pass
        elif re == '2':
            while True:
                print(l.get_str())
                p = input(ch)
                if p == 'c':            # изменить строку
                    print('изменить строку')
                elif p == 's':          # сохранить изменения
                    print('сохранить изменения')
                elif p == 'd':          # удалить запись
                    print('удалить запись')
                elif p == 'a':          # добавить новой записью
                    print('добавить запись')
                else:
                    break
        else:
            break
    print('работа основной программы')
    input()