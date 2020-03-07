import re


class Word_Counter:
    def __init__(self, txtpath):
        self._mapping = dict()
        with open(txtpath) as f:
            data = f.read()
            words = [s.lower() for s in re.findall("\w+", data)]
            for word in words:
                self._mapping[word] = self._mapping.get(word, 0) + 1

    def most_common(self, n):
        return sorted(self._mapping.items(), key=lambda item: item[1], reverse=True)[:n]


if __name__ == '__main__':
    most_common_3 = Counter(r"C:\pytest\test.txt").most_common(3)
    for item in most_common_3:
        print(item)
