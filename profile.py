# -*- coding: utf-8 -*- 

from view_cons import prtup as prt

class profile:
    st = 'none'
    flag = False
    path = 'config\\profile.ini'
    
    def __init__(self, path = self.path):              
        self.prof = self.fileToList(self.path)                 
        print(self.st)
    
    def fileToList(self, path):
        f = open(path, 'r')
        st = f.read()
        st = st[:-1]
        f.close()
        return list(st.split(';'))
    
    def listToFile(self, plist, path):
        f = open(path, 'w')
        for a in plist:
            f.write(a + ';')
        f.close()
    
    def set_value(self, value):
        if value >= len(self.prof) or value < 0:                    # здесь устанавливаем 
            return -1                                        # какой профиль используется
        else:                                           # проверка что бы не выйти за границу кортежа с профилями
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
            
    def set_path(self, path)
        if type(path) == str:
            self.path = path  
        else:
            return -1

            
if __name__ == "__main__":
    
    
    l = profile()
    
    print(l.get_list())
    l.set_value(1)
    print(l.get_str())
    l.set_str('jjjjjjdsss')
    print(l.get_str())
    l.save()
    #prt(l.get_m())
    #print(t)
    #l.set_value(50)
    #print(l.get_value())
    #prt(l.get_m())
    
    
    input()