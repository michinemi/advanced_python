import json
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person)
# use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)
# the result is a JSON string:
print(person_json) 
print(person_json2) 
with open('person.json', 'w') as f:
    json.dump(person, f) # you can also specify indent etc...


from itertools import accumulate
items = [135,111,82, 63]
wout_fee = [x*(1-0.05) for x in items]
kal = sum(wout_fee)
print(kal)
print(kal*(1-0.05))