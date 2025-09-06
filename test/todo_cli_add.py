import click
from typing import List, Dict

# ---- In-memory storage（メモリ保存、永続化なし）----
_tasks: List[Dict] = []
_next_id = 1  # タスクIDを連番で管理


@click.group()
def cli():
    """学習用 ToDo CLI"""
    pass


@cli.command()
@click.argument("title", nargs=-1, required=True)
def add(title):
    """新しいタスクを追加"""
    global _next_id
    text = " ".join(title)  # タプルを結合して文字列に変換
    task = {"id": _next_id, "title": text, "done": False}
    _tasks.append(task)
    click.echo(f"追加: {text}")
    _next_id += 1


if __name__ == "__main__":
    cli()

# python todo_cli_add.py add 買い物 とすると
# 追加: 買い物
# が出力。
