import pandas as pd

# 读取制表符分隔的文件（.txt 或 .tsv）
file_path = 'C:/Users/rainc/Desktop/1-1-111制表符分隔.txt'
data = pd.read_csv(file_path, sep="\t")

# 保存为新的 CSV 文件
data.to_csv("converted_output.csv", index=False)


