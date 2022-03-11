import re
def snake_to_camel(word):
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('are_city'))