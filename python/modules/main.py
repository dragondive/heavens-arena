import message

print(type(message))
print(dir(message))
print(message.message_provider.get_message())   # error!

# PS C:\WORK\dragondive\heavens-arena\python\modules> python main.py
# <class 'module'>
# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
# Traceback (most recent call last):
#   File "C:\WORK\dragondive\heavens-arena\python\modules\main.py", line 5, in <module>
#     print(message.message_provider.get_message())
#           ^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: module 'message' has no attribute 'message_provider'
