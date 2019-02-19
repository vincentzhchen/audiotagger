import pandas as pd


class AudioTaggerModifier(object):
    @classmethod
    def strip_str(cls, arg):
        """Removes leading trailing spaces from a string.

        Args:
            arg (str, dataframe of str, series of str): TITLE, ARTIST, etc.

        Returns:
            anonymous (input type): Returns input data with stripped strings.
        """
        if arg.__class__ == str:
            arg = arg.strip()

        elif arg.__class__ == pd.Series:
            arg = arg.str.strip()

        elif arg.__class__ == pd.DataFrame:
            for col in arg:
                arg[col] = arg[col].str.strip()

        return arg

    @classmethod
    def _create_spacing_for_characters(cls, arg):
        left = ["(", "["]
        right = [")", "]"]
        both = ["/"]

        for c in left:
            if c in arg:
                arg = arg.replace(c, " " + c)

        for c in right:
            if c in arg:
                arg = arg.replace(c, c + " ")

        for c in both:
            if c in arg:
                arg = arg.replace(c, " " + c + " ")

        return arg

    @classmethod
    def create_spacing_for_characters(cls, arg):
        """Create spaces next to special characters.

        Args:
            arg (str, dataframe of str, series of str): TITLE, ARTIST, etc.

        Returns:
            anonymous (input type): Returns cleaned input.
        """
        if arg.__class__ == str:
            arg = AudioTaggerModifier._create_spacing_for_characters(arg)

        elif arg.__class__ == pd.Series:
            arg = arg.apply(AudioTaggerModifier._create_spacing_for_characters)

        elif arg.__class__ == pd.DataFrame:
            for col in arg:
                arg[col] = arg[col].apply(
                    AudioTaggerModifier._create_spacing_for_characters)

        return arg

    @classmethod
    def _remove_multiple_whitespace(cls, arg):
        return " ".join(arg.split())

    @classmethod
    def remove_multiple_whitespace(cls, arg):
        """Removes multiple whitespaces in the middle of a string.

        This implementation also removes all whitespace characters (e.g.
        tab, newline, return, etc.)

        Args:
            arg (str, dataframe of str, series of str): TITLE, ARTIST, etc.

        Returns:
            anonymous (input type): Returns cleaned input.
        """
        if arg.__class__ == str:
            arg = AudioTaggerModifier._remove_multiple_whitespace(arg)

        elif arg.__class__ == pd.Series:
            arg = arg.apply(AudioTaggerModifier._remove_multiple_whitespace)

        elif arg.__class__ == pd.DataFrame:
            for col in arg:
                arg[col] = arg[col].apply(
                    AudioTaggerModifier._remove_multiple_whitespace)

        return arg
