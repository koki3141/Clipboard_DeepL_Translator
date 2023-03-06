# Clipboard_DeepL_Translator
以下のサイトからdeeplのapi-keyを取得
>https://www.deepl.com/ja/pro-api?cta=header-pro-api/

必要なモジュールをインストール
```
pip install -r requirements.txt
```

# Powershellにaliasとして登録する方法
PowerShellを起動

profileを作成
```
New-Item $profile -type file -force 
```
dl.pyを実行する関数を作成
```
echo 'function deepl {python C:\Users\$path$\dl.py}' > $profile
```
aliasを登録
```
echo 'Set-Alias -Name dl -Value deepl'> $profile
```


