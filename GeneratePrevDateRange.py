from GeneratePrevDay import generatePrevDay
import datetime

def generateDateRange(prevDaysAmount):#, year, month, day):
    today = datetime.datetime.now().strftime("%y-%m-%d").split("-")
    year = today[0]
    month = today[1]
    day = today[2]
  
    dates = []
    
    for i in range(prevDaysAmount+1):
        try:
            year, month, day = generatePrevDay(year, month, day)
            dates.append(year+"-"+month+"-"+day)
        except:
            print("Failed date!")
    return dates
