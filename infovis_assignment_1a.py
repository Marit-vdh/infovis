import re
import numpy as np


def read_file_performance(file):
    # create lists for all the different types of data
    performance = []
    gender = []
    coaching = []
    class_x_percentage = []
    father_occupation = []

    # skip the first sixteen lines
    for i in range(16):
        file.readline()

    # add the data to the lists
    for line in file:
        clean_line = line.strip()
        split_line = clean_line.split(",")
        performance.append(split_line[0])
        gender.append(split_line[1])
        coaching.append(split_line[3])
        class_x_percentage.append(split_line[8])
        father_occupation.append(split_line[10])

    return performance, gender, coaching, class_x_percentage, father_occupation


def read_file_coffee(file):
    species = []
    origin_country = []
    aroma = []
    color = []
    processing = []

    file.readline()

    for line in file:
        clean_line = line.strip()
        split_line = re.split(r',\s*(?=(?:[^"]*"[^"]*")*[^"]*$)', clean_line)
        species.append(split_line[1])
        origin_country.append(split_line[3])
        aroma.append(split_line[20])
        color.append(split_line[34])
        processing.append(split_line[19])

    return species, origin_country, aroma, color, processing


def frequency(data_list):
    frequency = {}
    for item in data_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency


def proportion_percentage(data_list):
    total = len(data_list)
    frequencies = frequency(data_list)

    for fr in frequencies:
        # print(f"Proportion {fr}: {frequencies[fr]} / {total}")
        print(f"Percentage {fr}: {(frequencies[fr] / total)*100}")


def mean(data_list):
    total = 0
    for number in data_list:
        total += float(number)

    return total / len(data_list)


def std(data_list):
    floats = []
    for number in data_list:
        floats.append(float(number))

    return np.std(floats)


# with open("CEE_DATA.arff", "r") as performance_data:
#     results = read_file_performance(performance_data)

# for result in results:
#     proportion_percentage(result)

with open("merged_data_cleaned.csv", "r") as coffee_data:
    coffee_results = read_file_coffee(coffee_data)

print(std(coffee_results[2]))
# proportion_percentage(coffee_results[2])

# print(mean(coffee_results[3]))

# for result in coffee_results:
#     proportion_percentage(result)
