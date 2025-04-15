import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体 + 负号支持
#plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 或者 ['Microsoft YaHei']
#plt.rcParams['axes.unicode_minus'] = False

# 读取数据
#df = pd.read_csv("南宁市监测站-air-quality.csv")
df = pd.read_csv("西安长安区-air-quality.csv")

# 清洗列名 + 转换
df.columns = df.columns.str.strip()
df["pm25"] = pd.to_numeric(df["pm25"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date", "pm25"])

# 提取年、月日
df["year"] = df["date"].dt.year
df["month_day"] = df["date"].dt.strftime("%m-%d")

# ✅ 关键：将 month_day 转成有序类别，保证横坐标顺序正确
ordered_days = pd.date_range("2000-01-01", "2000-12-31", freq="D").strftime("%m-%d")
df["month_day"] = pd.Categorical(df["month_day"], categories=ordered_days, ordered=True)

# 作图
#plt.figure(figsize=(16, 9))
sns.set_theme(style="darkgrid")

sns.relplot(data=df, x="month_day", y="pm25", hue="year", kind='scatter', size=1)#, size=1)
plt.ylim(0, 420)
plt.title("xian PM2.5 10 years")
plt.xlabel("day")
plt.ylabel("PM2.5 (μg/m³)")
# 从已有横坐标中每隔15天取一个显示
xtick_locations = df["month_day"].cat.categories[::15]
plt.xticks(xtick_locations, rotation=45)

#plt.xticks(rotation=45)
plt.legend(title="year", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("pm25趋势图.png", dpi=400, bbox_inches='tight')
plt.show()




