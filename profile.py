# -*- coding: utf-8 -*- 

import fileio as iof
from view_cons import prtup as prt

class profile:
    def __init__(self):
        self.masters = iof.fileToTuple('config\\masters.ini')                 # загружаем 
        self.controls = iof.fileToTuple('config\\controls.ini')                    # значения 
        self.prof = iof.fileToTuple('config\\profile.ini')                             # из файлов
        self.list = []
        for a in self.prof:
            r = a.split(',')
            sm = r[0]
            m = int(r[1])
            c = int(r[2]) 
            st = sm + ' ' + self.masters[m] + ' ' + self.controls[c]
            self.list.append(st)
    
    def get_m(self):
        return self.list
    
    def set_value(self, value):
        if value >= len(self.prof) or value < 0:                    # здесь устанавливаем 
            return -1                                        # какой профиль используется
        else:                                           # проверка что бы не выйти за границу кортежа с профилями
            self.value = value
    
    def get_value(self):                                # отдать значение 
        if hasattr(self, 'value'):                  # проверить 
            return self.value                   # существует ли
        else:
            return -1
        
if __name__ == "__main__":
    
    l = profile()
    prt(l.get_m())
    #print(t)
    #l.set_value(50)
    #print(l.get_value())
    #prt(l.get_m())
    
    
    input()