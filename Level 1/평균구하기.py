#https://programmers.co.kr/learn/courses/30/lessons/12944
#sum 함수를 쓰면 더 간단하게 할 수 있다더라...하하...
def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    return (answer / len(arr))
