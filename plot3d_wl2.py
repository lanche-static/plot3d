import xlrd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Excelファイルを開く
workbook = xlrd.open_workbook('data.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')

# データを取得する
x = []
y = []
z = []
labels = []
for row in range(1, worksheet.nrows):
    label = worksheet.cell(row, 0).value
    if label:  # ラベルがある行のみ取得する
        x_value = worksheet.cell(row, 1).value
        y_value = worksheet.cell(row, 2).value
        z_value = worksheet.cell(row, 3).value
        if isinstance(x_value, float) and isinstance(y_value, float) and isinstance(z_value, float):
            x.append(x_value)
            y.append(y_value)
            z.append(z_value)
            labels.append(label)

# 3次元座標データをプロットする
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)

# ラベルを表示する
for i in range(len(labels)):
    label = labels[i]
    x_pos = x[i]
    y_pos = y[i]
    z_pos = z[i]
    if label:
        ax.text(x_pos, y_pos, z_pos, label, zdir=(0, 0, 2), ha='left', va='bottom', color='red', fontsize=5)
        #ax.plot([x_pos, x_pos], [y_pos, y_pos], [z_pos + 0.12, z_pos + 0.7], color='red')

# グラフを表示する
plt.show()
