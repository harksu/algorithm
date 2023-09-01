# 파이썬 알고리즘 인터뷰 공부하면서 실습 코드

import re
import collections


def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(
        r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    counts = collections.Counter(words)

    return (counts.most_common(1)[0][0])


paragraph = "bob hit a ball, the hit BALL flew far after it was hit"
print(mostCommonWord(paragraph, banned=['hit']))
