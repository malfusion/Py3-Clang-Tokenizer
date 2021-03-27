# Py3-Clang-Tokenizer

A Python3 port of the C/C++ tokenizer available at [JonathanPierce/PyTokenize](https://github.com/JonathanPierce/PyTokenize). Added a few extra abilities such parsing from an in-memory file buffer and removing functionality that were not neceassary for my use-case.

# Installation (Mac OSX)

- Make sure the latest XCode Command Line Tools are installed
  - ```xcode-select --install```
- Make sure llvm is installed 
  - ```brew install llvm```
- The above command installs llvm to the system with the library present at a path like:
  - ```/usr/local/Cellar/llvm/11.1.0/lib```
- Make sure to change the Config line in tokenizer.py according to your installation:
  - ```clang.cindex.Config.set_library_path("/usr/local/Cellar/llvm/11.1.0/lib")```
 
# Usage (Library)
- Using a string of code written in C/C++
```python3 
from tokenizer import Tokenizer
tokenizer = Tokenizer(c_str='''
              for (int i=0; i<200; i++){
                cout<<i;
              }''')
print(tokenizer.full_tokenize())
print(tokenizer.full_tokenize_compressed())
```
- Using a C/C++ file
```python3
from tokenizer import Tokenizer
tokenizer = Tokenizer(path='./test_file.cpp')
print(tokenizer.full_tokenize())
print(tokenizer.full_tokenize_compressed())
```


# Usage (Command Line)
```bash
python tokenizer.py ../relative/path/to/code/file.cpp
```
