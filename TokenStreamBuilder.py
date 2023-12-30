import re


none = re.compile('None')
faculty = re.compile('^[A-Z]{4}$')
code = re.compile('^[0-9]{4}')
or_re = re.compile('or')
and_re = re.compile('and')
left_brace = re.compile('\\(')
right_brace = re.compile('\\)')


def remove_item(list_, item):
    return [i for i in list_ if i != item]


def fix_line(raw_line):
    broken_line = ['PREREQUISITES:', 'CSCI', '1300', 'or', 'MATH', '1000', 'or', 'MATH', '1280', ')', 'and', '(',
                   'CSCI', '1105', 'or', 'CSCI', '1110', 'or', 'CSCI', '1503', 'or', 'CSCI', '2202', ')']
    broken_code_0 = re.compile('^\\d{3}$')
    broken_code_1 = re.compile('^\\d')
    broken_code_2 = re.compile('^CSCI\\d{4}')
    broken_code_3 = re.compile('^\\d$')

    brace_split = re.compile('(\\()|(\\))').split
    raw_line = [part for word in raw_line for part in brace_split(word) if part]

    if raw_line == broken_line:
        raw_line.insert(1, "(")
    raw_line = remove_item(raw_line, 'PREREQUISITES:')
    raw_line = remove_item(raw_line, ',')

    i = 0
    while i < len(raw_line) - 1:
        if ((broken_code_0.match(raw_line[i]) and broken_code_1.match(raw_line[i + 1])) or raw_line[i] == 'CSC'
                or raw_line[i] == 'MA'):
            raw_line[i] = raw_line[i] + raw_line[i + 1]
            raw_line.pop(i + 1)
        elif raw_line[i] == 'CSCi':
            raw_line[i] = 'CSCI'
        elif broken_code_2.match(raw_line[i]):
            raw_line.insert(i + 1, raw_line[i].replace('CSCI', ""))
            raw_line[i] = 'CSCI'
        elif broken_code_3.match(raw_line[i]):
            raw_line.pop(i + 1)
        i += 1
    return raw_line


class TokenStreamBuilder:
    """Build a token stream for each line in a file containing prerequisites.

    This class acts as a "manual scanner" -- it returns a token stream (list of tokens) that represents a parsable form
    of the text describing the prerequisites for a single course.

    Unfortunately, the process of converting valid strings into Token objects could not be automated. There were two
    reasons:
    First, errors in the original pdf. Missing characters that would be impossible for an algorithm to know
    where to add BEFORE scanning. These had to be hardcoded in.
    Second, the PdfReader object does not return a perfect text representation of the pdf. White spaces are either added
    or neglected at random. This results in broken strings -- strings that would otherwise be valid tokens are broken in
    such a random way that special cases had to be identified and fixed while the prerequisites were still in text form.

    The TokenStreamBuilder object creates a Token object for valid strings in the input file. It creates a list of
    tokens and returns that list as a TokenStream object. The TokenStream can then be parsed and a grammar can be used
    to understand the prerequisite pattern it is conveying.

    Attributes:
        file (txt file): the txt file containing the lines of raw prerequisite strings

    Methods:
        build_token_stream(self):
            Builds and returns a token stream for each line in the input file
    """
    def __init__(self, raw_prerequisites):
        """Constructor method.

        Args:
            raw_prerequisites (txt file): the txt file containing prerequisite strings to be scanned
        """
        self.file = raw_prerequisites

    def build_token_stream(self):
        """Builds and returns a token stream for each line in file.

        Note: a token stream is a TokenStream object which itself is a list of tokens - each token is a Token object.

        Returns:
            list of token streams
        """
        with open(self.file, 'r') as f:
            for line in f:
                raw_line = line.rsplit()
                raw_line = fix_line(raw_line)   # Call helper function that hardcodes a correct line

                patterns = [none, faculty, code, or_re, and_re, left_brace, right_brace]
                matches = [word for word in raw_line if any(pattern.match(word) for pattern in patterns)]
                for match in matches:
                    raw_line.remove(match)

                #print(matches)
                print('->', raw_line, '\n')

#plan:
#break line into list of characters
#goal: a list of course title objects to fill an adjacency list. some entries in list will themselves be lists, representing optional ('or' prerequisites)