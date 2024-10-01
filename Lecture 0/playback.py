#Get input
RAP=input()

#replace " " string with "..."
def playback(SHORT):
    print(str.strip(SHORT).replace(" ","..."))

playback(RAP)
