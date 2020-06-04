import re

def tokenizer(data):
    current = 0
    tokens = []
    while(current < len(data)):
        char = data[current]

        if(char=='('):
            tokens.append({
                'type': 'paren',
                'value': '('
            })
            current += 1
            continue

        if(char==')'):
            tokens.append({
                'type': 'paren',
                'value': ')'
            })
            current += 1
            continue

        WHITESPACE = re.compile("\s")
        if(WHITESPACE.match(char)):
            current += 1
            continue

        NUMBERS = re.compile("[0-9]")
        if(NUMBERS.match(char)):
            value = ""
            while(NUMBERS.match(char)):
                value += char
                current += 1
                char = data[current]
            tokens.append({
                'type': 'number',
                'value': value
            })
            continue

        if(char=='"'):
            value = ""
            current+=1
            char = data[current]
            while(char != '"'):
                value += char
                current += 1
                char = data[current]
            current += 1
            char = data[current]
            tokens.append({
                'type': 'string',
                'value': value
            })
            continue

        LETTERS = re.compile("[a-z]")
        if(LETTERS.match(char)):
            value = ""

            while(LETTERS.match(char)):
                value += char
                current += 1
                char = data[current]
            tokens.append({
                'type': 'name',
                'value': value
            })
            continue

        print("I don't know what this character is: " + char)

        return tokens

def parser(tokens):
    current = 0
    def walk():
        current = 0
        token = tokens[current]
        if(token['type']=='number'):
            current += 1
            return {
                'type': 'NumberLiteral',
                'value': token['value']
            }

        if(token['type']=='string'):
            current += 1
            return {
                'type': 'StringLiteral',
                'value': token['value']
            }

        if(token['type']=='paren' and token['value']=='('):
            current += 1
            token = tokens[current]
            node = {
                'type': 'CallExpression',
                'name': token['value']
                'params': []
            }
            current += 1
            token = tokens[current]

            while(token['type']!='paren' or (token['type']=='paren' and token['value']!=')')):


data = "(add 1 2)"
tokenizer(data)