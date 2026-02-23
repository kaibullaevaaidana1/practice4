import sys
import json


def apply_patch(source, patch):
    for key, value in patch.items():
        if value is None:

            if key in source:
                del source[key]
        elif isinstance(value, dict) and isinstance(source.get(key), dict):

            apply_patch(source[key], value)
        else:

            source[key] = value


def main():
    source = json.loads(sys.stdin.readline())
    patch = json.loads(sys.stdin.readline())

    apply_patch(source, patch)

    sys.stdout.write(json.dumps(source, separators=(",", ":"), sort_keys=True) + "\n")


if __name__ == "__main__":
    main()