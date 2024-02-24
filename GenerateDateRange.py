import datetime

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def pad(string):
    while len(string) < 2:
        return "0" + string
    return string
    
def generatePrevDay(year, month, day):
    if (int(day)) > 0:
        day = str(int(day)-1)
    elif month == "00":
        year = str(int(year)-1)
        month = "12"
        day = str(days[11])
    else:
        month = (str(int(month)-1))
        day = str(days[int(month)])
    day = pad(day)
    month = pad(month)
    year = pad(year)
    return year, month, day
    
def generateDateRange(prevDaysAmount):#, year, month, day):
    today = datetime.datetime.now().strftime("%y-%m-%d").split("-")
    year = today[0]
    month = today[1]
    day = today[2]
    dates = [today[0]+"-"+today[1]+"-"+today[2]]

    for i in range(prevDaysAmount+1):
        try:
            year, month, day = generatePrevDay(year, month, day)
            dates.append(year+"-"+month+"-"+day)
        except:
            print("Failed date!")
    return dates
    
if __name__ == "__main__":
    print(generateDateRange(10))
