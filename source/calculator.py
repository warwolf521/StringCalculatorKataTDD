def add(numbers: str) -> int:
    if numbers.startswith("//"):
        delimiter = numbers[2:numbers.index("\n")]
        numbers = numbers[numbers.index("\n") + 1:]
        numbers = numbers.replace(delimiter, ",")
    else:
        numbers = numbers.replace("\n", ",")
    numbersSplited = numbers.split(",")
    negatives = [int(number) for number in numbersSplited if int(number) < 0]
    if negatives:
        raise Exception(f"negatives not allowed: {', '.join(map(str, negatives))}")
    return sum(int(number) for number in numbersSplited)