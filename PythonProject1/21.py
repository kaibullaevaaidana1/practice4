import sys
import importlib


def classify_queries():
    input_data = sys.stdin.read().strip().splitlines()
    q = int(input_data[0])

    for i in range(1, q + 1):
        module_path, attribute = input_data[i].split()

        try:
            module = importlib.import_module(module_path)
        except ModuleNotFoundError:
            print("MODULE_NOT_FOUND")
            continue

        if not hasattr(module, attribute):
            print("ATTRIBUTE_NOT_FOUND")
        else:
            attr = getattr(module, attribute)
            if callable(attr):
                print("CALLABLE")
            else:
                print("VALUE")


if __name__ == "__main__":
    classify_queries()