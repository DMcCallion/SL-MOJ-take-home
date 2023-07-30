import csv

import requests


URL = "https://courttribunalfinder.service.gov.uk/search/results.json?postcode="


def call_api(postcode: str) -> list:
    """contacts API and requests data for a specified postcode, returning list of courts"""
    api_call = requests.get(f"{URL}{postcode}")
    return api_call.json()


def get_csv() -> list:
    """reads csv file and returns a list of dicts"""
    people = []

    with open('people.csv', newline='') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:

            people.append(row)
    return people


def get_desired_court(court_type: str, court_data: list) -> dict | None:
    """Takes person's requested type of court and a list of court data
    finds the nearest in the court data, and returns that court info
    """
    for court in court_data:
        if court_type in court['types']:
            return court
    print("-----------------------------")
    print("NO COURT FOUND")
    print("-----------------------------")
    return None


def format_output(person: dict, court: dict) -> str:
    """Given dict of info about person and court, formats the data into a string and returns it"""

    dx_number = court["dx_number"]
    if not dx_number:
        dx_number = "Not Found"

    output = "Person Name: " + person["person_name"] + "\n"
    output += "Home Postcode: " + person["home_postcode"] + "\n"
    output += "Looking For: " + person["looking_for_court_type"] + "\n"

    output += "\n"

    output += "Court Name: " + court["name"] + "\n"
    output += "DX number: " + dx_number + "\n"
    output += "Straight Line Distance: " + \
        str(court["distance"]) + " Miles \n"
    output += "-----------------------------"
    return output


if __name__ == "__main__":

    people = get_csv()

    for person in people:
        api_response = call_api(person["home_postcode"])
        court = get_desired_court(
            person["looking_for_court_type"], api_response)

        if not court:
            continue

        print(format_output(person, court))
