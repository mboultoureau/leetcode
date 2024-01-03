int climbStairs(int n) {
    if (n <= 2) {
        return n;
    }

    int previous_one = 1;
    int previous_two = 2;

    for (int i = 2; i < n ; i++) {
        int current = previous_one + previous_two;
        previous_one = previous_two;
        previous_two = current;
    }

    return previous_two;
}