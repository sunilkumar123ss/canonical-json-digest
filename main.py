"""Deterministic project-local JSON serialization and SHA-256 content digests."""
import argparse
import hashlib
import json
import math


def _object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate object key: " + key)
        result[key] = value
    return result


def _invalid_constant(value):
    raise ValueError("non-finite JSON number: " + value)
