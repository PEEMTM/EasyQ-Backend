class SyntaxError(Exception):
    def __init__(self):
        super().__init__("Syntax Error")

    def __init__(self, message):
        super().__init__(message)
