def solution(sequence, k):
    answer = [0, float("inf")]

    start, end = 0, 0
    partial_sum = sequence[0]

    while start <= end < len(sequence):
        if sequence[end] == k:
            return [end, end]
        if partial_sum == k:
            answer = [start, end] if answer[1] - answer[0] > end - start else answer
            partial_sum -= sequence[start]
            start += 1
        elif partial_sum < k and end + 1 < len(sequence):
            end += 1
            partial_sum += sequence[end]
        else:
            partial_sum -= sequence[start]
            start += 1

    return answer