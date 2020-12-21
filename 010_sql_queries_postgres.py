import json
import psycopg2


# ----------------------------------------------------------------------------
def get_credentials():

    credentials_file = r'c:\postgres_credentials.json'
    # {"user": "***", "password": "***", "port": "***", "host": "***"}

    with open(credentials_file, 'r') as file:
        postgres_credentials = json.load(file)

    # postgres_credentials = {'user': '***', 'password': '***', 'port': '***', 'host': '***'}

    return postgres_credentials
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
def execute_and_print(sql_query):

    credentials = get_credentials()
    user = credentials['user']
    password = credentials['password']
    port = credentials['port']
    host = credentials['host']
    database = 'exercises'

    conn = psycopg2.connect(dbname=database, user=user, password=password, port=port, host=host)

    cur = conn.cursor()
    cur.execute(sql_query)
    tables = cur.fetchall()

    print('\n')
    for table in tables:
        print(table)

    conn.close()
# ----------------------------------------------------------------------------



# ----------------------------------------------------------------------------
# The Complete SQL Bootcamp 2020: Go from Zero to Hero - Jose Portilla
# (Udemy online education platform: https://www.udemy.com/ )

#  SQL Assessment Test 2
# Questions and Expected Results
# Keep in mind there is usually more than one way to answer these questions.
# These questions start off with the basics and then get continually more difficult.
# ----------------------------------------------------------------------------



# ------------------------------------------------------------------------------------
# How can you retrieve all the information from the cd.facilities table?

sql_query = r'''
SELECT * FROM cd.facilities
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# You want to print out a list of all of the facilities and their cost to members.
# How would you retrieve a list of only facility names and costs?

sql_query = r'''
SELECT name, membercost FROM cd.facilities
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# How can you produce a list of facilities that charge a fee to members?
# Expected Results should have just 5 rows

sql_query = r'''
SELECT name, membercost FROM cd.facilities
WHERE membercost > 0
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# How can you produce a list of facilities that charge a fee to members, and that fee
# is less than 1/50th of the monthly maintenance cost?
# Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.
# Result is just two rows

sql_query = r'''
SELECT facid, name, membercost, monthlymaintenance FROM cd.facilities
WHERE membercost > 0 AND membercost < (monthlymaintenance / 50) 
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# How can you produce a list of all facilities with the word 'Tennis' in their name?
# Expected Result is 3 rows

sql_query = r'''
SELECT name FROM cd.facilities
WHERE name LIKE '%Tennis%'
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# How can you retrieve the details of facilities with ID 1 and 5?
# Try to do it without using the OR operator.
# Expected Result is 2 rows

sql_query = r'''
SELECT * FROM cd.facilities
WHERE facid IN (1, 5)

'''
execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# How can you produce a list of members who joined after the start of September 2012?
# Return the memid, surname, firstname, and joindate of the members in question.
# Expected Result is 10 rows

sql_query = r'''
SELECT memid, surname, firstname, joindate FROM cd.members
WHERE joindate >= '2012-09-01 00:00:00'
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# How can you produce an ordered list of the first 10 surnames in the members table?
# The list must not contain duplicates.
# Expected Result should be 10 rows if you include GUEST as a last name

sql_query = r'''
SELECT DISTINCT(surname) FROM cd.members
ORDER BY surname
LIMIT 10
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# You'd like to get the signup date of your last member. How can you retrieve this information?
# Expected Result: 2012-09-26 18:08:45

sql_query = r'''
SELECT joindate FROM cd.members
ORDER BY joindate DESC
LIMIT 1
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# You'd like to get the signup date of your last member. How can you retrieve this information?
# Expected Result: 2012-09-26 18:08:45

sql_query = r'''
SELECT joindate FROM cd.members
ORDER BY joindate DESC
LIMIT 1
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# Produce a count of the number of facilities that have a cost to guests of 10 or more.
# Expected Result: 6

sql_query = r'''
SELECT COUNT(guestcost) from cd.facilities
WHERE guestcost >= 10
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# Produce a list of the total number of slots booked per facility in the month of September 2012.
# Produce an output table consisting of facility id and slots, sorted by the number of slots.
# Expected Result is 9 rows

sql_query = r'''
SELECT facid, SUM(slots)
FROM cd.bookings
WHERE starttime >= '2012-09-01' AND starttime <='2012-09-30'
GROUP BY facid
ORDER BY SUM(slots) DESC
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# Produce a list of facilities with more than 1000 slots booked.
# Produce an output table consisting of facility id and total slots, sorted by facility id.
# Expected Result is 5 rows

sql_query = r'''
SELECT facid, SUM(slots) from cd.bookings
GROUP BY facid
HAVING SUM(slots) > 1000
ORDER BY facid
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'?
# Return a list of start time and facility name pairings, ordered by the time.
# Expected Result is 12 rows

sql_query = r'''
SELECT starttime, cd.facilities.name from cd.bookings
INNER JOIN cd.facilities ON cd.bookings.facid = cd.facilities.facid
WHERE cd.facilities.name LIKE '%Tennis Court%'
AND starttime >= '2012-09-21 00:00:00' AND starttime < '2012-09-22 00:00:00'
ORDER BY starttime
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# How can you produce a list of the start times for bookings by members named 'David Farrell'?
# Expected result is 34 rows of timestamps

sql_query = r'''
--SELECT cd.members.firstname as name, cd.members.surname as surname, starttime
SELECT starttime
FROM cd.bookings
INNER JOIN cd.members ON cd.bookings.memid = cd.members.memid
WHERE cd.members.firstname LIKE 'David' AND cd.members.surname LIKE 'Farrell'
--ORDER BY starttime
'''

execute_and_print(sql_query)
# ------------------------------------------------------------------------------------














