import re
from inquirer import errors

def date_format(_, current):
    # valdidate format
    re_YYYY_MM_DD_hh_mm = "[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]"
    if not re.search(re_YYYY_MM_DD_hh_mm, current):
        raise errors.ValidationError('', 'Invalid date format. Has to be YYYY-MM-DD hh:mm')
       
    return True