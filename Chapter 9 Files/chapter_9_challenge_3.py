# Take the items in this list of lists: [["Top Gun", "Risky BUsiness",
# "Minority Report"], ["Titantic", "The Revenant", "Inception"], ["Training
# Day", "Man On Fire", "Flight"]] and write them to a CSV file. The data
# from each list should be a row in the file, with each item in the list
# seperated by commas.

import csv
import os

filepath = os.path.join(os.sep, "Users", "golbeckm", "Desktop", "AISES", "chapter_9_challenge_3.csv")

list_of_lists = [["Top Gun", "Risky Business", "Minority Report"], ["Titantic", "The Revenant", "Inception"], ["Training Day", "Man On Fire", "Flight"]]

with open(filepath, "w+") as file:
    writer_to_file = csv.writer(file, delimiter = ",")
    writer_to_file.writerow(["Top Gun", "Risky Business", "Minority Report"])
    writer_to_file.writerow(["Titantic", "The Revenant", "Inception"])
    writer_to_file.writerow(["Training Day", "Man On Fire", "Flight"])
