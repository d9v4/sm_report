def fileToDict(path):    
    f = open(path, 'r')
    st = f.read()
    sp = st.split('\n')
    f.close()
    return {a.split('#')[0]:a.split('#')[1] for a in sp}
    
def fileToTuple(path):
    f = open(path, 'r')
    st = f.read()
    f.close()
    return st.split(';')
    
def tupleToFile(tuple, path):
    f = open(path, 'w')
    for a in tuple:
        f.write(a + ';')
    f.close()
    
if __name__ == "__main__":
    print(fileToDict('config\speed_of_size.ini'))
    input()
