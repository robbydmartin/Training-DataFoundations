# Errors and Exceptions
# All exceptions are errors, but not all errors are exceptions

# Errors - problems that prevent our application from running correctly
# Ex: syntax error, there is no handling this problem, just have to fix it!
# errors come with error messages to help diagnose the issue
# Ex: syntax, indentation, name, value, type 0 division error, etc.

# Exceptions - problems that are raised during runtime and can be detected
#   and handled by using try-except (try-catch in Java)

try:
    x = int("Ribs") # we know this is goint to throw a type error
except ValueError:
    print("Conversion has failed")

# try-except-else-finally
try:
    number = int(input("Please enter a number: "))
    result = 10/number

except ValueError:
    print("Invalid input. Please enter a valid integer")
except ZeroDivisionError:
    print("You cannot divide by zero")

# It's a good idea to have a generic catch-all exception block to
#   handle anything we hae not thought of
except Exception:
    print("I have no idea how you got here")

else:
    # runs only if NO exception occurs.
    print(f"Result: {result}")

finally:
    # runs no matter what, whether or not an exception is thrown
    print("Execution complete.")

# We can manually raise(throw) an exception using the 'raise' keyword
#y = -5
#if y < 0:
    #raise Exception("Sorry, no negative numbers allowed")

# We can create custom exceptions by creating our own custom excpetion class
class myCustomException(Exception):
    def __init__(self, message="this is not the exception you are looking for"):
        super().__init__(message)

userNumber = input("Please enter your favorite integer: ")
if not type(userNumber) is int:
    raise myCustomException()

print(userNumber)