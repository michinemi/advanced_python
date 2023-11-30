# To force exception to occur when a certain condition is met
x = 5
if x < 0:
    raise Exception('x should be positive')

# Using assert statement
assert (x>=0), 'x is not positive'

# To handle exceptions
try:
    a = 5 / 0
except Exception as e:
    print(f'ERORR - {e}')
else:
    print('OK')
finally: # runs always no matter what
    print('cleaning up...')

#  To define own exception
class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)
try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)