def isdigit(arg):
    """ returns true if arg is an integer or float """
    arg_is_int = type(arg) == int
    arg_is_float = type(arg) == float
    args_is_both_float_and_int = arg_is_int or arg_is_float
    return args_is_both_float_and_int

def minus(a, b):
    """ subtracts b from a if both are numbers """

    if isdigit(a) and isdigit(b): # if a and b are both numbers
        return(a - b) # subtract and return result
    else: # else return error string
        return("numbers only")

