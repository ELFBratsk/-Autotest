#import pytest
import unittest

import pytest


class TestAbs():

    def test_abs1(self):
        assert  abs(-42) == 42, "Should be absolute value of a number"

#def test_abs2():
   # assert abs(-42) == -42, "Should be absolute value of a number"


if __name__ == "__main__":
    #unittest.main()
    #test_abs1()
    pytest.main()
    print('Passed')