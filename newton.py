from math import cos, sin
import unittest

def dx(f, x):
    return abs(0 - f(x))

def newton(f, df, x0, e):
  iterations_count = 0
  delta = dx(f, x0)

  while delta > e:
    x0 = x0 - f(x0) / df(x0)
    delta = dx(f, x0)
    iterations_count += 1

  return (x0, f(x0), iterations_count)

class NewtonTest(unittest.TestCase):
  def test_root_find(self):
    def df(x):
      return -2 * 2 * sin(2 * x) + 2 * x * cos(2 * x)

    def f(x):
      return x ** 2 * cos(2 * x) + 1
      
    actual_result = newton(f, df, 2, 0.0001)
    expected_result = (1.1832211213551906, -5.082387317756343e-05, 12)

    self.assertEqual(actual_result, expected_result)

unittest.main()
