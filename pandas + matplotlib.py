from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter
import csv

plt.style.use('seaborn-darkgrid')
data = pd.read_csv("data.csv")
ids=data["Responder_id"]
lang_response=data['LanguagesWorkedWith']

language_counter = Counter()
for response in lang_response:
    language_counter.update(response.split(';'))

# print(language_counter.most_common(3))

language = []
popularity = []

for item in language_counter.most_common(15):
    language.append(item[0])
    popularity.append(item[1])
print(language)
print(popularity)

# row = next(csv_reader)
# print(row['LanguagesWorkedWith'].split(';'))
language.reverse()
popularity.reverse()
plt.barh(language, popularity)
plt.title('most popular programming lan')
# plt.ylabel('programming lan')
plt.xlabel('num. of people who use ')
# plt.tight_layout()
plt.show()
