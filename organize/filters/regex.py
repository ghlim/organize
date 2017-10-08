import re
from .filter import Filter


class Regex(Filter):

    """
    Matches filenames with the given regular expression

    :param str expr:
        The regular expression to be matched
    """

    def __init__(self, expr):
        self.expr = re.compile(expr)

    def matches(self, path):
        return self.expr.match(path.name)

    def parse(self, path):
        # TODO: regex.xyz namespace
        return self.expr.match(path.name).groupdict()
