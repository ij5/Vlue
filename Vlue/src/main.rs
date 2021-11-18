#[macro_use]
extern crate lalrpop_util;

// mod grammar;
mod parser;
mod ast;
mod vm;

use std::{env, io::Read};
use std::fs::File;

#[test]
fn test_fn_call(){
    
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() == 1 {
        panic!("Please input file name.");
    }
    let mut f = File::open(args[1].as_str()).expect("file not found.");
    let mut input = String::new();
    f.read_to_string(&mut input).expect("Something went wrong reading this file.");
    
    parser::parse(input.as_str());
    
    
}