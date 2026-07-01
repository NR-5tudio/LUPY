import sys
lua = None

def ToString(Var):
    return f"{Var}"

def get_list_length(arr):
    return int(len(arr))

def GetArrayItem(arr: list, item_num: int):
    try: item = arr[item_num-1]
    except Exception as e: print(f"Error: {e}"); sys.exit(1)
    return item

def Add_Addons(Addon, funcs):
    Addon("ToString", ToString)
    Addon("GetLength", get_list_length)
    Addon("GetItem", GetArrayItem)