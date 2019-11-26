

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

@slack_submitter_wrapper
def divide(a, b):
    return a//b

if __name__ == "__main__":
    # Execute!
    divide(9,0)
