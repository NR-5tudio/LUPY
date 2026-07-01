import sys
lua = None



def get_list_length(arr):
    return int(len(arr))

def GetArrayItem(arr: list, item_num: int):
    try: item = arr[item_num-1]
    except Exception as e: print(f"Error: {e}"); sys.exit(1)
    return item

# ============================================
# LowPie Converters Addon
# ============================================
# Converts between types: strings, numbers, booleans, lists, etc.

def ToString(Var):
    """Convert anything to a string"""
    return str(Var)

def ToNumber(Var):
    """Convert a string or number to a number (float/int)"""
    try:
        return float(Var)
    except:
        return None

def ToInt(Var):
    """Convert to integer (whole number)"""
    try:
        return int(Var)
    except:
        return None

def ToFloat(Var):
    """Convert to float (decimal number)"""
    try:
        return float(Var)
    except:
        return None

def ToBool(Var):
    """Convert to boolean (True/False)"""
    if isinstance(Var, bool):
        return Var
    if isinstance(Var, (int, float)):
        return Var != 0
    if isinstance(Var, str):
        return Var.lower() in ["true", "1", "yes", "y"]
    if isinstance(Var, (list, tuple, dict)):
        return len(Var) > 0
    return bool(Var)

def ToList(Var):
    """Convert to a list (array)"""
    if isinstance(Var, (list, tuple)):
        return list(Var)
    if isinstance(Var, dict):
        return list(Var.values())
    if isinstance(Var, str):
        return list(Var)  # "abc" becomes ["a", "b", "c"]
    return [Var]  # Anything else becomes a single-item list

def ToTuple(Var):
    """Convert to a tuple (immutable list)"""
    if isinstance(Var, (list, tuple)):
        return tuple(Var)
    if isinstance(Var, dict):
        return tuple(Var.values())
    if isinstance(Var, str):
        return tuple(Var)
    return (Var,)

def IsString(Var):
    """Check if variable is a string"""
    return isinstance(Var, str)

def IsNumber(Var):
    """Check if variable is a number (int or float)"""
    return isinstance(Var, (int, float))

def IsInt(Var):
    """Check if variable is an integer"""
    return isinstance(Var, int)

def IsFloat(Var):
    """Check if variable is a float"""
    return isinstance(Var, float)

def IsBool(Var):
    """Check if variable is a boolean"""
    return isinstance(Var, bool)

def IsList(Var):
    """Check if variable is a list"""
    return isinstance(Var, list)

def IsTable(Var):
    """Check if variable is a table (dict in Python)"""
    return isinstance(Var, dict)

def IsNone(Var):
    """Check if variable is None (nil in Lua)"""
    return Var is None

def TypeOf(Var):
    """Get the type of a variable as a string"""
    if isinstance(Var, str):
        return "string"
    elif isinstance(Var, int):
        return "integer"
    elif isinstance(Var, float):
        return "float"
    elif isinstance(Var, bool):
        return "boolean"
    elif isinstance(Var, list):
        return "list"
    elif isinstance(Var, dict):
        return "table"
    elif Var is None:
        return "nil"
    else:
        return type(Var).__name__

def Add_Addons(Addon, funcs):
    
    Addon("ToString", ToString)
    funcs.append({
        "name": "ToString", 
        "description": "Converts anything to a string",
        "example": "ToString(500) will return '500'"
    })
    
    Addon("ToNumber", ToNumber)
    funcs.append({
        "name": "ToNumber", 
        "description": "Converts to a number (float/int)",
        "example": "ToNumber('3.14') will return 3.14"
    })
    
    Addon("ToInt", ToInt)
    funcs.append({
        "name": "ToInt", 
        "description": "Converts to an integer",
        "example": "ToInt('42') will return 42"
    })
    
    Addon("ToFloat", ToFloat)
    funcs.append({
        "name": "ToFloat", 
        "description": "Converts to a float (decimal)",
        "example": "ToFloat('3.14') will return 3.14"
    })
    
    Addon("ToBool", ToBool)
    funcs.append({
        "name": "ToBool", 
        "description": "Converts to a boolean (True/False)",
        "example": "ToBool('true') will return True"
    })
    
    Addon("ToList", ToList)
    funcs.append({
        "name": "ToList", 
        "description": "Converts to a list (array)",
        "example": "ToList('abc') will return {'a', 'b', 'c'}"
    })
    
    Addon("ToTuple", ToTuple)
    funcs.append({
        "name": "ToTuple", 
        "description": "Converts to a tuple (immutable)",
        "example": "ToTuple({'a', 'b'}) will return ('a', 'b')"
    })
    
    Addon("IsString", IsString)
    funcs.append({
        "name": "IsString", 
        "description": "Checks if variable is a string",
        "example": "if IsString(name) then ..."
    })
    
    Addon("IsNumber", IsNumber)
    funcs.append({
        "name": "IsNumber", 
        "description": "Checks if variable is a number",
        "example": "if IsNumber(age) then ..."
    })
    
    Addon("IsInt", IsInt)
    funcs.append({
        "name": "IsInt", 
        "description": "Checks if variable is an integer",
        "example": "if IsInt(count) then ..."
    })
    
    Addon("IsFloat", IsFloat)
    funcs.append({
        "name": "IsFloat", 
        "description": "Checks if variable is a float",
        "example": "if IsFloat(price) then ..."
    })
    
    Addon("IsBool", IsBool)
    funcs.append({
        "name": "IsBool", 
        "description": "Checks if variable is a boolean",
        "example": "if IsBool(flag) then ..."
    })
    
    Addon("IsList", IsList)
    funcs.append({
        "name": "IsList", 
        "description": "Checks if variable is a list",
        "example": "if IsList(files) then ..."
    })
    
    Addon("IsTable", IsTable)
    funcs.append({
        "name": "IsTable", 
        "description": "Checks if variable is a table (dict)",
        "example": "if IsTable(config) then ..."
    })
    
    Addon("IsNone", IsNone)
    funcs.append({
        "name": "IsNone", 
        "description": "Checks if variable is None (nil)",
        "example": "if IsNone(value) then ..."
    })
    
    Addon("TypeOf", TypeOf)
    funcs.append({
        "name": "TypeOf", 
        "description": "Returns the type of a variable as a string",
        "example": "TypeOf(123) will return 'integer'"
    })

    Addon("GetLength", get_list_length)
    funcs.append({
        "name": "GetLength", 
        "description": "Returns length of a list as an int",
        "example": "GetLength({'A', 'B', 'C'}) will return 3"
    })

    Addon("GetItem", GetArrayItem)
    funcs.append({
        "name": "GetItem", 
        "description": "Returns an item from a list by number",
        "example": "GetItem({'A', 'B', 'C'}, 2) will return 'B'"
    })