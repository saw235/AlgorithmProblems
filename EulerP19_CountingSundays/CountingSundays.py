def get_nday(month,year): 
    
    leap = False
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        if year % 4 == 0:
            leap = True
        else:
            leap = False


    d = {
        0 : 31, #Jan
        2 : 31, #Mar
        3 : 30, #April
        4 : 31, #May
        5 : 30, #June
        6 : 31, #July
        7 : 31, #August
        8 : 30, #September
        9 : 31, #October
        10 : 30, #November
        11 : 31 #December
    }

    if leap:
        d[1] = 29
    else:
        d[1] = 28

    return d[month] 



days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

i = 0
j = 1900
days_elapsed = 1
count = 0

while True:
    if j > 2000:
        break
    print(j)
    #for a year
    while True:

        if i >= 12:
            break

        #get the days_elapsed for each month
        ans = days[(days_elapsed-1)%7]

        #print(ans)
        if ans == "Sunday":
            print('-')
            count += 1


        days_elapsed += get_nday(i,j)
        i += 1

    i = 0
    j += 1

print(count - 2)