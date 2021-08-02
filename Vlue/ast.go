package main

import (
	"io"

	"github.com/alecthomas/participle/v2/lexer"
)

func Parse(r io.Reader) (*Program, error) {
	program := &Program{}
	err := parser.Parse("", r, program)
	if err != nil {
		return nil, err
	}
	program.init()
	return program, nil
}

type Program struct {
	Pos lexer.Position

	Statements []*Statement `@@*`

	Table map[int]*Statement
}

type Statement struct {
	Pos lexer.Position

	Index int

	Expression *Expression ` | ( @@ ";" )`
}

type Expression struct {
	Pos lexer.Position

	Equality *Equality `@@`
}

type Equality struct {
	Pos lexer.Position

	Comparison *Comparison `@@`
	Op         *string     `[ @("!" "=" | "=" "=")`
	Next       *Equality   `  @@ ]`
}

type Comparison struct {
	Pos lexer.Position

	Addition *Addition   `@@`
	Op       *string     `[ @(">" | "<" | ">" "=" | "<" "=")`
	Next     *Comparison `@@ ]`
}

type Addition struct {
	Pos lexer.Position

	Multiplication *Multiplication `@@`
	Op             *string         `[ @("-" | "+")`
	Next           *Addition       `@@ ]`
}

type Multiplication struct {
	Pos lexer.Position

	Unary *Unary          `@@`
	Op    *string         `[ @("/" | "*")`
	Next  *Multiplication ` @@ ]`
}

type Unary struct {
	Pos lexer.Position

	Op    *string `( @("!" | "-")`
	Unary *Unary  ` @@ )`
	Value *Value  `| @@`
}

type Value struct {
	Pos lexer.Position

	Number        *float64    `  @Float | @Int`
	String        *string     `| @String`
	Bool          *bool       `| @("true" | "false")`
	Undefined     *bool       `| @"undefined"`
	SubExpression *Expression `| "(" @@ ")"`
}
