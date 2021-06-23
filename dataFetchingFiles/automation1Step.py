# Variation: 1 Step
# This version does not narrow down possible topics.
# Due to the wikipedia package's long wait times, users may get annoyed.
# This version allows you to give your input just once and then leave.

import wikipedia
import paragraphGenerator

def getTopic():
    #Recieve the possible terms from Wikipedia
    searchTerm = input("What do you want your paragraph to be on? ")
    print("\nSearching...\n")
    results = wikipedia.search(searchTerm, results = 1)
    
    #Return the topic back to the main program
    return results[0]
    
def main():    
    topic = getTopic()
    data = paragraphGenerator.getWikipediaData(topic)
    if data == False:
        return None
    
    topicSentence = paragraphGenerator.generateTopicSentence(topic)
    paragraphBody = paragraphGenerator.generateParagraphBody(data)
    conclusionSentence = paragraphGenerator.generateConclusionSentence(topic)
    
    paragraphGenerator.outputParagraph(topicSentence, paragraphBody, conclusionSentence)