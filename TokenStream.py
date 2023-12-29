from Token import Token


class TokenStream:
    """List of valid Tokens.

    This is a list of tokens that represents a parsable form of the text describing the prerequisites for a single
    course.

    Attributes:
        tokens (list): List of tokens

    Methods:
        add_token(self, token): Adds a token to the list of tokens
    """
    def __init__(self, tokens=None):
        if tokens is None:
            tokens = []
        self.tokens = tokens

    def add_token(self, token: Token):
        """Adds a token to the list of tokens.

        Args:
            token (Token): Token to be added.

        Returns:
            void
        """
        self.tokens.append(token)
