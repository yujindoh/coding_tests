#https://programmers.co.kr/learn/courses/30/lessons/42576
#정확성 테스트는 통과했는데 효율성 테스트를 통과 못함... .count() 같은 내장함수들이 효율성을 깎아먹는다고 함.
#그래서 다른 사람들 풀이를 열심히 봤는데 한번도 본적 없는 모듈들을 쓰길래 그부분에 대해 더 공부할 필요성이 있다고 느낌.

def solution(participant, completion):
    for a in participant:
        if a in completion:
            if participant.count(a) > completion.count(a):
                return a
        else:
                return a
