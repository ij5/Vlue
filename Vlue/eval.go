package main

import (
	"fmt"
	"io"

	"github.com/alecthomas/participle/v2"
	"github.com/alecthomas/repr"
	"golang.org/x/tools/go/analysis/passes/nilfunc"
)

type Evaluatable interface {
	Eval(ctx *Context) (interface{}, error)
}

type Function func(args ...interface{}) (interface{}, error)

type Context struct {
	Functions map[string]Function
	Vars      map[string]interface{}
	Input     io.Reader
	Output    io.Writer
}

func (p *Program) init() {
	p.Table = map[int]*Statement{}
	for index, stmt := range p.Statements {
		stmt.Index = index
		p.Table[stmt.Pos.Offset] = stmt
	}
}
