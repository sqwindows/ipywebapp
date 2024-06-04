import click


# 命令格式：ipyweb demoTest start
@click.command(help='ipyweb demoTest start')
@click.argument('args', nargs=1, default='', type=str)
def demoTest(args=''):
    click.echo(f'command: demoer args: {args}')
