import random

chicago_day_trip_lists = {
    "destination_options": ["Humboldt Park", "Andersonville", "Bridgeport", "Edgewater", "Rogers Park"],
    "restaurant_options": ["Split Rail", "First Slice", "Jackalope", "Edgewater Tacos", "Karachi Chaat House"],
    "entertainment_options": ["Burlesque at Dorothy Downstairs", "Trivia Night at Eli Tea Bar", "a Gallery Show at Co-Prosperity", "a Play at The Edge Theatre", "Concert at RoPa Cabana"],
    "transport_options": ["Car", "CTA", "Rideshare", "Bike", "Scooter"],
}



def pick_neighborhood():
    user_destination = False
      
    while user_destination == False:
        destination = random.choice(chicago_day_trip_lists["destination_options"])
        user_destination = input("Let's take a day trip to " + destination + ". Sound good? Please type Y or N. ")
        if user_destination == "Y":
            print("Awesome! " + destination + " is a cool neighborhood.")
            user_destination = True
        elif user_destination == "N":
            print("Ok - finding another option...")
            user_destination = False
        else:
            print("Try again. ")
            user_destination = False

pick_neighborhood()

