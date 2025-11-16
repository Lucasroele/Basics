

def expose(obj):

    """
    This function will print the dir() of an object in a structured more readable manner
    """
    arr = []
    dirlist = dir(obj)
    len_dirlist = len(dirlist)
    num_rows = len_dirlist//8
    if num_rows * len_dirlist//8 < len_dirlist:
        num_rows += 1
    j = 0
    for i, str in enumerate(dirlist):
        if j == 8:
        


        j += 1
        



