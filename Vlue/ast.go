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

	Expression *Expression `( @@ ";" )`
}

type Expression struct {
	Pos lexer.Position
}

type Unary struct {
	Op    string `( @("!" | "-")`
	Unary *Unary ` @@ )`
	Value *Value `| @@`
}

type Value struct {
	Number        float64     `  @Float | @Int`
	String        string      `| @String`
	Bool          bool        `| @("true" | "false")`
	Undefined     bool        `| @"undefined"`
	SubExpression *Expression `| "(" @@ ")"`
}
