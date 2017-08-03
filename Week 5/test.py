def genPrimes():
    number = 2
    prime_list = [2]
    yield number
    while True:
        continue_while = False
        number += 1
        for divisor in prime_list:
            if number % divisor ==  0:
                continue_while = True
                break
        if continue_while:
            continue
        prime_list.append(number)
        yield number
