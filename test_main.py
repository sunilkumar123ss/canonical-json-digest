import hashlib
import unittest
from main import canonical_bytes, digest, loads_strict


class CanonicalJSONTests(unittest.TestCase):
    def test_object_order_and_whitespace_do_not_change_digest(self):
        left = loads_strict('{"b":2, "a":{"z":0,"y":1}}')
        right = loads_strict('{ "a": {"y":1,"z":0},"b":2 }')
        self.assertEqual(digest(left), digest(right))
        self.assertEqual(canonical_bytes(left), b'{"a":{"y":1,"z":0},"b":2}')










if __name__ == '__main__':
    unittest.main()
