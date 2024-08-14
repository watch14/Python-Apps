from  time import strftime


def getTodos(file):
    """ Return file content - todos - taks in a List """
    with open(file, "r") as f:
        todos =  f.readlines()
        return todos


def saveFile(file, todos_arg):
    """ Save / Write the content/todos in the file """
    with open(file, "w") as f:
        f.writelines(todos_arg)


def printToods(file):
    """
    get the contetnt of the file 
    and Print each line enumerated 
    """
    todos = getTodos(file)
    print("Your todos:")
    for index, item in enumerate(todos):
        print(f"{index + 1}. {item.strip("\n")}")
        
        
def currentTime():
    """ return current time:
        - %a : day of the week
        - %d : day of the month
        - %b : month
        - %Y : year
        - %H %M %S : hours, minutes, seconds
    """
    curr = strftime("(%d %b %Y %H:%M:%S)")
    return curr
        
if __name__ == "__main___":
    pass

