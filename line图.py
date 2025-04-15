

# 读取制表符分隔的文件（.txt 或 .tsv）
"""
file_path = 'C:/Users/rainc/Desktop/1-1-111制表符分隔.txt'
data = pd.read_csv(file_path, sep="\t")

# 保存为新的 CSV 文件
data.to_csv("converted_output.csv", index=False)
"""

import calendar
import pandas as pd

a = calendar.calendar(2025,w=2,l=1,c=6)
#print(a)
with open('wenjiantest.txt', 'w') as f:
 f.write(' book \n book')
 f.write(a)
b=pd.read_table('wenjiantest.txt')
b.to_csv('aaa.csv')
