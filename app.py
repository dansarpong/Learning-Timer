from timeit import repeat
import winsound, time

# sound 1
def breakBeep():
    freq = 200
    dur = 50

    for i in range(5):	
        winsound.Beep(freq, dur)	
        freq+= 100
        dur+= 50

# sound 2
def nextBeep():
    freq = 800
    dur = 500

    for i in range(5):	
        winsound.Beep(freq, dur)	
        freq-= 100
        dur-= 50

# Alarm system
def timer(study=3):
    #initial 2 minutes prep
    print("2 minutes to prepare for study session begins!\n")
    time.sleep(110)
    winsound.PlaySound("beep.wav", winsound.SND_FILENAME)

    # learning period with break and prep
    for i in range(study):
        #learn
        print("Start first lesson now!\n")
        time.sleep(1490)
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        
        #break
        print("4 minutes break...")
        time.sleep(240)
        breakBeep()
        print("Break ends in 1 minute. Get ready!\n")
        time.sleep(60)
        nextBeep()

    # recalling period
    for i in range(study):
        # Recall session
        print("Start first recall session now!\n")
        time.sleep(1490)
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        
        #break
        while i != (study-1):
            print("5 minutes break...\n")
            time.sleep(300)
            nextBeep()

# main study app
def main():    
    try:
        # Use default time or set time manually
        default_user = str(input("Do you want to use the default 3-hour study schedule? (y/n)\n"))
        if default_user.lower() in ["y", "yes"]:
            timer()
        else:
            study_hours = int(input("How many study hours for today? "))
            print("Good stuff! Let's begin!")
            time.sleep(2)
            timer(study_hours)

        # Check if user wants to reuse app
        repeat_check = input("Are we done for the day? (y/n) ")
        if repeat_check.lower() in ["n", "no"]:
            main()
    except:
        print("Error!")

    exit()

main()