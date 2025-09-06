import click
import json
from pathlib import Path
from typing import List, Dict, Optional

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


def find_tasks(task_id: int) -> Optional[Dict]:
    return next((t for t in _tasks if t["id"] == task_id), None)


# ==== CLI定義 ====
@click.group()
def cli():
    """ToDo CLI"""
    load_tasks()  # 毎回起動時に読み込む


@cli.command()
@click.argument("title", nargs=-1, required=True)
def add(title):
    """新しいタスクを追加する。"""
    global _next_id
    text = " ".join(title)
    task = {"id": _next_id, "title": text, "done": False}
    _tasks.append(task)
    save_tasks()
    click.echo(f"追加: #{_next_id} {text}")
    _next_id += 1


@cli.command()
@click.argument("task_id", type=int)
def dell(task_id: int):
    """タスクを削除する。"""
    global _tasks
    before_len = len(_tasks)
    _tasks = [item for item in _tasks if item["id"] != task_id]
    save_tasks()

    if len(_tasks) < before_len:
        click.echo(f"削除: #{task_id}")
    else:
        click.echo(f"ID {task_id} は見つかりませんでした")


@cli.command()
@click.argument("task_id", type=int)
def done(task_id: int):
    """タスクを完了にする。"""
    t = find_tasks(task_id)
    if not t:
        click.echo(f"#{task_id} は見つかりません。", err=True)
        raise SystemExit(1)
    if t["done"]:
        click.echo(f"#{task_id} は既に完了です。")
        return
    t["done"] = True
    save_tasks()
    click.echo(f"完了: #{task_id} {t['title']}")


@cli.command()
@click.argument("task_id", type=int)
def undone(task_id: int):
    """タスクを未完了に戻す。"""
    t = find_tasks(task_id)
    if not t:
        click.echo(f"#{task_id} は見つかりません。", err=True)
        raise SystemExit(1)
    if not t["done"]:
        click.echo(f"#{task_id} は既に未完了です。")
        return
    t["done"] = False
    save_tasks()
    click.echo(f"未完了に戻しました: #{task_id} {t['title']}")


@cli.command()
def list():
    """タスク一覧を表示する。"""
    if not _tasks:
        click.echo("タスクはありません。")
        return
    for task in _tasks:
        status = "✔" if task["done"] else "✗"
        click.echo(f"[{status}] #{task['id']}: {task['title']}")


if __name__ == "__main__":
    cli()
