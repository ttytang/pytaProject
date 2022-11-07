def aver_data(f):
    '''
    >>> aver_data('../../question_bank/exp.csv')
    [91975.0, 723.9175, 296.1225, 294.33624999999995, 25.5325, 131.0875, -18.8875, 16.9075]
    >>> abs(aver_data('../../question_bank/exp.csv')[0]-91975)<0.1
    True
    >>> abs(aver_data('../../question_bank/exp.csv')[1]-723.9175)<0.1
    True
    >>> abs(aver_data('../../question_bank/exp.csv')[2]-296.1225)<0.1
    True
    >>> abs(aver_data('../../question_bank/exp.csv')[3]-294.33624999999995)<0.1
    True
    >>> abs(aver_data('../../question_bank/exp.csv')[4]-25.5325)<0.1
    True
    >>> abs(aver_data('../../question_bank/exp.csv')[5]-131.0875)<0.1
    True
    >>> abs(aver_data('../../question_bank/exp.csv')[6]+18.8875)<0.1
    True
    >>> abs(aver_data('../../question_bank/exp.csv')[7]-16.9075)<0.1
    True
    >>> aver_data('../../question_bank/exp_not_exist.csv')
    File Not Exists
    '''
    #*****Create a average data function as described*******************#
    #****open a file specified by parameter f***************************#
    #****read the content of the file***********************************#
    #****and calculate the average of each row in it********************#
    #****and return the contents in a list with proper precision********#
    #*****Below is your coding area for implementation******************#
    #*****You can add lines if needed***********************************#


