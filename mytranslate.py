#!/usr/bin/python3
'''
This program is about a set of actions that a person will take depending on the weather. It is a translator between English and Spanish
'''
EtoS = {'If' : 'Si', 'sunny' : 'Soleda', 'Tomorrow' : 'Manana', 'I' : 'Yo',
        'will' : 'sera', 'go' : 'vamos', 'to' : 'a', 'the' : 'el', 'beach' : 'playa', 'with' : 'con', 'my' : 'mi',
        'friends':'amigos','snows':'nieves','ski':'esqui','resort':'recurso','family':'familia',
        'rains':'lluvias','stay':'permanecer','indoors':'adentro','and':'y',                                            #This is the dictionary of words translated from English to Spanish.
        'watch':'reloj','favourite':'favorite','movie':'peliculas','weather':'clima','yesterday':'ayer',
        'for':'para','a':'una','hike':'caminata','on':'en',          
        'small':'pequena','hill':'colina','near':'cerca',
        'house':'casa','then':'tomar','dog':'perro','dogs':'perros','out':'afuera','walk':'caminar',
        'Regardless':'independientermente','of':'de','order':'orden','large':'grande',
        'pepperoni':'pepperoni','pizza':'pizza','tomorrow':'manana','dinner':'cena','it':'eso','is':'es','like':'mi gusta','take':'tomar','regardless':'independientemente','two':'dos','best':'el mejor','pizzas':'pizzas','friend':'amigo','a':'uno','mine':'mio','movies':'películas','dogs':'perros','three':'tres','cat':'gata','cats':'gatas'}


StoE = dict([(value,key) for key, value in EtoS.items()]) #Simplifies the process of reversing the entire dictionary.
dicts = {'English to Spanish' : EtoS, 'Spanish to English' : StoE} #Defines the dictionary to the given directions.

def translateWord(word, dictionary) : #This function uses if statements to tell the function what to do if there words/characters in the phrase.

    if word in dictionary.keys() : #Uses an if loop to go through the keys in the dictionary.
        return dictionary[word] #Returns the answer if it finds a word.
    elif word != '' :
        return '"' + word + '"' #The elif function states that to what to do if the function has no value to the key.
    return word

def translate(phrase, dicts, direction) :
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Uppercase letters are defined here
    LCletters = 'abcdefghijklmnopqrstuvwxyz' #Lowercase letters are defined here
    letters = UCletters + LCletters #This combines the upper and lower case letters into a new function called letters.
    dictionary = dicts[direction] #This defines the dictionary to the direction of the translation taking place.
    translation = ''
    word = ''
    for character in phrase : #A for loop that looks for every character in the phrase.
        if character in letters : #An if loop that looks for every character in the letters.
            word = word + character #This adds the word to the character.
        else : 
            translation = translation + translateWord(word, dictionary) + character #This tells the loop to add the translated phrase + the character.
            word = ''
    translation = translation + translateWord(word, dictionary) 
    return translation + "."

sentence = 'Regardless of the weather, I will order pepperoni pizzas tomorrow for dinner.' #The english sentence being used to translate into spanish.
translated = translate(sentence, dicts, 'English to Spanish') #Gives the direction for the sentence to be translated into spanish.
print(translated) #Prints the translated sentence.
print('--------------------------------------')
print('Input:', sentence) #This prints the orignal sentence + the word input to determine that this is being translated.
print('Output:', translated) #This prints the translated sentence + the word output to determine that this has been translated.
print('--------------------------------------')
sentence = ' Yo sera vamos afuera a el playa con dos de mi elmejor amigos' #The spanish sentence being translated into english.
translated = translate(sentence, dicts, 'Spanish to English') #Gives the direction for the sentence to be translated into English.
print('Input:', sentence) #This prints the orignal sentence + the word input to determine that this is going to be translated.
print('Output:', translated) #This prints the translated sentence+ the word output to determine that this has been trasnlated.
print('--------------------------------------')

def reverseDictionary(EtoS):                        #The function that reverses the the dictionary.
   EtoS={value:key for key ,value in EtoS.items()}
   print(EtoS)
reverseDictionary(EtoS)

