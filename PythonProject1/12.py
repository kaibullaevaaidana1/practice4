import sys
import json

def diff(obj1, obj2, path=''):
    differences = []

    # Все ключи из обоих объектов
    keys = set()
    if isinstance(obj1, dict):
        keys.update(obj1.keys())
    if isinstance(obj2, dict):
        keys.update(obj2.keys())

    for key in keys:
        new_path = f"{path}.{key}" if path else key

        val1 = obj1.get(key, "<missing>") if isinstance(obj1, dict) else "<missing>"
        val2 = obj2.get(key, "<missing>") if isinstance(obj2, dict) else "<missing>"

        if isinstance(val1, dict) and isinstance(val2, dict):
            differences.extend(diff(val1, val2, new_path))
        elif val1 != val2:
            v1 = json.dumps(val1, separators=(',', ':')) if val1 != "<missing>" else "<missing>"
            v2 = json.dumps(val2, separators=(',', ':')) if val2 != "<missing>" else "<missing>"
            differences.append(f"{new_path} : {v1} -> {v2}")

    return differences

def main():
    obj1 = json.loads(sys.stdin.readline())
    obj2 = json.loads(sys.stdin.readline())

    differences = diff(obj1, obj2)
    if differences:
        for line in sorted(differences):
            print(line)
    else:
        print("No differences")

if __name__ == "__main__":
    main()