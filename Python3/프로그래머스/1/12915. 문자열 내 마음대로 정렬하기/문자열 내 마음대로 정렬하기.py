def solution(strings, n):
    answer = {}
    result = []
    for i in strings:
        answer[i] = i[n]
    
    # 값 기준으로 정렬
    sorted_dict = sorted(answer.items(), key=lambda item: (item[1], item[0]))

    for key, value in sorted_dict:
        result.append(key)
    return result

