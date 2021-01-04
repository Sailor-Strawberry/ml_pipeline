import pandas as pd
import numpy as np
import sys,os
import csv
import yaml
from pathlib import Path
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from base import Feature, get_arguments, generate_features
from sklearn.preprocessing import LabelEncoder
import warnings
import jpholiday

sys.path.append(os.pardir)
sys.path.append('../..')
sys.path.append('../../..')
warnings.filterwarnings("ignore")


CONFIG_FILE = '../configs/config.yaml'
with open(CONFIG_FILE) as file:
    yml = yaml.load(stream=file, Loader=yaml.SafeLoader)

RAW_DATA_DIR_NAME = yml['SETTING']['RAW_DATA_DIR_NAME']  # 特徴量生成元のRAWデータ格納場所
Feature.dir = yml['SETTING']['FEATURE_PATH']  # 生成した特徴量の出力場所
feature_memo_path = Feature.dir + '_features_memo.csv'



# Target
class hoge(Feature):
    def create_features(self):
        self.train['hoge'] = train['hoge']
        self.test['hoge'] = test['hoge']
        create_memo('hoge','ここに変数の説明を入力')

class hoge(Feature):
    def create_features(self):
        cols = 'hoge'
        tmp_df = pd.concat([train, test], axis=0, sort=False).reset_index(drop=True)
        le = LabelEncoder().fit(tmp_df[cols])
        self.train['hoge'] = le.transform(train[cols])
        self.test['hoge'] = le.transform(test[cols])
        create_memo('hoge','ここに変数の説明を入力')



# 特徴量メモcsvファイル作成
def create_memo(col_name, desc):

    file_path = Feature.dir + '/_features_memo.csv'
    if not os.path.isfile(file_path):
        with open(file_path,"w"):pass

    with open(file_path, 'r+') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

        # 書き込もうとしている特徴量がすでに書き込まれていないかチェック
        col = [line for line in lines if line.split(',')[0] == col_name]
        if len(col) != 0:return

        writer = csv.writer(f)
        writer.writerow([col_name, desc])

if __name__ == '__main__':

    # CSVのヘッダーを書き込み
    create_memo('特徴量', 'メモ')

    args = get_arguments()
    train = pd.read_csv(RAW_DATA_DIR_NAME + 'train.csv')
    test = pd.read_csv(RAW_DATA_DIR_NAME + 'test.csv')

    # globals()でtrain,testのdictionaryを渡す
    generate_features(globals(), args.force)

    # 特徴量メモをソートする
    feature_df = pd.read_csv(feature_memo_path)
    feature_df = feature_df.sort_values('特徴量')
    feature_df.to_csv(feature_memo_path, index=False)