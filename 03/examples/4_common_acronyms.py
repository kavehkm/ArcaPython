# define acronyms
acronyms = {
    'AFK': 'Away From Keyboard',
    'BBIAB': 'Be Back In A Bit',
    'BBL': 'Be Back Later',
    'BBS': 'Be Back Soon',
    'BRB': 'Be Right Back',
    'IDK': 'I Dont Know',
    'KISS': 'Keep It Simple Stupid',
    'LOL': 'Laughing Out Loud'
}


# get acronym from user input
acr = input('enter acronym: ')

# search acronyms dictionary
result = acronyms.get(acr, '!404!')

# bring back result to user
print('result is:', result)
