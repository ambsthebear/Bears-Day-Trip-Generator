import random

chicago_reco_lists = {
    "destination_options": ["West Town", "Andersonville", "Bridgeport", "Edgewater", "Rogers Park"],
    "restaurant_options": ["Split Rail", "First Slice", "Jackalope", "Edgewater Tacos", "Smackdab"],
    "entertainment_options": ["Burlesque at Dorothy Downstairs", "Trivia Night at Eli Tea Bar", "a Gallery Show at Co-Prosperity", "a Play at The Edge Theatre", "Concert at RoPa Cabana"],
    "transport_options": ["a Car", "the CTA", "a Rideshare", "a Bike", "a Scooter"],
}


def pick_neighborhood(): # Selects neighborhood with user option to say Y/N
    user_destination = False
      
    while user_destination == False:
        destination = random.choice(chicago_reco_lists["destination_options"])
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
    
    return destination


def pick_transport(): # Selects transport with user option to say Y/N
    user_transportation = False
      
    while user_transportation == False:
        transportation = random.choice(chicago_reco_lists["transport_options"])
        user_transportation = input("You can take " + transportation + " to get there. Does that work for you? Please type Y or N. ")
        if user_transportation == "Y":
            print("Way to go! We love " + transportation + "!")
            user_transportation = True
        elif user_transportation == "N":
            print("Ok - finding another option...")
            user_transportation = False
        else:
            print("Try again. ")
            user_transportation = False
    
    return transportation


def pick_restaurant(): # Selects restaurant with user option to say Y/N
    user_restaurant = False
      
    while user_restaurant == False:
        restaurant = random.choice(chicago_reco_lists["restaurant_options"])
        user_restaurant = input("We like " + restaurant + ". Want to try it? Please type Y or N. ")
        if user_restaurant == "Y":
            print("Enjoy your food at " + restaurant + "!")
            user_restaurant = True
        elif user_restaurant == "N":
            print("Ok - finding another option...")
            user_restaurant = False
        else:
            print("Try again. ")
            user_restaurant = False
    
    return restaurant


def pick_entertainment(): # Selects entertainment with user option to say Y/N
    user_entertainment = False
      
    while user_entertainment == False:
        entertainment = random.choice(chicago_reco_lists["entertainment_options"])
        user_entertainment = input("How about going to " + entertainment + "? Please type Y or N. ")
        if user_entertainment == "Y":
            print("Great choice. We hope you enjoy " + entertainment + "!")
            user_entertainment = True
        elif user_entertainment == "N":
            print("Ok - finding another option...")
            user_entertainment = False
        else:
            print("Try again. ")
            user_entertainment = False
    
    return entertainment


destination = pick_neighborhood() 

print("Now let's figure out how you'll get there...")

transportation = pick_transport()

print("You'll probably get hungry, so let's look at some restaurants.")

restaurant = pick_restaurant()

print("Finally, you can end your day with a fun activity.")

entertainment = pick_entertainment()

your_chicago_day_trip = f"Have a great day in {destination}. You'll get there by taking {transportation}, have some food at {restaurant}, then go to{entertainment}"
print(your_chicago_day_trip)
