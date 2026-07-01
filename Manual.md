# Manual
Here you can learn everything about LowPie, no need to click through a bunch of links. Just read what you want to learn and try it out yourself.

> **NOTE**: The name is not "loopy" but "Low-Pie". A lot of people mistake this.

> **NOTE**: if you want to learn how to actually code or script with LowPie go to `Codes.md`

# Running using SourceCode
## Creating a LowPie file and setting up Python (LowPie Source Code)
First, create a `main.lp` file. You can replace **main** with any name you like.

## To run `main.lp` using the source code
You will need Python installed. Version **3.13** is recommended, but anything above **3.10** should work.

## install all the packages listed here:
- `pip install lupa` - Required for Lua integration.
- `pip install easygui` - For GUI dialogs.
- `pip install rich` - For fancy console output.
- `pip install json` - For Json loading (Data.json)
- `pip install pyperclip` - For copying/pasting

## Running LowPie
After creating your `main.lp` file, open CMD and run the following command:

> **NOTE:** Replace the names with your actual file paths.

```
{PythonPath} LowPie.py {LowPieFilePath}
```

**Example:**
```
D:\Python\python.exe D:\downloads\LowPie.py D:\MyLowPie\main.lp
```

If Python is already in your system environment variables:

> **TIP:** You can open CMD in your project folder and simply run `LowPie.py` without the full path.

```
python LowPie.py main.lp
```



# Version Notices 
## V 0.2
That is all for now. There are not many more functions or variables than this.

But in the future, sooner or later, I will be adding many more functions. You will be able to create your own GUIs, systems, games, file controls, and a lot of other stuff.

But for now, this is the full version.

## V 0.34
- `for loop` now work normally in LowPie like its just python code!
```lua
potato = {"A", "b", "c"}

for i in list(potato) do
    print(i)
end
```
Based on the few researches I've made (using Ai so dont blame me if I was mistaken)
This code will work 100% Using LowPie.

- Added Converters (few not much :\)
- Added File Managers.
- Fixed few bugs
- Moved the codes from `Manual.md` to `Codes.md`
This Manual.md is so random, so i think i'll orginize it more.
