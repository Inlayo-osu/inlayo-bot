import json
import os


def fileIO(filename, method, data=None):
    if method == "load":
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    elif method == "save":
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    else:
        raise ValueError(f"Invalid method: {method}. Use 'load' or 'save'")


class dataIO:
    @staticmethod
    def load_json(filename):
        return fileIO(filename, "load")
    
    @staticmethod
    def save_json(filename, data):
        return fileIO(filename, "save", data)
