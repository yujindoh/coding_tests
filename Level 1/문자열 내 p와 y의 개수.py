#https://programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    if s.count('p') + s.count('P') == s.count('y') + s.count('Y'):
        return True
    return False
