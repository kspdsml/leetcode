freq_map = {}

s = "rabbit"
t = "barrit"

for i in range(len(s)):
    if s[i] in freq_map:
        freq_map[s[i]] += 1
    else:
        freq_map[s[i]] = 1
    if t[i] in freq_map:
        freq_map[t[i]] -= 1
    else:
        print('false')
print(freq_map)