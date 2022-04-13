def solution(prices):  
    answer = []
    for n in range(len(prices)):
        answer.append(len(prices) - n - 1)
        for m in range(n + 1, len(prices)):                  
            if( prices[n] > prices[m] ):
                answer[n] = m - n
                break
    return answer