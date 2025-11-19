# 卒論解析用のプログラムやデータを保存するリポジトリ
# EGG data
mat_to_csvフォルダは、SSSEP~.mat(生データ)から、各端子のPLIを算出したcsvファイルの出し方。
実行結果は、PLI_0_kumakura_rest.csv,concentration_1_kumakura_practice.csvが出力される。場所は、csv->0_kumakura->PLIdata

現在、yamashita_overloadだけがエラーでてうまくいっていないけど

PLI_Analysis.ipynbはmat_to_csvで作成したcsvファイルを使って一秒ごとのPLIを算出して描画するプログラム。
PLI_Analysisいじった2.ipynbはpracticeしか成功してない😭その理由はpractice以外のcsvファイルは7端子の列まで表示しているから。

export_mean_PLI_自作.ipynbは,5つ(rest,boredom,flow,fow_ultra,overload)のPLI_数字_人名_フェーズ.csvからmean_PLI_人名.csvに書き換える作業をするpythonコード


# ECG data
mat_to_csvフォルダは、SSSEP~.mat(生データ)から、心電図を算出したcsvファイルの出し方。
実行結果は、ECG_kumakura_boredom.csvが出力される。場所は、csv->0_kumakura->ECG

export_rr_interval自分で作成は、ECG_人名_フェーズ.csvからrr_interval_人名_フェーズ.csvに書き換える作業をするpythonコード

export_HRV_parameters自作.ipynbは、ECG_人名_フェーズ.csvから人名_HRV.csvに書き換える作業をするpythonコード


constants.pyはジュピターノートブックでは作業可能であるが、colabでは出来なさそう・・・（constants.pyはpath_to_matlab_repository_folder = "/content/soturon"を変更)

# Kubiosについて
import直後の画面のStartとlengthはどのように決定しているのか？

SDSD,PNN20,PNN50がどこに書いてあるのかわからない。と思ったけど、結局HRVパラメータのところで計算して出てくるからいいのでは？と思った。

Kubios_HRV.csvのkubios_lf,kubios_hf,kubios_lf/hfは手動のような気がする。手動でいける。
kubiosをインポートした後、.csvの方を開いて、kubios_lfにはFrequency-Domain ResultsのLF(ms^2),kubios_hfにはHF(ms^2),kubios_lf/hfにはLF/HF ratio:を記入する。

# 次の目標　
csvの一人分を全部揃わせること

今足りないもの(last yearの中で)

・export_HRV_parameters自作.ipynbの前処理、ノイズ処理にrrのcsvを使うのでは？という疑問。アップロードした前処理のファイルが使えないか模索する。後で。余力あったら。

・HRV_and_PLI.csv              (←HRV、PLI、アンケート、kubios_HRVをつなげること)




