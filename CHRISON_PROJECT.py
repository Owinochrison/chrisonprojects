#LESSON ONE
name = "CHRISON"
print("HELLO")
print(name)
print(type(name))
print(type(36))
print(type(98.98))
print(type(True))
age = 24
print("I am", age)
salary = 124000
print(f"My name is {name}. I am {age} years old. I earn KES {salary} per momth")

#LESSON TWO

#VARIABLES  
steps = 12900
water_intake = 8
fasting = True
work_out = False
name = "CHRISON"

print ("My name is", name)
print ("I am fasting today", fasting)
print ("I have walked", steps, "steps today.")
print ("I drank", water_intake, "glasses of water.")
print ("I have worked out today", work_out)
#long code using f-string
print(f"My name is {name}. I have walked {steps} steps today, I drank {water_intake} glasses of water. I am fasting today: {fasting}. I have worked out today: {work_out}")

#LESSON THREE

#USE OF OPERATORS
#ADDITION 
morning_steps = 7600
evening_steps = 2000
total_steps = morning_steps + evening_steps
print(f"Total steps: {total_steps}")

#calculate remaining steps to target of 10000 today
#SUBTRACTION
steps_remaining = 10000 - total_steps
print(f"Steps to reach today goal:{steps_remaining}")

#calculation of weekly target steps
#MULTIPLICATION
weekly_target = 10000 * 7
print(f"Weekly target steps: {weekly_target}")

#AVERAGE OF THE DAILY STEP TARGET
#DIVISION
daily_average_steps = (7000 // 7)#two division lines to avoid the answer being in float.
print(f"Daily average steps: {daily_average_steps}")

# How many full sets of 1000 steps?
full_thousands = total_steps // 1000
print(f"Full thousands: {full_thousands}")

# Power: how many steps in 2 weeks squared?
print(f"10000 to the power of 2: {10000 ** 2}")


bench_press_sets = 3
reps_per_set = 10
weight_per_rep_kg = 50
total_reps = bench_press_sets * reps_per_set
total_volume_kg = total_reps * weight_per_rep_kg
reps_per_minute = total_reps // 4   # assume 4 minutes of work time

print("=== BENCH PRESS SESSION ===")
print(f"Sets: {bench_press_sets}")
print(f"Reps per set: {reps_per_set}")
print(f"Total reps: {total_reps}")
print(f"Weight per rep: {weight_per_rep_kg} kg")
print(f"Total volume lifted: {total_volume_kg} kg")
print(f"Reps per minute: {reps_per_minute}")

#COMPARIZON OPERATOR
steps = 9200
water_glasses = 6
sleep_hours = 7
fasting = "OMAD"

print(steps >= 8000)          # Did I hit my step target?
print(water_glasses == 8)     # Did I drink exactly 8 glasses?
print(sleep_hours < 6)        # Did I sleep under 6 hours?
print(fasting != "None")      # Am I on a fasting protocol?
print(steps > 10000)          # Did I exceed 10,000 steps?

#Joining text with +
first_name = name
greeting = "Welcome, " + first_name + "."
print(greeting)

#LESSON FOUR
#conditional logic
#three conditions ; if, else, elif

#use of if
steps = 1000
if steps >=10000:
    print("Steps target hit.")
print("Daily check complete")
#use of else
steps = 70600
if steps >= 10000:
    print("Target hit. Well done")
else:
    print(f"Target missed. You need {10000 - steps} more steps.")

steps = 5678
if steps >= 10000:
    print("Excellent. 10,000 steps exceeded.")
elif steps >= 9000:
    print(f"On target. {steps} steps hit.")
elif steps >= 6000:
    print("Halfway. Below target but moving.")
else: print("sedentary.")

#use of "and", "or"
steps = 9200
water_glasses = 9
cold_shower = True
sleep_hours = 7

if steps >= 10000 and water_glasses >= 8:
    print("Steps and water: both on target.")
else:
    print("Steps or water below target.")

if sleep_hours >= 7 and cold_shower:
    print("Sleep and cold shower: both done.")
else:
    print("Sleep or cold shower missed.")

#nested if
workout_done = False
weight_lifted_kg = 7000
personal_best_kg = 5000

if workout_done:
    print("Workout logged.")
    if weight_lifted_kg > personal_best_kg:
        print("New personal best! Previous:", personal_best_kg, "kg")
        print("New record:", weight_lifted_kg, "kg")
    else:
        print("Solid session. No new record today.")
else:
    print("Rest day. No workout logged.")

#USING IMPORT FUNCTION
from ast import Import
import math
steps = 15000
target = 10000

progress_pctg = (steps / target)* 100
rounded = math.floor(progress_pctg)

print("Steps today:", steps)
print("progress ",rounded,"%")

if progress_pctg >= 100:
    print("Target hit.")
elif progress_pctg >=80:
    print("Close. Push the last", target - steps, "steps.")
else:
    print("Still",target - steps ,"steps to go.")

#LESSON FIVE
#Conditional Logic
#use of for, while, break, continue, pass statements.

for day in range(5):
    print("Keep moving!")
for month in range(1, 31):
    print("Month", month, "- Step goal: 8,000 steps")

glasses = 0
while glasses < 8:
    glasses = glasses + 1
    print("Glass", glasses, "done.")

#WEEK TWO LESSON ONE
#Lists Storing Multiple Values
#Square brackets [] are used to create a list. Each item is separated by a comma.
daily_steps = [8200, 5100, 11300, 6800, 9400, 4200, 10100]
print(daily_steps)
daily_habits = ["8 glasses water", "8000 steps", "cold shower", "OMAD fast", "workout"]
print(daily_habits)
print("First habit:", daily_habits[0])
print("Last habit:", daily_habits[-1])
print("Total habits:", len(daily_habits))
length = len(daily_steps)
print("Total days logged:", length)

#Looping Through a List
daily_habits = ["8 glasses water", "8000 steps", "cold shower", "OMAD fast", "workout"]
for habit in daily_habits:
    print("Habit:", habit)  

#Combine the loop with a condition to make decisions about each item:
weekly_steps = [8200, 5100, 11300, 6800, 9400, 4200, 10100]
for steps in weekly_steps:
    if steps >= 10000:
        print(steps, "steps - Target hit!")
    elif steps >= 8000:
        print(steps, "steps - Close to target.")
    else:
        print(steps, "steps - Below target.")

#Checking If a Value Is in a List
skills_learned = ["welding", "tiling", "copywriting", "phone repair"]
if "welding" in skills_learned:
    print("Welding is in the list of skills learned.")
if "plumbing" not in skills_learned:
    print("Plumbing is not in the list of skills learned. Please consider learning it.")

#   Changing an Item in a List
fasting_protocols = ["OMAD", "2MAD", "16:8", "Autophagy Marathon"]
print("Before:", fasting_protocols)

# Update the fourth item (index 3)
fasting_protocols[3] = "Extended 72hr"
print("After:", fasting_protocols)

#EXERCISE 
#Write a loop that prints each count and says whether you hit 8,000 steps. After the loop, print the total number of days tracked using len().
week_steps = [9200, 7400, 10500, 8800, 6900, 11000, 9600]
for steps in week_steps:
    if steps >= 8000:
        print(f"{steps} steps - Target hit!")
    else:
        print(f"{steps} steps - Below target.")
print(f"Total days tracked: {len(week_steps)}")

#===LESSON TWO: LIST METHODS===
#Adding and Removing Items
fasting_protocols.append("5:2")
print("Updated fasting protocols:", fasting_protocols)
fasting_protocols.insert(2, "Alternate Day Fasting")
print("After inserting at index 2:", fasting_protocols)
fasting_protocols.remove("2MAD")
print("After removing '2MAD':", fasting_protocols)
fasting_protocols.pop(1)  # Removes the item at index 1
print("After popping index 1:", fasting_protocols)
fasting_protocols.sort()
print("Sorted fasting protocols:", fasting_protocols)
fasting_protocols.reverse()
print("Reversed fasting protocols:", fasting_protocols)
index = fasting_protocols.index("16:8")  # Returns the index of "16:8"
print(index)
count = fasting_protocols.count("OMAD")  # Counts occurrences of "OMAD"
print(count)

habits = ["8 glasses water", "cold shower", "OMAD fast", "workout", "cold shower"]
print("Before:", habits)    
habits.remove("cold shower")  # Removes only the first one
print("After:", habits)
weekly_steps = [9200, 10500, 8800, 11000, 7600]
print("Before:", weekly_steps)

removed = weekly_steps.pop()   # Removes last item
print("Removed:", removed)
print("After:", weekly_steps)

removed2 = weekly_steps.pop(1) # Removes item at index 1
print("Removed:", removed2)
print("After:", weekly_steps)

skills = ["welding", "tiling", "upholstery", "phone repair"]
skills.reverse()
print(skills)

habits = ["8 glasses water", "cold shower", "OMAD fast", "workout"]
position = habits.index("OMAD fast")
print("OMAD fast is at position:", position)

daily_results = ["hit", "miss", "hit", "hit", "miss", "hit", "hit"]
hit_count = daily_results.count("hit")
miss_count = daily_results.count("miss")
print("Days goal hit:", hit_count)
print("Days missed:", miss_count)

#===WEEK TWO: LESSON THREE===
#Dictionaries: Labelled Data Storage
daily_log = {
    "steps" : 9200,
    "water_glases" : 7,
    "cold_shower" : True,
    "fasting_protocol" : "AUTOPHAGY",
    "sleep_hours" : 8,
}
print(daily_log)
#printing value in a dictionary.
print("Steps today: ", daily_log["steps"])
print("Fasting protocol: ",daily_log["fasting_protocol"] )
print("Cold shower: ", daily_log["cold_shower"])
#Adding and Updating Values 
#add a new key
daily_log["Pages_read"] = 22
daily_log["Junk_food"] = "100/="
print("After adding pages read: ",daily_log)
#Update an existing key
daily_log["steps"] = 16900
print("After updating steps: ",daily_log)
#Deleting a Key
del daily_log["Junk_food"]
#print after deletion
print(daily_log)
#Checking If a Key Exists
if "steps" in daily_log:
    print("Steps recorded: ", daily_log["steps"])
if "sleep_hours" not in daily_log:
    print("Sleep_hours not logged yet.")

# Loop through keys and values together
for key, value in daily_log.items():
    print(key, ":", value)

# EXERCISE 
#Create a dictionary called my_log with at least five entries
my_log = {
    "steps" : 12300,
    "water_glasses" : 9,
    "fasting_protocol" : "AUTOPHAGY",
    "cold_shower" : True,
    "sleep_hours" : 8.0
}
#Then write a loop that prints every key and value.
for key, value in my_log.items():
    print(key, ":", value)
#After the loop, check if steps is greater than or equal to 15000 and print a message based on the result.
if my_log["steps"] >= 10000:
    print("Step goal reached,", my_log["steps"],"steps hit.")
else:
    print("Step goal missed")

#===WEEK TWO: LESSON FOUR===
#Nested Data and String Methods

week_log = [
    {"day": "Monday", "steps": 9200, "water_glasses": 7, "cold_shower": True, "fasting_protocol": "AUTOPHAGY", "sleep_hours": 8},
    {"day": "Tuesday", "steps": 10500, "water_glasses": 8, "cold_shower": False, "fasting_protocol": "OMAD", "sleep_hours": 7},
    {"day": "Wednesday", "steps": 8800, "water_glasses": 6, "cold_shower": True, "fasting_protocol": "16:8", "sleep_hours": 6},
    {"day": "Thursday", "steps": 11000, "water_glasses": 9, "cold_shower": True, "fasting_protocol": "AUTOPHAGY", "sleep_hours": 8},
    {"day": "Friday", "steps": 7600, "water_glasses": 5, "cold_shower": False, "fasting_protocol": "OMAD", "sleep_hours": 7}

]
print(week_log)
#Loop through the list of dictionaries and print each day's log.    
for day_log in week_log:
    print(f"Day: {day_log['day']}, Steps: {day_log['steps']}, Water Glasses: {day_log['water_glasses']}, Cold Shower: {day_log['cold_shower']}, Fasting Protocol: {day_log['fasting_protocol']}, Sleep Hours: {day_log['sleep_hours']}")

#Accessing Values Inside Nested Data
print("Day: ", week_log[0]["day"])  # Prints "Monday"
print("Steps: ", week_log[0]["steps"])  # Prints 8800
print("Fasting Protocol: ", week_log[0]["fasting_protocol"])  # Prints "AUTOPHAGY"
print("Thursday log: ", week_log[3])  # Prints the entire Thursday dictionary

#Looping Through a List of Dictionaries
for log in week_log:
    if log["steps"] >= 10000:
        print(f"{log['day']}: Target hit with {log['steps']} steps.")
    else:
        print(f"{log['day']}: Below target with {log['steps']} steps.")
for log in week_log:
    status = "Goal hit" if log["steps"] >= 8000 else "Below goal"
    print(log["day"], "-", log["steps"], "steps -", status)

#WEEK THREE: LESSON ONE
#Introduction to Functions
def show_daily_log():
    print("Step goal: 10,000 steps")
    print("Water goal: 8 glasses")
    print("Fasting protocol: OMAD")
    print("Cold shower: Yes")
#call the function
show_daily_log()
print("=== DAILY LOG ===")
show_daily_log()

def check_steps(steps):
    if steps >= 10000:
        print(steps, "steps - Goal exceeded")
    elif steps >= 8000:
        print(steps, "steps - Goal hit")
    else:
        print(steps, "steps - Below goal")

# Call with different values
check_steps(9200)
check_steps(7500)
check_steps(11000)
check_steps(6800)

def log_day(day, steps, protocol):
    print(f"{day}: {steps} steps | Protocol: {protocol}")

log_day("Monday", 9200, "OMAD")
log_day("Tuesday", 10500, "2MAD")
log_day("Wednesday", 8800, "Autophagy Marathon")

#a function to calculate the avg steps
#return
def calculate_avg_steps(steps_list):
    total = sum(steps_list)
    avg = total / len(steps_list)
    return avg

weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
avg = calculate_avg_steps(weekly_steps)
print("Average steps this week:", avg)

def get_status(steps):
    if steps >= 10000:
        print("Exceeded")
    elif steps >= 8000:
        print("Hit")
    else:
        print("Missed")
    return(steps)

get_status(9200)
get_status(7500)
get_status(6800)
get_status(12000)

#Exercise
#Write a function called day_report(steps, water, protocol) that prints a formatted report of a day's discipline data
def day_report(steps, water, protocol):
    print("=== DAILY REPORT ===")
    print(f"Steps: {steps}")
    print(f"Water intake: {water} glasses")
    print(f"Fasting protocol: {protocol}")
    print()
def hit_goal(steps):
    return steps >= 8000
day_report(9200, 8, "OMAD")
day_report(7500, 6, "16:8")
day_report(11000, 9, "Autophagy Marathon")

print("Goal hit (9200)?", hit_goal(9200))
print("Goal hit (7500)?", hit_goal(7500))

#Default Parameters, Scope, and Docstrings
def check_steps(steps, goal=8000):
    #Check if the steps meet or exceed the target.
    if steps >= goal:
        print(f"{steps} steps - Goal hit!")
    else:
        print(f"{steps} steps - Below goal.")
check_steps(9200)  # Uses default goal of 8000
check_steps(7500)  # Uses default goal of 8000

# Override the default goal
check_steps(9200, goal=10000)
check_steps(11500, goal=10000)

#Multiple default parameters
def log_day(steps, water=8, protocol="OMAD"):
    print(f"Steps: {steps} | Water: {water} glasses | Protocol: {protocol}")

log_day(9200)                        # Uses both defaults
log_day(10500, water=9)              # Override water only
log_day(8800, water=7, protocol="2MAD")  # Override both


def client_report(name, goal, sessions=4, bench_kg=60):
    print(f"{name} | Goal: {goal} | Sessions/week: {sessions} | Bench: {bench_kg}kg")

# Positional arguments
client_report("James", "fat loss")

# Keyword arguments: order does not matter
client_report(goal="muscle gain", name="Mwangi", bench_kg=100)

# Mix of positional and keyword
client_report("Sandra", "endurance", bench_kg=50)


# Global variable
step_goal = 8000  # Global variable

def check_today(steps):
    result = "hit" if steps >= step_goal else "missed"  # result is local
    print(f"Goal {result}: {steps} steps")

check_today(9200)
check_today(7000)

# This would cause an error - result does not exist here:
# print(result)

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi <30:
        return "Overweight"
    else:
        return "Obese"

weight = 69
height = 1.82

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Weight: {weight}kg | Height: {height}m")
print(f"BMI: {bmi} | Category: {category}")

#Modules and Importing
#MATH, RANDOM, DATETIME
#The math Module
import math
#2 POWER 10
print("2 to the power of 10:", math.pow(2,10) )
# Square root
print("Square root of 144:", math.sqrt(144))
# Round down and round up
print("Floor of 7.9:", math.floor(7.9))
print("Ceiling of 7.1:", math.ceil(7.1))
# Pi
print("Pi:", math.pi)

import math

total_days = 50
training_days_per_week = 5
weeks = total_days / 7

print(f"Total days: {total_days}")
print(f"Full weeks: {math.floor(weeks)}")

# Distance calculation using Pythagoras
walk_east = 3.0   # km
walk_north = 4.0  # km
distance = math.sqrt(walk_east**2 + walk_north**2)
print(f"Direct distance: {distance} km")

import random

# Random integer between 1 and 10 (inclusive)
for i in range(5):
    print("Random number:", random.randint(1, 10))

# Random float between 0 and 1
print("Random float:", random.random())

# Random choice from a list
skills = ["welding", "tiling", "upholstery", "phone repair", "copywriting"]
print("Today's skill focus:", random.choice(skills))

# Shuffle a list
random.shuffle(skills)
print("Shuffled:", skills)

import random

print("Simulated step counts for this week:")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day in days:
    steps = random.randint(5000, 13000)
    status = "OK" if steps >= 8000 else "low"
    print(f"  {day}: {steps} steps ({status})")

#The datetime Module
from datetime import datetime, date

# Today's date and time
now = datetime.now()
print("Current datetime:", now)

# Just the date
today = date.today()
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# Days between two dates
start = date(2025, 1, 1)
end = date(2025, 12, 31)
delta = end - start
print("Days in 2025:", delta.days)

#Importing Specific Functions
from math import sqrt, floor, ceil
from random import randint, choice

# No need to write math.sqrt() or random.randint()
print("Square root of 225:", sqrt(225))
print("Floor of 9.7:", floor(9.7))

protocols = ["OMAD", "2MAD", "Autophagy Marathon"]
print("Today's protocol:", choice(protocols))
print("Random step bonus:", randint(100, 500), "steps")

#Exercise
import random
import math

def generate_week():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    total = 0
    goal_days = 0

    for day in days:
        steps = random.randint(6000, 12000)
        total += steps
        if steps >= 8000:
            goal_days += 1
        print(f"  {day}: {steps} steps")

    avg = math.floor(total / 7)
    print(f"\nAverage steps : {avg}")
    print(f"Days on goal  : {goal_days}/7")

generate_week()

#The Problem: Building Lists with Loops
weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

goal_days = []
for steps in weekly_steps:
    if steps >= 8000:
        goal_days.append(steps)

print(goal_days)

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

goal_days = [steps for steps in weekly_steps if steps >= 8000]

print(goal_days)

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

# Convert each step count to km/calories
calories = [round(s * 0.04, 2) for s in weekly_steps]
print("Steps:", weekly_steps)
print("Calories  :", calories)

clients = [
    {"name": "James",   "goal": "fat loss",    "sessions": 4},
    {"name": "Mwangi",  "goal": "muscle gain", "sessions": 5},
    {"name": "Sandra",  "goal": "endurance",   "sessions": 3},
    {"name": "Patrick", "goal": "fat loss",    "sessions": 4},
    {"name": "Grace",   "goal": "fat loss",    "sessions": 3},
]

# Get names of all fat loss clients
fat_loss_names = [c["name"] for c in clients if c["goal"] == "fat loss"]
print("Fat loss clients:", fat_loss_names)

# Get all clients with 4 or more sessions per week
active_clients = [c for c in clients if c["sessions"] >= 4]
print("Active clients:", [c["name"] for c in active_clients])

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

# Build a list of status strings for each day
statuses = ["Goal hit" if s >= 8000 else "Below goal" for s in weekly_steps]

for i, status in enumerate(statuses):
    print(f"Day {i+1}: {weekly_steps[i]} steps - {status}")

people = [
    {"name": "James",   "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200]},
    {"name": "Sandra",  "steps": [7000, 7500, 6800, 8000, 7200, 8500, 7800]},
    {"name": "Mwangi",  "steps": [10000, 11500, 9800, 12000, 10500, 11000, 10800]},
    {"name": "Patrick", "steps": [8500, 9000, 8800, 9200, 8600, 9400, 9100]},
]

# 1. All step counts above 10,000 across all people
all_steps = [s for p in people for s in p["steps"]]
high_steps = [s for s in all_steps if s > 10000]
print("Steps above 10,000:", high_steps)

# 2. Names with average steps above 9,000
high_avg_names = [p["name"] for p in people if sum(p["steps"]) / len(p["steps"]) > 9000]
print("High average performers:", high_avg_names)

#Week 3 Gate: Functions and Modules
#Simulate writing a file.
import io

# Simulating file write using in-memory buffer
file_content = io.StringIO()
file_content.write("Steps: 9200\n")
file_content.write("Water: 8 glasses\n")
file_content.write("Protocol: OMAD\n")
file_content.write("Cold shower: Yes\n")

print("File written. Contents:")
print(file_content.getvalue())

import io

# Simulate file content
file_data = """Steps: 9200
Water: 8 glasses
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
"""

# Simulate reading the whole file
f = io.StringIO(file_data)
content = f.read()
print("Full file content:")
print(content)

#Reading Line by Line
import io

file_date = """Steps:9900
water : 8 glasses
protoco: OMAD 
Cold shower: YES
Sleep hours :7.5 hours
"""
f = io.StringIO(file_data)
lines = f.readlines()

print(f"Number of lines: {len(lines)}")
print()
for line in lines:
    line = line.strip() #remove new lines at the end.
    print("Line", line)

import io

# Simulated file: one line per day with step count
weekly_data = """Monday: 9200
Tuesday: 7500
Wednesday: 10500
Thursday: 8800
Friday: 6900
Saturday: 11000
Sunday: 9600
"""

goal = 8000
days_on_goal = 0

f = io.StringIO(weekly_data)
for line in f:
    line = line.strip()
    if ":" in line:
        day, steps_str = line.split(":", 1)
        steps = int(steps_str.strip())
        status = "Goal hit" if steps >= goal else "Below goal"
        print(f"{day}: {steps} steps - {status}")
        if steps >= goal:
            days_on_goal += 1

print(f"\nDays on goal: {days_on_goal}/7")

import io

# Daily egg collection log: pen, eggs_collected, feed_kg
farm_log = """Pen A,240,12
Pen B,185,10
Pen C,310,15
Pen D,92,8
Pen E,275,13
"""

total_eggs = 0
total_feed = 0
low_pens = []

f = io.StringIO(farm_log)
for line in f:
    line = line.strip()
    if line:
        pen, eggs, feed = line.split(",")
        eggs = int(eggs)
        feed = int(feed)
        efficiency = eggs / feed
        status = "Good" if eggs >= 200 else "Low yield"
        print(f"{pen}: {eggs} eggs | {feed}kg feed | {efficiency:.1f} eggs/kg [{status}]")
        total_eggs += eggs
        total_feed += feed
        if eggs < 200:
            low_pens.append(pen)

print(f"\nTotal eggs: {total_eggs}")
print(f"Total feed used: {total_feed}kg")
print(f"Pens needing attention: {', '.join(low_pens)}")

#WEEK 4: LESSON ONE
#Error Handling
#An unhandled error
# This will crash
# This will crash
steps = "9000"
goal = 8000
steps_int = int(steps)  # This will raise a ValueError
if steps_int     >= goal:  # Can't compare string to number
    print("Goal hit")

#try and except
steps_data = ["9200", "7500", "ten thousand", "8800", "6900"]

for item in steps_data:
    try:
        steps = int(item)
        if steps >= 8000:
            print(steps, "- Goal hit")
        else:
            print(steps, "- Below goal")
    except ValueError:
        print(f"'{item}' is not a valid number. Skipping.")

#exceptions can be handled with try-except blocks. This allows the program to continue running even if an error occurs, instead of crashing. 
#Multiple except Blocks
def calculate_average(steps_list):
    try:
        total = sum(steps_list)
        avg = total / len(steps_list)
        return round(avg)
    except ZeroDivisionError:
        print("Error: List is empty. Cannot calculate average.")
        return 0
    except TypeError:
        print("Error: List contains non-numeric values.")
        return 0

print("Average:", calculate_average([9200, 10500, 8800, 11000]))
print("Average:", calculate_average([]))
print("Average:", calculate_average([9200, "eight thousand", 10500]))

#else and finally
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print("Execution of safe_divide complete.") 
safe_divide(100, 4)
safe_divide(100, 0)
safe_divide(9200, 7)

#Raising Your Own Errors
def log_steps(steps):
    if not isinstance(steps, int):
        raise TypeError("Steps must be an integer.")
    if steps < 0:
        raise ValueError("Steps cannot be negative.")
    print(f"Steps logged: {steps}")

try:
    log_steps(9200)
    log_steps(-500)
    log_steps("nine thousand")
except ValueError as e:
    print("ValueError:", e)
except TypeError as e:
    print("TypeError:", e)

#Error Handling With Data Processing
daily_logs = [
    {"day": "Monday",    "steps": "9200"},
    {"day": "Tuesday",   "steps": "not recorded"},
    {"day": "Wednesday", "steps": "10500"},
    {"day": "Thursday",  "steps": None},
    {"day": "Friday",    "steps": "8800"},
]

valid_steps = []
for log in daily_logs:
    try:
        steps = int(log["steps"])
        valid_steps.append(steps)
        print(f"{log['day']}: {steps} steps")
    except (ValueError, TypeError):
        print(f"{log['day']}: invalid data - skipped")

if valid_steps:
    avg = sum(valid_steps) / len(valid_steps)
    print(f"\nAverage from valid days: {round(avg)} steps")

#EXCERCISE
def safe_log_entry(data):
    try:
        steps = int(data["steps"])
    except (ValueError, TypeError, KeyError):
        print("Invalid steps data. Skipping entry.")
        return None

    water    = data.get("water", 0)
    protocol = data.get("protocol", "Unknown")

    print(f"Steps: {steps} | Water: {water} glasses | Protocol: {protocol}")
    return steps

entries = [
    {"steps": "9200", "water": 8,   "protocol": "OMAD"},
    {"steps": "bad",  "water": 7,   "protocol": "2MAD"},
    {"steps": "8800", "protocol": "OMAD"},
    {"steps": "11000","water": 9},
]

results = [safe_log_entry(e) for e in entries]
valid = [r for r in results if r is not None]
print(f"\nValid entries: {len(valid)}")

#OR

def safe_log_entry(data):
    # Try to extract steps
    try:
        steps = int(data.get("steps"))
    except (ValueError, TypeError, KeyError):
        print("Error: 'steps' must be a valid integer.")
        return None

    # Handle missing water (default 0)
    water = data.get("water", 0)

    # Handle missing protocol (default "Unknown")
    protocol = data.get("protocol", "Unknown")

    # Print a clean report

    print(f"  Steps   : {steps} | Water: {water} ml | Protocol: {protocol}")


    return {"steps": steps, "water": water, "protocol": protocol}
# Valid entry
entry1 = {"steps": "9200", "water": 1500, "protocol": "Morning Walk"}
safe_log_entry(entry1)

# Missing water and protocol
entry2 = {"steps": "8500"}
safe_log_entry(entry2)

# Invalid steps
entry3 = {"steps": "nine thousand", "water": 1200}
safe_log_entry(entry3)


#WEEK 4: LESSON 3
#Working with JSON
import json

daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5
}

# Convert to JSON string
json_text = json.dumps(daily_log)
print("Type:", type(json_text))
print("JSON:", json_text)

# Pretty print with indentation
pretty = json.dumps(daily_log, indent=2)
print("\nPretty JSON:")
print(pretty)


#JSON TO PYTHON
import json

# This is what an API response might look like
api_response = '{"steps": 9200, "water_glasses": 8, "cold_shower": true, "protocol": "OMAD"}'

# Convert JSON string to Python dictionary
data = json.loads(api_response)

print("Type:", type(data))
print("Steps:", data["steps"])
print("Cold shower:", data["cold_shower"])
print("Protocol:", data["protocol"])

#READING AND WRITING FILES IN JSON
#Simulate File Read and Write
import json

# Simulate writing
daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "protocol": "OMAD",
    "cold_shower": True,
    "sleep_hours": 7.5
}
json_string = json.dumps(daily_log, indent=2)
print("Saved JSON:")
print(json_string)

# Simulate reading it back
loaded_data = json.loads(json_string)
print("\nRead back as Python dict:")
for key, value in loaded_data.items():
    print(f"  {key}: {value}")


#Navigating Nested JSON
#Try It: Nested JSON
import json

# Simulated API response with nested data
api_json = '''
{
  "client": "James Omondi",
  "week": 1,
  "daily_logs": [
    {"day": "Monday",    "steps": 9200,  "protocol": "OMAD"},
    {"day": "Tuesday",   "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800,  "protocol": "OMAD"},
    {"day": "Thursday",  "steps": 11000, "protocol": "Autophagy Marathon"},
    {"day": "Friday",    "steps": 7600,  "protocol": "OMAD"},
    {"day": "Saturday",  "steps": 5400,  "protocol": "2MAD"}
  ]
}
'''

data = json.loads(api_json)

print("Client:", data["client"])
print("Week:", data["week"])
print()

for log in data["daily_logs"]:
    status = "OK" if log["steps"] >= 8000 else "low"
    print(f"  {log['day']}: {log['steps']} steps ({status})")

import json

responses = [
    '{"steps": 9200, "protocol": "OMAD"}',
    'not valid json at all',
    '{"steps": 10500, "protocol": "2MAD"}'
]

for r in responses:
    try:
        data = json.loads(r)
        print(f"Parsed OK: {data['steps']} steps")
    except json.JSONDecodeError:
        print(f"Invalid JSON: {r[:30]}...")

#EXCERCISE
import json

week_report = {
    "name": "James",
    "steps": [9200, 10500, 8800, 11000, 7600],
    "protocols": ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD"]
}

# Convert to JSON
json_str = json.dumps(week_report, indent=2)
print("JSON output:")
print(json_str)

# Load back and calculate average
loaded = json.loads(json_str)
avg = sum(loaded["steps"]) / len(loaded["steps"])
print(f"\nAverage steps for {loaded['name']}: {round(avg)}")

#WEEK 4: LESSON 4
#Working with CSV Files
import csv
import io
# Simulated CSV content
csv_data = """name,phone,skill,city
James Omondi,0712345678,welding,Nairobi
Sandra Weru,0723456789,tiling,Mombasa
Patrick Njiru,0734567890,phone repair,Nairobi
Grace Achieng,0745678901,copywriting,Kisumu
Brian Kamau,0756789012,upholstery,Nairobi"""

f = io.StringIO(csv_data)
reader = csv.reader(f)

for row in reader:
    print(row)

#Try It: Skip the Header
import csv
import io   
csv_data = """name,phone,skill,city
James Omondi,0712345678,welding,Nairobi
Sandra Weru,0723456789,tiling,Mombasa
Patrick Njiru,0734567890,phone repair,Nairobi"""

f = io.StringIO(csv_data)
reader = csv.reader(f)
next(reader)  # Skip header row

for row in reader:
    name, phone, skill, city = row
    print(f"{name} | {skill} | {city}")

#Reading with DictReader
f = io.StringIO(csv_data)
reader = csv.DictReader(f)
next(reader)  # Skip header row

for row in reader:
    print(f"{row['name']} | {row['skill']} | {row['city']}")  

#OR 
import csv
import io

csv_data = """name,steps,water,protocol,cold_shower
James Omondi,9200,8,OMAD,True
Sandra Weru,10500,9,2MAD,True
Patrick Njiru,7600,6,OMAD,False
Grace Achieng,11000,8,Autophagy Marathon,True"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

for row in reader:
    steps = int(row["steps"])
    status = "Goal hit" if steps >= 8000 else "Below goal"
    print(f"{row['name']}: {steps} steps | {row['protocol']} | {status}")


#Writing CSV with csv.writer
import csv
import io   

output = io.StringIO()
writer = csv.writer(output)

# Write header
writer.writerow(["name", "steps", "protocol", "goal_hit"])

# Write data rows
data = [
    ["James",   9200,  "OMAD",              True],
    ["Sandra",  10500, "2MAD",              True],
    ["Patrick", 7600,  "OMAD",              False],
    ["Grace",   11000, "Autophagy Marathon", True],
]

for row in data:
    writer.writerow(row)

print("Generated CSV:")
print(output.getvalue())

#Writing with DictWriter
import csv
import io

clients = [
    {"name": "James",   "skill": "welding",      "city": "Nairobi",  "sessions": 4},
    {"name": "Sandra",  "skill": "tiling",        "city": "Mombasa",  "sessions": 3},
    {"name": "Patrick", "skill": "phone repair",  "city": "Nairobi",  "sessions": 4},
    {"name": "Grace",   "skill": "copywriting",   "city": "Kisumu",   "sessions": 2},
]

output = io.StringIO()
fieldnames = ["name", "skill", "city", "sessions"]
writer = csv.DictWriter(output, fieldnames=fieldnames)

writer.writeheader()
writer.writerows(clients)

print(output.getvalue())

#Exercise: Reading and Processing CSV Data using DictReader

import csv
import io

csv_data = """day,steps,protocol
Monday,9200,OMAD
Tuesday,7500,2MAD
Wednesday,10500,OMAD
Thursday,4200,OMAD
Friday,8800,Autophagy Marathon
Saturday,11000,2MAD
Sunday,9600,OMAD"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

valid_steps = []
for row in reader:
    steps = int(row["steps"])
    if steps >= 7000:
        valid_steps.append(steps)
        print(f"{row['day']}: {steps} steps ({row['protocol']})")
    else:
        print(f"{row['day']}: {steps} steps - flagged as invalid")

avg = sum(valid_steps) / len(valid_steps)
print(f"\nAverage (valid days): {round(avg)} steps")

#Crop Harvest: CSV Reader
import csv
import io

crop_data = """crop,quantity,price
wheat,1000,5.00
corn,800,3.50
soybeans,600,4.25"""

f = io.StringIO(crop_data)
reader = csv.DictReader(f)

for row in reader:
    crop = row["crop"]
    quantity = int(row["quantity"])
    price = float(row["price"])
    total_value = quantity * price
    print(f"{crop}: {quantity} units at ${price:.2f} each = ${total_value:.2f}")

#OR
import csv, io

harvest_csv = """field,crop,bags_harvested,target_bags
North Plot,Maize,48,50
South Plot,Beans,22,30
East Plot,Wheat,61,55
West Plot,Maize,35,50
Centre Plot,Sorghum,44,40
"""

reader = csv.DictReader(io.StringIO(harvest_csv))

print(f"{'Field':<15} {'Crop':<10} {'Harvested':>10} {'Target':>8} {'Status':>12}")
print("-" * 58)

for row in reader:
    harvested = int(row["bags_harvested"])
    target = int(row["target_bags"])
    pct = (harvested / target) * 100
    status = "On target" if harvested >= target else f"Short by {target - harvested} bags"
    print(f"{row['field']:<15} {row['crop']:<10} {harvested:>10} {target:>8} {status:>12}")


#Step 4: Full Grade Tracker

import csv
import io
import json

csv_data = """name,score1,score2,score3
James Omondi,85,90,78
Sandra Weru,72,,88
Patrick Njiru,91,87,94
Grace Achieng,60,bad data,70
Brian Kamau,55,48,62"""

# Functions
def parse_score(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def calculate_average(scores):
    valid = [s for s in scores if s is not None]
    if not valid:
        return None
    return round(sum(valid) / len(valid), 1)

def letter_grade(avg):
    if avg is None: return "N/A"
    if avg >= 90:   return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else:           return "F"

# Process CSV
f = io.StringIO(csv_data)
reader = csv.DictReader(f)
results = []

print("=" * 50)
print(f"{'NAME':<20} {'AVG':>5}  {'GRADE':>5}  NOTES")
print("=" * 50)

for row in reader:
    scores = [
        parse_score(row["score1"]),
        parse_score(row["score2"]),
        parse_score(row["score3"])
    ]
    invalid_count = scores.count(None)
    avg = calculate_average(scores)
    grade = letter_grade(avg)
    notes = f"{invalid_count} invalid score(s)" if invalid_count else "All scores valid"

    print(f"{row['name']:<20} {str(avg):>5}  {grade:>5}  {notes}")

    results.append({
        "name": row["name"],
        "scores": [row["score1"], row["score2"], row["score3"]],
        "average": avg,
        "grade": grade
    })

print("=" * 50)

# Class summary
valid_avgs = [r["average"] for r in results if r["average"] is not None]
class_avg = round(sum(valid_avgs) / len(valid_avgs), 1)
print(f"\nClass average: {class_avg}")
print(f"Students: {len(results)}")

# Export as JSON
print("\nJSON export:")
print(json.dumps(results, indent=2))


#WEEK 5: LESSON ONE
#Week 4 Gate: Files, Errors and Data
#Working with a Simulated Response
# Simulates what response.json() returns from a fitness API
data = {
    "user_id": 1,
    "name": "James Omondi",
    "date": "2024-11-18",
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5,
    "workout_completed": True
}

print("Name:", data["name"])
print("Steps:", data["steps"])
print("Protocol:", data["fasting_protocol"])
print("Cold shower:", data["cold_shower"])
print("Sleep:", data["sleep_hours"], "hours")
print("User ID:", data["user_id"])


#Accessing Nested Data

data = {
    "user": {
        "id": 1,
        "name": "Sandra Weru",
        "city": "Nairobi"
    },
    "metrics": {
        "steps": 10500,
        "sleep_hours": 8.0,
        "bench_press_kg": 80
    },
    "skills": ["welding", "tiling", "copywriting"]
}

print(data["user"]["name"])
print(data["user"]["city"])
print(data["metrics"]["steps"])
print(data["metrics"]["bench_press_kg"], "kg bench press")
print("Skills:", data["skills"])
print("First skill:", data["skills"][0])

#Looping Through a List Response
for skill in data["skills"]:
    print("Skill:", skill)  

# Simulates: response.json() from /api/weekly-logs
weekly_logs = [
    {"day": "Monday",    "steps": 9200,  "protocol": "OMAD"},
    {"day": "Tuesday",   "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800,  "protocol": "OMAD"},
    {"day": "Thursday",  "steps": 11000, "protocol": "OMAD"},
    {"day": "Friday",    "steps": 7600,  "protocol": "2MAD"},
]

for log in weekly_logs:
    status = "Goal met" if log["steps"] >= 10000 else "Short"
    print(f"{log['day']:12} {log['steps']:6} steps  {status}")

#Using .get() for Missing Keys
records = [
    {"name": "Patrick Njiru", "steps": 9100, "water_glasses": 7},
    {"name": "Grace Achieng", "steps": 8400},           # no water logged
    {"name": "Brian Kamau",   "steps": 10200, "water_glasses": 9},
]

for r in records:
    water = r.get("water_glasses", "not logged")
    print(f"{r['name']}: steps={r['steps']}, water={water}")

#Filtering API Results
filtered_records = [r for r in records if r.get("water_glasses") is not None]
print("\nFiltered Records:")
for r in filtered_records:
    print(f"{r['name']}: steps={r['steps']}, water={r['water_glasses']}")   



#WEEK 5: DAY 2
#Parsing API Responses
#Navigate Nested Structure

response = {
    "status": "success",
    "user": {
        "id": 42,
        "name": "Kevin Mwangi",
        "location": {
            "city": "Kisumu",
            "country": "Kenya"
        }
    },
    "today": {
        "steps": 10800,
        "cold_shower": True,
        "fasting": {
            "protocol": "OMAD",
            "window_hours": 23
        },
        "workout": {
            "completed": True,
            "bench_press_kg": 90,
            "duration_minutes": 55
        }
    }
}

# Navigate layer by layer
name = response["user"]["name"]
city = response["user"]["location"]["city"]
steps = response["today"]["steps"]
protocol = response["today"]["fasting"]["protocol"]
bench = response["today"]["workout"]["bench_press_kg"]

print(f"Name:     {name}")
print(f"City:     {city}")
print(f"Steps:    {steps}")
print(f"Protocol: {protocol}")
print(f"Bench:    {bench} kg")


#Handle None Values

users = [
    {"name": "James Omondi",  "workout": {"bench_press_kg": 80, "duration_minutes": 45}},
    {"name": "Sandra Weru",   "workout": None},   # did not train today
    {"name": "Grace Achieng", "workout": {"bench_press_kg": 60, "duration_minutes": 40}},
]

for user in users:
    name = user["name"]
    workout = user["workout"]
    if workout is None:
        print(f"{name}: rest day")
    else:
        bench = workout.get("bench_press_kg", "not recorded")
        mins = workout.get("duration_minutes", "?")
        print(f"{name}: bench={bench}kg, duration={mins}min")

#Extracting Fields from a List of Records
# Raw API response: list of full user records
raw = [
    {"id": 1, "name": "James Omondi",  "email": "james@smp.ke", "steps": 9200,  "protocol": "OMAD", "sleep": 7.5, "active": True},
    {"id": 2, "name": "Sandra Weru",   "email": "sw@smp.ke",    "steps": 10500, "protocol": "2MAD", "sleep": 8.0, "active": True},
    {"id": 3, "name": "Patrick Njiru", "email": "pn@smp.ke",    "steps": 8100,  "protocol": "OMAD", "sleep": 6.5, "active": False},
    {"id": 4, "name": "Grace Achieng", "email": "ga@smp.ke",    "steps": 11000, "protocol": "OMAD", "sleep": 7.0, "active": True},
    {"id": 5, "name": "Brian Kamau",   "email": "bk@smp.ke",    "steps": 7400,  "protocol": "2MAD", "sleep": 9.0, "active": True},
]

# Extract only active users with name, steps, protocol
clean = [
    {
        "name": r["name"],
        "steps": r["steps"],
        "protocol": r["protocol"]
    }
    for r in raw if r["active"]
]

for record in clean:
    print(f"{record['name']:20} {record['steps']:6} steps  {record['protocol']}")

#Paginated Responses
#Paginated Response Structure
# What page 1 of a paginated API looks like
page_1 = {
    "page": 1,
    "total_pages": 3,
    "per_page": 3,
    "next_page": 2,
    "data": [
        {"name": "James Omondi",  "steps": 9200},
        {"name": "Sandra Weru",   "steps": 10500},
        {"name": "Patrick Njiru", "steps": 8100},
    ]
}

page_2 = {
    "page": 2,
    "total_pages": 3,
    "per_page": 3,
    "next_page": 3,
    "data": [
        {"name": "Grace Achieng", "steps": 11000},
        {"name": "Brian Kamau",   "steps": 7400},
        {"name": "Kevin Mwangi",  "steps": 10800},
    ]
}

# Combine pages manually
all_records = page_1["data"] + page_2["data"]
print(f"Total records collected: {len(all_records)}")
for r in all_records:
    print(f"  {r['name']}: {r['steps']} steps")

#Parse and Summarize
api_response = {
    "week": "2024-W47",
    "members": [
        {"name": "James Omondi",  "daily_steps": [9200, 10100, 8800, 11000, 9400, 10200, 8600]},
        {"name": "Sandra Weru",   "daily_steps": [10500, 9800, 10200, 11500, 9100, 10800, 10000]},
        {"name": "Patrick Njiru", "daily_steps": [8100, 7900, 8500, 9200, 8800, 7600, 9000]},
        {"name": "Grace Achieng", "daily_steps": [11000, 10800, 9900, 12000, 10500, 11200, 10300]},
    ]
}

print(f"Week: {api_response['week']}")
print("-" * 54)
print(f"{'Name':<20} {'Avg Steps':>10}  {'Days 10k+':>10} {'Best day':>10}")
print("-" * 54)

for member in api_response["members"]:
    steps = member["daily_steps"]
    avg = round(sum(steps) / len(steps))
    days_hit = sum(1 for s in steps if s >= 10000)
    best_day = max(steps)
    print(f"{member['name']:<20} {avg:>10,}  {days_hit:>10} {best_day:>10}")


#Combining Nested Data into One Clean Record
#Full Parse and Flatten
raw_members = [
    {
        "profile": {"name": "James Omondi", "city": "Nairobi"},
        "metrics": {"steps": 9200, "sleep_hours": 7.5, "bench_press_kg": 80},
        "discipline": {"cold_shower": True, "protocol": "OMAD"}
    },
    {
        "profile": {"name": "Grace Achieng", "city": "Mombasa"},
        "metrics": {"steps": 11000, "sleep_hours": 7.0, "bench_press_kg": 60},
        "discipline": {"cold_shower": False, "protocol": "OMAD"}
    },
    {
        "profile": {"name": "Brian Kamau", "city": "Kisumu"},
        "metrics": {"steps": 7400, "sleep_hours": 9.0, "bench_press_kg": 70},
        "discipline": {"cold_shower": True, "protocol": "2MAD"}
    },
]

# Flatten each nested record into one clean dict
flattened = []
for m in raw_members:
    record = {
        "name":       m["profile"]["name"],
        "city":       m["profile"]["city"],
        "steps":      m["metrics"]["steps"],
        "sleep":      m["metrics"]["sleep_hours"],
        "bench":      m["metrics"]["bench_press_kg"],
        "protocol":   m["discipline"]["protocol"],
        "cold_shower": m["discipline"]["cold_shower"],
    }
    flattened.append(record)

for r in flattened:
    shower = "yes" if r["cold_shower"] else "no"
    print(f"{r['name']}, {r['city']}: {r['steps']} steps, {r['protocol']}, shower={shower}")

#The Same Skill, Different Context: Farm Commodity Prices
#Parse a Commodity Price API Response
# Simulated response from a commodity prices API
commodity_response = {
    "status": "ok",
    "market": "Wakulima Market, Nairobi",
    "date": "2026-08-13",
    "prices": [
        {"commodity": "Maize",       "unit": "90kg bag", "price_kes": 3200, "change_pct": -2.1, "available": True},
        {"commodity": "Beans (Dry)", "unit": "90kg bag", "price_kes": 9800, "change_pct":  4.5, "available": True},
        {"commodity": "Milk (Raw)",  "unit": "litre",    "price_kes":   62, "change_pct":  1.2, "available": True},
        {"commodity": "Tea Leaf",    "unit": "kg",        "price_kes":   28, "change_pct": -0.8, "available": False},
        {"commodity": "Wheat Flour", "unit": "50kg bag", "price_kes": 2900, "change_pct":  0.0, "available": True},
    ]
}

market = commodity_response["market"]
date   = commodity_response["date"]
print(f"Market: {market}  |  Date: {date}")
print("-" * 55)
print(f"{'Commodity':<15} {'Unit':<12} {'Price (KES)':>12}  {'Change':>8}  Status")
print("-" * 55)

for item in commodity_response["prices"]:
    if not item["available"]:
        status = "OUT OF STOCK"
    elif item["change_pct"] > 0:
        status = "rising"
    elif item["change_pct"] < 0:
        status = "falling"
    else:
        status = "stable"
    change = f"{item['change_pct']:+.1f}%"
    print(f"{item['commodity']:<15} {item['unit']:<12} {item['price_kes']:>12,}  {change:>8}  {status}")

#WEEK FIVE DAY 4
#Building a Live Data Script
#The Four-Part Structure
#1. CONFIGURE
#2.FETCH
#3.PROCESS
#4.OUTPUT

#The Four-Part Structure
import os

# Configuration
BASE_URL = "https://api.smptracker.com/v1"
API_KEY = os.environ.get("SMP_API_KEY", "demo_key_123")
DEFAULT_CITY = "Nairobi"
STEP_GOAL = 10000
MAX_RESULTS = 50

print("Configuration loaded:")
print(f"  Base URL:   {BASE_URL}")
print(f"  API Key:    {API_KEY[:8]}...")
print(f"  City:       {DEFAULT_CITY}")
print(f"  Step Goal:  {STEP_GOAL:,}")
print(f"  Max Results:{MAX_RESULTS}")

#Part 2: Fetch Function
# Simulates what a fetch function does in a script

def fetch_members(city="Nairobi", limit=50):
    """
    Fetches member data from the SMP API.
    Returns a list of member dicts or raises RuntimeError.
    In production: uses requests.get() with headers and params.
    """
    # Simulate the API response
    mock_response_status = 200
    mock_data = [
        {"id": 1, "name": "James Omondi",  "city": "Nairobi",  "steps": 9200,  "protocol": "OMAD"},
        {"id": 2, "name": "Sandra Weru",   "city": "Nairobi",  "steps": 10500, "protocol": "2MAD"},
        {"id": 3, "name": "Patrick Njiru", "city": "Mombasa",  "steps": 8100,  "protocol": "OMAD"},
        {"id": 4, "name": "Grace Achieng", "city": "Nairobi",  "steps": 11000, "protocol": "OMAD"},
        {"id": 5, "name": "Brian Kamau",   "city": "Kisumu",   "steps": 7400,  "protocol": "2MAD"},
        {"id": 6, "name": "Kevin Mwangi",  "city": "Nairobi",  "steps": 10800, "protocol": "OMAD"},
    ]

    if mock_response_status != 200:
        raise RuntimeError(f"API error: status {mock_response_status}")

    # Filter by city
    filtered = [m for m in mock_data if m["city"] == city]
    return filtered[:limit]


# Call the function
members = fetch_members(city="Nairobi")
print(f"Fetched {len(members)} members from Nairobi")
for m in members:
    print(f"  {m['name']}: {m['steps']} steps")

#Part 3: Processing Function
def process_members(members, step_goal=10000):
    """
    Takes a list of raw member records.
    Returns a summary dict with stats and categorized members.
    """
    if not members:
        return {"error": "No members to process"}

    total = len(members)
    goal_met = [m for m in members if m["steps"] >= step_goal]
    goal_missed = [m for m in members if m["steps"] < step_goal]
    avg_steps = round(sum(m["steps"] for m in members) / total)
    top_performer = max(members, key=lambda m: m["steps"])

    return {
        "total_members": total,
        "goal_met_count": len(goal_met),
        "goal_missed_count": len(goal_missed),
        "average_steps": avg_steps,
        "top_performer": top_performer["name"],
        "top_steps": top_performer["steps"],
        "goal_met": [m["name"] for m in goal_met],
    }


# Test with sample data
raw_members = [
    {"name": "James Omondi",  "steps": 9200,  "protocol": "OMAD"},
    {"name": "Sandra Weru",   "steps": 10500, "protocol": "2MAD"},
    {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD"},
    {"name": "Brian Kamau",   "steps": 7400,  "protocol": "2MAD"},
    {"name": "Kevin Mwangi",  "steps": 10800, "protocol": "OMAD"},
]

summary = process_members(raw_members, step_goal=10000)
print("Processed summary:")
for key, value in summary.items():
    print(f"  {key}: {value}")

#Part 4: Output
import json

def print_report(summary, city="Nairobi"):
    print("=" * 48)
    print(f"  SMP MEMBER REPORT: {city.upper()}")
    print("=" * 48)
    print(f"  Total members:    {summary['total_members']}")
    print(f"  Hit step goal:    {summary['goal_met_count']}")
    print(f"  Missed goal:      {summary['goal_missed_count']}")
    print(f"  Average steps:    {summary['average_steps']:,}")
    print(f"  Top performer:    {summary['top_performer']} ({summary['top_steps']:,} steps)")
    print("-" * 48)
    print("  Members who hit goal:")
    for name in summary["goal_met"]:
        print(f"    {name}")
    print("=" * 48)


summary = {
    "total_members": 5,
    "goal_met_count": 3,
    "goal_missed_count": 2,
    "average_steps": 9780,
    "top_performer": "Grace Achieng",
    "top_steps": 11000,
    "goal_met": ["Sandra Weru", "Grace Achieng", "Kevin Mwangi"]
}

print_report(summary, city="Nairobi")

# Save to JSON
output = json.dumps(summary, indent=2)
print("\nJSON output saved:")
print(output)

#The Complete Script
import json
import os

# --- Configuration ---
BASE_URL = "https://api.smptracker.com/v1"
API_KEY = os.environ.get("SMP_API_KEY", "demo_key_123")
TARGET_CITY = "Busia"
STEP_GOAL = 10000

# --- Fetch ---
def fetch_members(city, limit=50):
    # Simulated API response
    all_members = [
        {"name": "James Omondi",  "city": "Busia",  "steps": 9200,  "protocol": "OMAD", "sleep": 7.5},
        {"name": "Sandra Weru",   "city": "Nairobi",  "steps": 10500, "protocol": "2MAD", "sleep": 8.0},
        {"name": "Patrick Njiru", "city": "Mombasa",  "steps": 8100,  "protocol": "OMAD", "sleep": 6.5},
        {"name": "Grace Achieng", "city": "Nairobi",  "steps": 11000, "protocol": "OMAD", "sleep": 7.0},
        {"name": "Brian Kamau",   "city": "Kisumu",   "steps": 7400,  "protocol": "2MAD", "sleep": 9.0},
        {"name": "Kevin Mwangi",  "city": "Nairobi",  "steps": 10800, "protocol": "OMAD", "sleep": 7.5},
        {"name": "Chrison Son",   "city": "Busia",    "steps": 12000, "protocol": "2MAD", "sleep": 8.0},
    ]
    return [m for m in all_members if m["city"] == city][:limit]

# --- Process ---
def process_members(members, step_goal):
    goal_met = [m for m in members if m["steps"] >= step_goal]
    avg_steps = round(sum(m["steps"] for m in members) / len(members)) if members else 0
    avg_sleep = round(sum(m["sleep"] for m in members) / len(members), 1) if members else 0
    top = max(members, key=lambda m: m["steps"]) if members else {}
    return {
        "total": len(members),
        "goal_met": len(goal_met),
        "avg_steps": avg_steps,
        "avg_sleep": avg_sleep,
        "top_name": top.get("name", "N/A"),
        "top_steps": top.get("steps", 0),
        "achievers": [m["name"] for m in goal_met]
    }

# --- Output ---
def print_report(city, summary):
    print(f"\n{'='*48}")
    print(f"  SMP DAILY REPORT: {city.upper()}")
    print(f"{'='*48}")
    print(f"  Members:       {summary['total']}")
    print(f"  Hit {STEP_GOAL:,} steps: {summary['goal_met']}")
    print(f"  Avg steps:     {summary['avg_steps']:,}")
    print(f"  Avg sleep:     {summary['avg_sleep']} hrs")
    print(f"  Top:           {summary['top_name']} ({summary['top_steps']:,})")
    print(f"\n  Achievers: {', '.join(summary['achievers'])}")
    print(f"{'='*48}\n")

# --- Main ---
members = fetch_members(TARGET_CITY)
summary = process_members(members, STEP_GOAL)
print_report(TARGET_CITY, summary)

#EXAMPLE 2 OF THE ABOVE.
#The Same Structure: A Dairy Farm Daily Report
import json

# --- Configuration ---
COOPERATIVE = "Githunguri Dairy Cooperative"
MIN_LITRES = 15.0   # flag farms below this daily target

# --- Fetch ---
def fetch_farm_readings():
    # Simulated readings from morning collection
    return [
        {"farm": "Kamau wa Njoroge",  "location": "Githunguri", "litres": 22.5, "cows": 3},
        {"farm": "Wanjiku Farm",      "location": "Limuru",     "litres": 18.0, "cows": 2},
        {"farm": "Mwangi Dairy",      "location": "Githunguri", "litres": 31.5, "cows": 4},
        {"farm": "Achieng Holdings",  "location": "Thika",      "litres": 11.0, "cows": 2},
        {"farm": "Kariuki Homestead", "location": "Limuru",     "litres": 26.0, "cows": 3},
    ]

# --- Process ---
def process_readings(readings, min_litres):
    total = sum(r["litres"] for r in readings)
    avg = round(total / len(readings), 1) if readings else 0
    below_target = [r for r in readings if r["litres"] < min_litres]
    top = max(readings, key=lambda r: r["litres"])
    return {
        "farms_collected": len(readings),
        "total_litres": total,
        "average_litres": avg,
        "below_target": [r["farm"] for r in below_target],
        "top_farm": top["farm"],
        "top_litres": top["litres"]
    }

# --- Output ---
def print_farm_report(cooperative, summary):
    print(f"\n{'='*50}")
    print(f"  DAILY REPORT: {cooperative.upper()}")
    print(f"{'='*50}")
    print(f"  Farms collected:   {summary['farms_collected']}")
    print(f"  Total litres:      {summary['total_litres']:.1f} L")
    print(f"  Average per farm:  {summary['average_litres']} L")
    print(f"  Top farm:          {summary['top_farm']} ({summary['top_litres']} L)")
    if summary["below_target"]:
        print(f"  Below target:      {', '.join(summary['below_target'])}")
    else:
        print("  All farms met target today.")
    print(f"{'='*50}\n")

# --- Main ---
readings = fetch_farm_readings()
summary  = process_readings(readings, MIN_LITRES)
print_farm_report(COOPERATIVE, summary)


#WEEK SIX 
#Introduction to Pandas
import pandas as pd
data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "cold_shower": [True, True, False, True, True, True, True]
}

df = pd.DataFrame(data)
print(df.to_string())
#View data
print("Shape (rows, cols):", df.shape)
print("\nColumns:", list(df.columns))
print("\nData types:")
print(df.dtypes)
print("\nFirst 3 rows:")
print(df.head(3).to_string())

#Select column
# Single column (returns a Series)
print("Steps column:")
print(df["steps"])

print("\nSteps and protocol:")
print(df[["steps", "protocol"]].to_string())

#Select rows
# iloc: by position
print("First row (iloc[0]):")
print(df.iloc[0])

print("\nRows 0 to 2 (iloc[0:3]):")
print(df.iloc[0:3].to_string())

print("\nLast row (iloc[-1]):")
print(df.iloc[-1])

#Describe data
print("Statistics for all numeric columns:")
print(df.describe().to_string())

print("\nManual checks:")
print(f"Mean steps:  {df['steps'].mean():.0f}")
print(f"Max steps:   {df['steps'].max()}")
print(f"Min steps:   {df['steps'].min()}")
print(f"Total steps: {df['steps'].sum()}")

#WEEK 5 LESSON 2
#Filtering and Transforming Data using boolean filtering
import pandas as pd

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "water_glasses":[7, 8, 6, 9, 8, 7, 8],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "notes":    ["ok", "great", "tired", "best", "rest", "rest", "ok"],
})

# Days where step goal was hit
goal_days = df[df["steps"] >= 10000]
print("Days with 10k+ steps:")
print(goal_days[["day", "steps", "protocol"]].to_string())

print()
# Days with less than 7.5 hours sleep
low_sleep = df[df["sleep_hr"] < 7.5]
print("Days with under 7.5 hours sleep:")
print(low_sleep[["day", "sleep_hr"]].to_string())

#Multiple Conditions
#OMAD days with 10k+ steps using "&"
omad_goal = df[(df["protocol"]=="OMAD") & (df["steps"] >= 10000)]
print("OMAD days with 10k+ steps:")
print(omad_goal[["day","steps","protocol"]].to_string())

print()
# Days with either goal steps OR 8+ hours sleep using OR "|"
either = df[(df["steps"] >= 10000) | (df["sleep_hr"] >= 8.0)]
print("Days with 10k+ steps OR 8+ hrs sleep:")
print(either[["day", "steps", "sleep_hr"]].to_string())

#Filtering with .isin()
omad_only = df[df["protocol"].isin(["OMAD"])]
print("Omad only fasting protocol")
print(omad_only[["day","steps","protocol"]])

#Adding New Columns
# Boolean column: did we hit the step goal?
df["hit_goal"] = df["steps"] >= 10000

# Numeric column: steps deficit or surplus vs 10k goal
df["steps_vs_goal"] = df["steps"] - 10000

# Category column: water rating
df["hydration"] = df["water_glasses"].apply(lambda x: "Good" if x >= 8 else "Low")

print(df[["day", "steps", "hit_goal", "steps_vs_goal", "hydration"]].to_string())

#Renaming and Dropping Columns
# Rename column
df = df.rename(columns={"sleep_hr": "sleep_hours"})
print("After rename:")
print(list(df.columns))

# Drop a column
df = df.drop(columns=["notes"])
print("After drop:")
print(df.to_string())

#Sorting
# Sort by steps, highest first
ranked = df.sort_values("steps", ascending=False).reset_index(drop=True)
ranked.index = ranked.index + 1  # 1-based ranking

print("Step leaderboard:")
for i, row in ranked.iterrows():
    print(f"  #{i} {row['day']} {row['steps']:,} steps")

ranked1 = df.sort_values("sleep_hours", ascending=False).reset_index(drop=True)
ranked1.index = ranked1.index + 1  # 1-based ranking
df["wake_up_score"] = (df["sleep_hours"] * df["steps"]) / 1000
print(ranked1)  
print("="*50 + "\n")
print(df)

#WEEK SIX DAY 3
#Grouping and Aggregation

import pandas as pd

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})

# Average steps per fasting protocol
grouped = df.groupby("protocol")["steps"].mean().round(0)
print("Average steps by protocol:")
print(grouped)

print()
# Total steps per protocol
totals = df.groupby("protocol")["steps"].sum()
print("Total steps by protocol:")
print(totals)
