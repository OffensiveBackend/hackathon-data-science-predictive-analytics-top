"""
# Creating a rule-based chatbot.
"""
# Import the needed modules
import pandas as pd

# create a dataframe. Specify the dataset
df = pd.read_csv('health_data.csv') # csv == 'comma separated values'

# print the greeting message from the chatbot
print("HealthBot: Hi! I'm a simple bot Ask me about a symptom or quit.")

#  set a continous loop to handle different user qestions
while True:
    # let the user enter their prompts
    user_prompt = input("\n You:").lower() # Converts user's prompts into lowercase letters

    # check on the user input
    if user_prompt == 'quit':
        print("HealthBot: Goodbye! Stay healthy.")
        break

    # Create a librarian loop
    # Create a loop to search the dataset
    found_answer = False

    for index, row in df.iterrows(): # loop to itterate through all tems in the dataset
        # Clean the keywords from the dataset and handle potential NaN/null values
        # raw_keywords = str(row['Keywords'])
        keywords_list = str(row['Keywords']).split(',') # .split(',') cuts the keyword column into a list: ['head', ' pain', ' ache'].

        # check every keyword on the row
        for word in keywords_list:
            clean_word = word.strip().lower() # fetches the 'appropriate' keyword for a given instance, in small letters

            #check if the the keyword exists in the user prompt/ input
            if clean_word in user_prompt:
                print(f"healthBot:{row['Response']}")

                # update the found_answer be true si.split(',') cuts this string into a list: ['head', ' pain', ' ache'].nce matching word is found from the prompt
                found_answer = True
                break # this prevent further search through within  the data set bcoz the answer has been found

            if found_answer:
                break # this stops searching for other answer since an answer has been found
            
    if not found_answer:
        print("HealthBot: i don't understand this one. Try asking about 'Fever' or 'diet' .")