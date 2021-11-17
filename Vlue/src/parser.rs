lalrpop_mod!(pub grammar);

use lalrpop_util::lexer::Token;

#[allow(unused_imports)]
use super::ast::{Expr, OpCode};

#[allow(dead_code)]
fn print_type_of<T>(_:  &T) {
  println!("{}", std::any::type_name::<T>())
}


pub fn parse(input: &str){
  let result: Result<Box<Expr>, lalrpop_util::ParseError<usize, Token, &'static str>> = grammar::ExprParser::new().parse(input);
  match result {
    Ok(value) => {
      let res = exp_parse(*value);
      let Node::Num(n) = res;
      println!("{}", n);
    },
    Err(e)=>println!("{:?}", e),
  }
}

enum Node {
  
  Num(i32),

}


fn exp_parse(expr: Expr) -> Node {
  match expr{
    Expr::Op(l, op, r) => {
      parse_binary_expr(*l, op, *r)
    }
    Expr::Number(num) => {
      Node::Num(num)
    }
  }
}

fn parse_binary_expr(l: Expr, op: OpCode, r: Expr) -> Node {
  let left = exp_parse(l);
  let right = exp_parse(r);
  let left_value = match left {
    Node::Num(n) => n,
    _ => panic!("Expected a number."),
  };
  let right_value = match right {
    Node::Num(n) => n,
    _ => panic!("Expected a number."),
  };
  match op {
      OpCode::Add => Node::Num(left_value + right_value),
      OpCode::Sub => Node::Num(left_value - right_value),
      OpCode::Mul => Node::Num(left_value * right_value),
      OpCode::Div => Node::Num(left_value / right_value),
  }
}