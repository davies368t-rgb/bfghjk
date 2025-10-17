try:
    n=int(input("enter a number: "))
    if n%2 == 0:
        while True:
            print("bye")
    else:
        print("a bit odd but ok")

except ValueError:
    print("Exception", ValueError)
except NameError:
    print("Exception", NameError)