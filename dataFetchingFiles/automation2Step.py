# Variation: 2 Step
# This version does try to narrow down user topics.
# It takes a long time though due to the wikipedia package having long delays.
# To help a bit, the 1 step variation was crated to allow for less waiting.

import wikipedia
import paragraphGenerator

def getTopic():
    #Recieve the possible terms from Wikipedia
    searchTerm = input("What do you want your paragraph to be on? ")
    print("\nSearching...\n")
    results = wikipedia.search(searchTerm, results = 10)
    
    #List all the topics
    paragraphGenerator.createDivider()
    print("Possible Topics:\n")
    for x in range(len(results)):
        print("[" + str(x+1) + "] " + results[x])
    paragraphGenerator.createDivider()    
        
    #Get the user to select a topic, this will repeat until a valid option is provided    
    while True:
        selectedTopicIndex = input("\nWhich topic do you desire? Please enter a number. ")
        try:
            selectedTopic = results[int(selectedTopicIndex)-1]
            break
        except:
            print("\nOOPS! That's not a valid number!")
    
    #Return the topic back to the main program
    return (selectedTopic)
    
def main():    
    topic = getTopic()
    data = paragraphGenerator.getWikipediaData(topic)
    if data == False:
        return None
    
    topicSentence = paragraphGenerator.generateTopicSentence(topic)
    paragraphBody = paragraphGenerator.generateParagraphBody(data)
    conclusionSentence = paragraphGenerator.generateConclusionSentence(topic)
    
    paragraphGenerator.outputParagraph(topicSentence, paragraphBody, conclusionSentence)