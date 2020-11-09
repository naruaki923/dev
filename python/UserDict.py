from collections import UserDict, abc #Python 実践入門 P.178
class MyDict(UserDict):
  pass

def get_value(obj, key):
  if not isinstance(obj, abc.Mapping):
    raise ValueError
  return obj[key]

if __name__ == "__main__":
    my_dict = MyDict()
    get_value(my_dict, 'a')

# できなかった。2020/10/21
"""
以下エラー
Traceback (most recent call last):
  File "UserDict.py", line 12, in <module>
    get_value(my_dict, 'a')
  File "UserDict.py", line 8, in get_value
    return obj[key]
  File "C:\Users\naruaki\anaconda3\lib\collections\__init__.py", line 1010, in __getitem__
    raise KeyError(key)
KeyError: 'a'
"""
