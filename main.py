from dataFetchingFiles import automation2Step, automation1Step, automationSample
import paragraphGenerator
import time

def main():
    while True:
        paragraphGenerator.createDivider()
        selection = input("""Please Select A Valid Option:
                          
[1] 2 Step Generator
[2] 1 Step Generator
[3] Sample Generator
[4] What are the differences?
[5] Quit

Your choice: """)
        
        if selection == "1":
            automation2Step.main()
        elif selection == "2":
            automation1Step.main()
        elif selection == "3":
            automationSample.main()
        elif selection == "4":
            print("""\nThe 2 step generator helps narrow down topics but takes longer.
The 1 step version does not narrow down topics but is quicker.
The sample generator uses dummy data and does not fetch from the internet.\n""")
            time.sleep(2.5)
        elif selection == "5":
            print("Thank you for using this program!")
            break
        else:
            print("Invalid Number!")
    
main()