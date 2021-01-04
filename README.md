# 概要
takapy0210氏のパイプラインを基に、自分用に調整したもの。    
問題があればご連絡ください。     
オリジナル：https://github.com/takapy0210/ml_pipeline.git
## 動作検証済み環境
OS: MacOS BigSur  
python: 3.8.3

# 手順

## クローン
```sh
git clone https://github.com/Sailor-Strawberry/ml_pipeline
```

## フォルダ移動
```sh
cd ml_pipeline/code
```

## 特徴量生成
```sh
python 1_features_create.py
```

## 生成された特徴量の確認（確認したい場合）
```sh
python 2_features_verification.py
```

## 学習
```sh
python 3_run.py
```

## 特徴量生成テンプレート(通常)
```sh
class hoge(Feature):
    def create_features(self):
        self.train['hoge'] = train['hoge']
        self.test['hoge'] = test['hoge']
        create_memo('hoge','ここに変数の説明を入力')
```

## 特徴量生成テンプレート(LabelEncoding)
```sh
class hoge(Feature):
    def create_features(self):
        cols = 'hoge'
        tmp_df = pd.concat([train, test], axis=0, sort=False).reset_index(drop=True)
        le = LabelEncoder().fit(tmp_df[cols])
        self.train['hoge'] = le.transform(train[cols])
        self.test['hoge'] = le.transform(test[cols])
        create_memo('hoge','ここに変数の説明を入力')
```
