# plot3d
## 概要
エクセルの3次元座標列データをpythonのmatplotlibで描画します。

## 詳細
plot3d_wl4.pyと同じディレクトリにあるdata.xlsxの１つ目のシートを読み込み対象としています。<br>
2列目にx座標データ、3列目にy座標データ、4列目にz座標データを用意してください。<br>
各行の1列目の文字列は同じ行の2~4列目で表される座標に対応するラベルの扱いになり、<br>
プロットした座標にカーソルを合わせたときにラベルを表示されます。<br>

## 導入手順（Windows）
「plot3d」をローカルのwindows環境に導入する手順は以下の通りです。<br>
*※python3や、madplotlib,xlrd,mplcursors,pandasといったモジュールがお手持ちのデバイスにインストールされていないことが確実な場合は、先に手順7、手順6を実施してください。*

1. 左上の「<>Code」タブを選択後、右上の「<>Code」ボタンを押してください。<br>
2. 表示されるドロップダウン風リストの一番下の「Download ZIP」をクリックしてください。<br>
3. plot3d-main.zipが「ダウンロード」フォルダにダウンロードされますので、そのZipを解凍してください。※解凍場所は任意です。<br>
4. 解凍されたフォルダの内部構成と概要は以下の通りです。<br>

            plot3d-main
                        └ data.xlsx       ：分析対象データ。
                                            初期状態ではサンプルを置いてあるだけなので、用途に応じて置き換えてください。
                                            置き換える場合もファイル名は、「data.xmlx」で統一してください。
                                            この名前のエクセルの、1シート目が分析対象になるためです。
                        └ plot3d_wl2.py   ：実行ファイル（常時ラベル表示タイプ）。ダブルクリックして利用します。
                        └ plot3d_wl4.py   ：実行ファイル（選択データラベル表示タイプ）。ダブルクリックして利用します。
                        └ README.MD       ：利用法説明書。

5. 用途に応じて、「plot3d_wl2.py」か「plot3d_wl4.py」を使い分けてください。ダブルクリックで利用できます。<br>
6. 利用できない場合は、描画モジュールが不足している可能性があります。インストールするため、コマンドプロンプトで以下を実施してください。<br>

            pip3 install xlrd==1.2.0

            pip3 install matplotlib

            pip3 install mplcursors

            pip3 install pandas

*※「pip3」が使えなければ「pip」、それでもだめなら「py -m pip」に置き換えて上記4行を実行してみてください。*

7.python3がインストールされていない場合は以下手順でpython3をインストールしてください。（※Windowsの場合）<br>
            ①　[Python公式サイト（https://www.python.org/downloads/windows/）](https://www.python.org/downloads/windows/)にアクセスします。<br>
            <p><a href="https://www.python.org/downloads/windows/" target="_blank">Python公式サイト（https://www.python.org/downloads/windows/）にアクセスします。</a></p>
            ②　ダウンロードページで、最新バージョンのPython3を選択します。<br>
            ③　ダウンロードページ下部にある「Windows x86-64 executable installer」というリンクをクリックします。<br>
            ④　ダウンロードしたインストーラを開き、指示に従ってPythonをインストールします。<br>

*※インストールが完了したら、次のコマンドを実行してバージョンを確認できます。*

            python3 --version
