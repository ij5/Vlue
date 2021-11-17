#[derive(Debug)]
pub enum Expr {
  Number(i32),
  Op(Box<Expr>, OpCode, Box<Expr>)
}

#[derive(Debug)]
pub enum OpCode {
  Mul,
  Div,
  Add,
  Sub,
}