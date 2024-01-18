impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n == 1 {
            return 1;
        }

        let mut previous: i32 = 1;
        let mut current: i32 = 2;

        for _ in 2..n {
            let new_current = previous + current;
            previous = current;
            current = new_current;
        }

        current
    }
}