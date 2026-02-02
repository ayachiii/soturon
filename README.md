# 卒論解析用のプログラムやデータを保存するリポジトリ
# EGG data
preprocessingフォルダは、SSSEP~.mat(生データ)から、各端子のPLIを算出したcsvファイルの出し方。
実行結果は、PLI_0_kumakura_rest.csv,concentration_1_kumakura_practice.csvが出力される。場所は、csv->0_kumakura->PLIdata


PLI_Analysis.ipynbはpreprocessingで作成したcsvファイルを使って一秒ごとのPLIを算出して描画するプログラム。
PLI_Analysis_tetris.ipynbはtetrisのPLI描画プログラム。PLI_Analysis_image.ipynbはイメージトレーニングのPLI描画プログラム。


export_mean_PLI_自作.ipynbは,5つ(rest,boredom,flow,fow_ultra,overload)のPLI_数字_人名_フェーズ.csvからmean_PLI_人名.csvに書き換える作業をするpythonコード


# ECG data
preprocessingフォルダは、SSSEP~.mat(生データ)から、心電図を算出したcsvファイルの出し方。
実行結果は、ECG_kumakura_boredom.csvが出力される。場所は、csv->0_kumakura->ECG

export_rr_interval自分で作成は、ECG_人名_フェーズ.csvからrr_interval_人名_フェーズ.csvに書き換える作業をするpythonコード

export_HRV_parameters自作.ipynbは、ECG_人名_フェーズ.csvから人名_HRV.csvに書き換える作業をするpythonコード


# Kubiosについて
import直後の画面のStartとlengthはどのように決定しているのか？

SDSD,PNN20,PNN50がどこに書いてあるのかわからない。と思ったけど、結局HRVパラメータのところで計算して出てくるからいいのでは？と思った。

Kubios_HRV.csvのkubios_lf,kubios_hf,kubios_lf/hfは手動のような気がする。手動でいける。
kubiosをインポートした後、.csvの方を開いて、kubios_lfにはFrequency-Domain ResultsのLF(ms^2),kubios_hfにはHF(ms^2),kubios_lf/hfにはLF/HF ratio:を記入する。

# 全体の処理

HRV,PLI,アンケート,kubios_HRVの結合はconcat_HRV_PLI_Qでできそうだが、正規化、標準化をするコードがどこにあるのかわからない。それを探す。正規化、標準化ができると、focus_on_subjectのグラフが書けるようになる。

concat_HRV_PLI_Q自作.ipynbで、四つのデータの結合と標準化、正規化を行なっている。しかし、特に標準化と正規化において、お手本データと作成したデータの値が異なる点が懸念点。

focus_on_single_subject自作.ipynbにて、FczのconcentrationとLFを描画する。フローになっているかどうか判別できる。

# 次の目標　

今足りないもの(last yearの中で)

・export_HRV_parameters自作.ipynbの前処理、ノイズ処理にrrのcsvを使うのでは？という疑問。アップロードした前処理のファイルが使えないか模索する。後で。余力あったら。

・HRV_and_PLI.csvの正規化、標準化の値は算出されているが、先輩の出したものとは結構違っている。
・heartpyではなく、scipyを使ってFczのconcentrationとLFを描画している。フローになっているかどうか 1 被験者のデータをより深ぼって観察し，⾚丸の部分における他の指標の動きを観察する，およびこの時間帯とそれ以外で何かしらの分類タスクを施してみるなどをすることが，更なる知⾒の獲得につながると考える.ができるかどうか。

・箱ひげ図の取り組み

・先輩の解析の内容

修論:一元配置分散分析 HRV-LF,HRV-HF,認知作業負荷、FC3,FC4,FCz

二次回帰分析　独立変数をフロースコアに、従属関数をHRV-LF、認知作業負荷(FC3,FC4,FCz)をとった

その他の分析　フェーズ別分布:BPM,Breathing rate,IBI,認知作業負荷(FC3,FC4,FCz)の最大値、HRV-LF最小値,HRV-HF最小値,PNN20,PNN50,rMSSD,SDI,SD2,sdsd

二次回帰分析:bpm,breathingrate,認知作業負荷(FC3,FC4,FCz)の最大値、HRV-HF,HRV-LF,PNN20,PNN50,rMSSD,sd1,sd2,sdsd
              
卒論:フロースコアと各指標間の相関分析,フロースコアを従属変数、各指標を独立変数とした線形回帰分析、二次回帰分析。

相関分析:全ての参加者、フェーズのデータを結合して、心拍変動パラメーたと認知作業負荷でフロースコアに対する相関分析を行なっている。ピアソンの積率相関分析、集中度、難易度、時間感覚、満足感

回帰分析:Boredom,Flow,Flow_ultra,Overloadでの回帰分析。有意性を確認して、注目するべき指標を紹介している。今回でいうと、FC3とHF/LF


