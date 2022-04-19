def pars_files(files_list):
    dict_files1 = {}
    dict_files2 = {}
    for file in files_list:
        with open(file, 'r', encoding='utf-8') as fi:
            Si = []
            for line in fi:
                Si += [line]
            dict_files1[fi.name] = len(Si)
            dict_files2[fi.name] = Si
    return dict_files1, dict_files2

def cum_file(f_list, cum_file_name):
    dict_files1, dict_files2 = pars_files(files)
    T = ''
    while len(dict_files1) > 0:
        Ni = min(dict_files1, key=dict_files1.get)
        T += Ni + '\n'
        T += str(dict_files1[Ni]) + '\n'
        for x in dict_files2[Ni]:
            T += x
        dict_files1.pop(Ni)
        dict_files2.pop(Ni)
    fw = open('cum.txt', 'w', encoding='utf-8')
    fw.write(T)
    fw.close()

files = ['1.txt', '2.txt', '3.txt']
cum_file_name = 'cum.txt'

cum_file(files, cum_file_name)
