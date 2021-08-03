'''Barname baraye pish bini tarikh marg shoma doost aziz bar asas etelaat marja haye
reference = 'University of California, Berkley wellness letter Aprill 2000\n CNN Even one drinks could be shortening your life expectancy\n United Nations Development Programme UNIP(2019 report)'
'''
#AZ
import jdatetime as jdt
import datetime as dt

#######Data
lifeExpectancy = {'JPN' : {'Female' : 87.5, 'Male' : 81.1}, 'ISR' : {'Female' : 84.4, 'Male' : 81.1}, 'EU' : {'Female' : 83.8,
                    'Male' : 78.6}, 'USA' : {'Female' : 81.4, 'Male' : 76.3}, 'IRN' : {'Female' : 77.7, 'Male' : 75.4}, 'RUS' :
                  {'Female' : 77.6, 'Male' : 66.9}, 'CAR' : {'Female' : 55.0, 'Male' : 55.6}};

##somkeE = 0.5
alcoholEffects = {'d' : 4, 'w' : 2, 'm' : 0.5, 'f' : 0}
reference = 'University of California, Berkley wellness letter Aprill 2000\n CNN Even one drinks could be shortening your life expectancy\n United Nations Development Programme UNIP(2019 report)'


#######Input
def gettingInputs() :
    #BirthDate
    print('Insert your birthdate (Jalali)')
    year = int(input('Enter year : '))
    month = int(input('Enter month : '))
    day = int(input('Enter day : '))
    global jBirthDate
    jBirthDate = jdt.datetime(year, month, day)
    print(jBirthDate.strftime('%Y/%B/%d'))

    #Sex
    print('Enter 1 for female, 2 for male')
    i = int(input(' : '))
    global sex
    sex = 'Male'
    if i == 1:
        sex = 'Female'

    #Smoke
    print('Do you smoke ? f for false, t for true')
    global smoke
    smoke = False
    ##print("A") if a == b else print("B")
    ##(smoke = True) if str(input(' : ')) == 't' else (smoke = False)
    answer = str(input(' : '))
    if answer == 't' :
        smoke = True

    #Alcohol
    print('Do you drink ? d for daily, w for weekly, m for monthly, f for false')
    global alcohol
    alcohol = str(input(' : '))

    #Country
    print('Where do you live? JPN, ISR, EU, USA, IRN, RUS, Centeral African Republic(CAR)')
    global country
    country = str(input(' : '))

#######process&Printing
def ProcessAndPrinting():
    today = jdt.datetime.now()
    #Old
    oldDays = today - jBirthDate
    old = oldDays.days / 365
    print('Now you are %2.2f years old' % (old))
    #Start
    Average = lifeExpectancy[country][sex]
    if smoke :
        Average -= 0.5
    Average -= alcoholEffects[alcohol]
    print(f'Your regular life expectancy is {Average}')
    left = Average - old

    if left > 0:
        Average *= 365
        Av = int(Average)
        jDeathDatetime = jBirthDate + jdt.timedelta(days = Av)
        DeathDate = jDeathDatetime.strftime('%Y/%m/%d')
        leftDays = (jDeathDatetime - jBirthDate).days
        print(f'You will die in {DeathDate}')
        print(f'And you have {leftDays} days left')
        print('Also {%2.2f} years left' % (left))
    else :
        print('You will die soon')

def program():
    try:
        gettingInputs()
    except:
        print('Something went wrong, lets try again')
        gettingInputs()
###Start Actions
if __name__ == '__main__':
    program()
    ProcessAndPrinting()
