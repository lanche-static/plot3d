import xlrd
import mplcursors
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# エクセルファイルを開く
workbook = xlrd.open_workbook('data.xlsx')
sheet = workbook.sheet_by_index(0)

print('エクセルファイル「data.xlsx」の1シート目を開きました')

# データを取得
labels = []
xs = []
ys = []
zs = []

for row in range(1, sheet.nrows):
    label = sheet.cell_value(row, 0)
    x = sheet.cell_value(row, 1)
    y = sheet.cell_value(row, 2)
    z = sheet.cell_value(row, 3)
    
    # データが十分でない場合はスキップする
    if not (label and x and y and z):
        continue
    
    labels.append(label)
    xs.append(x)
    ys.append(y)
    zs.append(z)

# 3Dプロット
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs)

# ラベルを表示するためにmplcursorsを使用する
cursor = mplcursors.cursor(ax, hover=True)

@cursor.connect("add")
def on_add(sel):
    i = sel.target.index
    label = labels[i]
    sel.annotation.set(text=label)

plt.show()
