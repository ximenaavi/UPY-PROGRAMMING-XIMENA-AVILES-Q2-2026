
#INPUT
pronouns = ['yo', 'tu', 'el', 'nosotros', 'vosotros']

endings = {
    'ar' : ['o','as', 'a', 'amos', 'ais', 'an'],
    'er' : ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir' : ['o', 'es', 'e', 'imos', 'is', 'en']
}
verb = input("Give me a verb in infinive form: ")   #   Get the  verb from user

#PROCESSS 

stem = verb[:-2]    #Get the stem from the given verb
ending = verb[-2:]  #Get the ending from the given verb
conjugations = endings[ending]

#OUTPUT
for index, pronoun in enumerate(pronouns):
    termination = conjugations[index]
    print(f"{pronoun} {stem}{termination}")