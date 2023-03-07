if __name__=='__main__':
    try:
        import doctest
        import test
        doctest.testmod(test)
    except Exception as e:
        #print(test.current_student_id)
        print(e.__class__.__name__)
