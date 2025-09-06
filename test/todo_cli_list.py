import click
from typing import List, Dict

# ---- In-memory storage（メモリ保存、永続化なし）----
_tasks: List[Dict] = [
     {'id': 1, 'title': '買い物', 'done': False},
     {'id': 2, 'title': 'レポート 提出', 'done': False}
]


@click.group()
def cli():
    """学習用 ToDo CLI"""
    pass


@cli.command()
def list():
    """タスク一覧を表示"""
    if not _tasks:
        click.echo("タスクはありません。")
    for task in _tasks:
        status = "✔" if task["done"] else "✗"
        click.echo(f"[{status}] #{task['id']}: {task['title']}")


if __name__ == "__main__":
    cli()

# python todo_cli_list.py list 入力とすると
# [✗] #1: 買い物
# [✗] #2: レポート 提出
# が出力。
