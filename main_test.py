import unittest
from main import normalize

class MainTestClass(unittest.TestCase):
    def test_normalize_function(self):
        """It should test normalize function and get a normalized text"""
        input_text = 'در می‌زند و دوباره وارد مي شود . همه مي گویند قدمش پربرکت است .'
        expected_text = 'در می‌زند و دوباره وارد می‌شود. همه می‌گویند قدمش پربرکت است.'
        t, got_text = normalize(input_text)
        self.assertEqual(expected_text, got_text)

if __name__ == '__main__':
    unittest.main()
