def segment_func(x):
    '''
    >>> abs(-2.0-segment_func(-2.0))<0.000001
    True
    >>> abs(0-segment_func(0))<0.000001
    True
    >>> abs(10-segment_func(5))<0.000001
    True
    >>> abs(19-segment_func(8))<0.000001
    True
    >>> abs(0-segment_func(10))<0.000001
    True
    >>> abs(0-segment_func(100.1))<0.000001
    True
    '''
    #*****Create a segment function as described************************#
    #****When x is less than 5, return x********************************#
    #****When x is in [5,10), return 3*x-5******************************#
    #****When x is not less than 10, return 0***************************#
    #*****Below is your coding area for implementation******************#
    #*****You can add lines if needed***********************************#

    return result