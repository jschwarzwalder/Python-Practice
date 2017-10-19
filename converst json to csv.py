import json

reviews = []
with open('reviews.json') as json_data:
	for line in json_data:
		review = json.loads(line)
		reviews.append(review['reviewText'])
	
	
	print(type(reviews))
	print(len(reviews))