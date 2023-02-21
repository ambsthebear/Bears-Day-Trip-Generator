import random

chicago_reco_lists = {
    "destination_options": ["West Town", "Andersonville", "Bridgeport", "Edgewater", "Rogers Park"],
    "restaurant_options": ["Split Rail", "First Slice", "Jackalope", "Edgewater Tacos", "Karachi Chaat House"],
    "entertainment_options": ["Burlesque at Dorothy Downstairs", "Trivia Night at Eli Tea Bar", "a Gallery Show at Co-Prosperity", "a Play at The Edge Theatre", "Concert at RoPa Cabana"],
    "transport_options": ["a Car", "the CTA", "a Rideshare", "a Bike", "a Scooter"],
}

final_day_trip_dictionary = {
    "final_destination": "confirmed_destination",
    "final_transportation": "confirmed_transportation",
    "final_restaurant": "confirmed_restaurant",
    "final_entertainment": "confirmed_entertainment",
}

def pick_option(dictionary,key):
    choice = random.choice(dictionary[key])
    return choice

def day_trip_generator():
    day_trip_confirmation = False

    destination = pick_option(chicago_reco_lists, "destination_options") 
    transportation = pick_option(chicago_reco_lists, "transport_options")
    restaurant = pick_option(chicago_reco_lists, "restaurant_options")
    entertainment = pick_option(chicago_reco_lists, "entertainment_options")

    while day_trip_confirmation == False:
        your_chicago_day_trip = f"Enjoy your day in {destination}. You'll get there by taking {transportation}, have some food at {restaurant}, then go to {entertainment}."
        print(your_chicago_day_trip)

        day_trip_confirmation = input('Does this sound like a good day trip to you? If so, say "good to go". If not, please say which of these components you would like to change - destination, transportation, restaurant, or entertainment. ')
        if day_trip_confirmation == "good to go":
            print("Have a fantastic day!")
            final_day_trip_dictionary["final_destination"] = destination
            final_day_trip_dictionary["final_transportation"] = transportation
            final_day_trip_dictionary["final_restaurant"] = restaurant
            final_day_trip_dictionary["final_entertainment"] = entertainment
            day_trip_confirmation = True
        elif day_trip_confirmation == "destination":
            destination = pick_option(chicago_reco_lists, "destination_options")
            day_trip_confirmation = False
        elif day_trip_confirmation == "transportation":
            transportation = pick_option(chicago_reco_lists, "transport_options")
            day_trip_confirmation = False
        elif day_trip_confirmation == "restaurant":
            restaurant = pick_option(chicago_reco_lists, "restaurant_options")
            day_trip_confirmation = False
        elif day_trip_confirmation == "entertainment":
            entertainment = pick_option(chicago_reco_lists, "entertainment_options")
            day_trip_confirmation = False
        else:
            print("Try again...")
            day_trip_confirmation = False
  
confirm_day_trip = day_trip_generator()

final_day_trip = final_day_trip_dictionary.items()
return final_day_trip