# Write your solution here
def is_it_valid(pic: str) -> bool:
    
    if len(pic) != 11:
        return False
    
    from datetime import datetime
    import string

    dob_six_digits = pic[0:6]
    century = pic[6]
    dob = pic[0:4]
    if century == "+":
        dob += "18"
    elif century == "-":
        dob += "19"
    elif century == "A":
        dob += "20"
    else:
        return False
    dob += pic[4:6]

    format = "%d%m%Y"
    res = True
    try:
        res = bool(datetime.strptime(dob, format))
    except ValueError:
        return False
    
    personal_identifier = pic[7:10]
    for i in personal_identifier:
        if i not in string.digits:
            return False
    if len(personal_identifier) != 3:
        return False
    
    control_character = pic[10]

    dob_plus_pi = int(dob_six_digits + personal_identifier) % 31
    if control_character != "0123456789ABCDEFHJKLMNPRSTUVWXY"[dob_plus_pi]:
        return False

    return True
    

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))