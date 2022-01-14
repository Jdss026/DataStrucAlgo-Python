#Exercise 1

#January - 2200
#February - 2350
#March - 2600
#April - 2130
#May - 2190


expense = {"January":2200, "February": 2350, "March": 2600, "April": 2130, "May": 2190}

#for i in expense:
#    print("For month {}: ${}".format(i, expense[i]))

#1. In Feb, how many dollars you spent extra compare to January?

print("#1 - spent {} extra dollars in Feb - Jan".format(expense["February"]-expense["January"]))

#2. Find out your total expense in first quarter (first three months) of the year.

print("#2 - First quarter: {}".format(expense["January"]+expense["February"]+expense["March"]))

#3. Find out if you spent exactly 2000 dollars in any month
b = False
index = 0
for i in expense:
    if expense[i] == 2000:
        b = True
        index = i

if b is True:
    print("#3 - spent $2000 dollars in {}".format(index))
else:
    print("#3 - Never spent $2000 in any given month")


#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expense["June"] = 1980
print("#4 - The new expense list is: {}".format(expense))

#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

expense["April"] = expense["April"] - 200
print("#5 - The updated expense list is: {}".format(expense))