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

# ここで更新（上書き）
# id=2 の要素を探して更新
for person in data:
    if person["id"] == 2:
        person["age"] = 21           # 既存キーの更新
        break

# ファイルに書き戻し
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(data)
