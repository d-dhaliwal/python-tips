# https://docs.python.org/3/library/typing.html#typing.Generator



# 💥💥💥 Simple generator: yield values one by one
# This function pauses to return a value to the outer scope, then proceeds
DICTIONARY = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cat',
    'd': 'dog',
    'e': 'egoseismic',
    'f': 'facepalm',
    'g': 'gringo',
    'h': 'hilarious',
    'i': 'iPhone',
    'j': 'John Lennon',
    'k': 'KDE',
    'l': 'lemonsaurus',
    'm': 'Mickey Mouse',
    'n': 'Netherrealm',
    'o': 'of course',
    'p': 'pokerface',
}

def alphabet():
    for letter, word in DICTIONARY.items():
        yield word  # yield values one by one




# 💥💥💥 High-level API: just iterate it
for word in alphabet():
    print(word)
# -> apple
# -> banana
# -> ...



# 💥💥💥 Low-level usage: use next() to obtain another value.
g = alphabet()
print(g)  # -> <generator object alphabet at 0x7f425c7bbe40>
word = next(g)  # 'apple'
print(word)  # -> 'apple'





# 💥💥💥 WHen it reaches the end, a StopIteration error is raised

# This generator `g` will raise a StopIteration immediately because it's been exhausted in the previous example.
# It has nothing else to yield
try:
    while True:
        word = next(g)  # raises: StopIteration
        print(word)
except StopIteration:
    print('-- done')



# 💥💥💥 Generators can also receive values: they support bi-directional communication!
# The `yield` keyword can also *receive* values: a generator becomes a "listener" for incoming values
# In this example, `alphabet()` gets a value

def alphabet():
    """ Example generator with bi-directional data flow

    Input: letters
    Output: words
    """
    word = None
    while True:
        # Communication point:
        # Input: a letter
        # Output: a word
        letter = yield word
        word = DICTIONARY[letter]  # convert it into a word

    # You can also return a value.
    # We'll check this example out later
    return word  # Speak your final word


g = alphabet()
next(g)  # Initialize the generator. It returns `None` (the initial word)

print(g.send('e'))  # egoseismic
print(g.send('f'))  # facepalm
print(g.send('h'))  # hilarious
g.close()  # we're done with it. Returns `None`, always





# 💥💥💥 It is possible to raise an error "into" the generator and catch it there

def alphabet():
    word = None
    while True:
        # Communication point
        try:
            letter = yield word
        # If we were given an exception, return a default word
        except KeyError:
            word = '(default)'
        else:
            word = DICTIONARY[letter]  # convert it into a word


g = alphabet()
next(g)  # Initialize the generator. It returns `None` (the initial word)

print(g.throw(KeyError()))  # (default)
print(g.send('i'))  # iPhone
g.close()

# NOTE that:
# When a generator throws an exception, it exits. You can't continue consuming the items it generates.







# 💥💥💥 A generator that uses `yield` to request data from the outside
# This use case, however, is a little inside-out. Makes very little sense. But you can :)

def gimme_words():
    # Start building a sentence
    sentence = []
    for letter in 'abcdef':
        # Give every letter to some external caller and expect them to give us a word
        word = yield letter
        # Keep building the sentence
        sentence.append(word)

    # Return the sentence!
    return ' '.join(sentence)


# Initialize the generator
g = gimme_words()

# Keep going while we can
try:
    word = None
    while True:
        # Send the initial `None` to the generator. We just have to.
        letter = g.send(word)
        # Convert the letter that the generator gives us into a word and give it back to the generator
        word = DICTIONARY[letter]
# When done, print the resulting value
except StopIteration as e:
    print(e.value)
finally:
    g.close()
