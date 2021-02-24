log_file = open("um-server-01.txt") # allows file to open in terminal


def sales_reports(log_file): # function declaration with name and parameters
    for line in log_file:    # iterating through a list or array
        line = line.rstrip() # function definition that holds the body of code
        day = line[0:3]
        if day == "Mon":     # if day is equal to Monday
            print(line)      # print the line


sales_reports(log_file) # executing the defined function
