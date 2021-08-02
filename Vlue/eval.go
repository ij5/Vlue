package main

import (
	"fmt"
	"io"

	"github.com/alecthomas/participle/v2"
	"github.com/alecthomas/repr"
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

func (v *Value) Eval(ctx *Context) (interface{}, error) {
	switch {
	case v.Number != nil:
		return *v.Number, nil
	case v.Bool != nil:
		return *v.Bool, nil
	case v.String != nil:
		return *v.String, nil
	case v.Undefined != nil:
		return false, nil
	case v.SubExpression != nil:
		return
	}
	panic("unsupported value type " + repr.String(v))
}

func (u *Unary) Eval(ctx *Context) (interface{}, error) {
	if u.Value != nil {
		return *u.Value, nil
	}

	if u.Unary != nil {
		switch {
		case *u.Op == "!":
			j, err := u.Unary.Eval(ctx)
			if err != nil {
				panic(err)
			}
			switch j.(type) {
			case float64:
				if j == 0 {
					return false, nil
				} else {
					return true, nil
				}
			case string:
				if j == "0" || j == "false" {
					return false, nil
				} else {
					return true, nil
				}
			case bool:
				return !j.(bool), nil
			}
		case *u.Op == "-":
			j, err := u.Unary.Eval(ctx)
			if err != nil {
				panic(err)
			}
			switch j.(type) {
			case float64:
				return -j.(float64), nil
			default:
				return nil, fmt.Errorf("uminus requires float64.")
			}
		}
	}

	panic("unreachable")
}

func (m *Multiplication) Eval(ctx *Context) (interface{}, error) {
	lhs, err := m.Unary.Eval(ctx)
	if err != nil {
		return nil, err
	}
	op := m.Op
	rhs, err := m.Next.Eval(ctx)
	if err != nil {
		return nil, err
	}
	lhsNumber, rhsNumber, err := checkIsNumber(ctx, lhs, rhs)
	if err != nil {
		return nil, participle.Errorf(m.Pos, "invalid arguments for %s: %s", *m.Op, err)
	}
	switch *op {
	case "*":
		return lhsNumber * rhsNumber, nil
	case "/":
		return lhsNumber / rhsNumber, nil
	}
	panic("unreachable")
}

func (a *Addition) Eval(ctx *Context) (interface{}, error) {
	lhs, err := a.Multiplication.Eval(ctx)
	if err != nil {
		return nil, err
	}
	rhs, err := a.Next.Eval(ctx)
	if err != nil {
		return nil, err
	}
	lhsNumber, rhsNumber, err := checkIsNumber(ctx, lhs, rhs)
	if err != nil {
		return nil, participle.Errorf(a.Pos, "invalid arguments for %s: %s", *a.Op, err)
	}
	switch *a.Op {
	case "+":
		return lhsNumber + rhsNumber, nil
	case "-":
		return lhsNumber - rhsNumber, nil
	}
	panic("unreachable")
}

func (c *Comparison) Eval(ctx *Context) (interface{}, error) {
	lhs, err := c.Addition.Eval(ctx)
	if err != nil {
		return nil, err
	}
	rhs, err := c.Next.Eval(ctx)
	if err != nil {
		return nil, err
	}
	lhsNumber, rhsNumber, err := checkIsNumber(ctx, lhs, rhs)
	if err != nil {
		return nil, participle.Errorf(c.Pos, "invalid arguments for %s: %s", *c.Op, err)
	}
	switch *c.Op {
	case ">":
		return lhsNumber > rhsNumber, nil
	case "<":
		return lhsNumber < rhsNumber, nil
	case "<=":
		return lhsNumber <= rhsNumber, nil
	case ">=":
		return lhsNumber >= rhsNumber, nil
	}
	panic("unreachable")
}

func checkIsNumber(ctx *Context, lhs interface{}, rhs interface{}) (float64, float64, error) {
	lhsNumber, ok := lhs.(float64)
	if !ok {
		return 0, 0, fmt.Errorf("lhs must be a number.")
	}
	rhsNumber, ok := rhs.(float64)
	if !ok {
		return 0, 0, fmt.Errorf("rhs must be a number.")
	}
	return lhsNumber, rhsNumber, nil
}
