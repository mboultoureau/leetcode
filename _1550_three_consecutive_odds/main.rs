impl Solution {
    pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
        arr.windows(3).any(|n| n[0] % 2 == 1 && n[1] % 2 == 1 && n[2] % 2 == 1)
    }
}