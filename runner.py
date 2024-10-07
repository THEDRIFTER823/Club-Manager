import csv
from datetime import datetime

def get_name(id):
    #returns the name of the member with the specific ID
    data = csv.DictReader(open("data.csv"))
    for line in data:
        if line["member_id"] == str(id):
            return line["first_name"] + " " + line["last_name"]
    return "Name not found"

def get_info(name):
    #returns all personal information regarding the specific individual as a tuple
    data = csv.DictReader(open("data.csv"))
    for line in data:
        if get_name(line["member_id"]) == name:
            return line["member_id"], name, line["email_address"], line["phone_number"], line["home_address"]
    return "Info not found for " + name

def get_overdue():
    # returns a list of members who's dues are not paid
    array = []
    data = csv.DictReader(open("data.csv"))
    for line in data:
        if line["payment_status"] == "Overdue":
            array.append(get_name(line["member_id"]))
    return array

def get_paid():
    # returns a list of members who's dues are paid
    array = []
    data = csv.DictReader(open("data.csv"))
    for line in data:
        if line["payment_status"] == "Paid":
            array.append(get_name(line["member_id"]))
    return array

def get_membership_duration(name):
    # returns the start date and end date of someone's membership
    data = csv.DictReader(open("data.csv"))
    for line in data:
        if get_name(line["member_id"]) == name:
            return line["membership_start_date"] + " to " + line["membership_end_date"]

