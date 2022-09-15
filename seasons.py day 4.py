#program to display season

month=input("enter a month")
date=int(input("enter the date"))
if(date>0 and date<=31):
    if(month=='april' or month=='may'):
         print(" the season currently is summer")
    if(month=='june' and date<=20):
         print("the season currently is summer")
    if(month=='march' and date>20):
         print("the season currently is summer")
    if(month=='june' and date>20):
         print("the season currently is spring")
    if(month=='july'or month=='august'):
         print("the season currently is spring")
    if(month=='september' and date<=20):
         print("the season currently is spring")
    if(month=='september' and date>20):
         print("the season currently is fall")
    if(month=='october' or month=='november'):
         print("the season currently is fall")
    if(month=='december' and date<=20):
         print("the season currently is fall")
    if(month=='january' or month=='february'):
         print("the season currently is winter")
    if(month=='march' and date<=20):
         print("the season currently is winter")
    if(month=='december' and date>20):
        print("the season currently is winter")

else:
    print("enter valid input")
