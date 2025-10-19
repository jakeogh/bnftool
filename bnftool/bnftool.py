#!/usr/bin/env python3
# -*- coding: utf8 -*-
# tab-width:4

from __future__ import annotations

from signal import SIG_DFL
from signal import SIGPIPE
from signal import signal

import click
from click_auto_help import AHGroup
from clicktool import click_add_options
from clicktool import click_global_options
from clicktool import tv
from mptool import output

signal(SIGPIPE, SIG_DFL)


def get_bnf_syntax():
    BNF_syntax = {
        "< >": "Defined element",
        "=": "is defined as",
        "|": "exclusive OR",
        "{ }": "Group; one element is required",
        "[ ]": "Optional; can be omitted",
        ". . .": "Previous element(s) may be repeatsd",
        "( )": "Comment",
    }
    return BNF_syntax


@click.group(no_args_is_help=True, cls=AHGroup)
@click_add_options(click_global_options)
@click.pass_context
def cli(
    ctx,
    verbose_inf: bool,
    dict_output: bool,
    verbose: bool = False,
) -> None:

    tty, verbose = tv(
        ctx=ctx,
        verbose=verbose,
        verbose_inf=verbose_inf,
    )


@cli.command()
@click_add_options(click_global_options)
@click.pass_context
def syntax(
    ctx,
    verbose_inf: bool,
    dict_output: bool,
    verbose: bool = False,
) -> None:

    tty, verbose = tv(
        ctx=ctx,
        verbose=verbose,
        verbose_inf=verbose_inf,
    )

    output(
        get_bnf_syntax(),
        reason=None,
        tty=tty,
        pretty_print=True,
        dict_output=dict_output,
        verbose=verbose,
    )
