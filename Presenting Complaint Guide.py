# Presenting Complaint Guide [Version 1.0]
# Copyright (c) 2022 Cian Finnegan under GNU Affero General Public License v3.0.
# All rights reserved.

##Function Definition:

lower_first = lambda s: s[:1].lower() + s[1:] if s else ''

##Header:
print("""

Presenting Complaint Guide [Version 1.0]
Copyright (c) 2022 Cian Finnegan under GNU Affero General Public License v3.0.
All rights reserved.

I made this program to format a formal medical presenting complaint from its constituent parts.
You should present this as the very first section of your history, as it introduces the patient.
It's far from perfect, but I hope that it serves to help you figure out how to put one together by yourself!

Hint: The summary at the end of your case presentation should largely mirror this presenting complaint, with the relevant findings from your physical examination added at the end.
If you can then follow this up with your subjective assessment of the evidence and a reasonable differential diagnosis, you will be doing great!

I hope this helps -

Cian.

""")

##Questions:

#Ascertaining the patient's name:
name = input("\nWhat is the patient's full name?\n\n")

#Ascertaining the patient's age, and making sure it is a number:
while True:
  try:
    age = int(input("\nWhat is the patient's age in years?\n\n"))
    break
  except ValueError:
    print("\nUnfortunately, I could not accept your last answer as it contained more than just a number. Please try again, using only numbers this time.\n\n")

#Ascertaining the patient's gender:
gender = str.lower(input("\nWhat is the patient's gender?\n\n"))

#Defining the most common gender categories:
cismale = ["male", "m", "man", "boy"]
cisfemale = ["female", "f", "woman", "girl"]
transmale = ["transgender man", "transgender male", "trans man", "trans male", "ftm", "female to male"]
transfemale = ["transgender woman", "transgender female", "trans woman", "trans female", "mtf", "male to female"]


#Establishing a title for the patient from their age and gender:
if age < 18:
  if gender in cismale:
      title = "boy"
  elif gender in cisfemale:
      title = "girl"
  elif gender in transmale:
      title = "transgender boy"
  elif gender in transfemale:
      title = "transgender girl"
  else:
      title = "{} person".format(gender)
else:
  if gender in cismale:
      title = "man"
  elif gender in cisfemale:
      title = "woman"
  elif gender in transmale:
      title = "transgender man"
  elif gender in transfemale:
      title = "transgender woman"
  else:
      title = "{} person".format(gender)

#Establishing whereabouts the patient first presented during this visit:
destination = lower_first(input("\nWhere in the hospital did the patient first arrive? (e.g. the emergency department, the acute medical unit)\n\n"))

#Establishing via which route the patient presented:
route = lower_first(input("\nHow did the patient end up in the hospital? (e.g. self-presented, was referred by their GP, was brought in by ambulance)\n\n"))

#Establishing the patient's causes for presenting:
complaint_list = []
complaint_list.append(input("\nType in below the most significant symptom that brought this patient in today, with any (brief) relevant descriptors added. (e.g. \"crushing central chest pain\")\n\n"))
while True:
    additional_complaint_unfiltered = input("\nIf they have any more relevant complaints, type in below the next most significant symptom that they're reporting.\nIf there's nothing more, type \"done\".\n\n")
    additional_complaint = str.lower(additional_complaint_unfiltered)
    if len(complaint_list) == 5:
        print("\nPerfect! That is more than enough to make a presenting complaint.\n\n")
        break
    elif additional_complaint != "done":
        complaint_list.append(additional_complaint)
    else:
        break

#Establishing the patient's relevent pre-existing diagnoses and contextual factors:
background_list = []
background_unfiltered = (input("\nType in below the most significant/relevant pre-existing diagnosis that the patient has (if any), with any (brief) relevant descriptors added. (e.g. \"type II diabetes mellitus\")\nIf they have none, type \"none\".\n\n"))
background = str.lower(background_unfiltered)
if background not in ["none", "done"]:
    background_list.append(background)
    while True:
        additional_background_unfiltered = input("\nIf they have any more relevant relevant pre-existing diagnoses, type in below the next most significant one.\nIf there's nothing more, type \"done\".\n\n")
        additional_background = str.lower(additional_background_unfiltered)
        if len(background_list) == 4:
            print("\nPerfect! That is more than enough to give context.\n\n")
            break
        elif additional_background != "done":
            background_list.append(additional_background)
        else:
            break
else:
    background_list.append("previously good health")

#Establishing the patient's smoking history:
smoking_status = str.lower(input("\nDoes the patient smoke?\n\n"))
while smoking_status in ["yes", "y", "yeah", "ya", "yep"]:
    try:
      pack_year_number = int(input("What is the patient's pack-year history?\nPack-year history = (number of years spent smoking) x average number of packs of cigarettes smoked per day) - There are 20 cigarettes in a standard pack.\n\n"))
      pack_year_history = "a {} pack-year smoking history".format(pack_year_number)
      background_list.append(pack_year_history)
      break
    except ValueError:
      print("\nUnfortunately, I could not accept your last answer as it contained more than just a number. Please try again, using only numbers this time.\n\n")


##Formatting and displaying the completed text for "Presenting Complaint"

number_of_complaints = len(complaint_list)
if number_of_complaints == 1:
    complaint_list_complete = complaint_list
elif number_of_complaints == 2:
    complaint_list_complete = "{} and {}".format(complaint_list[0], complaint_list[1])
elif number_of_complaints == 3:
    complaint_list_complete = "{}, {} and {}".format(complaint_list[0], complaint_list[1], complaint_list[2])
elif number_of_complaints == 4:
    complaint_list_complete = "{}, {}, {} and {}".format(complaint_list[0], complaint_list[1], complaint_list[2], complaint_list[3])
elif number_of_complaints == 5:
    complaint_list_complete = "{}, {}, {}, {} and {}".format(complaint_list[0], complaint_list[1], complaint_list[2], complaint_list[3], complaint_list[4])

number_of_backgrounds = len(background_list)
if number_of_backgrounds == 1:
    background_list_complete = background_list
elif number_of_backgrounds == 2:
    background_list_complete = "{} and {}".format(background_list[0], background_list[1])
elif number_of_backgrounds == 3:
    background_list_complete = "{}, {} and {}".format(background_list[0], background_list[1], background_list[2])
elif number_of_backgrounds == 4:
    background_list_complete = "{}, {}, {} and {}".format(background_list[0], background_list[1], background_list[2], background_list[3])
elif number_of_backgrounds == 5:
    background_list_complete = "{}, {}, {}, {} and {}".format(background_list[0], background_list[1], background_list[2], background_list[3], background_list[4])

presenting_complaint = "\nToday I took a history from {}, a {} year-old {} who {} to {} due to {} in the context of {}.\n\n".format(name, age, title, route, destination, complaint_list_complete, background_list_complete)
print("\nPhenomenal, here's your presenting complaint:\n")
print(presenting_complaint)
