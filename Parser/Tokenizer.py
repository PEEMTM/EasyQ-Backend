import re

class Tokenizer:
    def __init__(self, src):
        self.src = src
        self.pos = 0
        self.compute_next()

    def is_character(self, ch):
        return re.match("[a-zA-z]", ch)

    def is_operator(self, ch):
        return ch in ['+', '-', '*', '/', '%', '(', ')', '{', '}', '^', '=']

    def is_digit(self, ch):
        return ch.isdigit()

    def is_space(self, ch):
        return ch == ' '

    def compute_next(self):
        s = ""

        while self.pos < len(self.src):
            ch = self.src[self.pos]

            if self.is_digit(ch):
                s += ch
                while self.pos < len(self.src) and self.is_digit(self.src[self.pos]):
                    s += self.src[self.pos]
                    self.pos += 1
                break
            elif self.is_operator(ch):
                s += ch
                self.pos += 1
                break
            elif self.is_character(ch):
                s += ch
                while self.pos < len(self.src) and self.is_character(self.src[self.pos]):
                    s += self.src[self.pos]
                    self.pos += 1
                break
            elif self.is_space(ch):
                self.pos += 1
            else:
                raise SyntaxError(f"Unknown character: {ch}")

        self.next = s

    def peek(self):
        return self.next

    def peek_equals(self, s):
        return self.peek() == s

    def consume(self):
        result = self.next
        if self.pos < len(self.src):
            self.compute_next()
        else:
            self.next = ""
        return result

    def consume_equals(self, s):
        if self.peek_equals(s):
            self.consume()
        else:
            raise SyntaxError(self.peek())
