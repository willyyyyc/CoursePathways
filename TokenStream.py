from Token import Token


class TokenStream:
    """List of valid Tokens.

    This is a list of tokens that represents a parsable form of the text describing the prerequisites for a single
    course.

    Attributes:
        tokens (list): List of tokens

    Methods:
        get_stream(self): Returns token stream
    """
    def __init__(self, tokens):
        self.tokens = tokens

    def get_stream(self):
        """Returns token stream.

        Returns:
            list of tokens
        """
        return self.tokens

    def __str__(self):
        return str(self.tokens)