

def predict(data, model_path):
    loaded_model = pickle.load(open(model_path, 'rb'))
    print("DONE load model")
    predict_label  =  loaded_model.predict(data)
    return predict_label

def RR_to_features(heart_data):
    from hrvanalysis import get_frequency_domain_features,get_time_domain_features, get_poincare_plot_features
    #chuyen heart_rate_list thanh RR_list
    for i in heart_data:
        RR_interval.append(60*1000/i)
    
    #tinh ra cac features
    feautures_1 = get_poincare_plot_features(RR_interval)
    SD1 = feautures_1['sd1']
    SD2 = feautures_1['sd2']
    feautures_2 = get_frequency_domain_features(RR_interval)
    LF = feautures_2['lf']
    HF = feautures_2['hf']
    LF_HF = feautures_2['lf_hf_ratio']
    HF_LF = 1/LF_HF
    LF_NU = feautures_2['lfnu']
    HF_NU = feautures_2['hfnu']
    TP = feautures_2['total_power']
    VLF = feautures_2['vlf']
    feautures_3 = get_time_domain_features(RR_interval)
    pNN50 = feautures_3['pnni_50']
    RMSSD = feautures_3['rmssd']
    MEAN_RR = feautures_3['mean_nni']
    MEDIAN_RR = feautures_3['median_nni']
    HR = feautures_3['mean_hr']
    SDRR = feautures_3['sdnn']
    SDRR_RMSSD = SDRR/RMSSD
    SDSD = feautures_3['sdsd']
    row_list = [["MEAN_RR", "MEDIAN_RR", "SDRR","RMSSD","SDSD","SDRR_RMSSD"
                 ,"HR","pNN50","SD1","SD2","VLF","LF","LF_NU","HF","HF_NU"
                 ,"TP","LF_HF","HF_LF"],
             [MEAN_RR,MEDIAN_RR,SDRR,RMSSD,SDSD,SDRR_RMSSD,HR,pNN50,SD1,SD2
              ,VLF,LF,LF_NU,HF,HF_NU,TP,LF_HF,HF_LF]]
    return row_list[1]

def save_csv(heart_data):
    list_features = RR_to_features(heart_data)
    value_stress = #predict func(list_features)
    list_features.append(value_stress)
    with open('data/final/data_user.csv','r') as file:
        csv_reader = csv.reader(file)
        listData = list(csv_reader)
    listData.append(list_features)
    with open('data/final/data_user.csv','w',newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(listData)