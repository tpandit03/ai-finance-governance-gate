import argparse, json
from .gate import run_gate

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="data/change_request.json")
    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as f:
        change = json.load(f)
    print(json.dumps(run_gate(change), indent=2))

if __name__ == "__main__":
    main()
