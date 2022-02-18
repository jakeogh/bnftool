#!/usr/bin/env python3
# -*- coding: utf8 -*-
# tab-width:4

# pylint: disable=C0111  # docstrings are always outdated and wrong
# pylint: disable=C0114  # Missing module docstring (missing-module-docstring)
# pylint: disable=W0511  # todo is encouraged
# pylint: disable=C0301  # line too long
# pylint: disable=R0902  # too many instance attributes
# pylint: disable=C0302  # too many lines in module
# pylint: disable=C0103  # single letter var names, func name too descriptive
# pylint: disable=R0911  # too many return statements
# pylint: disable=R0912  # too many branches
# pylint: disable=R0915  # too many statements
# pylint: disable=R0913  # too many arguments
# pylint: disable=R1702  # too many nested blocks
# pylint: disable=R0914  # too many local variables
# pylint: disable=R0903  # too few public methods
# pylint: disable=E1101  # no member for base
# pylint: disable=W0201  # attribute defined outside __init__
# pylint: disable=R0916  # Too many boolean expressions in if statement
# pylint: disable=C0305  # Trailing newlines editor should fix automatically, pointless warning

import os
import sys
import time
from pathlib import Path
from signal import SIG_DFL
from signal import SIGPIPE
from signal import signal
from typing import Iterable
from typing import Optional
from typing import Sequence
from typing import Union

import click
from asserttool import ic
from asserttool import validate_slice
from click_auto_help import AHGroup
from clicktool import click_add_options
from clicktool import click_global_options
from clicktool import tv
from eprint import eprint
from mptool import output
from retry_on_exception import retry_on_exception
#from unmp import unmp
#from prettyprinter import cpprint
#from prettyprinter import install_extras
#install_extras(['attrs'])
from timetool import get_timestamp
from unmp import unmp

#from prettytable import PrettyTable
#output_table = PrettyTable()

# click-command-tree
#from click_plugins import with_plugins
#from pkg_resources import iter_entry_points

signal(SIGPIPE, SIG_DFL)

#@with_plugins(iter_entry_points('click_command_tree'))
@click.group(no_args_is_help=True, cls=AHGroup)
@click_add_options(click_global_options)
@click.pass_context
def cli(ctx,
        verbose: Union[bool, int, float],
        verbose_inf: bool,
        ) -> None:

    tty, verbose = tv(ctx=ctx,
                      verbose=verbose,
                      verbose_inf=verbose_inf,
                      )


@cli.command()
@click_add_options(click_global_options)
@click.pass_context
def syntax(ctx,
           verbose: Union[bool, int, float],
           verbose_inf: bool,
           ) -> None:

    tty, verbose = tv(ctx=ctx,
                      verbose=verbose,
                      verbose_inf=verbose_inf,
                      )

    BNF_syntax = {
        '< >': 'Defined element',
        '=': 'is defined as',
        '|': 'exclusive OR',
        '{ }': 'Group; one element is required',
        '[ ]': 'Optional; can be omitted',
        '. . .': 'Previous element(s) may be repeatsd',
        '( )': 'Comment',
        }

    output(BNF_syntax, tty=tty, verbose=verbose)


#@cli.command()
#@click.argument("paths", type=str, nargs=-1)
#@click.argument("sysskel",
#                type=click.Path(exists=False,
#                                dir_okay=True,
#                                file_okay=False,
#                                allow_dash=False,
#                                path_type=Path,),
#                nargs=1,
#                required=True,)
#@click.option('--ipython', is_flag=True)
#@click_add_options(click_global_options)
#@click.pass_context
#def cli(ctx,
#        paths: Sequence[str],
#        sysskel: Path,
#        ipython: bool,
#        verbose: Union[bool, int, float],
#        verbose_inf: bool,
#        ) -> None:
#
#    tty, verbose = tv(ctx=ctx,
#                      verbose=verbose,
#                      verbose_inf=verbose_inf,
#                      )
#
#    if paths:
#        iterator = paths
#    else:
#        iterator = unmp(valid_types=[bytes,], verbose=verbose)
#    del paths
#
#    index = 0
#    for index, path in enumerate(iterator):
#        path = Path(os.fsdecode(path))
#
#        if verbose:  # or simulate:
#            ic(index, path)
#        #if count:
#        #    if count > (index + 1):
#        #        ic(count)
#        #        sys.exit(0)
#
#        with open(path, 'rb') as fh:
#            path_bytes_data = fh.read()
#
#        if not count:
#            output(path, tty=tty, verbose=verbose)
#
#    if count:
#        output(index + 1, tty=tty, verbose=verbose)
#
##        if ipython:
##            import IPython; IPython.embed()
