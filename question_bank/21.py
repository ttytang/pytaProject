def try_flow():
    '''
    >>> try_flow()
    4
    '''
    #****Below is one code snippet**************************************#
    #****Please read and find the result of func inner_try()************#
    #*****Replace blank with specific value of x and remain other parts*#
    x=1
    def inner_try():
        try:
            x = x + 1
        except:
            x = 3
        else:
            x = 2
        finally:
            x += 1
        return x
    return ___________
flow_code=try_flow()