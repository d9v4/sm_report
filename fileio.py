# -*- coding: utf-8 -*- 

def fileToDict(path):    
    f = open(path, 'r')
    st = f.read()
    st = st[:-1]
    sp = st.split('\n')
    f.close()
    return {a.split('#')[0]:a.split('#')[1] for a in sp}
    
def dictToFile(dict, path):
    f = open(path, 'w')
    for a in dict:
        f.write(a + '#' + dict[a] + '\n')
    f.close()
    
def fileToTuple(path):
    f = open(path, 'r')
    st = f.read()
    st = st[:-1]
    f.close()
    return st.split(';')
    
def tupleToFile(tuple, path):
    f = open(path, 'w')
    for a in tuple:
        f.write(a + ';')
    f.close()
    
if __name__ == "__main__":
    
    #d = fileToTuple('config\\test_w1.ini')
    #d.append('Петров Н.Н.')
    #tupleToFile(d, 'config\\test_w1.ini')
    
    d = fileToDict('config\\speed_of_size.ini')
    print(d)
    #dictToFile(d, 'config\\test_w1.ini')
    input()
