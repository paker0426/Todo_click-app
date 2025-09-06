# ToDo CLI

シンプルなタスク管理を行うPython製CLIアプリです。
タスクの追加・削除・完了/未完了の切り替え・一覧表示をサポートしています。

## 特徴

* JSONファイル (`tasks.json`) に保存するため、終了後もタスクを保持
* Clickライブラリを使用したシンプルなCLIインターフェイス
* タスクの完了状態を「✔ / ✗」で表示
* 学習用に最小限の構成

## 使い方

### ヘルプの表示

```bash
python main.py --help
```

### タスクの追加

```bash
python main.py add "買い物に行く"
```

出力例:

```
追加: #1 買い物に行く
```

### タスクの一覧

```bash
python main.py list
```

出力例:

```
[✗] #1: 買い物に行く
```

### タスクを完了にする

```bash
python main.py done 1
```

出力例:

```
完了: #1 買い物に行く
```

### タスクを未完了に戻す

```bash
python main.py undone 1
```

出力例:

```
未完了に戻しました: #1 買い物に行く
```

### タスクを削除する

```bash
python main.py dell 1
```

出力例:

```
削除: #1
```

## ディレクトリ構成

```
.
├── main.py        # CLI本体
└── tasks.json     # タスク保存ファイル（自動生成）
```

## 開発メモ

* ライブラリ: [Click](https://click.palletsprojects.com/)
* JSONを使ったシンプルなデータ保存
* 学習用にMVC分離やテスト追加などの拡張も容易

---
