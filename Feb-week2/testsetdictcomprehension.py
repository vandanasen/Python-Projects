names=['bob','John','alice','j','Jane','Bob']
set_names = {name[0].upper()+ name[1:].lower() for name in names if len(name)>1}
print(set_names)
mcase={'a':10,'b': 34,'A':7,'z':3}
mcase_freq={k.lower():mcase.get(k.lower(),0)+mcase.get(k.upper(),0) for k in mcase.keys()}
print(mcase_freq)




