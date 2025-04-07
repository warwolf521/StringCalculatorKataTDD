def add(numbers: str) -> int:
    numbersSplited = numbers.replace("\n", ",").split(",")
    return sum(int(number) for number in numbersSplited)