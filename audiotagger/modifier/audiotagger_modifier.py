class AudioTaggerModifier(object):
    @staticmethod
    def remove_leading_trailing_spaces(var):
        """Removes leading trailing spaces from string tags.

        Args:
            var (str): TITLE, ARTIST, etc.

        Returns:
            anonymous (str): Stripped string.
        """
        return var.strip()

    @staticmethod
    def remove_multiple_whitespace(var):
        """Removes multiple whitespaces in the middle of a string.

        This implementation also removes all whitespace characters (e.g.
        tab, newline, return, etc.)

        Args:
            var (str): TITLE, ARTIST, etc.

        Returns:
            anonymous (str): Returns clean string.
        """
        return " ".join(var.split())

    @staticmethod
    def uppercase(var):
        return var.upperc()

    @staticmethod
    def lowercase(var):
        return var.lower()

    @staticmethod
    def title(var):
        return var.title()
