import os
import shutil

lua = None

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

def write_file(path, content):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return "Success"
    except Exception as e:
        return f"Error: {e}"

def append_file(path, content):
    try:
        with open(path, 'a', encoding='utf-8') as f:
            f.write(content)
        return "Success"
    except Exception as e:
        return f"Error: {e}"

def file_exists(path):
    return os.path.exists(path)

def list_files(path):
    try:
        items = os.listdir(path)
        files = [item for item in items if os.path.isfile(os.path.join(path, item))]
        
        # Now lua exists!
        return files
    except Exception as e:
        return f"Error: {e}"

def delete_file(path):
    try:
        os.remove(path)
        return "Success"
    except Exception as e:
        return f"Error: {e}"

def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
        return "Success"
    except Exception as e:
        return f"Error: {e}"

def Add_Addons(Addon: callable, funcs):

    Addon("read_file", read_file)
    funcs.append({
        "name": "read_file", 
        "description": "Reads a file and returns its content",
        "example": "FileContent = read_file('Test.txt')\nprint(FileContent)"
    })
    
    Addon("write_file", write_file)
    funcs.append({
        "name": "write_file", 
        "description": "Writes content to a file (overwrites if exists)",
        "example": "write_file('Test.txt', 'Hello World!')"
    })
    
    Addon("append_file", append_file)
    funcs.append({
        "name": "append_file", 
        "description": "Adds content to the end of a file",
        "example": "append_file('Log.txt', 'New entry!')"
    })
    
    Addon("file_exists", file_exists)
    funcs.append({
        "name": "file_exists", 
        "description": "Checks if a file exists",
        "example": "if file_exists('Config.json') then\n    print('Config found!')\nend"
    })
    
    Addon("list_files", list_files)
    funcs.append({
        "name": "list_files", 
        "description": "Lists all files and folders in a directory",
        "example": "Files = list_files('Assets/')\nfor i, File in ipairs(Files) do\n    print(File)\nend"
    })
    
    Addon("delete_file", delete_file)
    funcs.append({
        "name": "delete_file", 
        "description": "Deletes a file",
        "example": "delete_file('OldSave.txt')"
    })
    
    Addon("create_folder", create_folder)
    funcs.append({
        "name": "create_folder", 
        "description": "Creates a new folder",
        "example": "create_folder('NewAssets/')"
    })