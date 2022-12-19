use rand::Rng;
use std::{env, fs};


fn get_console_input() -> Vec<String>{
    let console_output: Vec<_> = env::args().collect();
    return console_output;
}

fn main() {
    let mut numbers:Vec<i64> = vec![];
    let path = &get_console_input()[1];
    let mut lower_limit:&i64 = &get_console_input()[2].parse::<i64>().unwrap();
    let mut upper_limit:&i64 = &get_console_input()[3].parse::<i64>().unwrap();
    let amount: u32 = get_console_input()[4].parse::<u32>().unwrap();
    
    if upper_limit < lower_limit{
        let temp:&i64 = upper_limit;
        upper_limit = lower_limit;
        lower_limit = temp;
    }
    
    for _i in 0..amount{
        let mut rng = rand::thread_rng();
        numbers.push(rng.gen_range(lower_limit.to_owned()..upper_limit.to_owned()));
    }
    let _file = fs::File::create(path); //clears old file's content
    fs::write(path, format!("{:?}",numbers)).expect("Unable to write file");
}


