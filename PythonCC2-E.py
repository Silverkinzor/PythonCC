# Extra thing based on the birthday code on p.31-32
# Proper number suffixes based on number entered.

while True:
    try:
        age = int(input("Enter age: ")) # Input and Input Validation
        if age > 0:
            break
        else:
            print("Invalid!")
    except ValueError:
        print("Invalid!")

suffix = ""
age_list = (list(str(age)))
last_age_digit = age_list.pop()
last_age_digit = int(last_age_digit)
second_last_age_digit = 0

if age > 9: # necessary as 11-13 use th instead of st, nd, rd
    second_last_age_digit = age_list.pop()
    second_last_age_digit = int(second_last_age_digit)

if second_last_age_digit == 1: # special case in 11-13
    suffix = "th"

else:
    if last_age_digit == 1: # suffix handling
        suffix = "st"

    elif last_age_digit == 2:
        suffix = "nd"

    elif last_age_digit == 3:
        suffix = "rd"

    else:
        suffix = "th"

message = "Happy " + str(age) + suffix + " Birthday!"

print(message)
