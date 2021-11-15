from os.path import exists

def read_rs_from_file():
    if exists('RS.csv'):
        with open('RS.csv', 'r', encoding='utf-8') as f:
            RS = f.readline().split(',')[:-1]
        return [int(x) for x in RS]
    else:
        raise OSError('File not found. Please generate RS.csv first!')
