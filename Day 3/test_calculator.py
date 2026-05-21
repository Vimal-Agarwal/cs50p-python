from calcultor import square

def main():
    test_square()

def test_square():
# assert used to test/verify that something in your code is working correctly.
    assert square(2) == 4 
    assert square(3) == 9

# this give assertion error and to solve this we use pytest third party package to detect the cause. by pip install pytest

if __name__ == "__main__":
    main()


# python -m pytest "Day 3/test_calculator.py" use this to test.