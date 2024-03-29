# private_works

月初作業を楽にしたいという名目で作成しました。

"画像ダウンロードしてきてモザイクかけるスクリプト"です。「picture」フォルダにダウンロード画像が、「mosaics」フォルダにモザイク画像が保存されます。

# Features

ネットワークフォルダまで画像をダウンロードしにいってモザイク（この部分のスクリプトも作成していました）が面倒だったので、一緒くたにしたものを作りました。

# Demo

こんな感じ

|picture|mosaic|  
|-|-|  
|<img src="https://user-images.githubusercontent.com/41788884/99633842-eb7ec180-2a82-11eb-8156-4a7ce578f11e.jpg" width="480">|<img src="https://user-images.githubusercontent.com/41788884/99634410-cd659100-2a83-11eb-9c3f-5aafe7da867d.jpg" width="480">|

# Requirement

- requests 2.24.0
- opencv-contrib-python 4.3.0.36
- numpy 1.19.1

**anacondaで仮想環境を構築しています。**

# Installation

- anacondaでの環境構築が終わっている場合

```bash
conda install requests
conda install opencv-contrib-python
```

- Pythonしかインストールしてないよって人向け

```
pip install requests
pip install opencv-contrib-python
```

**opencv-contrib-pythonが使えなかったら別途opencvとnumpyをconda install, pip installしてください。**

# Usage

```
git clone https://github.com/mtpeach0513/private_works.git
cd private_works
python img_download.py
```

# Note

要は”画像ダウンロードしてきてモザイクかけるスクリプト”をバッチファイルで定期実行するだけです。  
url_list.txtには.jpgで終わるurlを記述してください。（完全に月初作業にフォーカスしているので、特定のurlでないと意図しない座標にモザイクがかかると思います）  
img_down.batがそのバッチファイルにあたります。  
バッチファイルの、
```
cd private_works
call C:\ProgramData\Anaconda3\Scripts\activate.bat
call activate env_name
```
部分は適宜自分の環境に合わせてください。cdコマンドで作業ディレクトリ（img_download.pyがあるディレクトリ）に移動、callコマンドでanacondaの仮想環境を呼び出しています。  
callコマンド部分はanacondaで仮想環境を構築していない場合は不要です。


# Author

* momoyama
