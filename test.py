def solution(data, n): 
    # Your code here
    solutions_lst = []
    counters = [0] * (max(data) + 1)
    for item in data:
        counters[item] += 1
    for num in data:
        if counters[num] <= n:
            solutions_lst.append(num)
    return solutions_lst

print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))