x = input("Wprowadz liczbe calkowita ")
x = int(x)

x = input("Wprowadz liczbe calkowita ")
try:
    x = int(x)
except ValueError:
    print("ups, to nie jest liczba")

print('idziemy dalej')

#czy to zastąpi wyjątki? Nie
x = input("Wprowadz liczbe calkowita ")
if isinstance(x, int):
    print('To jest int')
elif isinstance(x, float):
    print('To jest float')
else:
    print('To jest string')

#The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.


try:
    print("Hello")
    result = 1 / 0
# except:
except (ZeroDivisionError, TypeError):
    print("Something went wrong")
    #raise ZeroDivisionError
# except NameError:
#     print('Name error')
# except:
#     print('Totally bad')
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")