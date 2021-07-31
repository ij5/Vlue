package main

import "fmt"

func evalFloats(ctx *Context, lhs interface{}, rhsExpr Evaluatable) (float64, float64, error) {
	rhs, err := rhsExpr.Eval(ctx)
	if err != nil {
		return 0, 0, err
	}
	lhsNumber, ok := lhs.(float64)
	if !ok {
		return 0, 0, fmt.Errorf("lhs must be a number")
	}
	rhsNumber, ok := rhs.(float64)
	if !ok {
		return 0, 0, fmt.Errorf("rhs must be a number")
	}
	return lhsNumber, rhsNumber, nil
}
