import sys
import json

def main():
    if len(sys.argv) != 2:
        print("Usage: jsonguard <file.json>")
        sys.exit(1)

    path = sys.argv[1]

    try:
        with open(path, "r", encoding="utf-8") as f:
            json.load(f)
        print("OK")
        sys.exit(0)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON at line {e.lineno}, column {e.colno}")
        sys.exit(1)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

if __name__ == "__main__":
    main()
