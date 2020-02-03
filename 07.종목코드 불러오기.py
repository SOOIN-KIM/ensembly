



# code_txt = open(file='kosp_list', mode= 'r',encoding='UTF-8')
#
# for lines in range(1567):
#     line = code_txt.readline()
#     print(line)
# print()

import pandas as pd


code_txt = pd.read_csv('kosp_list', encoding='UTF-8',header=0)
code_1 = code_txt['0']
code_2 = code_1.tolist()
print(code_2)
for code in code_2:
    print(code)


# def code_hub(code_txt):
#     code_txt = pd.read_csv('kosp_list', sep=',', encoding='UTF-8')
#     code = code_txt['0']
#     code.tolist()

