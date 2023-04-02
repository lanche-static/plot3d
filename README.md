# plot3d
エクセルの3次元座標列データをpythonのmatplotlibで描画します。

## 詳細
plot3d_wl4.pyと同じディレクトリにあるdata.xlsxの１つ目のシートを読み込み対象としています。
2列目にx座標データ、3列目にy座標データ、4列目にz座標データを用意してください。
各行の1列目の文字列は同じ行の2~4列目で表される座標に対応するラベルの扱いになり、
プロットした座標にカーソルを合わせたときにラベルを表示されます。

## 導入手順（windows）
plot3dをローカルのwindows環境に導入する手順は以下の通りです。

1. 左上の「<>Code」タブを選択後、右上の「<>Code」ボタンを押してください。<br>
2. 出てくるポップアップ風表示の一番下の「Download ZIP」をクリックしてください。<br>
3. plot3d-main.zipが「ダウンロード」フォルダにダウンロードされますので、そのZipを解凍してください。※解凍場所は任意です。<br>
4. 解凍されたフォルダの内部構成と概要は以下の通りです。<br>

            plot3d-main<
                        └ data.xlsx       ：分析対象データ。
                                            初期状態ではサンプルを置いてあるだけなので、用途に応じて置き換えてください。
                                            置き換える場合もファイル名は、「data.xmlx」で統一してください。
                                            この名前のエクセルの、1シート目が分析対象になるためです。
                        └ plot3d_wl2.py   ：実行ファイル（常時ラベル表示タイプ）。ダブルクリックして利用します。
                        └ plot3d_wl4.py   ：実行ファイル（選択データラベル表示タイプ）。ダブルクリックして利用します。
                        └ README.MD       ：利用法説明書。

5. 用途に応じて、「plot3d_wl2.py」か「plot3d_wl4.py」を使い分けてください。ダブルクリックで利用できます。
6. 利用できない場合は、描画モジュールが不足している可能性があります。インストールするため、コマンドプロンプトで以下を実施してください。

            pip3 install xlrd==1.2.0

            pip3 install matplotlib

            pip3 install mplcursors

            pip3 install pandas

※python3がインストールされていない場合は以下手順でpython3をインストールしてください。（※Windowsの場合）

            Python公式サイト（https://www.python.org/downloads/windows/）にアクセスします。
            ダウンロードページで、最新バージョンのPython3を選択します。
            ダウンロードページ下部にある「Windows x86-64 executable installer」というリンクをクリックします。
            ダウンロードしたインストーラを開き、指示に従ってPythonをインストールします。

インストールが完了したら、次のコマンドを実行してバージョンを確認します。

            python3 --version
