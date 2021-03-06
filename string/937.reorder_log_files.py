from typing import List

input_logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]


def reorder_log_files(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    # 2개 키를 람다로 표현
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


print(reorder_log_files(input_logs))
