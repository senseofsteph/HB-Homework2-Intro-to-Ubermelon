log_file = open("um-server-01.txt") # opens specified file


def sales_reports(log_file): # function declaration w parameter
    for line in log_file:    # iterating through a file
        line = line.rstrip() 
        day = line[0:3]
        if day == "Mon":     # if day is equal to Monday
            print(line)         # print the line


sales_reports(log_file) # function execution with one argument
