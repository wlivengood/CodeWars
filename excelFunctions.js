def count_if(values,criteria):
    if ">=" in str(criteria):
        count = len([value for value in values if value >= float(criteria[2:])])
    elif "<=" in str(criteria):
        count = len([value for value in values if value <= float(criteria[2:])])
    elif "<>" in str(criteria):
        count = len([value for value in values if value != float(criteria[2:])])
    elif ">" in str(criteria):
        count = len([value for value in values if value > float(criteria[1:])])
    elif "<" in str(criteria):
        count = len([value for value in values if value < float(criteria[1:])])
    else:
        count = values.count(criteria)
    return count
    
def sum_if(values,criteria):
    if ">=" in str(criteria):
        the_sum = sum([value for value in values if value >= float(criteria[2:])])
    elif "<=" in str(criteria):
        the_sum = sum([value for value in values if value <= float(criteria[2:])])
    elif "<>" in str(criteria):
        the_sum = sum([value for value in values if value != float(criteria[2:])])
    elif ">" in str(criteria):
        the_sum = sum([value for value in values if value > float(criteria[1:])])
    elif "<" in str(criteria):
        the_sum = sum([value for value in values if value < float(criteria[1:])])
    else:
        the_sum = sum([value for value in values if value == criteria])
    return the_sum
    
def average_if(values,criteria):
    the_sum = sum_if(values,criteria)
    count = count_if(values,criteria)
    return float(the_sum)/float(count)