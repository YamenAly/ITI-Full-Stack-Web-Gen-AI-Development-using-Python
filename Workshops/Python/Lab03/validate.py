import re
def validate_name(name):
    if re.fullmatch(r"^[a-zA-Z]+([a-zA-Z0-9](_|-| |\.|,|#|\+){0,})*[a-zA-Z0-9]+$", name) == None:
        return False
    else:
        return True
def validate_mail(mail):
    if re.fullmatch(r"^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$", mail) ==  None:
        return False
    else:
        return True
def validate_password(password):
    if re.fullmatch(r"(?=\S*[A-Z])(?=\S*[a-z])(?=\S*[0-9]).{6,}\S$", password) == None:
        return False
    else:
        return True

def validate_phone(phone):
    if re.fullmatch(r"^01[0125]\d{8}$", phone) == None:
        return False
    else:
        return True
    
def validate_date(date):
    if re.fullmatch("^\d{4}-\d{2}-\d{2}$", date) == None:
        return False
    else:
        return True