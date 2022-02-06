def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    else:
        positives = [x for x in arr if x > 0]
        negatives = [x for x in arr if x < 0]
        return [len(positives), sum(negatives)]
