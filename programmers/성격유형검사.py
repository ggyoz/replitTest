def solution(survey, choices):

    answer = ''
    charactor = {
        "R": 0,
        "T": 0,
        "C": 1,
        "F": 1,
        "J": 2,
        "M": 2,
        "A": 3,
        "N": 3
    }
    score = [{
        "R": 0,
        "T": 0
    }, {
        "C": 0,
        "F": 0
    }, {
        "J": 0,
        "M": 0
    }, {
        "A": 0,
        "N": 0
    }]

    for idx in range(len(choices)):

        if choices[idx] - 4 < 0:
            s = survey[idx][0]
        elif choices[idx] - 4 > 0:
            s = survey[idx][1]
        else:
            continue

        score[charactor[s]][s] += abs(choices[idx] - 4)

    for sco in score:
        value = -1
        word = ''
        for c in sco:
            if value < sco[c]:
                value = sco[c]
                word = c

        answer += word

    return answer
