import pandas as pd

print("Hola ferchu!")
data = {
    "Job title": ["Software Engineer", "Data Analyst"],
    "Company": ["Company A", "Company B"],
    "Status": ["Applied", "Pending"]
}

df = pd.DataFrame(data)

print(df)