

from functools import wraps
import sys, traceback

# For notification to slack
def slack_submitter_wrapper(func):
    @wraps(func)
    def slack_submitter(*args):
        try:
            return func(*args)
        except Exception as e:
            print(str(e))
            t, v, tb = sys.exc_info()
            print(traceback.format_exception(t,v,tb))
            print(traceback.format_tb(e.__traceback__))
            
            #slack.notify(xxx)
            
            raise e            
    return slack_submitter

"""
# If you use jupyter notebook, then you can use, 
from IPython.core.magic import (register_line_magic, register_cell_magic,
                                register_line_cell_magic)
@register_cell_magic
def cmagic(line, cell):
    "my cell magic"
    return line, cell

%%cmagic  
def cmagic(line, cell):
    "my cell magic"
    try:
        exec(cell)
    except Exception as e:
        print(str(e))
        "Be Supermarket"
"""
@slack_submitter_wrapper
def divide(a, b):
    return a//b

if __name__ == "__main__":
    # Execute!
    divide(9,0)
