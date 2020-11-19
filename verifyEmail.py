# from validate_email import validate_email
# print(validate_email('horacio@gmail.com'))

email = 'horac..io@gmail.es'

def validateEmail(email):
    emailName = 0

    if email[0] != '@':
        emailName += 1
        if email.count('@') > 1:
            return False
        if '.' not in email:
            return False
        else:
            domain = email[email.index('@'):]
            if domain[0] == '.' or ' ' in domain:
                return False
            else:
                if domain.count('.') > 1 or domain.count('.') == 0:
                    return False
                else:
                    last = domain[domain.index('.') + 1:]
                    if len(last) > 0:
                        return True
                    else:
                        return False
    else:
        return False

print(validateEmail(email))