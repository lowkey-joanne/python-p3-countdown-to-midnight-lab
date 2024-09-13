import time

def countdown(n):
    """Counts down from n to 1 and prints 'HAPPY NEW YEAR!'"""
    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(n):
    """Counts down from n to 1 with a 1-second pause between each print, then prints 'HAPPY NEW YEAR!'"""
    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
