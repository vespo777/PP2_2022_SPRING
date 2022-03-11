import re
def text_match(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'matching'
        else:
                return('not matching')

                