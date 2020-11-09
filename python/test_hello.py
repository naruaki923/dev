import unittest

class Testfunc(unittest.TestCase):
    def test_func(self):
      """
      こんにちは判定
      """
      from hello import func
      self.assertIsNone(func('こんにちは'))

if __name__ == '__main__':
  testFunc = Testfunc()
  testFunc.test_func()