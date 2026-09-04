import unittest
from aiforge import estimate_tokens,truncate
class Tests(unittest.TestCase):
 def test_text(self): self.assertEqual(estimate_tokens("abcd"),1);self.assertEqual(truncate("abcdef",3),"abc")
if __name__=="__main__":unittest.main()
