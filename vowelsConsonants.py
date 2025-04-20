def count_v_c(string):
    vowels='aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    for char in string:
         if char.isalpha():
           if char in vowels:
              vowel_count += 1
           else:
              consonant_count += 1
         return vowel_count, consonant_count
input_string = input("Enter a string: ")
vowels, consonants = count_v_c(input_string)
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
