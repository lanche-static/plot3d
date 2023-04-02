# plot3d
エクセルの3次元座標列データをpythonのmatplotlibで描画します

plot3d_wl4.pyと同じディレクトリにあるdata.xlsxの一つ目のシートを読み込み対象としています。
2列目にx座標データ、3列目にy座標データ、4列目にz座標データを用意してください。
各行の1列目の文字列は同じ行の2~4列目で表される座標に対応するラベルの扱いになり、
プロットした座標にカーソルを合わせたときにラベルを表示されます。

------------------------------------------------------
------------------------------------------------------

事前に以下を実行してください


pip3 install xlrd==1.2.0

pip3 install matplotlib

pip3 install mplcursors


------------------------------------------------------
------------------------------------------------------

python3がインストールされていない場合は以下参照
Windowsの場合

    Python公式サイト（https://www.python.org/downloads/windows/）にアクセスします。
    ダウンロードページで、最新バージョンのPython3を選択します。
    ダウンロードページ下部にある「Windows x86-64 executable installer」というリンクをクリックします。
    ダウンロードしたインストーラを開き、指示に従ってPythonをインストールします。

インストールが完了したら、次のコマンドを実行してバージョンを確認します。

python3 --version
