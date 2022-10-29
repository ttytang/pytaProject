def error_code2():
    '''
    >>> error_code2()
    1
    '''
    #****Below is one code snippet**************************************#
    #****Please read and find the result of x based on the flow*********#
    #*****Replace blank with specific value of x and remain other parts*#
    d='str'
    try:
        d[0]='S'
        x = 0
    except TypeError:
        x = 1
    except AttributeError:
        x = 2
    return ___________
e_code2=error_code2()