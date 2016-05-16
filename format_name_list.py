def namelist(names):
    name_list = []
    for i in range(len(names)):
        name = names[i]['name']
        name_list.append(name)
    length = len(name_list)
    if not length:
        return ""
    if length == 1:
        return name_list[0]
    name_string = ", ".join((name_list[:(length - 1)]))
    name_string += " & " + name_list[length - 1]
    return name_string
