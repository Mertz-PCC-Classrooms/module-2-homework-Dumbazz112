# Homework 2

For this assignment, you'll be working with three different files:

* `hw2_welcome.py`: prompt the user for their name and welcome them using "Hello" and their name.
* `hw2_temp.py`: prompt the user for the temperature in Celsius and convert it to Fahrenheit.
* `hw2_rate.py`: prompt the user for the number of hours worked and their pay rate and return to them their expected paycheck amount.

## HW2 - Welcome

### Description

For this assignment, modify the function "welcome" that uses `input` to prompt
the user for their name and then welcomes them with "Hello Username", where
"Username" is the name that was entered by the user.

#### Example Usage

``` console
    >>> python3 hw2_welcome.py
    What is your name?
    Name: Username
    Welcome Username
```

### Instructions

Replace/alter the contents in between the START and END comments below with
your code to fulfill the requirements for this assignment.

#### Requirements

* You *must* use `input` to prompt the user for a name
* You *must* print out a statment that addresses their name and uses the word
    "welcome" (see also Example Usage)

## HW2 - Temp

### Description

For this assignment, modify the function "temp" to use `input` to prompt
the user for a temperature in Celsius that they would like to covert into
Farenheit.  Once you've obtained the Celsius value, convert it into Farenheit
and print to the screen the coversion.

#### Example Usage

``` console
    >>> python3 hw2_temp.py
    What is the temperature you would like to convert (C)?
    Temp (in C): 32
    Temperature 32C is 89.6F
```

### Instructions

Replace/alter the contents in between the START and END comments below with
your code to fulfill the requirements for this assignment.

#### Requirements

- You *must* use `input` to prompt the user for Temperature
- You *must* print out a statment to the console that has the value of the
    calculated temperature in Farenheit.

## HW2 - Rate

### Description

For this assignment, modify the function "rate" to use `input` to prompt
the user for their number of hours worked and their pay rate (in dollars). Then
calculate their expected pay check by multiplying the two numbers.  Print that
value back to the user.

#### Example Usage

``` console
    >>> python3 hw2_rate.py
    How many hours did you work?
    Hours: 36
    What is your pay rate (in dollars)?
    Pay Rate: 12.75
    Your expected paycheck is: $475.0
```

### Instructions

Replace/alter the contents in between the START and END comments below with
your code to fulfill the requirements for this assignment.

#### Requirements

* You *must* use `input` to prompt the user for the number of hours and their
    pay rate.
* You *must* print out a statment to the console that has the value of the
    expected pay check.
* DO NOT place additional punctuation to the paycheck.  For example, if the
    the calculated value of the pay check is 1006.58234234, DO NOT place
    additional comma's such as 1,006.58234234.
