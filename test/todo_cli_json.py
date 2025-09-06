import json
from pathlib import Path

DATA_FILE = Path("tasks.json")  # 保存先ファイル
_tasks = []  # タスクを入れるリスト（メモリ上）
_next_id = 1  # IDカウンタ


def save_tasks():
    """タスクをJSONに保存"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(_tasks, f, indent=2, ensure_ascii=False)


def load_tasks():
    """JSONからタスクを読み込み"""
    global _tasks, _next_id
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            _tasks = json.load(f)
        # 次のIDは「最大ID + 1」
        if _tasks:
            _next_id = max(task["id"] for task in _tasks) + 1
        else:
            _next_id = 1


def add_task(title: str):
    """タスクを追加"""
    global _next_id
    task = {"id": _next_id, "title": title, "done": False}
    _tasks.append(task)
    _next_id += 1
    save_tasks()


def list_tasks():
    """タスクを表示"""
    for task in _tasks:
        status = "✔" if task["done"] else "✘"
        print(f"{task['id']}: {task['title']} [{status}]")


if __name__ == "__main__":
    # 起動時に既存データを読み込み
    load_tasks()

    # データを追加
    add_task("買い物に行く")
    add_task("勉強する")

    # 保存されている内容を一覧表示
    print("=== タスク一覧 ===")
    list_tasks()
