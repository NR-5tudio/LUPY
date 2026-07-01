# Codes
Here you will find **ALMOST** every code snippet, along with an example of how to use it.

> If you want to use LowPie using an Ai: Just let the Ai read this md and everything will work.

> If you want to learn by your self: you can read this OR run 'help()' and u can read there as well.



-----------
-----------
-----------
-----------
-----------
-----------
-----------
-----------
-----------
-----------
# print
Prints text to the console
```lua
print('Hello world')
```


# exit
Stops the program immediately
```lua
exit()
```


# input
Asks the user for input and returns it as a string
```lua
name = input('What is your name?')
```


# fill
Formats a string with variables
```lua
fill('Hello ', Name, '!')
```


# colored_print
Prints text in color
```lua
colored_print('Error!', 'red')
```


# MyHome
Value of the current working directory (where your code is running)
```lua
print(MyHome)
```


# list
Tells the `for loop` that THIS variable is a list
```lua
for item in list(MY_LIST) do
    print(item)
end
```


# read_file
Reads a file and returns its content
```lua
FileContent = read_file('Test.txt')
print(FileContent)
```


# write_file
Writes content to a file (overwrites if exists)
```lua
write_file('Test.txt', 'Hello World!')
```


# append_file
Adds content to the end of a file
```lua
append_file('Log.txt', 'New entry!')
```


# file_exists
Checks if a file exists
```lua
if file_exists('Config.json') then
    print('Config found!')
end
```


# list_files
Lists all files and folders in a directory
```lua
Files = list_files('Assets/')
for i, File in ipairs(Files) do
    print(File)
end
```


# delete_file
Deletes a file
```lua
delete_file('OldSave.txt')
```


# create_folder
Creates a new folder
```lua
create_folder('NewAssets/')
```


# ToString
Converts anything to a string
```lua
ToString(500) will return '500'
```


# ToNumber
Converts to a number (float/int)
```lua
ToNumber('3.14') will return 3.14
```


# ToInt
Converts to an integer
```lua
ToInt('42') will return 42
```


# ToFloat
Converts to a float (decimal)
```lua
ToFloat('3.14') will return 3.14
```


# ToBool
Converts to a boolean (True/False)
```lua
ToBool('true') will return True
```


# ToList
Converts to a list (array)
```lua
ToList('abc') will return {'a', 'b', 'c'}
```


# ToTuple
Converts to a tuple (immutable)
```lua
ToTuple({'a', 'b'}) will return ('a', 'b')
```


# IsString
Checks if variable is a string
```lua
if IsString(name) then ...
```


# IsNumber
Checks if variable is a number
```lua
if IsNumber(age) then ...
```


# IsInt
Checks if variable is an integer
```lua
if IsInt(count) then ...
```


# IsFloat
Checks if variable is a float
```lua
if IsFloat(price) then ...
```


# IsBool
Checks if variable is a boolean
```lua
if IsBool(flag) then ...
```


# IsList
Checks if variable is a list
```lua
if IsList(files) then ...
```


# IsTable
Checks if variable is a table (dict)
```lua
if IsTable(config) then ...
```


# IsNone
Checks if variable is None (nil)
```lua
if IsNone(value) then ...
```


# TypeOf
Returns the type of a variable as a string
```lua
TypeOf(123) will return 'integer'
```


# GetLength
Returns length of a list as an int
```lua
GetLength({'A', 'B', 'C'}) will return 3
```


# GetItem
Returns an item from a list by number
```lua
GetItem({'A', 'B', 'C'}, 2) will return 'B'
```


