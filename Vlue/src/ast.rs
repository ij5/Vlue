#[derive(Debug)]
pub enum Expr {
  Number(i32),
  Op(Box<Expr>, OpCode, Box<Expr>),
  CompOp(Box<Expr>, CompOpCode, Box<Expr>),
  FnCall(String, Vec<Expr>),
}

#[derive(Debug)]
pub enum Symbols {
  LSB,
  RSB,
  SEMI,
  NL,
  COMMA,
}

#[derive(Debug)]
pub enum Stmt {
  VarDec(String, Box<Type>),
  Expr(Box<Expr>)
}

#[derive(Debug)]
pub enum Type {
  Int(i32),
  Float(f32),
  Str(String),
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