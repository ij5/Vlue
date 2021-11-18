#[derive(Debug)]
pub enum Expr {
  Number(i32),
  Op(Box<Expr>, OpCode, Box<Expr>),
  CompOp(Box<Expr>, CompOpCode, Box<Expr>),
}

#[derive(Debug)]
pub enum OpCode {
  Mul,
  Div,
  Add,
  Sub,
}

#[derive(Debug)]
pub enum CompOpCode {
  Eq,
  NotEq,
  Lt,
  LtE,
  Gt,
  GtE,
}