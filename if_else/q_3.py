# Write a program that takes a character as input and prints whether it is a vowel or a consonant.

alph= (input("Enetr A Character: "))
alph=alph.lower()

if(alph=='a' or alph=='e' or alph=='i'  or alph=='o'  or alph=='u'  ):
    print("The Character Is Vowel")
else:
    print("The Character Is Consonant")