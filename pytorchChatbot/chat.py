import random
import json

import torch

import test

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)


FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Doc_Assistant"
print("Let's chat! (type 'quit' to exit)")


intent_tags_list = []

def chatbot_response(sentence):

    #if sentence == "results":
        #res = listToString(what_are_your_symptoms(filter_disease(intent_tags_list)))

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    print("\n *************")
    print(sentence)
    print("\n *************")

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    print(tag)

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                res = random.choice(intent['responses'])
                intent_tags_list.append(tag)   
    elif "results" in sentence:
        dic= test.what_are_your_symptoms(filter_disease(intent_tags_list))
        res=dic
        print("\n ****/////***")
        print(dic)
        print("\n ***/////****")
    else:
        res = " I do not understand..."
    print(filter_disease(intent_tags_list))

    return res

def filter_disease(tags_list):

    symptoms_list = []

    with open('disease.json','r') as f:
        diseases = json.load(f)

    for tag in tags_list:
        for disease in diseases:
            if tag in diseases[disease]['symptoms']:
                symptoms_list.append(tag)

    return list(set(symptoms_list))


def listToString(s):
	
	# initialize an empty string
	str1 = ""
	
	# traverse in the string
	for ele in s:
		str1 = ele + ", " + str1
	
	# return string
	return str1

