class Constants:

    # 分析結果格納フォルダ
    folder_name = "20240917_kyoto"

    # データセット作成フェーズ
    subject_name_list = ["kumakura", "kim", "souma", "fujii", "tubota", "toki", "mori",
                         "hochi", "yamada", "takei", "tenshin", "masanori", "enoki", "ito", "yoshioka", "chizuru"]
    # subject_name_list = ["mori"]
    phase_name_list = ["rest", "boredom", "flow", "ultra", "overload"]
    fs = 500.0

    # 分析フェーズ
    target_columns = ["bpm", "ibi", "lf", "hf",
                      "min_lf", "min_hf",
                      "lf/hf", "kubios_lf", "kubios_hf", "kubios_lf/hf", "sdsd", "rmssd", "pnn20", "pnn50", "concentration_FC3", "concentration_FC4", "concentration_FCz", "concentration_mean", "FC3", "FC4", "FCz", "mean_3ch",
                      "max_concentration_FC3", "max_concentration_FC4", "max_concentration_FCz", "max_concentration_mean",
                      "lf_diff", "hf_diff", "lfhf_diff", "hr_mad", "sd1", "sd2", "s", "sd1/sd2", "breathingrate", "lf_nu", "hf_nu"]

    target_phases = ["boredom", "flow", "ultra", "overload"]
    survey_items = ["difficulty", "fast", "fulfillment",
                    "absorb", "questionnaire_average"]

    path_to_matlab_repository_folder = "/content/soturon"
