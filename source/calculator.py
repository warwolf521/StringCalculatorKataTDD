def add(numbers: str) -> int:
    numbersSplited = numbers.split(",")
    return sum(int(number) for number in numbersSplited)