METHOD = "findItinerary"

CASES = [
    dict(args=([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']],), expected=['JFK', 'MUC', 'LHR', 'SFO', 'SJC']),
    dict(args=([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']],), expected=['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']),
    # 只有一张机票
    dict(args=([['JFK', 'AAA']],), expected=['JFK', 'AAA']),
    # 字典序最小的 KUL 是死路，必须先飞 NRT 再回来
    dict(args=([['JFK', 'KUL'], ['JFK', 'NRT'], ['NRT', 'JFK']],), expected=['JFK', 'NRT', 'JFK', 'KUL']),
    # 重复的机票，每张都要用一次
    dict(args=([['JFK', 'ATL'], ['ATL', 'JFK'], ['JFK', 'ATL'], ['ATL', 'JFK']],), expected=['JFK', 'ATL', 'JFK', 'ATL', 'JFK']),
    # 多个环套在一起，重复机票 TIA→ANU
    dict(args=([['EZE', 'AXA'], ['TIA', 'ANU'], ['ANU', 'JFK'], ['JFK', 'ANU'], ['ANU', 'EZE'], ['TIA', 'ANU'], ['AXA', 'TIA'], ['TIA', 'JFK'], ['ANU', 'TIA'], ['JFK', 'TIA']],), expected=['JFK', 'ANU', 'EZE', 'AXA', 'TIA', 'ANU', 'JFK', 'TIA', 'ANU', 'TIA', 'JFK']),
]
