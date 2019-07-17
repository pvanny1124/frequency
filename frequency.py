import math

def getNthMostFrequentCharacters(n):
  with open("./words.txt") as file: 

    # get rid of any excess spaces or newlines in the file
    data = file.read().replace('\n', '').replace(' ', '')

    #declare a dictionary that will hold the frequencies
    letters_map = dict()

    # count the frequencies of each character
    for character in data:
      # shorthand to check if the character already exists, then increment by 1. 
      # If not, add the character to the dictionary and save 1 as it's value.
      letters_map[character] = letters_map.get(character, 0) + 1 

    # calculate the sum of all frequencies
    sum_of_all_frequencies = sum(letters_map.values())

    # replace the frequency of each letter with the 
    # probability of each letter showing up in the file
    # using the formula: probability of letter = (frequency of letter / sum of frequencies of all letters)
    for letter in letters_map:
      letters_map[letter] = letters_map[letter] / sum_of_all_frequencies

    # sort the dictionary by value using the second value of each tuple that the map.items() 
    # function holds which is the frequency associated to a letter.
    sorted_frequencies = sorted(letters_map.items(), key = lambda letter:letter[1], reverse = True)
    return sorted_frequencies[:n]

def sumOfAllOtherProbabilites(most_frequent_chars):
  # get sum of probabilities that are not in top N.
  
    sum_of_top_n_probabilities = 0
    for (letter, probability) in most_frequent_chars:
      sum_of_top_n_probabilities += probability

    return 1 - sum_of_top_n_probabilities

def getCentralAngles(chars):
  # calculate central angle of segment for each letter
  # using the formula: probability of letter = (central angle of segment / 2pi)
  for index, (letter, probabilty) in enumerate(chars):
    central_angle = probabilty * math.pi
    chars[index] = (letter, central_angle, probabilty)
  return chars
