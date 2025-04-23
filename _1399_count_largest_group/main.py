class Solution:
    def countLargestGroup(self, n: int) -> int:
        sums = Counter()

        for i in range(1, n + 1):
            sum_of_digit = sum([int(k) for k in list(str(i))])
            sums[sum_of_digit] += 1

        nb_groups = 0
        _, max_value = sums.most_common(1)[0]
        for _, value in sums.most_common():
            if value != max_value:
                break

            nb_groups += 1

        return nb_groups