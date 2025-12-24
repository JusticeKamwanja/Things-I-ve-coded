def apology(language):
    if language.lower() == 'swa':
        output = 'Kosa langu'
    if language.lower() == 'eng':
        output = 'My fault'
    if language.lower() == 'kal':
        output = 'Mutio'
    if language.lower() == 'esp':
        output = 'Mea culpa'
    return output

apologies = [apology('eng'), apology('esp'), apology('kal'),apology('swa')]

for apology in apologies:
    print(apology)