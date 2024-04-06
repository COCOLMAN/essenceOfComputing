"""
주어진 수열에서 구간의 숫자 합이 사전에 지정한 숫자와 같은 구간을 찾는 알고리즘을 작성하라.
"""


def solution(want: int, numbers: list[int]) -> tuple[int, int]:
    l_cursor = 0
    while l_cursor < len(numbers) - 1:
        total = numbers[l_cursor]
        r_cursor = l_cursor + 1
        if total == want:
            return l_cursor, l_cursor
        while r_cursor < len(numbers):
            total += numbers[r_cursor]
            if total == want:
                return l_cursor, r_cursor
            r_cursor += 1
        l_cursor += 1
    return -1, -1


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert solution(11, numbers) == (4, 5)
