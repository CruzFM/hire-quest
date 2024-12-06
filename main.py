import pandas as pd
import csv

def check_url():
    # inputs from the user
    application_url = input("Please enter the URL: ")
    # validates input from the user
    is_valid_url = ".com" in application_url or ".net" in application_url
    is_char_valid = not application_url.startswith(".")
    # evals if the input is a url nor naaaht
    if is_valid_url and is_char_valid:
        print("It's a valid URL")
    else:
        print("It's not a valid URL. Ending program.")

check_url()

data = {
    "Job title": ["Software Engineer", "Data Analyst"],
    "Company": ["Company A", "Company B"],
    "Status": ["Applied", "Pending"]
}

# creates a CSV file
with open("job_applications.csv", "w") as file:
    writer = csv.writer(file)

    writer.writerow(data.keys())

    rows = zip(*data.values())
    writer.writerows(rows)


df = pd.DataFrame(data)

# print(df)