#Error Handeling
try:
    a = 10 + "te"

except ZeroDivisionError as message:
    print(message)

except NameError as message:
    print(message)

except Exception as e:
    print(e)

finally:
    print("this is running")