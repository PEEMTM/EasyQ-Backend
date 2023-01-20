from Parser import Tokenizer

class Parser:
    def __init__(self, src, host):
        self.tkz = Tokenizer(src)
        self.statement = []
        self.parse()

    def parse(self):
        self.parse_program()
        if self.tkz.peek() != "":
            raise SyntaxError()

    def is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def parse_program(self):
        while self.tkz.peek() != "":
            self.statement.append(self.parse_statement())

    def eval(self):
        for each in self.statement:
            each.eval()
