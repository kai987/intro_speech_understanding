
def next_birthday(date, birthdays):
    '''
    Find the next birthday after the given date.

    @param:
    date - a tuple of two integers specifying (month, day)
    birthdays - a dict mapping from date tuples to lists of names, for example,
      birthdays[(1,10)] = list of all people with birthdays on January 10.

    @return:
    birthday - the next day, after given date, on which somebody has a birthday
    list_of_names - list of all people with birthdays on that date
    ''' 
    if not birthdays:
        return None, []

    future_dates = [
        day for day, names in birthdays.items()
        if day > date and names
    ]

    if future_dates:
        birthday = min(future_dates)
    else:
        valid_dates = [
            day for day, names in birthdays.items()
            if names
        ]
        if not valid_dates:
            return None, []
        birthday = min(valid_dates)

    list_of_names = birthdays[birthday]

    return birthday, list_of_names
    
