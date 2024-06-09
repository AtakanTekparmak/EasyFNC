import json
import tomllib

# Define constants
TEMPLATE_FILE_TYPES = ["json", "toml"]

def load_template(file_path: str, file_type: str = "json") -> dict:
    """
    Load a template from a JSON file and return it as a dictionary.
    """
    if file_type not in TEMPLATE_FILE_TYPES:
        raise ValueError(f"Invalid file type. Expected one of {TEMPLATE_FILE_TYPES}")
    if file_type == "json":
        return load_json(file_path)
    elif file_type == "toml":
        return load_toml(file_path)
    

def load_json(file_path: str) -> dict:
    """
    Load a JSON file and return it as a dictionary.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found")
    return data

def load_toml(file_path: str) -> dict:
    """
    Load a TOML file and return it as a dictionary.
    """
    try:
        with open(file_path, "rb") as file:
            data = tomllib.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found")
    except tomllib.TOMLDecodeError:
        raise tomllib.TOMLDecodeError(f"Error decoding TOML file {file_path}")
    return data