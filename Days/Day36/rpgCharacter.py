full_dot = '●'
empty_dot = '○'

def create_character(cname, strength, intllg, charisma):
    if not isinstance(cname, str):
        return "The character name should be a string"
    elif cname == "" :
        return "The character should have a name"
    elif len(cname) > 10:
        return "The character name is too long"
    elif " " in cname:
        return "The character name should not contain spaces"
    elif not all(isinstance(x, int) for x in (strength, intllg, charisma)):
        return "All stats should be integers"
    elif (strength or intllg or charisma) < 1:
        return "All stats should be no less than 1"
    elif (strength or intllg or charisma) > 4:
        return "All stats should be no more than 4"
    elif (strength + intllg + charisma) != 7:
        return "The character should start with 7 points"
    return f"{cname}\nSTR {full_dot * strength}{empty_dot * (10 - strength)}\nINT {full_dot * intllg}{empty_dot * (10 - intllg)}\nCHA {full_dot * charisma}{empty_dot * (10 - charisma)}"

print(create_character('ren', 4, 2, 1))