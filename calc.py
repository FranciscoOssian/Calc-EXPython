import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'<{self.type}: {self.value}>'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_index = 0

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        left_operand = self.parse_term()

        while self.current_index < len(self.tokens):
            if self.current_token().type in ['OPERATOR'] and self.current_token().value in ['+', '-']:
                operator = self.consume_token()
                right_operand = self.parse_term()

                left_operand = Token('NUMBER', self.evaluate(left_operand, operator, right_operand))
            else:
                break

        return left_operand

    def parse_term(self):
        left_operand = self.parse_factor()

        while self.current_index < len(self.tokens):
            if self.current_token().type in ['OPERATOR'] and self.current_token().value in ['*', '/']:
                operator = self.consume_token()
                right_operand = self.parse_factor()

                left_operand = Token('NUMBER', self.evaluate(left_operand, operator, right_operand))
            else:
                break

        return left_operand

    def parse_factor(self):
        if self.current_index < len(self.tokens):
            token = self.consume_token()

            if token.type == 'NUMBER':
                return token
            elif token.type == 'LPAREN':
                result = self.parse_expression()
                if self.current_index < len(self.tokens) and self.current_token().type == 'RPAREN':
                    self.consume_token()
                    return result
                else:
                    raise Exception('Erro de sintaxe: parêntese de fechamento ausente')
            else:
                raise Exception('Erro de sintaxe: fator inesperado')
        else:
            raise Exception('Erro de sintaxe: expressão incompleta')

    def current_token(self):
        if 0 <= self.current_index < len(self.tokens):
            return self.tokens[self.current_index]
        else:
            raise Exception('Erro de sintaxe: índice de token fora dos limites')

    def consume_token(self):
        token = self.current_token()
        self.current_index += 1
        return token

    def evaluate(self, left, operator, right):
        if operator.value == '+':
            return left.value + right.value
        elif operator.value == '-':
            return left.value - right.value
        elif operator.value == '*':
            return left.value * right.value
        elif operator.value == '/':
            return left.value / right.value

class Calculator:
    def calculate(self, expression):
        tokens = self.tokenize(expression)
        parser = Parser(tokens)
        result = parser.parse()
        return result.value

    def tokenize(self, expression):
        tokens = []
        for token in re.findall(r'(\d+\.\d+|\d+|[+\-*/()])', expression):
            t = token
            if '.' in t:
                tokens.append(Token('NUMBER', float(t)))
            elif t.isdigit():
                tokens.append(Token('NUMBER', int(t)))
            elif t in ['+', '-', '*', '/']:
                tokens.append(Token('OPERATOR', t))
            elif t == '(':
                tokens.append(Token('LPAREN', t))
            elif t == ')':
                tokens.append(Token('RPAREN', t))

        return tokens
