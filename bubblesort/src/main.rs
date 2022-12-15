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
    let input_args = get_console_args();
    if input_args != ["Empty Arr"]{
        let mut to_sort: Vec<u64> = input_args.iter().flat_map(|x| x.parse()).collect();
        for i in 0..to_sort.len() {
            for j in 0..to_sort.len(){
                if to_sort[i] > to_sort[j] {
                    let first_el:u64 = to_sort[i];
                    to_sort[i] = to_sort[j];
                    to_sort[j] = first_el;
                }
            }
        }
        println!("{:?}", to_sort)
    }
    else {
        println!("{:?}", input_args)
    }
    
}