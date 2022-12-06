import requests
import random

API_URL = "https://api-inference.huggingface.co/models/xlm-roberta-base"
headers = {"Authorization": f"Bearer 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"}

def user_phase_input():
    input_phrase = input("Give me a random string of words: Put <mask> in the 3rd last word!")
    return input_phrase

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# step to use here:
#The user should be giving a unique response phrase to generate the key words

output = query({
    "inputs": "The answer to the universe is <mask> and nothing .",
})


print(output)
passwords_keys = []

for i in output:
  #print(i)
  for j in i:
    if(j == 'sequence'):
      print(i[j])
      x = i[j]
      x = x.split(" ")
      passwords_keys.append(x[-3])
print(passwords_keys)

dictionary = "abcdefghijklmnopqrstuvwxyz"
def key_generator(x):
    list = x
    key = random.choice(list)
    print(f"The chosen key phrase was: {key}")
    return key

generated_key = key_generator(passwords_keys)
key_number = 0
for i in generated_key:
    location_of_string = dictionary.find(i)
    key_number = location_of_string + key_number

print(f"The final key is: {key_number}")
