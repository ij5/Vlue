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

	Expression *Expression `( @@ ";"`
	If         *If         `| @@ )`
}

type Decorator struct {
	Pos lexer.Position

	Message string `"@" @String`
}

type Declaration struct {
	Pos lexer.Position

	Variable string      `"var" @Ident`
	Value    *Expression `"=" @@`
}

type If struct {
	Pos lexer.Position

	Condition       *Expression `"if" "(" @@ ")"`
	Then            *Statement  `"{" @@ "}"`
	ElseIfCondition *Expression `( "else" "if" "(" @@ ")"`
	ElseIfThen      *Statement  `"{" @@ "}" )*`
	ElseThen        *Statement  `( "else" "{" @@ "}" )?`
}

type Value struct {
	Pos lexer.Position

	Number   *float64 ` @Number`
	Variable *string  `| @Ident`
	String   *string  `| @String`
	Call     *Call    `| @@`
}

type Expression struct {
	Pos lexer.Position

	Value *Uminus `( @@ ) ";"`
}

type Operator string

type Comparison struct {
	Pos lexer.Position
}

type First struct {
	Pos lexer.Position

	Expression *Expression `"(" @@ ")" | @@`
}

type Factor struct {
	Pos lexer.Position

	Operator Operator `@("*" | "/")`
	Value    *Uminus  `| @@ )`
}

type Term struct {
	Pos lexer.Position

	Operator Operator `@("+" | "-")`
	Factor   *Factor  `@@`
}

type Uminus struct {
	Pos lexer.Position

	First *First `( @@ | "-" @@ )`
}

type Call struct {
	Pos lexer.Position

	Left  string     `@Ident`
	Right *Parameter `"(" @@ ")"`
}

type Parameter struct {
	Left  *Expression `@@`
	Right *Expression `("," @@)*`
}
