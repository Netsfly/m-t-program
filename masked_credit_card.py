cardnumber = input(" card number ")
def mask(cardnumber):
    if len(cardnumber) == 16 and cardnumber.isdigit():
        masknum = "*" * 12 + cardnumber[-4:]
        return masknum
    else:
        print('invalid')
print(mask(cardnumber))