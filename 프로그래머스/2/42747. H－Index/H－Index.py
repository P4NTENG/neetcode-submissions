# 제출11111
def solution(citations):
    h = 0
    citations = sorted(citations)
    for index, citation in enumerate(reversed(citations)):
        if citation >= index + 1:
            h += 1
    return h