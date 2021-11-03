_end = '_end_'
T = int(input())
for test_case in range(1, T + 1):
    A, B = [int(i) for i in input().split()]
    root = dict()
    answer = 0
    words = []
    for _ in range(A):
        words.append(input())
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    words = []
    for _ in range(B):
        words.append(input())
    for word in words:
        current_dict = root
        for letter in word:
            if letter not in current_dict:
                answer -= 1
                break
            current_dict = current_dict[letter]
        answer += 1
    print('#{} {}'.format(test_case, answer))