import message.message_provider

print(message.message_provider.get_message())

# PS C:\WORK\dragondive\heavens-arena\python\modules> python main.py
# Traceback (most recent call last):
#   File "C:\WORK\dragondive\heavens-arena\python\modules\main.py", line 1, in <module>
#     import message.message_provider
#   File "C:\WORK\dragondive\heavens-arena\python\modules\message\message_provider.py", line 1, in <module>
#     from answer.deep.answer_provider import get_answer
#   File "C:\WORK\dragondive\heavens-arena\python\modules\answer\deep\answer_provider.py", line 1, in <module>
#     from message.message_provider import get_real_message
# ImportError: cannot import name 'get_real_message' from partially initialized module 'message.message_provider' (most likely due to a circular import) (C:\WORK\dragondive\heavens-arena\python\modules\message\message_provider.py)
