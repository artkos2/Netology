
import datetime

def make_trace(old_function):
    def new_function(*args, **kwargs):
        with open("logs.txt", 'r+') as f:
            f.seek(0, 2)
            f.write(f'время {datetime.datetime.now()}\n')
            f.write(f'вызвана функция {old_function.__name__}\n')
            f.write(f'с аргументами {args} и {kwargs}\n')
            result = old_function(*args, **kwargs)
            f.write(f'Получили {result}\n')
            f.write('-'*120)
            f.write('\n')
            return result
    return new_function

def make_trace_path(path=None):
    def make_trace(old_function):
        def new_function(*args, **kwargs):
            with open(path, 'r+') as f:
                f.seek(0, 2)
                f.write(f'время {datetime.datetime.now()}\n')
                f.write(f'вызвана функция {old_function.__name__}\n')
                f.write(f'с аргументами {args} и {kwargs}\n')
                result = old_function(*args, **kwargs)
                f.write(f'Получили {result}\n')
                f.write('-'*120)
                f.write('\n')
                return result
        return new_function
    return make_trace