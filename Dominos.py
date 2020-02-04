# THIS IS A SCRIPT THAT TRACKS HOURS WORKED, MILES DRIVEN DURING SHIFT, AND TIPS EARNED
# THE INFORMATION IS THEN STORED IN A CSV READY FOR EXPORT TO A SPREADSHEET

import csv
from datetime import date

today = date.today()
pay_rate = 6.50
new_entry = str(input('Do you want to add a new entry? y/n'))
if new_entry == str('y'):
    hours_worked = int(input('How many hours did you work during this shift? '))
    miles_driven = int(input('How many miles did you drive during this shift? '))
    tips_earned = int(input('How much did you earn in tips during this shift? '))
    base_pay = pay_rate * hours_worked
    total_earned = base_pay + tips_earned
    adjusted_pay = total_earned / hours_worked

    print(f'Base pay: ${base_pay:.2f}')
    print(f'Total earned with tips: ${total_earned:.2f}')
    print(f'Hourly pay rate with tips: ${adjusted_pay:.2f}')

    with open('dominos.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([today, hours_worked, miles_driven, tips_earned])
else:
    pass