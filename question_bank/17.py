def get_tensplace(x):
    '''
    #will insert student ID in the first line by code automatically
    #such as current_student_id = '1000000000'
    >>> import sys; from io import StringIO; savedStdout=sys.stdout; f=StringIO(); sys.stdout=f; get_tensplace(4325); sys.stdout=savedStdout; print(f.getvalue()==str(current_student_id)+'\\n'+'2'+'\\n');
    True
    >>> import sys; from io import StringIO; savedStdout=sys.stdout; f=StringIO(); sys.stdout=f; get_tensplace(-35); sys.stdout=savedStdout; print(f.getvalue()==str(current_student_id)+'\\n'+'-3'+'\\n');
    True
    >>> import sys; from io import StringIO; savedStdout=sys.stdout; f=StringIO(); sys.stdout=f; get_tensplace(2); sys.stdout=savedStdout; print(f.getvalue()==str(current_student_id)+'\\n'+'0'+'\\n');
    True
    '''
    #*****Get the digit on tens place of one number ********************#
    #*****And return it ************************************************#
    #*****Below is your coding area for implementation******************#
    #*****Add lines if necessary ***************************************#

    return tensplace