# Variation: DUMMY DATA
# This version does not fetch from wikipedia.
# It instead uses local data to emulate the wikipedia experience.
# This is done in case you want to test this out without wait times.

import paragraphGenerator

sampleData = [
              "The cat (Felis catus) is a domestic species of small carnivorous mammal. [1][2] It is the only domesticated species in the family Felidae and is often referred to as the domestic cat to distinguish it from the wild members of the family.[4] A cat can either be a house cat, a farm cat or a feral cat; the latter ranges freely and avoids human contact.[5] Domestic cats are valued by humans for companionship and their ability to hunt rodents. About 60 cat breeds are recognized by various cat registries.",
              
              "The domestic dog (Canis familiaris or Canis lupus familiaris)[4] is a domesticated descendant of the wolf. The dog derived from an ancient, extinct wolf. The modern grey wolf is the dog's nearest living relative.[7] The dog was the first species to be domesticated,[8][7] by hunter–gatherers over 15,000 years ago,[6] before the development of agriculture. Their long association with humans has led dogs to be uniquely adapted to human behavior,[9] leading to a large number of domestic individuals.",
              
              "Snakes are elongated, limbless, carnivorous reptiles of the suborder Serpentes /sɜːrˈpɛntiːz/.[2] Like all other squamates, snakes are ectothermic, amniote vertebrates covered in overlapping scales. Many species of snakes have skulls with several more joints than their lizard ancestors, enabling them to swallow prey much larger than their heads with their highly mobile jaws. To accommodate their narrow bodies, snakes' paired organs (such as kidneys) appear one in front of the other instead of side by side. Most have only one functional lung. They do be scary.",
              
              "A pig is any of the animals in the genus Sus, within the even-toed ungulate family Suidae. Pigs include domestic pigs and their ancestor, the common Eurasian wild boar (Sus scrofa), along with other species. Pigs, like all suids, are native to the Eurasian and African continents, ranging from Europe to the Pacific islands. Suids other than the pig are the babirusa of Indonesia, the pygmy hog of South Asia, the warthog of Africa, and other pig genera from Africa."
            ]

def getTopic():
    #Supply sample results
    results = ["Cats", "Dogs", "Snakes", "Pigs"]
    
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
            selectedTopic = [results[int(selectedTopicIndex)-1], int(selectedTopicIndex)-1]
            break
        except:
            print("\nOOPS! That's not a valid number!")
    
    #Return the topic back to the main program
    return (selectedTopic)
    
def main():    
    topic = getTopic()
    data = sampleData[topic[1]]
    
    topicSentence = paragraphGenerator.generateTopicSentence(topic[0])
    paragraphBody = paragraphGenerator.generateParagraphBody(data, 2, 4)
    conclusionSentence = paragraphGenerator.generateConclusionSentence(topic[0])
    
    paragraphGenerator.outputParagraph(topicSentence, paragraphBody, conclusionSentence)