def freqQuery(queries):
    d = {}
    res = []
    for q in queries:
        if q[0] == 1:
            if q[1] in d:
                d[q[1]] = d[q[1]] + 1
            else:
                d[q[1]] = 1
        elif q[0] == 2:
            if q[1] in d:
                d[q[1]] = d[q[1]] - 1
        elif q[0] == 3:
            flag = False
            for i in d:
                if d[i] == q[1] :
                    flag = True
                    break
            if flag: res.append(1)
            else: res.append(0)
    return res

if __name__ == '__main__':
    print(freqQuery([[1,1], [2,2], [3,2], [1,1], [1,1], [2,1], [3,2]]))