fn main() {
    assert!(Solution::roman_to_int("III".to_string()) == 3);
    assert!(Solution::roman_to_int("LVIII".to_string()) == 58);
    assert!(Solution::roman_to_int("MCMXCIV".to_string()) == 1994);

    println!("MCMXCIV: {}", Solution::roman_to_int("MCMXCIV".to_string()));
}


pub struct Solution {}

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut result: i32 = 0;
        let chars: Vec<char> = s.chars().collect();
        let mut i = 0;

        while i < s.len() {
                let char = chars[i];

                if i + 1 < s.len() {
                    let next_char = chars[i + 1];

                if char == 'I' && (next_char == 'V' || next_char == 'X') {
                    result -= 1;
                    i += 1;
                    continue;
                }

                if char == 'X' && (next_char == 'L' || next_char == 'C') {
                    result -= 10;
                    i += 1;
                    continue;
                }

                if char == 'C' && (next_char == 'D' || next_char == 'M') {
                    result -= 100;
                    i += 1;
                    continue;
                }
            }

            match char {
                'I' => result += 1,
                'V' => result += 5,
                'X' => result += 10,
                'L' => result += 50,
                'C' => result += 100,
                'D' => result += 500,
                'M' => result += 1000,
                _ => panic!("Unexpected token")
            }

            i += 1;
        }

        result
    }
}