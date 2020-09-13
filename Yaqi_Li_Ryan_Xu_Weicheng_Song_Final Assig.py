## NAMES: RYAN ZEHONG XU, CHRIS YAQI LI, WEICHENG SONG
##
## COURSE: CMPT 120 D200
##
## SEMESTER & CAMPUS: FALL 2018, SFU BURNABY
##
## INSTRUCTOR: DIANA CUKIERMAN
##
## SUBMISSION DATE: Dec 3th, 2018
##
## DESCRIPTION: The code initially prompt the user to input a series of 649
##              lotto draws data and process them with some math functions.
##              User will be offered a choice to either process all data or
##              only the selected ones. Eventually, the program will create
##              excel file with some results and several statistics.


## TO READ FROM CSV INPUT FILE

def read_csv_into_list_of_lists(IN_file):
    '''
    PROVIDED. CMPT 120
    A csv file should be available in the folder (where this program is)
    A string with the name of the file should be passed as argument to this function
    when invoking it
    (the string would include the csv extension, e.g "ID_data.csv")
    '''

    import csv

    lall = []

    print("\n.... TRACE - data read from the file\n")
    with open(IN_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for inrow in csv_reader:
            print(".......",inrow)
            lall.append(inrow)
    return lall

def convert_lall_to_separate_lists(lall):
    '''
      RECOMMENDED THAT YOU DEVELOP THIS FUNCTION

      input parameter: list of lists with all the data
      as returned from read_csv_into_list_of_lists(...)
      
      return: several lists:
          dates of draws,
          numbers drawn for each draw,
          jackpot for each draw
          number of winners for each draw

     these lists would be such that accross the lists,
     the same index refers to one draw.
    '''
    for i in range(len(lall)):
        print ("\n JUST TO TRACE, the draw being processed is:")
        print ("\nindex# " + str(i))
        print ("date " + lall[i][0])
        temp = lall[i].copy()
        temp.remove(lall[i][0])
        temp.remove(lall[i][8])
        temp.remove(lall[i][9])
        print ("numbers drawn " + str(temp))
        print ("jackpot " + lall[i][8])
        print ("num winners " + lall[i][9])
            
            

## TO WRITE TO CSV INPUT FILE 
            
def append_1_draw_to_output_list(lout,date,lfreq_ran,avg_paid):
    '''
    PROVIDED. CMPT 120
    this function would append one line (the result associated to one draw)
    to a list. (this list will later be used to create the output file)
    
    
    The input parameters to this function are:
        - the list used to incorporate all the results
        - a string representing the date of this one draw to be appended
        - the list with the range frequency distribution for this draw
        - the average paid to each winner for this draw
    '''
    
    lout.append("'" + date + "'" + ",")
    for freq in lfreq_ran:
        lout.append(str(freq) + ",")
    lout.append(str(avg_paid) + "\n")
    return


def write_list_of_output_lines_to_file(lout,file_name):
    '''
    PROVIDED. CMPT 120
    Assumptions:
    1) lout is the list containing all the lines to be saved in the output file
    4) the output file contains just text representing one draw data per line 
    5) after each line in the file  there is the character "\n"
       so that the next draw is in the next line, and also
       there is (one single) "\n" character after the last line
    6) after the output file was created you should be able to open it
       with Excell as well
    '''
    
    fileRef = open(file_name,"w") # opening file to be written
    for line in lout:
        fileRef.write(line)
                                    
    fileRef.close()  
    return

def makelist(IN_file): ## make a list of lists without printing
    import csv
    lall = []
    with open(IN_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for inrow in csv_reader:
            lall.append(inrow)
    return lall

def prompt(): ## recursively prompt the user to chooce one of the three options
    print ("\nPlease choose one of three options:")

    print ("\nType ALL to process all the data")
    print ("Type SEL to process selected draws")
    print ("Type END to end this program")

    resp = input ("\nType ALL, SEL OR END (not case sensitive) ==> ")

    if resp.upper() == 'END':
        print ("BYE .... no more stats for you!!")
         
    elif resp.upper() == 'ALL':
        processall()

    elif resp.upper() == 'SEL':
        processsel()
    return
    

def processall(): ## process all data
    print ("\n============= ALL the data will be processed ============")

    print ("\n\n\nPlease confirm the output file name for your selected data")
    print ("    (if there is a file with this name in the folder\n      this new file substitute the previous one)")

    lst = makelist(infile)

    outfile = str(input ("\nType x for OUTPUT file name 'OUT_results3.csv', or a new file name ==> "))
    if outfile.lower() == 'x':
        outfile = 'OUT_results3.csv'

    convert_lall_to_separate_lists(lst)

    print ("\n\nTRACING: Here is the output saved to the file!\n")

    lout = []

    for i in range(len(lst)):
        lres = [0] * 5
        for k in range(1, len(lst[i]) - 2):
            j = 0
            while int(lst[i][k]) > j*10:
                j += 1
            lres[j-1] += 1
        st = ""
        for z in lres:
            st += str(z) + ','
        avg = 0
        if int(lst[i][9]) != 0:
            avg = int(lst[i][8]) / int(lst[i][9])

        append_1_draw_to_output_list(lout,lst[i][0],lres,avg)
        
        print ("'" + lst[i][0] + "'," + st + str(avg))

    write_list_of_output_lines_to_file(lout, outfile)

    processdata(lst)

    
    return

def processsel(): ## process selected data
    print ("\n============= SELECTED data will be processed ============")
    sel = str(input ("\n\n\nWant to select by month (M) or day of week (D)? ==> "))

    if sel.lower() == 'm':
        print ("\nPlease select a month")
        print ("Only the draws associated to this month will be processed")
        monnum = SEL_prompt()
        monlst = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        mo = monlst[int(monnum)-1]
        c = 0
        st = ""
        lst = makelist(infile)
        for i in range(len(lst)): ## check if theres any draws in the given month
            firstDash = lst[i][0].index('-')
            secondDash = firstDash + 4
            mon = lst[i][0][firstDash + 1: secondDash]
            if mo == mon:
                c += 1
        if c == 0:
            print ("The file does not have any draws in " + mo)
            print ("Nothing will be processed, you can try another option")
            prompt()
        print (c, "draws were found in the data for", mon)

        print ("\nPlease confirm the output file name for your selected data")
        print ("    (if there is a file with this name in the folder\n      this new file substitute the previous one)")

        outfile = str(input ("\nType x for OUTPUT file name 'OUT_results3.csv', or a new file name ==> ")) ## confirm name of output file
        if outfile.lower() == 'x':
            outfile = 'OUT_results3.csv'

        for i in range(len(lst)): ## trace printing for input data with true conditions
            firstDash = lst[i][0].index('-')
            secondDash = firstDash + 4
            mon = lst[i][0][firstDash + 1: secondDash]
            if mo == mon:
                print ("\n JUST TO TRACE, the draw being processed is:")
                print ("\nindex# " + str(i))
                print ("date " + lst[i][0])
                temp = lst[i].copy()
                temp.remove(lst[i][0])
                temp.remove(lst[i][8])
                temp.remove(lst[i][9])
                print ("numbers drawn " + str(temp))
                print ("jackpot " + lst[i][8])
                print ("num winners " + lst[i][9])

        print ("\n\nTRACING: Here is the output saved to the file!\n")

        lout = []
        
        for i in range(len(lst)): ## trace printing for output data
            lres = [0] * 5
            firstDash = lst[i][0].index('-')
            secondDash = firstDash + 4
            mon = lst[i][0][firstDash + 1: secondDash]
            if mo == mon:
                for k in range(1, len(lst[i]) - 2):
                    j = 0
                    while int(lst[i][k]) > j*10:
                        j += 1
                    lres[j-1] += 1
                st = ""
                for z in lres:
                    st += str(z) + ','
                avg = 0
                if int(lst[i][9]) != 0:
                    avg = int(lst[i][8]) / int(lst[i][9])

                '''
                res = str(lst[i][0]) + ',' + st + str(avg) + "\n"
                '''

                append_1_draw_to_output_list(lout,lst[i][0],lres,avg)

                print ("'" + lst[i][0] + "'," + st + str(avg))

        write_list_of_output_lines_to_file(lout, outfile) ## output data to new excel file

        lst2 = []
        
        for i in range(len(lst)): ## make new list of data for further process
            firstDash = lst[i][0].index('-')
            secondDash = firstDash + 4
            mon = lst[i][0][firstDash + 1: secondDash]
            if mo == mon:
                lst2.append(lst[i])

        processdata(lst2)
        return

    if sel.lower() == 'd':
        print ("\nPlease select a day in a week")
        print ("Only the draws associated to this day of week will be processed")
        day = SEL_day_prompt()
        monlst = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        c = 0
        st = ""
        lst = makelist(infile)
        for i in range(len(lst)): ## check if theres any draws in the given day of week
            firstDash = lst[i][0].index('-')
            secondDash = firstDash + 4
            mon = lst[i][0][firstDash + 1: secondDash]
            m = monlst.index(mon) + 1
            d = int(lst[i][0][:firstDash])
            y = int(lst[i][0][secondDash + 1:]) + 2000
            if dow (y, m, d) == day:
                    c += 1
        if c == 0:
            print ("The file does not have any draws on " + day)
            print ("Nothing will be processed, you can try another option")
            prompt()
        print (c, "draws were found in the data for", day)

        print ("\nPlease confirm the output file name for your selected data")
        print ("    (if there is a file with this name in the folder\n      this new file substitute the previous one)")

        outfile = str(input ("\nType x for OUTPUT file name 'OUT_results3.csv', or a new file name ==> ")) ## confirm output file name
        if outfile.lower() == 'x':
            outfile = 'OUT_results3.csv'

        for i in range(len(lst)): ## trace printing for input data with true conditions
            firstDash = lst[i][0].index('-')
            secondDash = firstDash + 4
            mon = lst[i][0][firstDash + 1: secondDash]
            m = monlst.index(mon) + 1
            d = int(lst[i][0][:firstDash])
            y = int(lst[i][0][secondDash + 1:]) + 2000
            if dow (y, m, d) == day:
                print ("\n JUST TO TRACE, the draw being processed is:")
                print ("\nindex# " + str(i))
                print ("date " + lst[i][0])
                temp = lst[i].copy()
                temp.remove(lst[i][0])
                temp.remove(lst[i][8])
                temp.remove(lst[i][9])
                print ("numbers drawn " + str(temp))
                print ("jackpot " + lst[i][8])
                print ("num winners " + lst[i][9])

        print ("\n\nTRACING: Here is the output saved to the file!\n") ## trace printing for output data

        lout = []

        for i in range(len(lst)):
            lres = [0] * 5
            firstDash = lst[i][0].index('-')
            secondDash = firstDash + 4
            mon = lst[i][0][firstDash + 1: secondDash]
            m = monlst.index(mon) + 1
            d = int(lst[i][0][:firstDash])
            y = int(lst[i][0][secondDash + 1:]) + 2000
            if dow (y, m, d) == day:
                for k in range(1, len(lst[i]) - 2):
                    j = 0
                    while int(lst[i][k]) > j*10:
                        j += 1
                    lres[j-1] += 1
                st = ""
                for z in lres:
                    st += str(z) + ','
                avg = 0
                if int(lst[i][9]) != 0:
                    avg = int(lst[i][8]) / int(lst[i][9])

                append_1_draw_to_output_list(lout,lst[i][0],lres,avg)

                print ("'" + lst[i][0] + "'," + st + str(avg))

        write_list_of_output_lines_to_file(lout, outfile) ## output data to new excel file

        lst2 = []
        
        for i in range(len(lst)): ## make new list for further process
            firstDash = lst[i][0].index('-')
            secondDash = firstDash + 4
            mon = lst[i][0][firstDash + 1: secondDash]
            m = monlst.index(mon) + 1
            d = int(lst[i][0][:firstDash])
            y = int(lst[i][0][secondDash + 1:]) + 2000
            if dow (y, m, d) == day:
                lst2.append(lst[i])

        processdata(lst2)
        return
        
def SEL_prompt(): ## prompt for month
    check = False
    while check == False:
        a = input ("Please type a month number (1 to 12) ==> ")
        if a.isdigit() == False:
            print ("This was not an integer. Please retype")
            check = False
        else:
            if int(a) < 1 or int(a) > 12:
                print ("The month number is out of range. Please retype")
                check = False
            else:
                check = True
    return a

def SEL_day_prompt(): ## prompt for day of week
    check = False
    while check == False:
        a = str(input ("Please enter the day of week (Monday, Tuesday, Wednesday...) ==> "))
        daysInWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        c = 0
        if a.isdigit() or a not in daysInWeek:
            print ("This is not a valid day in a week. Please retype")
            check = False
        else:
            return a

def dow(year, month, day): ## function which return the day of week given date
    import datetime
    res = datetime.date(year, month, day).strftime("%A")
    return res

def processdata(data): ## further process of data
    print("\n=========== STATS: ===========\n")
    jackpot = []
    average = []
    count = [0] * 49
    group = [0] * 5
    print ("draw processed %s" %(len(data)))

    for x in data: ## calculation of jackpot and average
        jackpot.append(int(x[8]))
        if int(x[9]) != 0:
            average.append(int(x[8])/int(x[9]))
        else:
            average.append(0)
        aves = 0
    for x in data:
        if int(x[9]) != 0:
            aves = int(x[8])/int(x[9])
        if x[8] == str(max(jackpot)):
            jcdate = x[0]
        if aves == max(average):
            avdate = x[0]
        for i in range (len(x)):
            if i != 0 and i != 8 and i != 9:
                    count[int(x[i])-1] += 1
    for i in range (len(count)):
        if i <= 9:
            group[0] += count[i]
        elif i <= 19:
            group[1] += count[i]
        elif i <= 29:
            group[2] += count[i]
        elif i <= 39:
            group[3] += count[i]
        elif i <= 49:
            group[4] += count[i]

    pailie = sorted(count,reverse = True)
    pailiehao = [0]*49
    countcp = count.copy()
    pailiecp = pailie.copy()
    for i in range (len(count)):
        for b in range (len(count)):
            if pailie[i] == count[b]:
                pailiehao[i] = b + 1
                count[b] = -5
                pailie[i] = -2
    countcp.append(0)
    for i in range (len(countcp)-1):
        countcp[-1-i] = countcp[-2-i]
    countcp[0] = 0    

    ## output results
    print("\nmax jackpot %s" %(max(jackpot)))
    print("date max jackpot %s" %(jcdate))

    print ("\nmax average won %s" %(max(average)))
    print ("date max average won %s" %(avdate))

    print ("\nnumber of times each number was drawn \n%s" %(countcp))

    print ("\nnumber of numbers in each range - all selected draws considered \nranges: (0,10], (10,20], (20,30], (30,40], (40,50) \n%s" %(group))

    print ("\nSix most frequently drawn numbers")

    ct = 0
    while (ct < 6):
        print("number %s was drawn %s times" %(pailiehao[ct],pailiecp[ct]))
        ct += 1

    resp2 = input ("\nWould you like to graph the ranges distributions? (Y/N): ")

    if resp2.lower() == 'n':
        prompt()

    elif resp2.lower() == 'y':
        huaturtle(group)
        prompt()
    return

def huaturtle(group): ## function which graphs the distributions of numbers

    import turtle
    t = turtle.Pen()
    turtle.speed(10)
    t.down()
    t.color("black","blue")

    for i in range(len(group)):
        t.begin_fill()
        t.forward(30)
        t.left(90)
        t.forward(group[i]*30)
        t.left(90)
        t.forward(30)
        t.left(90)
        t.forward(group[i]*30)
        t.end_fill()
        t.left(90)
        t.forward(60)
    return


## TOP LEVEL

print ("    Welcome to the CMPT 120 6-49 Processing System!")
print ("    ===============================================")

print ("\nYou first need to provide the input file name")
print ("You will be asked to provide the output file name later")

print ("\nThe input file should be in this folder")
print ("The output file should be created in this folder")

print ("\nYou will be able to provide new names for the files")
print ("or accept the default names. Both files should have the extension  .csv")

infile = str(input ("\nType x for INPUT file name 'IN_data_draws3.csv', or a new file name ==> "))
if infile.lower() == 'x':
    infile = 'IN_data_draws3.csv'

read_csv_into_list_of_lists(infile)
lst = makelist(infile)

prompt()
