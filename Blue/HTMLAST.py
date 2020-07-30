from ast import *

class SourceGenerator(NodeVisitor):
    def __init__(self, indent_width, add_line_information=False):
        self.result = []
        self.indent_width = indent_width
        self.add_line_information = add_line_information
        self.indentation = 0
        self.new_lines = 0

    def write(self, x):
        if(self.new_lines):
            if(self.result):
                self.result.append('\n' * self.new_lines)
            self.result.append(self.indent_width * self.indentation)
            self.new_lines = 0
        self.result.append(x)

    def newline(self, node=None, extra=0):
        self.new_lines = max(self.new_lines, 1+extra)
        if node is not None and self.add_line_information:
            self.write('# line: %s' % node.lineno)
            self.new_lines = 1

    def body(self, statements):
        self.new_line = True
        self.indentation += 1
        for stmt in statements:
            self.visit(stmt)

        self.indentation += 1