def add(numbers: str) -> int:
    if numbers.startswith("//"):
        delimiter = numbers[2:numbers.index("\n")]
        numbers = numbers[numbers.index("\n") + 1:]
        numbers = numbers.replace(delimiter, ",")
    else:
        numbers = numbers.replace("\n", ",")
    numbersSplited = numbers.split(",")
    return sum(int(number) for number in numbersSplited)