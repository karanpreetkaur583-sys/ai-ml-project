# Mood Music Recommender (Simple + Smart)

# Step 1: Training data
sentences = [
    "i am happy",
    "i feel good",
    "this is amazing",
    "i am sad",
    "i feel bad",
    "this is terrible",
    "i am angry",
    "this is frustrating",
    "i feel calm",
    "i am relaxed"
]

moods = [
    "Happy", "Happy", "Happy",
    "Sad", "Sad", "Sad",
    "Angry", "Angry",
    "Relaxed", "Relaxed"
]

stop_words = ["i", "am", "is", "the", "this"]

data = {
    "Happy": {},
    "Sad": {},
    "Angry": {},
    "Relaxed": {}
}

# Training
for i in range(len(sentences)):
    words = sentences[i].split()
    mood = moods[i]
    
    for word in words:
        if word not in stop_words:
            data[mood][word] = data[mood].get(word, 0) + 1

# Prediction function
def predict(text):
    words = text.split()
    
    score = {m: 0 for m in data}
    
    for mood in data:
        for word in words:
            if word in data[mood]:
                score[mood] += data[mood][word]
    
    best_mood = max(score, key=score.get)
    return best_mood

# Music recommendation
def recommend(mood, genre):
    music = {
        "Happy": {
            "pop": ["Shape of You", "Good Time"],
            "slow": ["Perfect", "Photograph"]
        },
        "Sad": {
            "pop": ["Someone Like You", "Let Her Go"],
            "slow": ["Fix You", "All I Want"]
        },
        "Angry": {
            "pop": ["Believer", "Stronger"],
            "slow": ["Numb", "Boulevard of Broken Dreams"]
        },
        "Relaxed": {
            "pop": ["Sunflower", "Lovely"],
            "slow": ["Lo-fi Beats", "Calm Piano"]
        }
    }
    
    return music.get(mood, {}).get(genre, ["No songs found"])

# -------------------------
# User Input
# -------------------------
user_input = input("How are you feeling today? ").lower()

mood = predict(user_input)

print("Detected Mood:", mood)

# NEW FEATURE
genre = input("What type of music do you like? (pop/slow): ").lower()

songs = recommend(mood, genre)

print("\nRecommended Songs:")
for song in songs:
    print("-", song)