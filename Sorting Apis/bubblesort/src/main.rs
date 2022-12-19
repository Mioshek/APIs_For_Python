use std::env;
use std::fs;

fn get_sequence(path:&String) -> Vec<String>{
    
    let raw_sequence = fs::read_to_string(path).expect("Content");
    let sequence = raw_sequence.split(";").map(str::to_string).collect();
    return sequence;
}

fn main() {
    let terminal_output: Vec<_> = env::args().collect();
    let path = &terminal_output[1];
    let input_args = get_sequence(path);
    // println!("{:?}", input_args);
    let mut to_sort: Vec<i64> = input_args.iter().flat_map(|x| x.parse()).collect();
    for i in 0..to_sort.len() {
        for j in 0..to_sort.len(){
            if to_sort[i] > to_sort[j] {
                let first_el:i64 = to_sort[i];
                to_sort[i] = to_sort[j];
                to_sort[j] = first_el;
            }
        }
    }
    let _file = fs::File::create(path); //clears old file's content
    fs::write(path, format!("{:?}",to_sort)).expect("Unable to write file");
}
