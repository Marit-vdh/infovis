import pandas as pd
import numpy as np
import re
import csv


def read_file(file):
    data = {}

    file.readline()

    for line in file:
        clean_line = line.strip()
        split_line = re.split(r',\s*(?=(?:[^"]*"[^"]*")*[^"]*$)', clean_line)

        if split_line[0] == "2016":
            cleared_line = []

            for element in split_line:
                if element == "..":
                    cleared_line.append(np.nan)
                else:
                    cleared_line.append(element)

            data.update(
                {
                    cleared_line[2]: [
                        cleared_line[4],  # access to electricity
                        cleared_line[5],  # value of GDP added by agriculture
                        cleared_line[6],  # age dependency
                        cleared_line[7],  # consumer price index
                        cleared_line[8],  # female contributing family workers
                        cleared_line[9],  # male contributing family workers
                        cleared_line[10],  # gender equality rating
                        cleared_line[11],  # social protection rating
                        cleared_line[12],  # electric power consumption
                        cleared_line[13],  # fixed broadband internet subscribers
                        cleared_line[14],  # GDP per capita
                        cleared_line[15],  # GINI index
                        cleared_line[16],  # government expenditure on education
                    ]
                }
            )
        else:
            return data


def covid_dictionary(file):
    covid = {}
    file.readline()
    for line in file:
        clean_line = line.strip()
        split_line = re.split(r',\s*(?=(?:[^"]*"[^"]*")*[^"]*$)', clean_line)

        if split_line[3] == "2020-12-31":
            covid.update({split_line[2]: [split_line[4], split_line[7]]})

    return covid


with open("wealth_data.csv", "r", encoding="latin-1") as wealth:
    wealth_data = read_file(wealth)

wealth_df = pd.DataFrame.from_dict(
    wealth_data,
    orient="index",
    columns=[
        "electricity_access",
        "agriculture",
        "age_dependency",
        "cpi",
        "female_family_workers",
        "male_family_workers",
        "gender_equality",
        "social_protection",
        "electric_consumption",
        "internet_subscribers",
        "GDP_per_capita",
        "GINI_index",
        "education_government_spending",
    ],
)

with open("owid-covid-data.csv", "r") as covid:
    covid_data = covid_dictionary(covid)

covid_df = pd.DataFrame.from_dict(
    covid_data, orient="index", columns=["total_cases", "total_deaths"]
)

joined_df = wealth_df.join(covid_df)
print(joined_df)

joined_df.to_csv("combined_database.csv")
# print(joined_df["electricity_access"].corr(joined_df["total_cases"], method="pearson"))

# print(joined_df.corr(method="pearson", numeric_only=True))
