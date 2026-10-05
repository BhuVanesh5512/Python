def summarize_scores(*scores, **options):
    if not scores:
        return None

    total = 0
    count = 0
    smallest = scores[0]
    largest = scores[0]

    for score in scores:
        total += score
        count += 1

        if smallest > score:
            smallest = score

        if largest < score:
            largest = score

    round_digits = options.get("round_digits", 2)
    average = round(total / count, round_digits)

    return {
        "min": smallest,
        "max": largest,
        "average": average
    }
    
result = summarize_scores(10, 15, 25, 30, round_digits=1)

print(result)