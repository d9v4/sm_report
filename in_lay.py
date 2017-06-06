def parse_name(name):
    dict = {'65': 221, '52': 374, '49': 414, '45': 500}
    index = name.find('*')
    marker = name[index - 2: index]
    return dict[marker]