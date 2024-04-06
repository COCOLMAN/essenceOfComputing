"""
[예제 1.3]
일련의 실수가 주어질 때 합이 가장 큰 구간을 찾는 가장 효율적인 알고리즘을 설계하라.

[예제 1.3]의 선형 복잡도 알고리즘을 의사 코드로 작성하라.
"""


def solution(numbers: list[int]):
    start_idx = 0
    cursor = start_idx

    total = numbers[cursor]
    max_total = total
    max_start_idx, max_end_idx = start_idx, cursor
    cursor += 1

    while cursor < len(numbers):
        number = numbers[cursor]
        total += number
        if total > max_total:
            max_total = total
            max_start_idx = start_idx
            max_end_idx = cursor
        if total < 0:
            total = 0
            start_idx = cursor + 1
        cursor += 1

    return max_start_idx+1, max_end_idx+1


numbers1 = [1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -12.2, 34.2, 5.4, -7.8, 1.1, -4.9]
assert solution(numbers1) == (5, 10)

numbers2 = [1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -62.2, 44.2, 5.4, -7.8, 1.1, -4.9]
assert solution(numbers2) == (9, 10)
