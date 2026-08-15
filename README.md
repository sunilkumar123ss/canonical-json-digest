# Canonical JSON Digest

Produce consistent local JSON bytes and content hashes from strict input.

All bundled examples use synthetic data.

## Run

Requires Python 3.9 or later; no third-party packages or network access are needed.

```sh
python3 main.py
python3 main.py --help
python3 -m unittest -v
```

Run these commands from this repository's directory. The demo can also be launched from any directory by passing the absolute path to `main.py`.

## How it works

`loads_strict()` rejects duplicate keys and non-finite numbers. `canonical_bytes()` recursively accepts JSON types, rejects non-string object keys and cycles, sorts dictionary keys, removes optional whitespace, and emits UTF-8. Shared subobjects are permitted because they are not cycles. `digest()` hashes those exact bytes with SHA-256.

Objects with different insertion orders produce equal digests; array order remains meaningful. Cost follows serialization size plus sorting work for each object's keys.

## Reuse

```python
from main import loads_strict, canonical_bytes, digest

left = loads_strict('{"b":2,"a":1}')
right = loads_strict('{ "a": 1, "b": 2 }')
assert canonical_bytes(left) == b'{"a":1,"b":2}'
assert digest(left) == digest(right)
```

## Demo behavior

Run `python3 main.py --json '{"z":0,"a":[1,2]}'` to inspect the encoded text and its digest. The default uses a synthetic order description.

## Boundaries

This is project-local deterministic serialization, not the RFC 8785 JSON Canonicalization Scheme. Python's float spelling remains in use: `1` and `1.0` differ. Unicode normalization is not performed, so visually equal strings can have different bytes. There are no input-size or nesting-depth limits beyond interpreter behavior. A plain content digest is not a signature or proof of authorship.

## Verification

`test_main.py` exercises boundary conditions, invalid inputs, and meaningful behavior specific to this implementation. The default demo is deterministic and completes without external services. See the collection's verification report for the recorded run; run the commands above to verify this repository independently.

## Repository checks

```sh
python3 verify.py
```

This runs the isolated test suite, synthetic example, and CLI help. The included GitHub Actions workflow repeats these checks when the repository is published. No hosted CI result is claimed by the local verification report.
