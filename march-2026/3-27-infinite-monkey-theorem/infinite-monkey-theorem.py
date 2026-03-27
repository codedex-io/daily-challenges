def infinite_monkey(target, attempt):
    target_len = len(target)

    # init vars to track the best window found
    best_index = 0
    best_score = 0

    # slide the window across every valid position
    for i in range(len(attempt) - target_len + 1):
        window = attempt[i : i + target_len]

        # compare each character one by one
        matches = 0
        for j in range(target_len):
            if window[j] == target[j]:
                matches += 1

        # convert to a percentage score
        score = (matches / target_len) * 100

        # update best if this window is better
        if score > best_score:
            best_score = score
            best_index = i

    # calculate attempts using the formula, or None if score is 0
    if best_score == 0:
        attempts = None
    else:
        attempts = round(1 / (best_score / 100) ** target_len)

    return {
        'best_index': best_index,
        'similarity': round(best_score, 2),
        'attempts': attempts
    }