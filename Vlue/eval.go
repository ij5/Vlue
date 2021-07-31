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


func (v *Value) Eval(ctx *Context)(interface{}, error){
	switch{
	case v.Number != nil:
		return *v.Number, nil
	case v.String != nil:
		return *v.String, nil
	case v.Variable != nil:
		value, ok := ctx.Vars[*v.Variable]
		if !ok {
			return nil, fmt.Errorf("unknown variable %q", *v.Variable)
		}
		return value, nil
	case v.Call != nil:
		return v.Call.
	}
	panic("unsupported value type "+repr.String(v))
}

func (f *Factor) Eval(ctx *Context) (interface{}, error){
	value, err := 
}

