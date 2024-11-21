import hashlib
import unittest
from main import canonical_bytes, digest, loads_strict


class CanonicalJSONTests(unittest.TestCase):
    def test_object_order_and_whitespace_do_not_change_digest(self):
        left = loads_strict('{"b":2, "a":{"z":0,"y":1}}')
        right = loads_strict('{ "a": {"y":1,"z":0},"b":2 }')
        self.assertEqual(digest(left), digest(right))
        self.assertEqual(canonical_bytes(left), b'{"a":{"y":1,"z":0},"b":2}')

    def test_array_order_matters(self):
        self.assertNotEqual(digest([1, 2]), digest([2, 1]))

    def test_duplicate_keys_rejected_at_any_depth(self):
        for text in ('{"a":1,"a":2}', '{"outer":{"x":1,"x":2}}'):
            with self.subTest(text=text), self.assertRaises(ValueError): loads_strict(text)

    def test_nonfinite_numbers_rejected(self):
        for text in ('NaN', 'Infinity', '-Infinity', '1e999'):
            with self.subTest(text=text), self.assertRaises(ValueError): loads_strict(text)
        with self.assertRaises(ValueError): canonical_bytes(float('nan'))

    def test_non_json_values_and_keys_rejected(self):
        for value in ({1: "value"}, {"x": (1, 2)}, {"x": {1, 2}}):
            with self.subTest(value=value), self.assertRaises(ValueError): canonical_bytes(value)






if __name__ == '__main__':
    unittest.main()
