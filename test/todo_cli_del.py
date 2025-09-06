import click
import json
from pathlib import Path
from typing import List, Dict

# ==== データ管理 ====
DATA_FILE = Path("tasks.json")
_tasks: List[Dict] = []
_next_id = 1


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
        _next_id = max((task["id"] for task in _tasks), default=0) + 1
    else:
        _tasks = []
        _next_id = 1


# ==== CLI定義 ====
@click.group()
def cli():
    """ToDo CLI（JSON保存対応）"""
    load_tasks()  # 毎回起動時に読み込む


@cli.command()
@click.argument("task_id", type=int)
def dell(task_id):
    """タスクを削除"""
    global _tasks
    before_len = len(_tasks)
    _tasks = [item for item in _tasks if item["id"] != task_id]
    save_tasks()

    if len(_tasks) < before_len:
        click.echo(f"削除: #{task_id}")
    else:
        click.echo(f"ID {task_id} は見つかりませんでした")


@cli.command(name="list")
def list_tasks():
    """タスク一覧を表示"""
    if not _tasks:
        click.echo("タスクはありません。")
        return
    for task in _tasks:
        status = "✔" if task["done"] else "✗"
        click.echo(f"[{status}] #{task['id']}: {task['title']}")


if __name__ == "__main__":
    cli()
