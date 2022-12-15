use std::env;

fn get_console_args() -> Vec<String>{
    let mut args: Vec<_> = env::args().collect();
    args.remove(0);
    if args.len() == 0{
        args.push("Empty Arr".to_string()); 
        return args;
    }
    else {
        return args;
    }
}

fn main() {
    let mut to_sort = get_console_args();
    for i in 0..to_sort.len() {
        for j in 0..to_sort.len(){
            let i_el:u64 = to_sort[i].parse().unwrap();
            let j_el:u64 = to_sort[j].parse().unwrap();
            if i_el > j_el {
                let first_el:String = to_sort[i].to_owned();
                to_sort[i] = to_sort[j].to_owned();
                to_sort[j] = first_el;
            }
        }
    }
    println!("{:?}", to_sort)
}