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


def loads_strict(text):
    value = json.loads(text, object_pairs_hook=_object, parse_constant=_invalid_constant)
    canonical_bytes(value)
    return value


def canonical_bytes(value):
    active = set()
    def validate(item):
        if item is None or type(item) in (str, bool, int):
            return
        if type(item) is float:
            if not math.isfinite(item):
                raise ValueError("numbers must be finite")
            return
        if type(item) not in (list, dict):
            raise ValueError("only JSON values are supported")
        identity = id(item)
        if identity in active:
            raise ValueError("circular references are not JSON")
        active.add(identity)
        try:
            if type(item) is dict:
                if any(type(key) is not str for key in item):
                    raise ValueError("object keys must be strings")
                children = item.values()
            else:
                children = item
            for child in children:
                validate(child)
        finally:
            active.remove(identity)
    validate(value)
    try:
        return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                          allow_nan=False).encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("strings must be valid Unicode without lone surrogates") from exc


def digest(value):
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", dest="json_text", default='{"tags":["api","lab"],"name":"Synthetic order","quantity":2}',
                        help="JSON value to serialize and hash; duplicate keys are rejected")
    args = parser.parse_args()
    try:
        value = loads_strict(args.json_text)
    except (ValueError, RecursionError) as exc:
        parser.error(str(exc))
    print(json.dumps({"canonical": canonical_bytes(value).decode("utf-8"), "sha256": digest(value)}, indent=2))


if __name__ == "__main__":
    main()
