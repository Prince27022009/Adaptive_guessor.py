attr = [
    "place",
    "fiction",
    "person",
    "org",
    "living",
    "real",
    "modern",
    "tech",
    "sport"
]

questions = {
    "place": "Is it a place or location?",
    "fiction": "Is it fictional?",
    "person": "Is it a person?",
    "org": "Is it an organization or company?",
    "living": "Is it currently alive?",
    "real": "Is it a real-world entity?",
    "modern": "Is it associated with the modern era (post-1900)?",
    "tech": "Is it strongly associated with technology or engineering?",
    "sport": "Is it primarily associated with sports?"
}

entities = {

    # places
    "Tokyo": {"place": True, "fiction": False, "person": False, "org": False, "living": False, "real": True, "modern": True, "tech": False, "sport": False},
    "Osaka": {"place": True, "fiction": False, "person": False, "org": False, "living": False, "real": True, "modern": True, "tech": False, "sport": False},
    "Delhi": {"place": True, "fiction": False, "person": False, "org": False, "living": False, "real": True, "modern": True, "tech": False, "sport": False},
    "Mumbai": {"place": True, "fiction": False, "person": False, "org": False, "living": False, "real": True, "modern": True, "tech": False, "sport": False},
    "New York": {"place": True, "fiction": False, "person": False, "org": False, "living": False, "real": True, "modern": True, "tech": False, "sport": False},
    "De Wallen": {"place": True, "fiction": False, "person": False, "org": False, "living": False, "real": True, "modern": True, "tech": False, "sport": False},
    "Bali": {"place": True, "fiction": False, "person": False, "org": False, "living": False, "real": True, "modern": False, "tech": False, "sport": False},
    "Kyoto": {"place": True, "fiction": False, "person": False, "org": False, "living": False, "real": True, "modern": False, "tech": False, "sport": False},
    "Mawsynram": {"place": True, "fiction": False, "person": False, "org": False, "living": False, "real": True, "modern": False, "tech": False, "sport": False},
    "Mount Everest": {"place": True, "fiction": False, "person": False, "org": False, "living": False, "real": True, "modern": False, "tech": False, "sport": False},

    #fictional
    "Ash Ketchum": {"place": False, "fiction": True, "person": True, "org": False, "living": True, "real": False, "modern": True, "tech": False, "sport": False},
    "Pikachu": {"place": False, "fiction": True, "person": False, "org": False, "living": True, "real": False, "modern": True, "tech": False, "sport": False},
    "Eren Yeager": {"place": False, "fiction": True, "person": True, "org": False, "living": False, "real": False, "modern": True, "tech": False, "sport": False},
    "Thorfinn": {"place": False, "fiction": True, "person": True, "org": False, "living": True, "real": False, "modern": False, "tech": False, "sport": False},
    "Tony Stark": {"place": False, "fiction": True, "person": True, "org": False, "living": False, "real": False, "modern": True, "tech": True, "sport": False},
    "Thor": {"place": False, "fiction": True, "person": True, "org": False, "living": True, "real": False, "modern": False, "tech": False, "sport": False},
    "Spiderman": {"place": False, "fiction": True, "person": True, "org": False, "living": True, "real": False, "modern": True, "tech": False, "sport": False},
    "Harry Potter": {"place": False, "fiction": True, "person": True, "org": False, "living": True, "real": False, "modern": True, "tech": False, "sport": False},
    "James Bond": {"place": False, "fiction": True, "person": True, "org": False, "living": True, "real": False, "modern": True, "tech": False, "sport": False},
    "Sherlock Holmes": {"place": False, "fiction": True, "person": True, "org": False, "living": False, "real": False, "modern": False, "tech": False, "sport": False},

    # people
    "Elon Musk": {"place": False, "fiction": False, "person": True, "org": False, "living": True, "real": True, "modern": True, "tech": True, "sport": False},
    "Jeff Bezos": {"place": False, "fiction": False, "person": True, "org": False, "living": True, "real": True, "modern": True, "tech": True, "sport": False},
    "Ratan Tata": {"place": False, "fiction": False, "person": True, "org": False, "living": True, "real": True, "modern": True, "tech": False, "sport": False},
    "Shahrukh Khan": {"place": False, "fiction": False, "person": True, "org": False, "living": True, "real": True, "modern": True, "tech": False, "sport": False},
    "Tom Cruise": {"place": False, "fiction": False, "person": True, "org": False, "living": True, "real": True, "modern": True, "tech": False, "sport": False},

    # sports
    "Cristiano Ronaldo": {"place": False, "fiction": False, "person": True, "org": False, "living": True, "real": True, "modern": True, "tech": False, "sport": True},
    "Lionel Messi": {"place": False, "fiction": False, "person": True, "org": False, "living": True, "real": True, "modern": True, "tech": False, "sport": True},
    "Sunil Chhetri": {"place": False, "fiction": False, "person": True, "org": False, "living": True, "real": True, "modern": True, "tech": False, "sport": True},
    "Sachin Tendulkar": {"place": False, "fiction": False, "person": True, "org": False, "living": True, "real": True, "modern": True, "tech": False, "sport": True},
    "Virat Kohli": {"place": False, "fiction": False, "person": True, "org": False, "living": True, "real": True, "modern": True, "tech": False, "sport": True},

    # organizations
    "Amazon": {"place": False, "fiction": False, "person": False, "org": True, "living": False, "real": True, "modern": True, "tech": True, "sport": False},
    "SpaceX": {"place": False, "fiction": False, "person": False, "org": True, "living": False, "real": True, "modern": True, "tech": True, "sport": False},
    "Tesla": {"place": False, "fiction": False, "person": False, "org": True, "living": False, "real": True, "modern": True, "tech": True, "sport": False},
    "Tata": {"place": False, "fiction": False, "person": False, "org": True, "living": False, "real": True, "modern": True, "tech": False, "sport": False},
    "Toyota": {"place": False, "fiction": False, "person": False, "org": True, "living": False, "real": True, "modern": True, "tech": True, "sport": False},
    "Volkswagen": {"place": False, "fiction": False, "person": False, "org": True, "living": False, "real": True, "modern": True, "tech": True, "sport": False},
    "BMW": {"place": False, "fiction": False, "person": False, "org": True, "living": False, "real": True, "modern": True, "tech": True, "sport": False},
    "McDonald's": {"place": False, "fiction": False, "person": False, "org": True, "living": False, "real": True, "modern": True, "tech": False, "sport": False},
    "Dominos": {"place": False, "fiction": False, "person": False, "org": True, "living": False, "real": True, "modern": True, "tech": False, "sport": False},
    "Blinkit": {"place": False, "fiction": False, "person": False, "org": True, "living": False, "real": True, "modern": True, "tech": True, "sport": False}
}

facts = {

    # places
    "Tokyo": [
        "Tokyo has the world’s busiest train station, Shinjuku Station, handling over 3.5 million passengers daily."
    ],
    "Osaka": [
        "Osaka is considered the birthplace of instant noodles, invented by Momofuku Ando in 1958."
    ],
    "Delhi": [
        "Delhi is home to Asia’s largest spice market, Khari Baoli, which has operated since the 17th century."
    ],
    "Mumbai": [
        "Thousands of flamingos migrate to Mumbai every year between October and March, especially around the Thane Creek."
    ],
    "New York": [
        "New York City is the most linguistically diverse city in the world, with over 800 languages spoken."
    ],
    "De Wallen": [
        "De Wallen operates under strict government regulation, where window prostitution is legal but heavily monitored."
    ],
    "Bali": [
        "Bali lies at the center of the Coral Triangle, often called the ‘Amazon of the seas’ due to its marine biodiversity."
    ],
    "Kyoto": [
        "Kyoto was deliberately spared major bombing during World War II due to its immense cultural and historical value."
    ],
    "Mawsynram": [
        "Mawsynram receives the highest average annual rainfall on Earth due to its unique monsoon wind funneling."
    ],
    "Mount Everest": [
        "Mount Everest is still growing at roughly 4–5 millimeters per year because of tectonic plate movement."
    ],

    # fictional characters
    "Ash Ketchum": [
        "Ash Ketchum’s age remains canonically 10 years old across more than two decades of Pokémon episodes."
    ],
    "Pikachu": [
        "Pikachu was originally designed with a chubbier body, which was later slimmed down to improve animation clarity."
    ],
    "Eren Yeager": [
        "Eren Yeager’s character arc was planned from the very beginning of the story, including his ultimate fate."
    ],
    "Thorfinn": [
        "Thorfinn’s character is loosely inspired by the real historical Viking explorer Thorfinn Karlsefni."
    ],
    "Tony Stark": [
        "Tony Stark was originally created as a commentary on Cold War-era weapons manufacturing ethics."
    ],
    "Thor": [
        "Marvel’s Thor draws more inspiration from Norse poetry than from traditional superhero archetypes."
    ],
    "Spiderman": [
        "Spider-Man was one of the first superheroes portrayed with everyday financial and personal struggles."
    ],
    "Harry Potter": [
        "Many spells in Harry Potter are derived from Latin roots describing their effects."
    ],
    "James Bond": [
        "James Bond’s code number 007 is reassigned after retirement or death, rather than belonging to one person forever."
    ],
    "Sherlock Holmes": [
        "Sherlock Holmes popularized forensic techniques in fiction before they were common in real investigations."
    ],

    # real people
    "Elon Musk": [
        "Elon Musk once funded SpaceX almost entirely from his PayPal earnings after nearly going bankrupt."
    ],
    "Jeff Bezos": [
        "Amazon was originally named ‘Cadabra’ before Jeff Bezos changed it due to pronunciation confusion."
    ],
    "Ratan Tata": [
        "Ratan Tata personally backed multiple startups anonymously before India’s startup ecosystem matured."
    ],
    "Shahrukh Khan": [
        "Shah Rukh Khan was the first Indian actor to own an IPL cricket team as a principal stakeholder."
    ],
    "Tom Cruise": [
        "Tom Cruise performs many of his own stunts to maintain realistic camera physics rather than visual effects."
    ],

    # sports
    "Cristiano Ronaldo": [
        "Cristiano Ronaldo’s leap height during headers has been measured comparable to professional basketball players."
    ],
    "Lionel Messi": [
        "Messi was diagnosed with a growth hormone deficiency as a child and received treatment funded by Barcelona."
    ],
    "Sunil Chhetri": [
        "Sunil Chhetri is one of the few footballers whose international goal tally rivals top global players."
    ],
    "Sachin Tendulkar": [
        "Sachin Tendulkar was once a fast bowler in his early training before switching focus to batting."
    ],
    "Virat Kohli": [
        "Virat Kohli transformed his fitness regime after 2012, setting new endurance benchmarks in Indian cricket."
    ],

    # organizations
    "Amazon": [
        "Amazon’s early recommendation system was built to compensate for its lack of physical storefront browsing."
    ],
    "SpaceX": [
        "SpaceX deliberately designs rockets to fail fast during testing to accelerate engineering learning cycles."
    ],
    "Tesla": [
        "Tesla releases many performance improvements through software updates rather than hardware changes."
    ],
    "Tata": [
        "The Tata Group reinvests a significant portion of profits into philanthropic trusts rather than shareholders."
    ],
    "Toyota": [
        "Toyota’s production system inspired modern lean manufacturing across industries worldwide."
    ],
    "Volkswagen": [
        "Volkswagen operates as a group of semi-independent brands sharing engineering platforms."
    ],
    "BMW": [
        "BMW began as an aircraft engine manufacturer before transitioning into automobiles."
    ],
    "McDonald's": [
        "McDonald’s real estate strategy often generates more revenue than its food operations."
    ],
    "Dominos": [
        "Domino’s early growth relied heavily on guaranteed delivery time rather than menu variety."
    ],
    "Blinkit": [
        "Blinkit pioneered ultra-fast grocery delivery by minimizing warehouse-to-customer distance."
    ]
}

# logic of prediction based on available data.


def filter(current, entities, current_attr, answer):
    
    #Eliminates entities that do not satisfy the given attribute constraint.
    
    return [
        entity for entity in current
        if entities[entity][current_attr] == answer
    ]


def evaluate(current, entities, current_attr):
   
  #  Evaluates how well an attribute splits the remaining entities.
  #  Lower score = better split (more balanced).
   
    true = 0
    false = 0

    for entity in current:
        if entities[entity][current_attr]:
            true += 1
        else:
            false += 1

    return abs(true - false)


def select(current, entities, attr, used_attr):
   
  #  Selects the attribute that best reduces uncertainty among the remaining entities.
    
    best_attr = None
    best_score = float("inf")  # start score as infinity

    for current_attr in attr:
        if current_attr in used_attr:
            continue

        score = evaluate(current, entities, current_attr)

        if score < best_score:
            best_score = score
            best_attr = current_attr

    return best_attr


def contradict(current):
    
   # Checks if no entities remain after filtering inconsistent answers.
 
    return len(current) == 0
    
   
# Working

def ask(question):
    
    # Ask a yes/no question to the user and return True or False.
   
    while True:
        ans = input(question + " (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        elif ans in ("n", "no"):
            return False
        else:
            print("Please answer with 'y' or 'n'.")


def show_fact(entity):
   
    # Show fact about the entity.
   
    if entity in facts and facts[entity]:
        print("\nDid you know?")
        print(facts[entity][0])


def guess():
    print("Think of one entity from the list.")
    print("Answer the questions honestly.\n")
    
    print("Available entities:") #Prints the list of entities
    for e in entities:
        print("-", e)
    print()

    current = list(entities.keys())
    used_attr = set()

    while len(current) > 1:
        current_attr = select(current, entities, attr, used_attr)

        if current_attr is None:
            break

        used_attr.add(current_attr)
        answer = ask(questions[current_attr])

        current = filter(current, entities, current_attr, answer)

        if contradict(current):
            print("\nYour answers contradict each other.")
            return

    if len(current) == 1:
        final = current[0]
        print("\nYour chosen entity is:", final)
        show_fact(final)
    else:
        print("\nCould not determine the entity with certainty.")
        
if __name__ == "__main__" :
    guess()  
    
    
