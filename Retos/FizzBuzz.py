def FizzBuzz():

    for Fizz_Buzz in range(1, 101):
        if Fizz_Buzz % 15 == 0:
            Fizz_Buzz = "fizzbuzz"
        elif Fizz_Buzz % 5 == 0:
            Fizz_Buzz = "buzz"
        elif Fizz_Buzz % 3 == 0:
            Fizz_Buzz = "fizz"
    
        print("-", Fizz_Buzz)
        
FizzBuzz()        