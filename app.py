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

# break
def break_time():
    print("4 minutes break...")
    time.sleep(240)
    breakBeep()
    print("Break ends in 1 minute. Get ready!\n")
    time.sleep(60)
    nextBeep()


# Alarm system (A) - Lessons with Breaks
def TimerA(lessons=3, study=25, recall=25):
    #initial 2 minutes prep
    print("2 minutes to prepare for study session...\n")
    time.sleep(110) # Sounds plays for ten seconds, hence the adjustments
    winsound.PlaySound("beep.wav", winsound.SND_FILENAME)

    # learning period with break
    for i in range(lessons):
        #learn
        print("Start first lesson now!\n")
        time.sleep((study*60)-10)
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)

        break_time() #break
        

    # recalling period with break
    for i in range(lessons):
        # Recall session
        print("Start first recall session now!\n")
        time.sleep((recall*60)-10)
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        
        #break
        while i != (recall-1):
            break_time()


# Alarm system (B) - Lessons without Breaks
def TimerB(lessons, study, recall):
    #initial 2 minutes prep
    print("\n2 minutes to prepare for study session...\n")
    time.sleep(110)
    winsound.PlaySound("beep.wav", winsound.SND_FILENAME)

    # learning period
    for i in range(lessons):
        #learn
        print(f"Start lesson {i+1} now!\n")
        time.sleep((study*60)-10)
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)

    # recalling period
    for i in range(lessons):
        # Recall session
        print(f"Start recall session {i+1} now!\n")
        time.sleep((recall*60)-10)
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)

# main study app
def main():
    try:
        default = str(input("Do you want to use the app's default settings to study(3 lessons - 3 hours)?(y/n) "))

        if default.lower() in ["n", "no"]:
            # Advice
            print("Please avoid adpoting long study hours.\nFor more information on how to study effectively, read \"A mind for numbers: How to excel at math and science\" by Barbara Oakley, Ph.D\n")
            time.sleep(3)
            # user's Preferred adjustments for the study sessions
            print("There are two available studying options (with or without breaks)")
            timer_type = str(input("Do you want to include the 5 minute breaks in your sessions?(y/n) "))   # Select user's preferred Timer type
            study_time = int(input("How many minutes do you wish to study for? "))                          # User's preferred study time
            recall_time = int(input("How many minutes do you wish to use for recalling each lesson? "))     # User's preferred recall time
            lesson_num =  int(input("How many lessons do you wish to study for this session? "))            # User's number of lessons to study
            print("Good stuff!")
            time.sleep(3)

            # Apply user's adjusments and begin
            if timer_type.lower().startswith("n"):
                TimerB(lesson_num,study_time, recall_time)
            else:
                TimerA(lesson_num, study_time, recall_time)

        else: # If user prefers default app settings
            TimerA()
        
        # If user wishes to use app again
        repeating = input("Do you wish to use the app again?(y/n) ")
        if repeating.lower().startswith("y"):
            main()
    except:
        print("An error occured! Restart the app and check again.")
        time.sleep(3)

# Beginning of application
print("Hello! Welcome to Study Timer v1.0")
time.sleep(1)
print("This app uses Pomodoro's Technique to facilitate studying (by default).\n")
time.sleep(2)
print("Thus, 25 minutes per lesson for the desired number of lessons\n and 25 minutes to recall each lesson\n with a 5 minute break after each lesson and recall session.\n")
time.sleep(3)
main()