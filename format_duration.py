def format_duration(seconds):
    if seconds == 0:
        return "now"
    secs = seconds % 60
    minutes = (seconds // 60) % 60
    hours = (seconds  // (60 * 60)) % 24
    days = (seconds // (60 * 60 * 24)) % 365
    years = seconds // (60 * 60 * 24 * 365)
    amounts = [years, days, hours, minutes, secs]
    units = ["year", "day", "hour", "minute", "second"]
    answer = ""
    num_amounts = len([i for i in amounts if i != 0])
    counter = 0
    for i in range(len(amounts)):
        if amounts[i]:
            counter += 1
            answer += str(amounts[i]) + " " + units[i]
            if amounts[i] > 1:
                answer += "s"
            if counter < num_amounts - 1:
                answer += ", "
            if counter == num_amounts - 1:
                answer += " and "  
    return answer
