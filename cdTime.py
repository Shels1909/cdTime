def getCDLength():
    num_tracks = int(input("How many tracks are in the CD?: "))
    sub_total_seconds = 0
    sub_total_minutes = 0
    for i in range(num_tracks):
        track_minutes = int(input("How many minutes are on this track?: ")) 
        track_seconds = int(input("How many seconds on this track?:"))
        
        # add track minutes and seconds to total CD Time
        sub_total_minutes = sub_total_minutes + track_minutes
        sub_total_seconds = sub_total_seconds + track_seconds
    
    # get the whole number of minutes that total seconds converts to\
    seconds_2_minutes = int(float(sub_total_seconds) / 60) 

    # add that to the total number of minutes
    total_minutes = sub_total_minutes + seconds_2_minutes
    
    #get the remaining seconds that were not carried over into minutes 
    total_seconds = sub_total_seconds % 60

    print("total minutes: ", total_minutes)
    print("total seconds: ", total_seconds)
    
getCDLength()
