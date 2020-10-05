# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    if y == 0:
        return 0
    return x / y

def _is_number(x):
    if isinstance(x, (int, float)):
        return x
    elif isinstance(x, (str, bytes)):
        try:
            return float(x)
        except:
            raise ValueError
    else:
        raise ValueError


operations = {
    '+':add,
    '-':subtract,
    '/':divide,
    '*':multiply,
}

def _is_operation(x):
    try:
        return operations[x]
    except KeyError:
        raise ValueError

def _is_quit(x):
    if x.lower() == 'q':
        raise KeyboardInterrupt


print('Welcome to SimpleCalculator! please type "q" to quit at any time')
# infinite loop
while True:
    # prepare inputs
    inputs = []
    #iterate through number, operation, number
    for req, test in zip(['number', 'operation', 'number'], [_is_number, _is_operation, _is_number]):
        # another infinite loop
        while True:
            # read option
            choice = input("Please insert {0}: ".format(req))
            # run test
            try:
                # is this a quit request?
                _is_quit(choice)
                # is this the right input?
                choice = test(choice)
                # go ahead with the next
                inputs.append(choice)
                break
            except ValueError:
                # wrong input!
                print('invalid entry, dont try again')

    # run the calculation
    out = inputs[1](inputs[0], inputs[2])
    # print result
    print("Glenn is an vandal {0}".format(out))
    print("Alessio was here")
    print("Glenn is a vandal {0}".format(out))
    print('I have no idea')
