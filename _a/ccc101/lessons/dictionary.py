b = {'CU': 'see you',
     # ':-)': "I'm happy",
     ':-)':"I'm happy",
     ':-(': "I'm unhappy",
     ';-)': 'wink',
     ':-P': 'stick out my tongue',
     '(~.~)': 'sleepy',
     'TA': 'totally awesome',
     'CCC': 'Canadian Computing Competition',
     'CUZ': 'because',
     'TY': 'thank-you',
     "YW": "you're welcome",
     'TTYL': 'talk to you later'}

while True:
    a = input()
    print(b.get(a, a))
    if a == "TTYL":
        break