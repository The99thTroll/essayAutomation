import random
import wikipedia
import wikipediaapi
import time

def generateTopicSentence(topic):
    #List of prompts
    prompts = ["X is a very interesting topic. ",
               "There are many cool things to know about X. ",
               "X has had a very rich and interesting history. ",
               "Not many people truly know about X. ",
               "I love X as it is so wonderful. ",
               "Have you heard about X? ",
               "Did you ever think about the story of X? "]
    
    #Randomly select a prompt then input the topic's name
    promptToUse = prompts[random.randint(0, len(prompts)-1)]
    return promptToUse.replace("X", topic)

def generateConclusionSentence(topic):
    #List of prompts
    prompts = [" Now you know all about X.",
               " As you can see, X has a wonderful history.",
               " I hope that now, when you think of X, you understand it better.",
               " And this is why I believe X is so splendid.",
               " I hope that by reading this, you have developed a liking for X.",
               " X is amazing and I hope you can see that now."]
    
    #Randomly select a prompt then input the topic's name
    promptToUse = prompts[random.randint(0, len(prompts)-1)]
    return promptToUse.replace("X", topic)

def generateParagraphBody(data, min = 3, max = 7):        
    #Split the text into seperate sentences
    summaryData = data.replace(". ", ".X-2M")
    summaryData = summaryData.split("X-2M")

    #Make sure the first sentence comes first
    bodyText = summaryData[0]
    summaryData.pop(0)
    
    #Randomize sentences
    random.shuffle(summaryData)
    sentenceCount = random.randint(min, max)
    selectedSentences = []
    
    for x in range(sentenceCount):
        selectedSentences.append(summaryData.pop(0))
    
    #Put the sentences back together and then return
    bodyText = bodyText + (" ".join(selectedSentences))
    
    return bodyText   

def outputParagraph(topicSentence, paragraphBody, conclusionSentence):
    print("")
    createDivider()
    print("\nHere is your completed paragraph:\n")
    
    paragraph = topicSentence + paragraphBody + conclusionSentence
    print(paragraph)
    time.sleep(7.5)

def getWikipediaData(topic):
    #Notify that the creation is going on
    print("\nNow building your essay...")

    #Get the data from wikipedia
    if wikipediaapi.Wikipedia('en').page(topic).exists():
        summaryData = wikipediaapi.Wikipedia('en').page(topic).summary
    else:
        print("OOPS! " + topic + " was not found!")
        time.sleep(1.5)
        return False
    return summaryData
    
def createDivider(length = 25):
    #Simple divider, can have size changed at will
    print("="+("-"*length)+"=")
