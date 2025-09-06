import click


# @cli.command()
# @cli.command() → 正しい（関数名がコマンド名になる）
# @cli.command(name="...") → 明示的に名前を変えたいときに使う
# 役割: サブコマンドを定義するためのデコレータ。
@click.command()
# @click.argument()
# 役割: 位置引数（必須の入力値） を指定する。
@click.option("--count", default=1, help="何回繰り返すか")
# @click.option()
# 役割: オプション引数（任意の入力値） を指定する。
@click.argument("name")
def hello(count, name):
    """挨拶を count 回出力するコマンド"""
    for _ in range(count):
        click.echo(f"Hello {name}!")


if __name__ == "__main__":
    hello()  # エントリポイント

# python todo_cli_cli.py taro --count 3 と入力すると 3回 "Hello taro!" が出力。
