def solution(array, commands):
    len(array) >= 1; len(array) <= 100
    len(commands) >=1; len(commands) <= 50
    answer = []
    for a in range(len(commands)):
        newarray = array[commands[a][0]-1 :commands[a][1]]
        newarray.sort()
        newnumber = newarray[commands[a][2]-1]
        answer.append(newnumber)
    return answer
