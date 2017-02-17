# -*- coding: utf-8 -*-
# @Author: Maria Villalobos
# @Date:   2017-02-16 13:37:47
# @Last Modified by:   mati
# @Last Modified time: 2017-02-16 17:11:06
# Advanced Python Programming - Lab 4
# This example was extracted from http://web.mit.edu/6.005/www/sp15/classes/03-code-review/
# and translated to Python for the purpose of this course

# Write a new version of the Day_Of_Year and leap functions
# by iteratively taking into account the following elements:

# THINGS TO TAKE INTO ACCOUNT
# 1. Don’t Repeat Yourself
# 2. Comments Where Needed
# 3. Fail fast
# 4. Avoid Magic Numbers
# 5. One purpose for each variable
# 6. Use Good Names (take naming conventions into account)
# 7. Use Whitespace to Help the Reader

from datetime import timedelta


def Day_Of_Year(Month, Day_Of_Month, Year):
    Day_Of_Month = 0

    for i in range(1,Month)+1:
    #find day of the year given the month of the year 
        if (i == 2):
            Day_Of_Month += 31
        if (i == 3):
            Day_Of_Month += 28
        if (i == 4):
            Day_Of_Month += 31
        if (i == 5):
            Day_Of_Month += 30
        if (i == 6):
            Day_Of_Month += 31
        if (i == 7):
            Day_Of_Month += 30
        if (i == 8):
            Day_Of_Month += 31
        if (i == 9):
            Day_Of_Month += 31
        if (i == 10):
            Day_Of_Month += 30
        if (i == 11):
            Day_Of_Month += 31
        if (i == 12):
            Day_Of_Month += 31
    return Day_Of_Month


def leap(year):
    four_digit_year = str(year)
    if (four_digit_year[2] == '1' or four_digit_year[2] == '3' or four_digit_year[2] == '5' or four_digit_year[2] == '7' or four_digit_year[2] == '9'): # 5 is a string not a integer
        if (four_digit_year[3] == '2' or four_digit_year[3] == '6'):
            return True
        else:
            return False
    else:
        if (four_digit_year.charAt(2) == '0' and four_digit_year.charAt(3) == '0'):
            return False
        if (four_digit_year[3] == '0' or four_digit_year[3] == '4' or four_digit_year[3] == '8'):
            return True
    return False


def get_crossover_signal(self, on_date):
    '''This is another example of Smelly Code from the Test- Driven Python Development book
    by Siddharta Govindaraj Chapter 3'''
    cpl = []
    for i in range(11):
        chk = on_date.date() - timedelta(i)
        for price_event in reversed(self.price_history):
            if price_event.timestamp.date() > chk:
                pass
            if price_event.timestamp.date() == chk:
                cpl.insert(0, price_event)
                break
            if price_event.timestamp.date() < chk:
                cpl.insert(0, price_event)
                break

            # Return NEUTRAL signal
            if len(cpl) < 11:
                cpl.insert(0, price_event)
                break

            # BUY signal
            if sum([update.price for update in cpl[-11:-1]]) / 10 \
                    > sum([update.price for update in cpl[-6:-1]]) / 5 \
                    and sum([update.price for update in cpl[-10:]]) / 10 \
                    < sum([update.price for update in cpl[-5:]]) / 5:
                        return 1
            # BUY signal
            if sum([update.price for update in cpl[-11:-1]]) / 10 \
                    < sum([update.price for update in cpl[-6:-1]]) / 5 \
                    and sum([update.price for update in cpl[-10:]]) / 10 \
                    > sum([update.price for update in cpl[-5:]]) / 5:
                        return -1

            # NEUTRAL signal
            return 0
