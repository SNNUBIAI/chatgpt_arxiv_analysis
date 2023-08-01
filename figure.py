import pandas as pd


import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font',family='Arial')


fig, axes = plt.subplots(1, 3, figsize = (20,6), dpi=120)
# 读取Excel文件
df = pd.read_excel('./articles.xlsx')
# df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
monthly_counts = pd.DataFrame(columns=['Month', 'Count'])

# Count the papers by month
for _, row in df.iterrows():
    date = str(row['Date'])
    year = date[:4]
    month = date[4:6]
    key = f'{year}-{month}'
    if key in monthly_counts['Month'].values:
        monthly_counts.loc[monthly_counts['Month'] == key, 'Count'] += 1
    else:
        monthly_counts = pd.concat([monthly_counts, pd.DataFrame({'Month': [key], 'Count': [1]})], ignore_index=True)

# Sort the DataFrame by month
monthly_counts.sort_values('Month', inplace=True)

# Plot the results
# axes[0].figure(figsize=(8, 6))
axes[0].bar(monthly_counts['Month'], monthly_counts['Count'], color='blue')
axes[0].set_xlabel('Month', fontsize=20)
axes[0].set_ylabel('Number of Papers', fontsize=20)
axes[0].set_title('Monthly Paper Submissions', fontsize=20)
axes[0].set_xticklabels(monthly_counts['Month'].values, rotation=35)
# axes[0].tight_layout()
# axes[0].show()
for i, value in enumerate(monthly_counts['Count'].values):
    axes[0].text(monthly_counts['Month'].index[i], value, str(value), ha='center', va='bottom', fontsize=14)
# 统计每天提交的论文数量
# date_counts = df['Date'].value_counts().sort_index()

# # 生成完整的日期范围
# date_range = pd.date_range(start=df['Date'].min(), end=df['Date'].max())

# # 创建新的Series，并将日期范围和统计结果合并
# date_counts = date_counts.reindex(date_range, fill_value=0)

# # 绘制柱状图
# # axes[0].figure(figsize=(8, 6))
# axes[0].bar(date_counts.index, date_counts.values)
# axes[0].set_title('Number of Papers Submitted by Date',fontsize=20)
# axes[0].set_xlabel('Date',fontsize=20)
# # axes[0].grid(True)
# axes[0].tick_params(axis='x', rotation=35)
# axes[0].set_ylabel('Number of Papers',fontsize=20)

# plt.show()


# df = pd.read_excel('articles_info.xlsx')
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

# 统计每天提交的论文数量并计算累计值
date_counts = df['Date'].value_counts().sort_index()
cumulative_counts = date_counts.cumsum()

# 绘制折线图
axes[1].plot(cumulative_counts.index, cumulative_counts.values, linestyle='-', color='black')

# 添加网格线
# plt.grid(True)

# 设置图形标题和坐标轴标签
axes[1].set_title('Cumulative Number of Papers Submitted by Date',fontsize=20)
axes[1].set_xlabel('Date',fontsize=20)
axes[1].tick_params(axis='x', rotation=35)
axes[1].set_ylabel('Cumulative Number of Papers',fontsize=20)

# 调整图形尺寸
# axes[1].figure(figsize=(8, 6))

# # 显示图形
# plt.tight_layout()
# plt.show()
#


# 读取Excel文件
# df = pd.read_excel('articles_info.xlsx')
# df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

# # 提取年份
df['Year'] = df['Date'].dt.year

# 计算每年的论文提交总数
yearly_counts = df.groupby('Year').size()

# 绘制柱状图
axes[2].bar(yearly_counts.index, yearly_counts.values, color='red')

# 在每个柱形上方显示数字
for i, value in enumerate(yearly_counts.values):
    axes[2].text(yearly_counts.index[i], value, str(value), ha='center', va='bottom', fontsize=14)

# 设置图形标题和坐标轴标签
axes[2].set_title('Total Paper Submissions Per Year',fontsize=20)
axes[2].set_xlabel('Year',fontsize=20)
axes[2].set_ylabel('Number of Papers',fontsize=20)
axes[2].tick_params(axis='x')
axes[2].set_xticks(yearly_counts.index)
axes[2].set_xticklabels(yearly_counts.index, rotation=30)
for size in axes[2].get_xticklabels():   #获取x轴上所有坐标，并设置字号
    size.set_fontname('Times New Roman')   
    size.set_fontsize('15')

# axes[2].figure(figsize=(8, 6))

# 显示图形
plt.tight_layout()
plt.show()

