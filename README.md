# キャプテン翼-RIVALS-対戦シミュレータ
* 本シミュレータは、[キャプテン翼-RIVALS-](https://tsubasa-rivals.com/ja/)用のBCG対戦シミュレータである
* 本BCGでは、ライバルモードにおいて3ターン全勝利することが獲得$TSUBASAUTを最大化する上で非常に重要であるため、相手のRP組合せによらず、全勝可能かをシミュレーションする


## シミュレータ概要
* 事前に自分の選手データを設定し、そのデータに基づいたコマンドの全組合せでRPを算出し、相手のRPを3ターン上回ることができる組合せが存在するかをチェックする
* 相手の全RPパターンに全て勝利できるか、一つでも敗北するパターンが存在するかを判定する
* 特殊効果(例:技属性の選手に対して力属性の選手は、全コマンドパラメータが150%upすること)も考慮している


## 注意点
* 仕様変更やバグ等により、正しく判定されない可能性があるため、その点をご理解の上、ご使用ください


## 動作確認環境
* macOS Big Sur(バージョン11.7.1)
* python 3.11.2
* PyYAML 6.0
  * シミュレータを実行して`ModuleNotFoundError: No module named 'yaml'`というエラーが出る場合、以下をインストールください
```
$ pip3 install pyyaml
``` 


## ファイル説明
```
.
├── LICENSE.txt            # ライセンスファイル
├── README.md              # 本ファイル
├── battle_simulator.py    # シミュレータプログラム
└── data
    ├── 1_Jitoh.csv        # エナジー1の次藤データ
    ├── 1_Misugi.csv       # エナジー1の三杉データ
    ├── 3_Dias.csv         # エナジー3のディアスデータ
    ├── 4_Tyou.csv         # エナジー4の肖データ
    └── own.yaml           # 自分の選手データ
```


## 準備
* 自分の選手データを`data/own.yaml`に入力する
* 入力項目は以下の通り
```
- type: toughness  # 力
  val: 2057        # VSパラメータ値
  commands: 2      # コマンド数
  main: 1          # 選手の属性にのみ設定
- type: agility    # 速
  val: 1213
  commands: 2
- type: skill      # 技
  val: 1416
  commands: 2
```

* 例. 技属性の選手で、コマンドは力0、速1、技5の場合
```
- type: toughness
  val: 1200
  commands: 0 
- type: agility
  val: 1200
  commands: 1
- type: skill
  val: 2000
  commands: 5
  main: 1 
```


## 実行方法
* ヘルプ表示
```
$ python3 battle_simulator.py -h
usage: python3 battle_simulator.py

battle simulator of TsubasaRivals

options:
  -h, --help            show this help message and exit
  -s, --special         all command parameters 150% up
  -e ENEMY, --enemy ENEMY
                        enemy data csv

end
```

* 特殊効果あり(`-s`)、エナジー3のディアス(`-e data/3_Dias.csv`)と対戦
  * 勝利するパターン
```
bash-3.2$ python3 battle_simulator.py -s -e data/3_Dias.csv
------------------------
|     YOUR COMMANDS     |
------------------------
[6171, 3085, 1819, 1819, 2124, 2124]

===== Pattern 1 =====
You win!
- You  : [7990, 1819, 7333]
- Enemy: [6853, 1142, 6853]

===== Pattern 2 =====
You win!
- You  : [6171, 6723, 4248]
- Enemy: [5303, 5303, 4242]

===== Pattern 3 =====
You win!
- You  : [6171, 2124, 8847]
- Enemy: [4242, 2121, 8485]

===== Pattern 4 =====
You win!
- You  : [3085, 6171, 7886]
- Enemy: [2284, 5711, 6853]

===== Pattern 5 =====
You win!
- You  : [6171, 6067, 4904]
- Enemy: [4455, 5940, 4455]

===== Pattern 6 =====
You win!
- You  : [7990, 3085, 6067]
- Enemy: [5940, 2970, 5940]

===== Pattern 7 =====
You win!
- You  : [6171, 4904, 6067]
- Enemy: [5711, 3426, 5711]

===== Pattern 8 =====
You win!
- You  : [3085, 2124, 11933]
- Enemy: [2121, 2121, 10607]

------------------------
|     TOTAL RESULT     |
------------------------
YOU WIN ALL PATTERN!!!
```

* 特殊効果なし、エナジー1の(`-e data/1_Misugi.csv`)と対戦
  * 敗北するパターン
```
bash-3.2$ python3 battle_simulator.py -e data/1_Misugi.csv
------------------------
|     YOUR COMMANDS     |
------------------------
[4114, 2057, 1213, 1213, 1416, 1416]

===== Pattern 1 =====
You lose...
- You  : None
- Enemy: [6514, 1628, 3257]

===== Pattern 2 =====
You lose...
- You  : None
- Enemy: [4275, 1425, 5700]

===== Pattern 3 =====
You lose...
- You  : None
- Enemy: [3507, 4384, 3507]

===== Pattern 4 =====
You lose...
- You  : None
- Enemy: [3800, 3800, 3800]

===== Pattern 5 =====
You lose...
- You  : None
- Enemy: [4384, 3507, 3507]

===== Pattern 6 =====
You lose...
- You  : None
- Enemy: [5066, 1266, 5066]

===== Pattern 7 =====
You lose...
- You  : None
- Enemy: [1036, 6218, 4145]

------------------------
|     TOTAL RESULT     |
------------------------
You lose...Continue?
```
