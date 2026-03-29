def test_example():
    assert 1 + 1 == 2
    
def sum (a, b):
    return a + b

print(sum(3, 4))


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

print(divide(10, 2))
print(divide(10, 0))    