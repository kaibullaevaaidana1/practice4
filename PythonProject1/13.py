import sys
import json
import re


token_re = re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)|\[(\d+)\]')

def resolve_query(obj, query):
    current = obj
    for match in token_re.finditer(query):
        key, index = match.groups()
        if key is not None:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return "NOT_FOUND"
        elif index is not None:
            idx = int(index)
            if isinstance(current, list) and 0 <= idx < len(current):
                current = current[idx]
            else:
                return "NOT_FOUND"
    return json.dumps(current, separators=(",", ":"))

def main():
    data = json.loads(sys.stdin.readline())
    q = int(sys.stdin.readline())
    for _ in range(q):
        query = sys.stdin.readline().rstrip()
        sys.stdout.write(resolve_query(data, query) + "\n")

if __name__ == "__main__":
    main()