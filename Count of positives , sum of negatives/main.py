def count_positives_sum_negatives(arr):
    counter_1 = 0
    counter_2 = 0
    if len(arr)>0:
        for x in arr:
            if x>0:
                counter_1 += 1
            else:
                counter_2 += x
        return [counter_1, counter_2]
    else:
        return []