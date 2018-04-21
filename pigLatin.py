def pigLatin(string):
    vowels = ['a','e','i','o','u','y']
    consonants= ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z', 'W']
    consonantBunch = ['h', 'c','g','l','s','t']
    for  i,v,k in zip(consonants,vowels,consonantBunch):
        if(v == string[0] and v != string[0]):
            if(v == string[1] or k == string[1]):
                doubleCons = string[3:] + string[0] + string[1] + "atasay"
                result = doubleCons
                break
        elif(i == string[0]):
            vowelLatin = string + "ay"
            result = vowelLatin
            break

        elif(v == string[0]):
            latinified = string[1:] + string[0] + "ay"
            result = latinified

    print(result)
    return result;

pigLatin("cheers")
#
# print("TEST CASES")
# print("-----------------------------------------------------------")
# print("NORMAL WORDS")
# print(" ")
# print("pig = igpay")
# pigLatin("pig")
# print("-----------------------------------------------------------")
# print("latin = atinlay")
# pigLatin("latin")
# print("-----------------------------------------------------------")
# print("banana = ananabay")
# pigLatin("banana")
# print("-----------------------------------------------------------")
# print("duck = uckday")
# pigLatin("duck")
# print("-----------------------------------------------------------")
# print("WORDS BEGINNING WITH VOWELS")
# print(" ")
# print("")
