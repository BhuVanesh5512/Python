def get_data():
    return input("Enter score: ")


def parse_score(data):
    try:
        return int(data)
    except ValueError:
        raise ValueError("Score must be an integer")


def validate_score(score):
    if not isinstance(score, int):
        raise TypeError("Score must be an integer")

    if 0 <= score <= 100:
        return score

    if score < 0:
        raise ValueError("Score should not be negative")

    raise ValueError("Score should not be above 100")


def process_score(data):
    score = parse_score(data)
    return validate_score(score)


try:
    data = get_data()
    result = process_score(data)
    print(f"Score: {result}")

except ValueError as error:
    print("ValueError:", error)

except TypeError as error:
    print("TypeError:", error)