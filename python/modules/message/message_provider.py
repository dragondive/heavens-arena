import answer.deep.answer_provider

def get_message():
    print(type(answer))
    print(dir(answer))
    print(type(answer.deep))
    print(dir(answer.deep))
    print(type(answer.deep.answer_provider))
    print(dir(answer.deep.answer_provider))
    return "Hello " + str(answer.deep.answer_provider.get_answer())