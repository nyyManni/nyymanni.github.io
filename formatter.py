
import sys
from pygments.formatters import HtmlFormatter


class CustomFormatter(HtmlFormatter):

    def quote(self, tokensource):
        for type, text in tokensource:
            yield type, text.replace(' ', '{{{space}}}').replace('`', "{{{backtick}}}")

    def format(self, tokensource, outfile):

        source = self._format_lines(self.quote(tokensource))
        for t, piece in source:

            outfile.write(piece.encode('utf-8'))
