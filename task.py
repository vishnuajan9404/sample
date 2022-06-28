
# Question one: Json file reader Answer
# Vishnu R


# 1.read json file
import json
i= open ("/home/vishnu/Desktop/abacies/2.json")
data= json.load(i)
j =data['quiz']
print(j) 
i.close()

# 2. print all keys present in maths
#print(j['maths'].keys())

# 3.In key "sports" there is only one question that is "q1", so add a new question "q2" 
dict1={'q2':{"question": "Who is Sachin Tendulkar", "options": ["Cricket Player", "Football Player", "Volleyball Player", "Hockey"], "answer": "Cricket Player"}}
j["sport"].update(dict1)
#print(j["sport"])

# 4. Delete "q2" from "maths".
del j["maths"]["q2"]
#print(j["maths"])

# 5. Change  answer  "Los Angeles Kings" of "q1" from "sports" to "Virginia"
a=(j['sport']['q1']['options'])
a[a.index("Los Angeles Kings")]="Virginia"
print(j["sport"])


# 6.Write this to a new JSON file.
with open('output.json', 'w') as i:
  json.dump(j, i, indent=2)









