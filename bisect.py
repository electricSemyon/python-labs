from math import cos
import unittest

def are_samesigned(x, y):
  return x * y > 0

def get_mid(x, y):
  return (x + y) / 2.0

def bisect(fn, low, high, iterations):
  for n in range(0, iterations):
    mid = get_mid(low, high)

    no_root_on_left = are_samesigned(fn(low), fn(mid))
    no_root_on_right = are_samesigned(fn(mid), fn(high))

    if no_root_on_left and no_root_on_right:
      return None
    elif no_root_on_left:
      low = mid
    elif no_root_on_right:
      high = mid

  return get_mid(low, high)

class BisectionTest(unittest.TestCase):
  def test_root_finding_on_range(self):
    def fn(x):
      return 2 ** x + cos(x)

    expected_result = -1.85205078125

    self.assertEqual(bisect(fn, -2.0, -1.0, 10), expected_result)

  def test_no_roots_on_range_case(self):
    def fn(x):
      return 2 ** x + cos(x)

    expected_result = None

    self.assertEqual(bisect(fn, 1.0, 2.0, 10), expected_result)

unittest.main()
