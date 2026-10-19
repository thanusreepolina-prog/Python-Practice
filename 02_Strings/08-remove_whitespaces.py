import re
text='python life'
print("original text:",text)
print("without white spaces:",re.sub(r'\s+', '',text))