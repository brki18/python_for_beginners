# Functions can be called directly

text = 'This is simple text'

# Methods are called upon some object
text2 = text.capitalize()


# print(text.capitalize())


def doc_example(msg):
    '''
    Info: This function is returning message passed as an argument
    :param msg:
    :return: msg
    '''
    return msg


doc_example('message')

# help(doc_example)
print(doc_example.__doc__)

