## Please install openai to run this program ##
### use this command  'pip install openai' to install OpenAI 
### This app only for Educatinal purposes 

import openai


def essay(topic, tokens):
    f = open("api_key.txt", "r")
    key = f.read()
    f.close()

    openai.api_key = key
    answer = openai.Completion.create(  
      model="text-davinci-002",
      prompt=f"Write a essay  about {topic}  ::\n\n\n\n\n",
      temperature = 0.5,
      max_tokens = tokens,
      top_p = 1,
      frequency_penalty=0,
      presence_penalty=0

    )
    text = answer["choices"][0]["text"]
    
    f2 = open("new.text", "w")
    f2.write(text)
    f2.close()
    
    return " \n Now Your Text File is Ready"





if __name__ == "__main__":
    essay_topic = input("Write a essay  about :-  ")
    words = int(input("Max_numbers_of_words :- "))
    print("Please wait your file is creating.......... \n ")
    print(essay(essay_topic, words))
    

