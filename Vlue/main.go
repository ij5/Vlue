package main

import (
	"os"

	"github.com/alecthomas/participle/v2"
	"github.com/alecthomas/participle/v2/lexer/stateful"
)

var (
	vlueLexer = stateful.MustSimple([]stateful.Rule{
		{Name: "Comment", Pattern: `\/\/[^\n]*`, Action: nil},
		{Name: "String", Pattern: `"(\\"|[^"])*"`, Action: nil},
		{Name: "Number", Pattern: `[-+]?(\d*\.)?\d+`, Action: nil},
		{Name: "Ident", Pattern: `[a-zA-Z_]\w*`, Action: nil},
		{Name: "EOL", Pattern: `[\n\r]+`, Action: nil},
		{Name: "whitespace", Pattern: `[ \t]+`, Action: nil},
	})
	parser = participle.MustBuild(
		&Program{},
		participle.Lexer(vlueLexer),
		participle.Unquote("String"),
	)
)

func main() {
	r, _ := os.Open("test.vl")
	program, err := Parse(r)
	if err != nil {
		panic(err)
	}

	funcs := map[string]Function{}

	err = program.Eval(os.Stdin, os.Stdout, funcs)
	if err != nil {
		panic(err)
	}
}
