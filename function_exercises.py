# %%


# %% [markdown]
# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# %%
# function asks if its a 2 or not
def is_two(something):
    # check to see if something is equal to two or not
    if something == 2 or something == '2':
        # if it is then it returns true
        return True
    # if not it returns false
    else:
        return False

# %% [markdown]
# 

# %%


# %%
# instructor 
#def is_two(my_input):
    # if my_input == 2 or my_input == '2':
    #   return True
    # else:
    #   return False


# ooorrrrr
    #return my_input == 2 or my_input == '2'

# %% [markdown]
# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# %%
# f(x) to check for vowels
def is_vowel(letter):
        # need to lowercase the input
        letter = letter.lower()
        # made a list of vowels
        vowels = ['a','e','i','o','u']
        # if statement to check against the list
        if letter in vowels:
            return True
        # if not on list then return is False
        else:
              return False

# %%


# %% [markdown]
# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this

# %%
# func for checking if letter is a consonant
def is_consonant(letter):
    # lowercasing it
    letter = letter.lower()
    # checking against the previous vowel list that was created
    if is_vowel(letter) == True:
        #if its on the vowel list then it returns false for the consonant
        return False
        # returns true if not on the vowel list
    else:
        return True

# %%


# %%
# instructor

#def is_consonant(my_string):
    #is_vowel() == False
    #len() == 1
    #== a letter==> .isalpha()

    #return not is_vowel(my_string) and len(my_string) == 1 and my_string.isalpha()

# %% [markdown]
# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
# 

# %%
#need func that accept a string and caps the first letter if its a consonant




# not finished.
    


def capitalize_starting_consonant(my_string):
    if len(my_string.split()) ==1:
    
        if is_consonant(my_string[0]):
            my_new_string += my_string[0].upper()
            my_new_string += my_string[1:]
        else:
            my_new_string = my_string
    else:
        return my_string

# %%


# %% [markdown]
# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# %%
# func for calculating a tip
def calculate_tip(amount, tip_pct):
    # need a float for the decimals and define the input
    amount = float(amount)
    tip_pct = float(tip_pct)
    # tip calculation
    tip_amt = tip_pct * amount
    total = tip_amt + amount
    # states the total bill with tip and the tip amount separately
    return (f'{total} is total with tip and {tip_amt} is the tip by itself')









# %%


# %% [markdown]
# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# %%
# function for a discount
def apply_discount(org_price, dis_pct):
    #setting up the inputs as floats
    org_price = float(org_price,)
    dis_pct = float(dis_pct,)
    # calc for discount
    dis_price = org_price * dis_pct
    apply_disc = org_price - dis_price

# returns the total after discount and states the percentage of discount
    return (f'Your total is {apply_disc} after your discount of {dis_pct * 100}%')

# %%


# %% [markdown]
# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# %%
# need func to take commas out of a number string
def handle_commas(string_num):
    my_new_num = ''
    for dig in string_num:
        if dig == ',':
            continue
        else:
            my_new_num += dig
    return int(my_new_num)



# %%


# %% [markdown]
# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# %%
# function for translating grade number to letter grade
def get_letter_grade(num_grade):
    # making sure its an integer
    num_grade = int(num_grade)
    # if statements for the split between letter grades
    if num_grade >= 90:
        return 'A'
    if num_grade >= 80:
        return 'B'
    if num_grade >= 70:
        return ('C')
    if num_grade >= 60:
        return ('D')
    else:
        return ('F')
    


# %%


# %% [markdown]
# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# %%

# function for removing vowels from a string
def remove_vowels(string):
    # lower casing the string
    string = str.lower(string)
    # list of vowels
    vowel = ['a','e','i','o','u']
    # checking each letter in the string for letters not in the vowel list
    result = [letter for letter in string if letter not in vowel ]
    # removing and joining the letters that arent on the vowel list together
    result = ''.join(result)

    return result




# %%


# %% [markdown]
# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#         - anything that is not a valid python identifier should be removed
#         - leading and trailing whitespace should be removed
#         - everything should be lowercase
#         - spaces should be replaced with underscores
#         - for example:
#             - Name will become name
#             - First Name will become first_name
#             - % Completed will become completed

# %%
# need function for removing all the random stuff from the string

#def normalize_name(string):
    # lowercasing, removing space in from and rear, and replaceing the spaces with '_'
   # string = str.lower(string)
    #string = string.strip()
    #tring = string.replace(" ","_")
    
   

   # return string
# just get it from the help....so confused

# %%


# %% [markdown]
# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#         - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#         - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# %%
# function to add a cumulative list for results
def cumulative_sum(list):
    
    cum_list = []
    length_list = len(list)
    cum_list = [sum(list[0:x:1]) for x in range(0, length_list+1)]
    return cum_list[1:]





# %% [markdown]
# Additional Exercise
# 
# - Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

# %% [markdown]
# 

# %% [markdown]
# 


