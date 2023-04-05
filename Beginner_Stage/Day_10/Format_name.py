def format_name(f_name, l_name):
    """ This function return an outputs of formatted names"""
    if f_name == "" or l_name == "":
        return "You did\'nt provide valid input "
    return f"{f_name.title()} {l_name.title()}"


a = format_name(input("What is your first name?\n"), input("What is your last name?\n"))
print(a)
