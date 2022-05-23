
original = str(input("Digit your sentence: ").lower().split())

words = original.split()
print(words)

new_words = []
    
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else: 
     vowel_pos = 0
     for letter in word:
         if letter not in "aeiou":
             vowel_pos = vowel_pos + 1
         else:
            break

    cons = word[:vowel_pos]
    the_rest = word[vowel_pos:]
    new_word = the_rest + cons + "yay"
    new_words.append(new_word)

    output = "".join(new_words)

    print(output)