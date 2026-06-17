import time
from functools import wraps

def timer(funcs):
    """Decorator that measures and prints a function's execution time."""
    @wraps(funcs)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = funcs(*args, **kwargs)
        duration = time.time() - start
        if funcs.__name__ == 'main':
            print(f"====== 🎉 Total Workflow Time: {duration:.4f}sec ======")
        else:
            print(f"⏱️ {funcs.__name__} took {duration:.4f}sec")
        return result   
    return wrapper
