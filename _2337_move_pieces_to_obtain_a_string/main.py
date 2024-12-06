class Solution:
    def canChange(self, start: str, target: str) -> bool:
        length = len(start)
        start_idx = 0
        target_idx = 0

        while start_idx < length or target_idx < length:
            while start_idx < length and start[start_idx] == '_':
                start_idx += 1
                continue

            while target_idx < length and target[target_idx] == '_':
                target_idx += 1
                continue

            if (start_idx < length and target_idx == length) or (target_idx < length and start_idx == length):
                return False

            if start_idx == length and target_idx == length:
                return True

            if start[start_idx] != target[target_idx]:
                return False

            if (start[start_idx] == 'L' and target_idx > start_idx) or (start[start_idx] == 'R' and target_idx < start_idx):
                return False

            start_idx += 1
            target_idx += 1

        return True