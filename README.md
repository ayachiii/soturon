# 卒論解析用のプログラムやデータを保存するリポジトリ
# EGG data
mat_to_csvフォルダは、SSSEP~.mat(生データ)から、各端子のPLIを算出したcsvファイルの出し方。
実行結果は、PLI_0_kumakura_rest.csv,concentration_1_kumakura_practice.csvが出力される。場所は、csv->0_kumakura->PLIdata

現在、yamashita_overloadだけがエラーでてうまくいっていないけど

PLI_Analysis.ipynbはmat_to_csvで作成したcsvファイルを使って一秒ごとのPLIを算出して描画するプログラム。
PLI_Analysisいじった2.ipynbはpracticeしか成功してない😭その理由はpractice以外のcsvファイルは7端子の列まで表示しているから。

# ECG data
mat_to_csvフォルダは、SSSEP~.mat(生データ)から、心電図を算出したcsvファイルの出し方。
実行結果は、ECG_kumakura_boredom.csvが出力される。場所は、csv->0_kumakura->ECG

export_rr_interval自分で作成は、ECG_人名_フェーズ.csvからrr_interval_人名_フェーズ.csvに書き換える作業をするpythonコード

export_HRV_parameters自作.ipynbは、ECG_人名_フェーズ.csvから人名_HRV.csvに書き換える作業をするpythonコード


constants.pyはジュピターノートブックでは作業可能であるが、colabでは出来なさそう・・・（constants.pyはpath_to_matlab_repository_folder = "/content/soturon"を変更)

# Kubiosについて
import直後の画面のStartとlengthはどのように決定しているのか？
SDSD,PNN20,PNN50がどこに書いてあるのかわからない。
LF,HFはどの値をとってるのかわからない

# 次の目標　
csvの一人分を全部揃わせること

今足りないもの(last yearの中で)


・PLIdata:mean_PLI_kumakura.csv

・HRV_and_PLI.csv              (←HRV、PLI、アンケート、kubios_HRVをつなげること)

・kubios_HRV.csv

・qustionnaire.csv



