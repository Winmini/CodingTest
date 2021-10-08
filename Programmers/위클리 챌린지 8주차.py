def solution(sizes):
    s_size = []
    m_size = []
    for i in sizes:
        s_size.append(min(i))
        m_size.append(max(i))
    return max(m_size)*max(s_size)