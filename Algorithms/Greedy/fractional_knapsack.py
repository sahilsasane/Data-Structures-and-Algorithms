def fractional_knapsack(value, weight, capacity):
    ratio = [v / w for v, w in zip(value, weight)]
    index = sorted(range(len(ratio)), key=lambda k: ratio[k], reverse=True)
    max_val = 0
    fractions = [0] * len(value)

    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_val += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]
            max_val += value[i] * fractions[i]
            break
    return max_val, fractions


value = [100, 60, 120]
weight = [20, 10, 30]
capacity = 50

max_value, fractions = fractional_knapsack(value, weight, capacity)
print("Maximum value in knapsack =", max_value)
print("Fractions of items taken:", fractions)
