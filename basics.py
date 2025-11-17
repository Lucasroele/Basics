def expose(obj, cols=6, nodunder=False):
                    
    """             
    Expose the attributes of an object in a formatted way.
    Args:
        obj: The object to expose.
        cols: Number of columns to display.
    """ 
    arr = []
    dirlist = dir(obj)
    if nodunder:
        dirlist = [a for a in dirlist if not a.startswith('__')]
    len_dirlist = len(dirlist)
    assert cols > 0 and cols <= 10, "cols must be between 1 and 10"
    num_cols = cols
    num_rows = (len_dirlist + num_cols - 1) // num_cols
    if num_rows * len_dirlist//num_cols < len_dirlist:
        num_rows += 1
    for i in range(num_rows):
        arr.append([])
    j = 0 
    for i, str in enumerate(dirlist):
        j = i//num_cols
        arr[j].append(str)

    max_lens = []
    for j in range(num_cols):
        max_lens.append(0)
    for i, row in enumerate(arr):
        for j, cel in enumerate(row):
            max_lens[j] = max(max_lens[j], len(cel))

    for i, row in enumerate(arr):
        printstr = ""
        for j, col in enumerate(row):
            printstr += f"{col:<{max_lens[j]+1}}"
        print(printstr) 
