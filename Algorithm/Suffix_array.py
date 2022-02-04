def calc_lcp(A, B):
    min_len = min(len(A), len(B))
    for c in range(min_len):  # A와 B를 비교해, 처음부터 연속된 같은 글자의 수가 LCP
        if A[:c + 1] != B[:c + 1]:
            break
    return c


def find_n_th_substring(suffix, n, max_len):
    lcp = 0
    i = 0
    while i < len(suffix):
        cur_idx, cur_suffix = suffix[i]
        candidate_num = max_len - cur_idx

        if candidate_num - lcp >= n:
            return cur_suffix[:n + lcp]
        else:
            n -= candidate_num - lcp
            if i != len(suffix) - 1:
                lcp = calc_lcp(cur_suffix, suffix[i + 1][1])
            i += 1
    return 0, 0