import json
from pathlib import Path

DATA_FILE = Path("data.json")  # 保存先ファイル

# JSONファイルを読み込み
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# data.jsonのテストデータ
# {"id": 1, "name": "Taro", "age": 20},
# {"id": 2, "name": "Hanako", "age": 25},
# {"id": 3, "name": "Jiro", "age": 30}

target_id = 2
before_len = len(data)

data = [item for item in data if item["id"] != target_id]

if len(data) < before_len:
    print(f"id={target_id} の要素を削除しました")
else:
    print(f"id={target_id} は見つかりませんでした")

# ファイルに書き戻し
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(data)
