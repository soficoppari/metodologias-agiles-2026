def sumar(numbers: str) -> int:
    if numbers == "":
        return 0
    elif "," in numbers or "\n" in numbers:
        numbers = numbers.replace("\n", ",")
        numeros = numbers.split(",")
        return sum(int(num) for num in numeros)
    else:
        return int(numbers)
    
