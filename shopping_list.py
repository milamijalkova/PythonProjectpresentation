import random
import json
from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK

import requests
import webbrowser


# Sample wardrobe
wardrobe = {
   'Top': [
       'Red T-Shirt', 'White Blouse', 'Black Crop Top', 'Blue Polo Shirt',  'Green Sweater', 'Striped Tank Top', 'Yellow Hoodie', 'Purple Silk Shirt',
       'Beige Knit Sweater', 'Floral Printed Blouse', 'Graphic Tee', 'Black Turtleneck'
   ],
   'Bottom': [
       'Blue Jeans', 'Black Skirt', 'Beige Chinos', 'White Denim Shorts',
       'Gray Joggers', 'Plaid Trousers', 'Leather Pants', 'High-Waisted Jeans',
       'Corduroy Pants', 'Ripped Skinny Jeans', 'Pleated Midi Skirt', 'Cargo Pants'
   ],
   'Outerwear': [
       'Black Blazer', 'Beige Trench Coat', 'Denim Jacket', 'Green Parka',
       'Brown Leather Jacket', 'White Faux Fur Coat', 'Red Windbreaker',
       'Camel Wool Coat', 'Oversized Hoodie', 'Navy Peacoat', 'Gray Puffer Jacket'
   ],
   'Footwear': [
       'White Sneakers', 'Black Ankle Boots', 'Red Heels', 'Brown Loafers',
       'Blue Running Shoes', 'Green Sandals', 'Chunky Black Boots',
       'Platform Sneakers', 'Strappy Beige Heels', 'White Flip-Flops',
       'Formal Black Oxfords', 'Hiking Boots'
   ],
   'Accessories': [
       'Gold Earrings', 'Silver Necklace', 'Black Leather Belt', 'Aviator Sunglasses',
       'Knitted Scarf', 'Black Fedora Hat', 'Patterned Silk Scarf',
       'Rose Gold Watch', 'Statement Earrings', 'Minimalist Ring Set',
       'Studded Handbag', 'Canvas Tote Bag', 'Beanie Hat', 'Leather Gloves'
   ]
}


# Compliments based on outfit ratings
compliments = [
   "🔥 You're looking amazing today!",
   "💖 This outfit is giving fashion-forward vibes!",
   "🌟 You're radiating confidence in this!",
   "✨ Trendsetter alert! You totally own this style!",
   "💃 This look was made for you!"
]




# Function to get current weather
import requests




def get_weather(city):
   API_KEY = "ac9152fa795e047823df67f561e6ac2d"  # 🔹 Replace with a real OpenWeatherMap API key
   url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"


   try:
       response = requests.get(url, timeout=5)
       response.raise_for_status()


       weather_data = response.json()


       if 'main' in weather_data and 'temp' in weather_data['main'] and 'weather' in weather_data:
           temperature = weather_data['main']['temp']
           condition = weather_data['weather'][0]['description'].capitalize()  # More specific description
           city_name = weather_data['name']  # Ensures proper city name formatting


           # 🔹 Assign season based on temperature
           if temperature > 25:
               season = "Summer"
           elif 15 <= temperature <= 25:
               season = "Spring"
           elif 5 <= temperature < 15:
               season = "Autumn"
           else:
               season = "Winter"


           print(f"\n🌍 The current weather in {city_name} is {condition} with {temperature}°C.")
           print(f"🌤️ Based on this, the recommended season for dressing is: {season}.")
           return season, condition  # ✅ Returns season and detailed weather condition


       else:
           raise KeyError("Missing data in API response")


   except requests.exceptions.Timeout:
       print("\n⚠️ Error: The request timed out. Please check your internet connection.")
   except requests.exceptions.HTTPError as err:
       print(f"\n⚠️ HTTP Error: {err}. Please check if the city name is correct.")
   except requests.exceptions.ConnectionError:
       print("\n⚠️ Error: No internet connection. Please check your network settings.")
   except requests.exceptions.RequestException:
       print("\n⚠️ General error occurred while retrieving weather data.")
   except KeyError:
       print("\n⚠️ Error: Weather data could not be processed. The API may have changed.")


   # 🔹 Defaulting to a reasonable fallback if an error occurs
   print("🌤️ Defaulting to season: Autumn (unknown weather)")
   return "Autumn", "unknown"




# Function to start interaction
def main():
   print("👗 Welcome to the Clueless Virtual Closet! 👠")



# Function to determine mood
def determine_mood():
   answer = input("\nHow do you feel right now?\n"
                  "a) Happy 😊\n"
                  "b) Confident 💪\n"
                  "c) Relaxed 😌\n"
                  "d) Cozy ☕\n"
                  "e) Energetic ⚡\n"
                  "Your choice (a/b/c/d/e): ").lower()


   mood_dict = {'a': 'Happy', 'b': 'Confident', 'c': 'Relaxed', 'd': 'Cozy', 'e': 'Energetic'}
   return mood_dict.get(answer, "Happy")




# Function to determine occasion
def determine_occasion():
   answer = input("\nWhat’s the plan for today?\n"
                  "a) Casual 🏡\n"
                  "b) Formal 👔\n"
                  "c) Sport 🏃‍♂️\n"
                  "Your choice (a/b/c): ").lower()


   occasion_dict = {'a': 'Casual', 'b': 'Formal', 'c': 'Sport'}
   return occasion_dict.get(answer, "Casual")




# Function to recommend an outfit
def recommend_outfit(season, occasion, mood):
   outfit = {'Top': None, 'Bottom': None, 'Outerwear': None, 'Footwear': None, 'Accessories': []}


   for category, items in wardrobe.items():
       if items:  # If user owns something in this category
           outfit[category] = random.choice(items)


   final_outfit = {key: value for key, value in outfit.items() if value}
   return final_outfit




# Function to like/dislike outfit
def rate_outfit():
   rating = input("\nDo you like this outfit? ❤️\n"
                  "1) Love it! 😍\n"
                  "2) It's okay 🙂\n"
                  "3) Not my style 🙃\n"
                  "Your choice (1/2/3): ").strip()


   if rating == "1":
       print(random.choice(compliments))
   elif rating == "2":
       print("👍 Glad you like it! You can always switch things up.")
   else:
       print("😅 No worries! Maybe try a different combo next time.")




# Function to display outfit and allow retry
def outfit_selection_loop():
   while True:
       city = input("\nEnter your city for weather-based recommendations: ")
       season, condition = get_weather(city)


       if season:
           print(f"\n🌤️ Detected season based on weather: {season} ({condition})")
       else:
           print("\n⚠️ Could not retrieve weather data. Defaulting to 'All' seasons.")
           season = "All"


       mood = determine_mood()
       occasion = determine_occasion()


       outfit = recommend_outfit(season, occasion, mood)
       print("\n🎉 Your Recommended Outfit:")
       for category, item in outfit.items():
           print(f"👕 {category}: {item}")


       rate_outfit()


       # Ask if user wants to try again or exit
       retry = input("\n👗 Would you like to try a different outfit or exit?\n"
                     "1️⃣ Try Again 🔄\n"
                     "2️⃣ Exit 🚪\n"
                     "3️⃣ View shopping list 🛍️\n"
                     "Your choice: ").strip()


       if retry == "2":
           print("👋 Goodbye! Stay stylish! ✨")
           break  # Exit loop


       elif retry == "3":

           while True:  # ✅ Loop inside the shopping list menu
               shopping_list_menu(shopping_list)
               retry = input("\n👗 Would you like to try a different outfit or exit?\n"
                             "1️⃣ Try Again 🔄\n"
                             "2️⃣ Exit 📜\n"
                             "3️⃣ View shopping list 🛍️\n"
                             "Your choice: ").strip()
               if retry in ["1", "2", "3"]:  # ✅ Ensure valid input before continuing
                 break


shopping_list = []
     #the list has an empty dictionary the items will be added by the user.


import datetime # to track the date when items are added

def add_item(shopping_list): #to add the items in the shopping list
    name = input("Enter the item name: ")
    category = input("Enter category (Top/Bottom/Outerwear/Footwear/Accessories): ")
    price = input("Enter the estimated price (or press Enter to skip): ")
    brand = input("Enter the brand (or press Enter to skip): ")
    season = input("Enter the season (Summer/Winter/Spring/Autumn/All): ")
    color = input("Enter the color: ")

    # Convert price to float (if provided) because if not it won't store it
    price = float(price) if price else None

    # Get today's date for tracking
    added_date = datetime.date.today().strftime("%Y-%m-%d")

    # Create the item dictionary
    item = {
        "name": name,
        "category": category,
        "price": price,
        "brand": brand or "Unknown",
        "season": season,
        "color": color,
        "added_date": added_date
    }

    shopping_list.append(item) # append the new item to the shopping list
    print(f"\n '{name}' added to your shopping list!\n")

def view_shopping_list(shopping_list):
    if not shopping_list:
        print("\n Your shopping list is empty!\n")
        return

    print("\n Your Shopping List:\n")
    for idx, item in enumerate(shopping_list, 1): #enumerate adds numbering
        print(f"{idx}. {item['name']} ({item['category']})")
        print(f"    Price: {'$' + str(item['price']) if item['price'] else 'N/A'}")
        print(f"   Brand: {item['brand']}")
        print(f"    Color: {item['color']} |  Season: {item['season']}")

def remove_item(shopping_list):
            if not shopping_list: #no items to remove if empty
                print("\n Your shopping list is empty!\n")
                return

            view_shopping_list(shopping_list)  # Show the current list
            name = input("Enter the name of the item to remove: ").strip()

            for item in shopping_list:
                if item["name"].lower() == name.lower():
                    shopping_list.remove(item)
                    print(f"\n '{name}' has been removed from your shopping list!\n")
                    return

            print(f"\n⚠ '{name}' was not found in your shopping list.\n")

import json #used for saving and loading the shopping list from a file

def save_shopping_list(shopping_list, filename="shopping_list.json"):
    try:
        with open(filename, "w") as f:
            json.dump(shopping_list, f, indent=4)
        print("\n Shopping list saved!\n")
    except IOError:
        print("\n⚠ Error: Unable to save the shopping list.\n")


def load_shopping_list(filename="shopping_list.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        return []  # Return an empty list if the file doesn't exist

def shopping_list_menu(shopping_list): #function to display and manage the shopping list menu
    while True:
        print("\n Shopping List Menu:")
        print("1️⃣ View Shopping List")
        print("2️⃣ Add an Item")
        print("3️⃣ Remove an Item")
        print("4️⃣ Save and Exit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            view_shopping_list(shopping_list)
        elif choice == "2":
            add_item(shopping_list)
        elif choice == "3":
            remove_item(shopping_list)
        elif choice == "4":
            save_shopping_list(shopping_list)
            break
        else:
            print("\n⚠️ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

# Main function
def main():


   while True:
       first_choice = input("\nWhat do you want to do first?\n"
                            "1️⃣ View shopping list 🛍️\n"
                            "2️⃣ Get dressed 👗\n"
                            "Your choice (1/2): ").strip()


       if first_choice == "1":
           #call the shopping list menu
           shopping_list_menu(shopping_list)
           continue  # Return to the main menu


       elif first_choice == "2":
           outfit_selection_loop()  # Start the outfit selection loop
           break  # Exit after dressing up
       else:
           print("⚠️ Invalid choice, please select again.")




if __name__ == "__main__":
   main()