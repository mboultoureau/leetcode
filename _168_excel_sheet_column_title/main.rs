impl Solution {
    pub fn convert_to_title(mut column_number: i32) -> String {
        let mut result: String = "".to_string();
        
        while column_number > 0 {
            let dividor: i32 = (column_number - 1) / 26;
            let remainder: i32 = (column_number - 1) % 26;
            let new_char: char = (remainder as u8 + 'A' as u8) as char;

            result = new_char.to_string() + &result;
            column_number = dividor;
        }

        result
    }
}