import string.message_provider

print(type(string))
print(dir(string))
print(type(string.message_provider))
print(dir(string.message_provider))
print(string.message_provider.get_message())

# PS C:\WORK\dragondive\heavens-arena\python\modules> python main.py
# <class 'module'>
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'message_provider']
# <class 'module'>
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'get_message']
# Hello World
