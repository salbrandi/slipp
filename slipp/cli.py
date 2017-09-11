# -*- coding: utf-8 -*-

"""This Module controls all the command line operations.
"""

# ------------------- #
# Third Party Imports #
# ------------------- #
import click



# ------------------- #
#    Local Imports    #
# ------------------- #
import .auth_fetcher
import .updater


auth_token = auth_fetcher.get_auth_token


@click.group()
def slipp:
    pass


@click.command()
@click.argument('playlist', help='Specify a playlist for ')
def run(playlist):
    pass


@click.command()
@click.argument('playlist')
def upodate(playlist):
    pass




slipp.add_command(queue_loads, name='run')
slipp.add_command(queue_loads, name='update')

if __name__ == '__main__':
    pass
