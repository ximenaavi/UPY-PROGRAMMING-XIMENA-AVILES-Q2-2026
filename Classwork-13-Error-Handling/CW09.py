#INPUT
pronouns = ['Yo', 'Tú', 'Él', 'Nosotros', 'Vosotros', 'Ellos']
endings = {
    'ar' : ['o','as', 'a', 'amos', 'ais', 'an'],
    'er' : ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir' : ['o', 'es', 'e', 'imos', 'is', 'en']
}
verb = input("Give me a verb in infinive form: ")   #   Get the  verb from user

#PROCESSS 
valido = True

if verb != verb.strip():
    print("El verbo no debe tener espacios extra")
    valido = False

if valido:
    if verb != verb.lower():
        print("El verbo debe escribirse en minúsculas")
        valido = False

if valido:
    stem = verb[:-2]    #Get the stem from the given verb
    ending = verb[-2:]  #Get the ending from the given verb
    try:
        conjugations = endings[ending]
    except KeyError:
        print("El verbo debe terminar en ar, er o ir")
        valido = False

#OUTPUT
if valido:
    for index, pronoun in enumerate(pronouns):
        termination = conjugations[index]
        print(f"{pronoun} {stem}{termination}")