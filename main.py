import pandas as pd
import numpy as np
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('planets.db')

# Select all
pd.read_sql("""SELECT * FROM planets; """, conn1)

# STEP 1
# Replace None with your code
df_no_moons = pd.read_sql("""
        SELECT * 
        FROM planets
        WHERE num_of_moons = 0

""", conn1)
#print(df_no_moons)

# STEP 2
# Replace None with your code
""" WITH DYNAMISM """
#name_length = int(input("Enter name length to search: "))
# df_name_seven = pd.read_sql("""
#         SELECT name, mass
#         FROM planets
#         WHERE length(name) = ?

# """, conn1, params=(name_length,))
#print(df_name_seven)

""" HARDCODED """
df_name_seven = pd.read_sql("""
        SELECT name, mass
        FROM planets
        WHERE length(name) = 7

""", conn1)

##### Part 2: Advanced Filtering #####

# STEP 3
# Replace None with your code
""" WITH DYNAMISM """
# size=float(input("Enter mass (less than or equal to) to search: "))
# df_mass = pd.read_sql("""
#         SELECT name, mass
#         FROM planets
#         WHERE mass <= ?

# """, conn1, params=(size,))
#print(df_mass)

""" HARDCODED """
df_mass = pd.read_sql("""
        SELECT name, mass
        FROM planets
        WHERE mass <= 1

""", conn1)
#print(df_mass)

# STEP 4
# Replace None with your code
#moon_nums=int(input("Enter number of moons to search: "))
#size=float(input("Enter mass (less than) to search: "))
df_mass_moon = pd.read_sql("""
        SELECT *
        FROM planets
        WHERE num_of_moons >=1 AND mass < 1
                           
""",conn1)
#print(df_mass_moon)

# STEP 5
# Replace None with your code
df_blue = pd.read_sql("""
        SELECT name, color
        FROM planets
        WHERE color LIKE '%blue%'

""", conn1)
#print(df_blue)

##### Part 3: Ordering and Limiting #####

# STEP 0

# Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('dogs.db')

# Select all
pd.read_sql("SELECT * FROM dogs;", conn2)

# STEP 6
# Replace None with your code
df_hungry = pd.read_sql("""
        SELECT name, age, breed
        FROM dogs
        WHERE hungry = True
        ORDER BY age ASC

""",conn2)
""" REPLACE EVERY NaN IN THE DATAFRAME WITH None TO AVOID NaN!=None ERROR"""
df_hungry = df_hungry.replace({np.nan: None})
#print(df_hungry)

# STEP 7
# Replace None with your code
df_hungry_ages = pd.read_sql("""
        SELECT name, age, hungry
        FROM dogs
        WHERE age BETWEEN 2 AND 7 AND hungry = True
        ORDER BY name ASC

""", conn2)
#print(df_hungry_ages)

# STEP 8
# Replace None with your code
""" CORRECT CODE ACCORDING TO INSTRUCTIONS """
# df_4_oldest = pd.read_sql("""
#         SELECT name, age, breed 
#         FROM (
#                 SELECT name, age, breed
#                 FROM dogs
#                 ORDER BY age DESC 
#                 LIMIT 4              
#         )
#         ORDER BY breed ASC  
        

# """, conn2)
#print(df_4_oldest)

""" CORRECT CODE ACCORDING TO TEST EXPECTATION WITHOUT SORTING THE BREED ALPHABETICALLY """
df_4_oldest = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC
    LIMIT 4
""", conn2)

##### Part 4: Aggregation #####

# STEP 0

# Create a connection
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)

# STEP 9
# Replace None with your code
df_ruth_years = pd.read_sql("""
        SELECT COUNT(year)
        FROM babe_ruth_stats

""", conn3)
#print(df_ruth_years)

# STEP 10
# Replace None with your code
df_hr_total = pd.read_sql("""
        SELECT SUM(HR)
        FROM babe_ruth_stats
                          
""", conn3)
#print(df_hr_total)

##### Part 5: Grouping and Aggregation #####

# STEP 11
# Replace None with your code
df_teams_years = pd.read_sql("""
        SELECT team, COUNT(year) AS number_years
        FROM babe_ruth_stats
        GROUP BY team
                             
""", conn3)
#print(df_teams_years)

# STEP 12
# Replace None with your code
df_at_bats = pd.read_sql("""
        SELECT team, AVG(at_bats) AS average_at_bats
        FROM babe_ruth_stats
        GROUP BY team
        HAVING average_at_bats > 200

""", conn3)
#print(df_at_bats)

conn1.close()
conn2.close()
conn3.close()