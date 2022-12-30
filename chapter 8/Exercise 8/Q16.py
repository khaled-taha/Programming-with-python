"""
16. Let L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]. Use a list comprehension to
produce a list of the gaps between consecutive entries in L. Then find the maximum gap size
and the percentage of gaps that have size 2
"""
L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

gaps = [L[i] - L[i - 1] for i in range(1, len(L)) if L[i] - L[i - 1] > 1]
print(max(gaps))
print(gaps.count(2) / len(gaps))
