use std::fs;

fn main()-> Result<(), Box<dyn std::error::Error>> {
   
    let path: &str = "hosts";

    let content: String = fs::read_to_string(&path)?;

    println!("{content}");
    Ok(()) 
  
   
} 
