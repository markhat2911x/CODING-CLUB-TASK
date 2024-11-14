from flask import Flask, jsonify, request, abort
import sys
import re

app = Flask(__name__)


default_file_path = "/Users/apple/Desktop/backend cc.txt"


if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    file_path = default_file_path
    print(f"No command-line argument provided. Using default file path: {file_path}")


ids = []
unique_ids = set()
try:
    with open(file_path, 'r') as file:
        for line in file:
            id_str = line.strip()
            
            if id_str[-4:] not in unique_ids:
                ids.append(id_str)
                unique_ids.add(id_str[-4:])
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)


@app.route("/", methods=["GET"])
def get_all_ids():
    return jsonify({"ids": ids})

if __name__ == "__main__":
    app.run(port=8000)
