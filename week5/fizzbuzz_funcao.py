def fizzbuzz(numero):
    numero=int(numero)
    if numero%3 == 0 and numero%5 == 0 :
        return "FizzBuzz"
    if numero%3==0 and not numero%5==0:
        return "Fizz"
    if numero%5==0 and not numero%3==0:
        return "Buzz"
    else:
        return numero