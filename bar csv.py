from matplotlib import pyplot as plt
import numpy as np
from collections import Counter
import csv
plt.style.use('seaborn-darkgrid')

with open("data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

# print(language_counter.most_common(3))

language=[]
popularity=[]

for item in language_counter.most_common(15):
    language.append(item[0])
    popularity.append(item[1])
print(language)
print(popularity)

    # row = next(csv_reader)
    # print(row['LanguagesWorkedWith'].split(';'))
language.reverse()
popularity.reverse()
plt.barh(language,popularity)
plt.title('most popular programming lan')
# plt.ylabel('programming lan')
plt.xlabel('num. of people who use ')
# plt.tight_layout()
plt.show()
