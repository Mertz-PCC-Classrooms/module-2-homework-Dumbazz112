"""
# HW2 - Rate

## Description

For this assignment, modify the function "rate" to use `input` to prompt
the user for their number of hours worked and their pay rate (in dollars). Then
calculate their expected pay check by multiplying the two numbers.  Print that
value back to the user.

### Example Usage

>>> python3 hw2_rate.py
How many hours did you work?
Hours: 36
What is your pay rate (in dollars)?
Pay Rate: 12.75
Your expected paycheck is: $475.0

## Instructions

Replace/alter the contents in between the START and END comments below with
your code to fulfill the requirements for this assignment.

### Requirements
- You *must* use `input` to prompt the user for the number of hours and their
    pay rate.
- You *must* print out a statment to the console that has the value of the
    expected pay check.
- DO NOT place additional punctuation to the paycheck.  For example, if the
    the calculated value of the pay check is 1006.58234234, DO NOT place
    additional comma's such as 1,006.58234234.
"""

def rate():
    # START: your code here
    # NOTE: you can remove the `pass` here if you want.  It's a null operation.
    pass
    # END: your code here

if __name__ == "__main__":
    rate()
    number_of_hours_worked = input("How many hours did you work?: ")
    number_of_hours_worked = float(number_of_hours_worked)
    print(f"Hours: {number_of_hours_worked}")
    
    rate_in_dollars = input("What is your pay rate (in dollars)?: ")
    print(f"Pay Rate: ${rate_in_dollars}")
    rate_in_dollars = float(rate_in_dollars)
    
    expected_paycheck = (number_of_hours_worked) * (rate_in_dollars)
    expected_paycheck = float(expected_paycheck)
    print(f"Your expected paycheck is: ${expected_paycheck}")
