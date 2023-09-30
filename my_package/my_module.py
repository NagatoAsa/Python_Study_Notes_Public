__all__ = ['test', 'test_A']
def test(x, y):
    print(x + y)
    return x + y


def test_A():
    print("testA")


def test_B():
    print("testB")


if __name__ == '__main__':
    test(1, 5)