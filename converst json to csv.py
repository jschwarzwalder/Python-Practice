import json
from random import shuffle

reviews = []
with open('reviews.json') as json_data:
	for line in json_data:
		review = json.loads(line)
		reviews.append(review['reviewText'])
	
	
	print(type(reviews))
	print(len(reviews))
	
shuffle(reviews)

CSV = open("nlp-input.csv", "w")

for i in range(0,300):
	task_name = "nlp-input-text-" + str(i)
	CSV.write(task_name + ", \"" + reviews[i] + "\"\n")
