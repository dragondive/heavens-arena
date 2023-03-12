import string.message_provider

print(type(string))
print(dir(string))
print(type(string.message_provider))
print(dir(string.message_provider))
print(string.message_provider.get_message())

# PS C:\WORK\dragondive\heavens-arena\python\modules> python main.py
# Traceback (most recent call last):
#   File "C:\WORK\dragondive\heavens-arena\python\modules\main.py", line 1, in <module>
#     import string.message_provider
# ModuleNotFoundError: No module named 'string.message_provider'; 'string' is not a package
