from datetime import datetime

def log_time(func):
    def wrapper(*args, **kwargs):
        print('START ', func.__name__)
        date_start = datetime.now()
        result = func(*args, **kwargs)
        print("END. TIME SPENT", datetime.now() - date_start)
        return result
    return wrapper
