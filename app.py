from flask import Flask, render_template, request, redirect, url_for, session
import random
# only made with Flask
app = Flask(__name__)
app.secret_key = 'supersecretkey'

stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]

word_list = ["master", "vettaikaran", "kaithi", "vikram", "thuppakki", "karnan", "villu", "dada", "theri", "sarkar",
             "titanic", "meryl", "gandhi", "einstein", "kolam", "pandora", "galaxy", "potter",
             "berlin", "mars", "everest", "serena", "putin", "beethoven", "gatsby", "saturn",
             "koala", "hawking", "beyonce", "mozart", "siam", "sphinx", "zuckerberg", "pluto",
             "shakespeare", "monalisa", "freddie", "eiffel", "apollo", "olympus", "zelensky",
             "peacock", "kaala", "matrix", "skyscraper", "turing", "daffodil", "spider", "cairo",
             "nile", "aristotle", "maradona", "sputnik", "guinness", "cleopatra", "mercury",
             "kilimanjaro", "unicorn", "kathmandu", "thanos", "columbus", "darwin", "mcqueen",
             "glacier", "yosemite", "kimono", "liberty", "cleveland", "himalayas", "phoenix",
             "asteroid", "komodo", "kryptonite", "roosevelt", "netflix", "amsterdam", "dicaprio",
             "romulus", "everglades", "toucan", "socrates", "tesla", "pokemon", "vesuvius",
             "ankara", "timberlake", "neptune", "medusa", "buffalo", "picasso", "hercules",
             "pyramid", "hawaii", "sherlock", "venice", "dinosaur", "armstrong", "bengal",
             "julius", "sydney", "tajmahal", "brazil", "sahara", "giza", "oklahoma", "supernova",
             "sundar", "lagoon", "vegas"]
hints = [
    "An expert or skilled worker.",
    "A famous Tamil movie starring Vijay.",
    "A 2019 Tamil movie directed by Lokesh Kanagaraj.",
    "A 2022 Tamil action thriller movie.",
    "A 2012 Tamil action movie starring Vijay.",
    "A 2021 Tamil movie based on the story of Karnan.",
    "A 2009 Tamil action movie starring Vijay.",
    "A 2023 Tamil drama film.",
    "A 2016 Tamil movie starring Vijay.",
    "A 2018 Tamil political action movie starring Vijay."
    "A famous ship that sank in 1912.",
    "First name of the actress who starred in 'The Devil Wears Prada'.",
    "The leader of the Indian independence movement.",
    "Theoretical physicist known for the theory of relativity.",
    "Traditional Tamil art form made with rice flour.",
    "The name of the planet in 'Avatar'.",
    "A system of millions or billions of stars.",
    "A famous young wizard created by J.K. Rowling.",
    "Capital city of Germany.",
    "The fourth planet from the Sun.",
    "The highest mountain on Earth.",
    "A famous female tennis player with 23 Grand Slam titles.",
    "The President of Russia.",
    "A famous composer of classical music.",
    "The main character in 'The Great Gatsby'.",
    "The planet known for its prominent ring system.",
    "A marsupial native to Australia.",
    "A famous theoretical physicist who worked on black holes.",
    "A world-renowned singer and performer.",
    "A prolific and influential composer of classical music.",
    "The former name of Thailand.",
    "A mythical creature with the body of a lion and the head of a human.",
    "The co-founder of Facebook.",
    "The dwarf planet once considered the ninth planet in our solar system.",
    "A renowned English playwright and poet.",
    "A famous painting by Leonardo da Vinci.",
    "The lead singer of the rock band Queen.",
    "A famous tower in Paris.",
    "The name of NASA's moon missions.",
    "The home of the Greek gods in mythology.",
    "The President of Ukraine.",
    "A large bird known for its colorful tail feathers.",
    "A Tamil movie starring Rajinikanth.",
    "A sci-fi film series about a simulated reality.",
    "A tall, modern building.",
    "The father of computer science.",
    "A type of flowering plant also known as a narcissus.",
    "A famous superhero who got his powers from a radioactive bite.",
    "The capital of Egypt.",
    "The longest river in the world.",
    "An ancient Greek philosopher.",
    "A legendary Argentine football player.",
    "The first artificial satellite launched into space.",
    "A book of world records.",
    "The last Pharaoh of Egypt.",
    "The smallest planet in the solar system.",
    "The highest mountain in Africa.",
    "A mythical horse with a single horn.",
    "The capital of Nepal.",
    "A Marvel supervillain who collected the Infinity Stones.",
    "The explorer who discovered America.",
    "The scientist who developed the theory of evolution.",
    "A famous fashion designer known for his car racing legacy.",
    "A large, slow-moving mass of ice.",
    "A national park known for its giant sequoias.",
    "A traditional Japanese garment.",
    "A colossal statue in New York Harbor.",
    "A city in Ohio named after a US President.",
    "A mountain range in Asia, home to the world's highest peaks.",
    "A mythical bird that regenerates from its ashes.",
    "A small rocky body orbiting the sun.",
    "A large lizard species found in Indonesia.",
    "A fictional material from Superman's home planet.",
    "The 32nd President of the United States.",
    "A popular streaming service.",
    "The capital city of the Netherlands.",
    "The actor who starred in 'Titanic'.",
    "The founder of Rome in Roman mythology.",
    "A subtropical wetland in Florida.",
    "A colorful bird known for its large beak.",
    "An ancient Greek philosopher known for his method of questioning.",
    "An inventor known for his work with electricity.",
    "A franchise of video games and anime featuring creatures to be caught.",
    "An active volcano in Italy.",
    "The capital city of Turkey.",
    "A famous singer and actor known for 'Cry Me a River'.",
    "The eighth planet from the sun.",
    "A Greek monster with snakes for hair.",
    "A large, herbivorous mammal native to North America.",
    "A Spanish painter known for Cubism.",
    "A Roman hero known for his strength.",
    "A monumental structure in Egypt.",
    "An island state in the US known for its beaches and volcanoes.",
    "A famous detective created by Arthur Conan Doyle.",
    "A city known for its canals and gondolas.",
    "Extinct reptiles that once roamed the Earth.",
    "The first man to walk on the moon.",
    "A breed of tiger found in India.",
    "A Roman general and dictator.",
    "A major city in Australia.",
    "A famous mausoleum in India.",
    "The largest country in South America.",
    "The largest hot desert in the world.",
    "The site of ancient pyramids in Egypt.",
    "A US state known for its Great Plains.",
    "A stellar explosion that occurs at the end of a star's lifecycle.",
    "The CEO of Google.",
    "A shallow body of water separated from a larger body by barrier islands or reefs.",
    "A city in Nevada known for its vibrant nightlife."
]


@app.route('/')
def index():
    session['word'] = random.choice(word_list)
    session['hint'] = hints[word_list.index(session['word'])]
    session['guessed_letters'] = ['_'] * len(session['word'])
    session['incorrect_guesses'] = 0
    session['stage'] = stages[-1]
    return render_template('index.html', stage=session['stage'], guessed_letters=session['guessed_letters'])


@app.route('/guess', methods=['POST'])
def guess():
    user_input = request.form['letter'].lower()
    if user_input == "hint":
        return render_template('index.html', stage=session['stage'], guessed_letters=session['guessed_letters'],
                               hint=session['hint'])

    if user_input in session['word']:
        for index, letter in enumerate(session['word']):
            if letter == user_input:
                session['guessed_letters'][index] = letter
    else:
        session['incorrect_guesses'] += 1

    if ''.join(session['guessed_letters']) == session['word']:
        return render_template('index.html', stage=session['stage'], guessed_letters=session['guessed_letters'],
                               message="Congratulations! You guessed the word: " + session['word'])

    if session['incorrect_guesses'] >= len(stages) - 1:
        return render_template('index.html', stage=stages[0], guessed_letters=session['guessed_letters'],
                               message="Game Over! The word was: " + session['word'])

    session['stage'] = stages[-(session['incorrect_guesses'] + 1)]
    return render_template('index.html', stage=session['stage'], guessed_letters=session['guessed_letters'])


@app.route('/restart')
def restart():
    session.clear()
    return redirect(url_for('index'))


@app.route('/quit')
def quit():
    return render_template('quit.html')


if __name__ == '__main__':
    app.run(debug=True)
