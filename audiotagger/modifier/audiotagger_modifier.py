# SPDX-License-Identifier: GPL-3.0-or-later
"""All tools to modify tags are here.

"""
import pandas as pd


def strip_str(arg):
    """Removes leading trailing spaces from a string.

    Args:
        arg (str, dataframe of str, series of str): TITLE, ARTIST, etc.

    Returns:
        arg (input type): Returns input data with stripped strings.
    """
    if isinstance(arg, str):
        arg = arg.strip()

    elif isinstance(arg, pd.Series):
        arg = arg.str.strip()

    elif isinstance(arg, pd.DataFrame):
        for col in arg:
            arg[col] = arg[col].str.strip()

    return arg


def _create_spacing_for_characters(arg):
    """Helper method to add spacings in a string.

    Args:
        arg (str): A string tag such as <title> or <artist>.

    Returns:
        arg (str): Returns the modified argument.
    """
    left = ["(", "["]
    right = [")", "]"]
    both = ["/"]

    for c in left:
        if c in arg:
            # e.g. foo(bar) -> foo (bar)
            arg = arg.replace(c, " " + c)

    for c in right:
        if c in arg:
            # e.g. (foo)bar -> (foo) bar
            arg = arg.replace(c, c + " ")

    for c in both:
        if c in arg:
            # e.g. foo/bar -> foo / bar
            arg = arg.replace(c, " " + c + " ")

    return arg


def create_spacing_for_characters(arg):
    """Create spaces next to special characters.

    Args:
        arg (str, dataframe of str, series of str): TITLE, ARTIST, etc.

    Returns:
        arg (input type): Returns cleaned input.
    """
    if isinstance(arg, str):
        arg = _create_spacing_for_characters(arg)

    elif isinstance(arg, pd.Series):
        arg = arg.apply(_create_spacing_for_characters)

    elif isinstance(arg, pd.DataFrame):
        for col in arg:
            arg[col] = arg[col].apply(_create_spacing_for_characters)

    return arg


def _remove_multiple_whitespace(arg):
    """Helper method to remove multiple white spaces in a string.

    """
    return " ".join(arg.split())


def remove_multiple_whitespace(arg):
    """Removes multiple whitespaces in the middle of a string.

    This implementation also removes all whitespace characters (e.g.
    tab, newline, return, etc.)

    Args:
        arg (str, dataframe of str, series of str): TITLE, ARTIST, etc.

    Returns:
        anonymous (input type): Returns cleaned input.
    """
    if isinstance(arg, str):
        arg = _remove_multiple_whitespace(arg)

    elif isinstance(arg, pd.Series):
        arg = arg.apply(_remove_multiple_whitespace)

    elif isinstance(arg, pd.DataFrame):
        for col in arg:
            arg[col] = arg[col].apply(_remove_multiple_whitespace)

    return arg
