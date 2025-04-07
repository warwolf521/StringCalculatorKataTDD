def add(numbers: str) -> int:
    numbersSplited = numbers.split(",")
    return int(numbersSplited[0]) + int(numbersSplited[1])