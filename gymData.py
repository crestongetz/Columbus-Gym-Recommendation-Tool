#Here we are storing a list of gyms types
types = ["powerlifting", "crossfit", "bodybuilding", "olympic", "martial arts", "yoga", "pilates", "traditional", "strongman", "budget"]

#TODO add api from google maps to get gym data
# Try gemini or ai api to sort gyms into types if not available in the data

#Fake Gym Data that has name, type, location, rating, and price
Gym_Data = [
    # Powerlifting Gyms
    {"name": "Iron Forge Powerlifting", "type": "powerlifting", "location": "Columbus, OH - Downtown", "rating": 4.8, "price": 75},
    {"name": "Heavy Metal Strength", "type": "powerlifting", "location": "Columbus, OH - North Side", "rating": 4.6, "price": 65},
    
    # Crossfit Gyms
    {"name": "CrossFit Columbus Central", "type": "crossfit", "location": "Columbus, OH - Short North", "rating": 4.7, "price": 150},
    {"name": "Elite CrossFit Arena", "type": "crossfit", "location": "Columbus, OH - East Side", "rating": 4.5, "price": 140},
    
    # Bodybuilding Gyms
    {"name": "Muscle Factory Gym", "type": "bodybuilding", "location": "Columbus, OH - West Side", "rating": 4.9, "price": 50},
    {"name": "Titan Physique Center", "type": "bodybuilding", "location": "Columbus, OH - South Side", "rating": 4.7, "price": 55},
    
    # Olympic Gyms
    {"name": "Olympic Lifting Academy", "type": "olympic", "location": "Columbus, OH - Campus Area", "rating": 4.8, "price": 85},
    #{"name": "Weightlifting Elite", "type": "olympic", "location": "Columbus, OH - Grandview", "rating": 4.6, "price": 80},
    
    # Martial Arts Gyms
    {"name": "Columbus Combat Academy", "type": "martial arts", "location": "Columbus, OH - Downtown", "rating": 4.7, "price": 120},
    {"name": "Warrior's Dojo", "type": "martial arts", "location": "Columbus, OH - North Side", "rating": 4.5, "price": 110},
    
    # Yoga Studios
    {"name": "Zen Yoga Studio", "type": "yoga", "location": "Columbus, OH - Short North", "rating": 4.6, "price": 90},
    {"name": "Serenity Flow Yoga", "type": "yoga", "location": "Columbus, OH - German Village", "rating": 4.8, "price": 95},
    
    # Pilates Studios
    {"name": "Core Pilates Studio", "type": "pilates", "location": "Columbus, OH - Upper Arlington", "rating": 4.7, "price": 100},
    {"name": "Balance Pilates Center", "type": "pilates", "location": "Columbus, OH - Bexley", "rating": 4.6, "price": 105},
    
    # Traditional Gyms
    {"name": "Fitness First Columbus", "type": "traditional", "location": "Columbus, OH - Multiple Locations", "rating": 4.4, "price": 40},
    {"name": "All-Access Fitness", "type": "traditional", "location": "Columbus, OH - Easton", "rating": 4.5, "price": 45},
    
    # Strongman Gyms
    {"name": "Titan Strongman Training", "type": "strongman", "location": "Columbus, OH - West Side", "rating": 4.8, "price": 70},
    {"name": "Brute Force Strongman", "type": "strongman", "location": "Columbus, OH - North Side", "rating": 4.7, "price": 68},
    
    # Budget Gyms
    {"name": "Budget Fit 24/7", "type": "budget", "location": "Columbus, OH - Multiple Locations", "rating": 4.2, "price": 20},
    {"name": "Value Fitness Center", "type": "budget", "location": "Columbus, OH - Hilliard", "rating": 4.1, "price": 18}
]