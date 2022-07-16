# one.py

print("Hello")


# built in variable
# python internall assigns __main__ to __name__ if the script is run
#  __name__ = "__main__"
# THIS HAPPENS ONLY IF THE FILE IS RUN DIRECTLY FROM PYTHON
# this allows us to check with an if condition is true

# if __name__ == "__main__":# 

def func():
    print("FUNC() IN ONE.PY")
print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    print('ONE.PY IS BEING RUN DIRECTLY')

else:
    print("ONE.PY has been inmported")