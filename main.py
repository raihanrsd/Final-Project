
"""
THIS PROGRAM IS THE PROGRAMMING EXTRAVAGANZA.
IT CAN DO COMPLEX DNA, mRNA, AMINO ACID OR PROTEIN SEQUENCE ANALYSIS
IT CAN ALSO GENERATE PASSWORD AND RESTRICT USER TO ACCESS A FILE THROUGH TWO LAYERS OF SECUTRITY
IT CAN MAKE RANDOM IDENTIFICATION NUMBER FOR PRODUCTS OF A COMPANY AND ALSO PROVIDE A GOOD CUSTOMER SERVICE AND ALSO SERVES THE COMPANY BY STORING THEIR INFO
IT DOES MAKES INTERESTING OUTPUT BASED ON WHO YOUR CRUSH IS xd
MOREOVER IT ALSO HAS AN EDUCATIVE MATHING GAME THROUGH WHICH YOU WILL BE ALBE TO CHECK YOUR CALCULATING SKILLS . IT CAN ALOS BE USED BY THE TEACHES TO INCREASE THE CALCULATING SKILLS OF THE STUDENTS
THE FUN STILL DOESN'T END
IT CAN MAKE BAR DIAGRAM THROUGH THE PROVIDED INFORMATION
LASTLY YOU CAN ALSO MANIPULATE IMAGES THROUGH THIS PROGRAM
WHOOOOOO THATS A LOT TO TAKE IN FOR ONE PROJECT BUT DONT WORRY COMMENTS ARE GIVEN TO GUIDE YOU THROUGH THE PROGRAM
"""


import random
# imports all the random functions which will be used a lot of times
import seaborn as sns
import matplotlib.pyplot as plt
# helps to make nice bar graphs 
from simpleimage import SimpleImage
# imports all the image functionality


def main():
    intro()
    # gives the general introduction of the program

    select_program = input('Which Program do you want to run?(click enter to end) ')
    # prompts the user to select what type of program he wants to run.
    while select_program != '':
        # keeps the program going until the user wants to end it by just clicking enter
        if select_program == "a" or select_program == 'A' or select_program == 'sequence analysis':
            #starts the DNA , mRNA anD Protien sequence analysis program 
            sequence_analysis()
            select_program = input('Which Program do you want to run?(click enter to end) ')
        elif select_program == "b" or select_program == 'B' or select_program == 'password generator':
            # starts the password generator program
            password_generator()
            select_program = input('Which Program do you want to run?(click enter to end) ')
        elif select_program == "c" or select_program == 'C' or select_program == 'production to customer':
            # starts the production to customer program
            production_to_customer()  
            select_program = input('Which Program do you want to run?(click enter to end) ')
        elif select_program == "d" or select_program == "D" or select_program == 'match_maker':
            # initiates the match making
            match_maker()
            select_program = input('Which Program do you want to run?(click enter to end) ')
        elif select_program == "e" or select_program == "E" or select_program == 'mathing':
            # plays the game
            mathing_game()
            select_program = input('Which Program do you want to run?(click enter to end) ')
        elif select_program == 'f' or select_program == 'F' or select_program == "bar representation":
            # creates bar diagram of the provided information
            bar_representation()
            select_program = input('Which Program do you want to run?(click enter to end) ')
        elif select_program == 'g' or select_program == 'G' or select_program == "image manipulation":
            # can manipulate different image in different ways through program
            image_manipulation()
            select_program = input('Which Program do you want to run?(click enter to end) ')
        else:
            # prompts user to input a valid input until the user has done so this will show this and continuously loop
            print('Please type a valid input in order to activate any program. \n:')
            select_program = input('Which Program do you want to run?(click enter to end) ')

    print('WHOOOO! The extravaganza has ended.')
    # signals the end of an amazing program






def intro():
    # introductes all the functionalities of each program shortly
    print('Welcome to Programming Extravaganza....')
    print("You can do all these amazing stuffs through this single program. \n Press the program's name or the key assigned to it for activating it.")
    print('')
    print('Sequence Analysis is an awesome program which can do a whole lot of computation related to DNA, mRNA and Amino Acid sequence in Protein.')
    print("enter a/A or write it's name in prompt to activate this program.")
    print('')
    print('Pass generator is a data security based program. You can get an amazing idea of how to generate a password, set password and change it.')
    print("enter b/B or write it's name in prompt to activate this program.")
    print('')
    print('Production to customer is a business oriented program. It is designed to set a unique no of code for every product and the customers can also verify the validity of those. It also has a lot of other functions.')
    print("enter c/C or write it's name in prompt to activate this program.")
    print('')
    print("It's a fun program to explain how different random selection by a lot of application is done")
    print("enter d/D or write it's name in prompt to activate this program.")
    print('')
    print("Mathing is an educative calculative game made to improve calculating skills")
    print("enter e/E or write it's name in prompt to activate this program.")
    print('')
    print('This program simply give a bar graphing of the given data.')
    print("enter f/F or write it's name in prompt to activate this program.")
    print('')
    print('This program can add a bacground to image to a green screened picture. It can also make an image brighter or darker and also add filters to an image.')
    print("enter g/G or write it's name in prompt to activate this program.")
    print('')





def image_manipulation():
    '''
    the real owners of these images / the sites which the images were collected from
    minions1 : wallpaperlist.com
    space : property of wallpapercave.com
    white : wallpapertip.com
    cat : wallpaperaccess.com
    cat1 : pinterest.com
    cat2 : wallpapertip.com
    '''
    '''
    This program can usee the green screen of image to replace the background.
    it can also increase or decrease the brightness of an image.
    Lastly it can also used for adding a custom made filter or made full balck and white image.
    '''
    intro7()
    picture = input('Select a picture: \n')
    #takes the name of image from the user which they want to manipulate
    image = SimpleImage('image/'+ picture + '.jpg')
    # uses the name to open the file with the same name 
    image.show()
    #shows the image
    print('')
    print('Input 1 or green screen for setting the backgrond with an image with a green screen .')
    print('Input 2 or bright to reduce or increase the brightness or darkness.')
    print('Input 3 or filter in order to activate or use bw or custom made filter.')
    # explains how to access different functions
    img_manipulation = input('What type of manipulation do you want? ')
    # asks the user to difine what type of image manipulation fo they want to do
    if img_manipulation == '1' or img_manipulation == 'green screen':
        # for green screening
        final_image = green_screen(image)
        final_image.show()
    elif img_manipulation == '2' or img_manipulation == 'bright':
        # for reducing or increasing brightness
        final_image = bright_dark_img(image)
        final_image.show()
    elif img_manipulation == '3' or img_manipulation == 'filter':
        # adding filters
        final_image = filter_creator(image)
        final_image.show()
    else:
        # in case if user inputs any invalid input.
        print('Enter a valid input next time for the program to proceed.')


def intro7():
    print('This program can usee the green screen of image to replace the background.')
    print("it can also increase or decrease the brightness of an image.")
    print('Lastly it can also used for adding a custom made filter or made full balck and white image.')
    print('')


def filter_creator(image):
    print('Type filter to use the filter or bw to make the image black and white')
    # this function helps to apply the filter or set the image black white
    want = input('Do you want BW filter or normal filter(just press enter to retrun the image)? ')
    # asks the user which filter they want
    while want != '':
        # loops over the program until the user just clicks enter
        if want == 'filter':
            intensity = 1
            # this variable can be changed in order to bring desiarable change to the filter to get the best image.
            for pixel in image:
                #loops over each pixel in the image
                average = (pixel.red + pixel.blue + pixel.green) // 3
                # calculates the average value of all three pixels
                if pixel.red > average * intensity:
                    # checks if a pixel is access bright and sets it's value to average and both other pixels value to average as well
                    pixel.red = average
                    pixel.blue = average
                    pixel.green = average
                if pixel.blue > average * intensity:
                    pixel.red = average
                    pixel.blue = average
                    pixel.green = average
                if pixel.green > average * intensity:
                    pixel.red = average
                    pixel.blue = average
                    pixel.green = average
            return image
            # returns the image
        elif want == 'bw':
            for pixel in image:
                # iterates over each pixels and sets all the pixel value to all their average va;ue to produce a black and white image
                average = (pixel.red + pixel.blue + pixel.green) // 3
                pixel.red = average
                pixel.blue = average
                pixel.green = average
            return image
        else:
            want = input('Do you want BW filter or normal filter(just press enter to retrun the image)? ')
            # in case if the user types any sort of invalid input




def bright_dark_img(image):
    print('Type bright ot dark to active get the respective outputs')
    # this function helps to increase or decrease the brightnesss of an image
    want = input('Do you want to make it brighter or darker(just press enter to retrun the image)? ')
    # asks the user what they intend to do
    while want != '':
        if want == 'bright':
            for pixel in image:
                # iterates over each pixels
                if pixel.red * 2 > 255:
                    # the highest value of any pixel can't be more than 255. Otherwise there would be an error
                    pixel.red = 255
                else:
                    # sets the pixel value twice as much if it's double value isn't more than 255
                    pixel.red = pixel.red * 2
                if pixel.blue * 2 > 255:
                    pixel.blue = 255
                else:
                    pixel.blue = pixel.blue * 2
                if pixel.green * 2 > 255:
                    pixel.green = 255
                else:
                    pixel.green = pixel.green * 2
        elif want == 'dark':
            # almost as same function as the bright image 
            # it doesn't need to check anything as the value can't be less than zero while dividing
            # but this division only returns an integer
            for pixel in image:
                pixel.red = pixel.red // 2
                pixel.blue = pixel.blue // 2
                pixel.green = pixel.green // 2
        else:
            # if the user types aby invalid input this pops up and asks the user to enter the valid input
            print('Enter a valid input. ')
        want = input('Do you want to make it brighter or darker(just press enter to retrun the image)? ')
    return image




def green_screen(image):
    # this function helps to change the background of a green screened image
    intensity_threshold = 1.6
    # this helps to measure if a pixel is sufficiently coloured or not
    background = input('Whta type of background do you want? ')
    # asks the user to set a background for the final image
    background = SimpleImage('image/'+ background +'.jpg')
    # loads in the back groung image 
    background.show()
    # displays the back ground image
    for x in range(image.width):
        # this is a nested loop
        # iterates as per the width of the image
        for y in range(image.height):
            # iterates as per the height of the image
            pixel = image.get_pixel(x, y)
            # gets the pixel form the real image to check
            if pixel.green >= ((pixel.red + pixel.blue + pixel.green) // 3) * intensity_threshold:
                # if the value of the green pixel is more than this amount then the pixels are changed
                pixel = background.get_pixel(x, y)
                # gets the pixels from the background image
                image.set_pixel(x, y, pixel)
                # sets the background image pixel in the real image
    return image


def intro6():
    print('This program can be used to make beautiful bar diagrams for the given data file.')

def bar_representation():
    """
    Uses the information in the datafile to create a wonderful bar diagram.
    """
    intro6()
    filename = input('Enter a filename: ')
    # takes the file name from the user
    bar_dict = {}
    # creates an empty dictionary
    if filename != '':
        with open('bar_info/' + filename + '.txt') as f:
            # opens the file with the matching filename
            next(f)
            next(f)
            # skips through the first 2 introductory lines
            count = int(input('Enter the starting year: '))
            # takes input from which year the data shows rthe statistics of.
            start_count = count
            # stores that year variable of count in another variable for later use
            for line in f:
                # iterates through each line of the file except for the line those were skipped
                line = line.strip()
                # strips the line of the new line '\n' charecter which are included as a default
                bar_dict[count] = float(line)
                # add the year to number stats in the bar dictionary setting the year as the key
                count += 1
                # increases the count by 1 which means nexr time through this loop this would take the value for the file of the next year.
        make_bar_plot(bar_dict)
        # this function is used to make the bar graph / diagram
        print('This stat shows the ' + filename + ' starting from the year ' + str(start_count) + ' to ' + str(count))
        # shows from which to which year the stat is and about what it is

def make_bar_plot(count_map):
    """
    Turns a dictionary (where values are numbers) into a bar plot.
    Labels gives the order of the bars! Uses a package called seaborn
    for making graphs.
    """
    # turn the counts into a list
    counts = []
    # loop over the labels, in order
    for label in count_map:
        counts.append(count_map[label])
    # format the data in the way that seaborn wants
    data = {
        'x':list(count_map.keys()),
        'y':counts
    }
    sns.barplot(x = 'x',y = 'y', data= data)
    plt.savefig("plot.png")


def intro5():
    print('This game is basically a calculating game where the game is made harder and harder in each levels. ')
    print('This program can also give rank to a gamer based on his total points.')
    print('')

def mathing_game():
    intro5()
    total_points = 0
    # sets the total point equal to 0
    total_chances = 5
    # sets the total number of chances
    digit = 10
    # sets the total num of digits in the game
    operator = get_operators()
    # gets the operator through this function
    num1 = get_num(digit)
    # gets the num as per the digit
    num2 = get_num(digit)
    expected_result = get_result(num1, num2, operator)
    # calculates the expected result based on both the numbers and mainly the operator  
    given_answer = input('What is ' + str(num1) +' ' + operator + ' ' + str(num2) + '?(click enter to end) \n:')
    # takes an answer from the user but showing them the mathematical expression at the same time
    if given_answer != '':
        # skip option in case if the user want to quit abd just clicks enter
        total_chances = evaluate_answer(expected_result, int(given_answer), total_chances)
        # evaluates the total chances left based on the expected result, given answer in integer and total chances that the user already had
        total_points = evaluate_points(expected_result, int(given_answer), total_points)
        # evaluates the total points left based on the expected result, given answer in integer and total points that the user already had
    while total_chances != 0 and given_answer != '':
        # loops until the user wants to quit or if he is out of chances 
        operator = get_operators()
        num1 = get_num(digit)
        num2 = get_num(digit)
        expected_result = get_result(num1, num2, operator)
        given_answer = input('What is ' + str(num1) +' ' + operator + ' ' + str(num2) + '?(click enter to end) \n:')
        if given_answer != '':
            total_chances = evaluate_answer(expected_result, int(given_answer), total_chances)
            total_points = evaluate_points(expected_result, int(given_answer), total_points)
            digit = level_up(total_points, digit)
            # levels up the game based on the gamers current point and the total number of digit
    rank(total_points)
    #provides a rank to user based on his/her total points



def rank(total_points):
    #provides a rank to user based on his/her total points
    if total_points < 100:
        print('Word harder, better luck next time. Practice on your calculations more.')
    elif total_points >= 100 and total_points < 200:
        print('You can do it keep going. A little bit of more practice will surely turn you into a mathematician.')
    elif total_points >= 200 and total_points < 300:
        print('Impressive! You are doing great.')
    elif total_points >= 300 and total_points < 400:
        print('You are on the verge on becoming an expert keep trying.')
    elif total_points >= 400 and total_points < 500:
        print('Congratulations! You are an expert in this game.')
    elif total_points >= 500 and total-points < 600:
        print('You are more than an expert.')
    elif total_points >= 600 and total_points < 700:
        print('A true math magician.')
    elif total_points >= 700 and total_points < 800:
        print('IQ 190+')
    elif total_points >= 800 and total_points < 900:
        print('Human Calculator.')
    else:
        print('Seriously, are you Ramnujan back form the dead? ')
    
    print("N.B.: Complements are only for those who didn't use calculator and gave most of their answer within 10 seconds.")






def level_up(total_points, digit):
    # this function is used to level up a game by increasing or returning the total digit back to main function which actually determines the number
    level_dict = {
        100 : 100,
        200 : 1000,
        300 : 10000,
        400 : 100000,
        500 : 1000000,
        600 : 10000000,
        700 : 100000000,
        800 : 1000000000,
        900 : 10000000000,
        1000 : 100000000000,
    }      # this dictionary is used to set the levels up in order to make the game more challenging
    if level_dict.get(total_points) != None:
        # checks if the key or required number of points to level up is in the dictionary
        digit = level_dict[total_points]
        #sets the new value of the digit according to the total points
    return digit

def evaluate_points(expected_result, given_answer, total_points):
    # this fucntion is increases the total points based on the given answer to the question
    if given_answer == expected_result:
        #checks if the answer is correct to the expected answer
        total_points += 10
        # adds 10 points if the answer is correct
        print('Your total point is', str(total_points), '.')
        # prints foe clarification
    else:
        # in case if the answer is incorrect
        print('Your total point is', str(total_points), '.')
    return total_points
    #returns the total point


def evaluate_answer(expected_result, given_answer, total_chances):
    # checks the answer and determines if the number of chances that the gamer has got
    if given_answer == expected_result:
        # if the answer is correct doesn't deduct from the chances
        print('That was correct.\nYou have', str(total_chances),'chances remaining.')
    else:
        # deducts one chance if the answer is incorrect
        total_chances = total_chances - 1
        print('That was incorrect. \nYou have', str(total_chances), 'chances remaining.')
    return total_chances


def get_result(num1, num2, operator):
    # determines the result of the mathematical expression based on the given numbers and mainly the operators
    if operator == '+':
        # add if operator is +
        return num1 + num2
    elif operator == '-':
        # subtracts for -
        return num1 - num2
    elif operator == '/' and num2 != 0:
        # checks the operator and num 2 and sends the answer in integer only
        return num1 // num2
    elif operator == '/' and num2 == 0:
        # special case only
        return 0
    return num1 * num2
    # returns multiplication if the operator doesn't match + - or /


def get_operators():
    # randomly generates any of the 4 operators for each random number from 0 to 3
    num = random.randint(0, 3)
    if num == 0:
        return '+'
    elif num == 1:
        return '-'
    elif num == 2:
        return '/'
    return '*'


def get_num(digit):
    # sets the number according to the total number of digits
    num = random.randint(0, digit)
    return num



def intro4():
    print('This is a fun program which would give you a prediction based on who your crush is.')
    print('This is just a fun program and explains how different randomised looking app/game works on the social media.')

def match_maker():
    intro4()
    name = input('Enter your name: ')
    c_name = input("Enter your crush's name: ")
    # collects your and your crush's name
    num = random.randint(0, 100)
    # generates a random number form 0 to 100
    # the predictions are made based on these randomised numbers 
    if num < 15 :
        print("You two should probable just move on. It's a dead end for you both.")
    elif num >= 15 and num < 30:
        print('Find yourself someone better.')
    elif num >= 30 and num < 50:
        print("There is a spark but you two aren't made for each other.")
    elif num >= 50 and num < 70:
        print("There is still hope.", name, "don't give up on", c_name, ".")
    elif num >= 70 and num < 95:
        print(c_name, "has a crush on you.")
    else:
        print('You two are destined to be together.')




def intro3():
    print('This special feature gives the companies a unique way to check the reach and sale of their product while providing efficient customer service as well.')
    print('This program would create batch of product number which are unique and store the informatiion in a special file where the owner or producer can only access it.')
    print('Here another functionality of this program is that the customer can verify if their product is legit even if the perpitrators manage to put an old already sold product number.')
    print("By using a secret key the owner may also check the all the product numbers from a ginormous database which even the ed can't open. ")
    print("Ther is another very well functionality of this program which the corporate companies might implement besides providing customers their valid product. A special file is made in this program which helps to detect how many product has been sold as per the query of the customers.")



def production_to_customer():
    """
    This special feature gives the companies a unique way to check the reach and sale of their product while providing efficient customer service as well.
    This program would create batch of product number which are unique and store the informatiion in a special file where the owner or producer can only access it.
    Here another functionality of this program is that the customer can verify if their product is legit even if the perpitrators manage to put an old already sold product number.
    By using a secret key the owner may also check the all the product numbers from a ginormous database which even the ed can't open. ")
    Ther is another very well functionality of this program which the corporate companies might implement besides providing customers their valid product.
    A special file is made in this program which helps to detect how many product has been sold as per the query of the customers.")
    """
    intro3()
    with open('industry_info/batch_no.txt') as f:
        # opens a file in which the batch no are stored 
        for line in f:
            # iterates over each line in the file and sets the value of batch_no as per the latest batch no
            batch_no = line.strip()
    print("If you want to make a new batch of product code. Input '1' or 'industry production'")
    print("If you want to verfy that your product is valid. Input '2' or 'customer_query'")
    # introduces the user to the functionality
    want = input('What you do you want to do?(click enter to end)  ')
    # asks the user about the operation that thwy want to do and stores the input in the want variable


    if want == '1' or want == 'industry production':
        # this functionality helps the manufacturer to produce randomly generated unique codes for each products with the batch name
        product_per_batch = int(input('How many products do you want to produce per batch?'))
        # asks the manufacturer foe how many products does he want the numbers to be generated 
        for i in range(product_per_batch):
            # iterates as per the total product number and also produces a unique number in each loop
            rand_part = pad(random.randint(0, 9999999), 7)
            # generates a random number of a definite length
            normal_part = pad(i, 5)
            # generates a serial no of definite length
            product_id = rand_part + normal_part
            # sets the product id according to the random and the normal serial part
            product_id = product_id[0:3] + str(batch_no) + product_id[4:]
            # includes batch no with in the program this can be changes according to the will of the user 
            with open('industry_info/product_batch'+ batch_no + '.txt', 'a') as f:
                # creates a new file with all the newly generated numbers
                f.write(product_id + '\n')
        batch_no = int(batch_no) + 1    # adds 1 to the existing batch no
        batch_no = str(batch_no)      # makes the bath no a string
        with open('industry_info/batch_no.txt', 'a') as f:
            # this program set the new batch no in file so that if the manufacturer makes a new batch he would get a new batch no also
            f.write('\n' + batch_no)
    

    elif want == '2' or want == 'customer query':
        # this program helps the user to identify if their product is legit or not based on the provided unique product no
        product_id_cus = input('What is your product ID? ')
        # prompts the user to enter their ID no
        valid_check = ''
        # creates an empty string of valid ckeck which will be later user
        if len(product_id_cus) == 11:
            with open('industry_info/product_batch'+ product_id_cus[3] + '.txt') as f:
                # opens the file corresponding to the batch no
                for line in f:
                    # iterates over each line in the file
                    line = line.strip()
                    # strips the line of any new line charecter
                    if line == product_id_cus:
                        # if the no matches to any number in the file
                        valid_check = product_validity(product_id_cus)
                        # checks if the number is actually valif=d or expired or used through this function 
        elif len(product_id_cus) == 13:
            with open('industry_info/product_batch'+ product_id_cus[3 : 5] +'.txt') as f:
                # works same if the batch no is 2 digit no
                for line in f:
                    line = line.strip()
                    if line == product_id_cus:
                        valid_check = product_validity(product_id_cus)
        elif len(product_id_cus) == 15:
            with open('industry_info/product_batch'+ product_id_cus[3 : 6] + '.txt') as f:
                # does the same work for 3 digits
                for line in f:
                    line = line.strip()
                    if line == product_id_cus:
                        valid_check = product_validity(product_id_cus)
        validity_check(valid_check)
        # finally gives the result for the product based on the valid check result

    elif want == '3' or want == 'list check':
        # this is a unique functionality where the maufacturer can access all the product no if the files are too large to open
        batch_list = []
        # creates an empth list
        batch_no = input('Which batch info do you want? ')
        with open('industry_info/product_batch'+ batch_no + '.txt') as f:
            for line in f:
                # opens the file,  iterates over each line and add the nums to the list
                line = line.strip()
                batch_list.append(line)
        print(batch_list)
        # prints the batch_list
    elif want == '':
        # for skipping the program
        print('The program has ended without doing anything')
    else:
        # if the user types an invalid input
        print('Invalid Input')
        want = input('What you do you want to do?(click enter to end)')



def validity_check(valid_check):
    # this function helps the provide the customer a result if the product is valid or not based on the valid check parameter
    if valid_check == 'valid product':
        print('Your product is valid.')
    elif valid_check == 'invalid product':
        print("Your product is invalid. This product ID is real yet we fear that perpitrators used one of our product code to make a fake product and use the old code. Don't use it.")
    else:
        print('This product is invalid.')


def product_validity(product_id_cus):
    # this function actually check if the product is valid ot not and also if the product has already been expired or sold
    with open('industry_info/sold_products.txt') as f:
        # opens the sold dictionary
        for line in f:
            line = line.strip()
            if line == product_id_cus:
                # if the product is already sold returns invalid
                return "invalid product"
    with open('industry_info/sold_products.txt', 'a') as f:
        # add the now sold product to the sold list for keeping the records so that the old code can't be valid anymore
        f.write('\n' + product_id_cus)
    return 'valid product'

def pad(num, length):
    # it adds 0 if the length of the number is less thean the desired lenght
    num_str = str(num)
    while len(num_str) < length:
        # iterates until the length is equal to the desired length
        num_str = "0" + num_str
    return num_str


def intro2():
    print('WELCOME to this amazing program.')
    print('Besides generating a random password which will be stored in a key(file).')
    print('This program can also match an already set password from the user and it can also change that password in a very secured way.')
    print('This program has actually been implemented to access certain file. Which can give a good idea how this program is useful in Database security and all other cool stuffs.')
    print('Moreover this program would also provide the user with a unique opprtunity to check if an intruder tried to hack into his files.')
    print('')



def password_generator():
    intro2()
    password_secret_dict ={
        1 : 'Q',
        2 : 'W',
        3 : 'E',
        4 : 'R',
        5 : 'T',
        6 : 'Y',
        7 : 'U',
        8 : 'I',
        9 : 'O',
        10 : 'P',
        11 : 'Z',
        12 : 'X',
        13 : 'C',
        14 : 'V',
        15 : 'B',
        16 : 'N',
        17 : 'M',
        18 : 'A',
        19 : 'S',
        20 : 'D',
        21 : 'F',
        22 : 'G',
        23 : 'H',
        24 : 'J',
        25 : 'K',
        26 : 'L',
        27 : '1',
        28 : '2',
        29 : '3',
        30 : '4',
        31 : '5',
        32 : '6',
        33 : '7',
        34 : '8',
        35 : '9',
        36 : '0',
        37 : '/',
        38 : '*',
        39 : '+',
        40 : '-',
        41 : '[',
        42 : ']',
        43 : '{',
        44 : '}',
        45 : '(',
        46 : ')',
        47 : '&',
        48 : '^',
        49 : '%',
        50 : '$',
        51 : '#',
        52 : '@',
        53 : '!',
        54 : '<',
        55 : '>',
        56 : 'a',
        57 : 'b',
        58 : 'c',
        59 : 'd',
        60 : 'e',
        61 : 'f',
        62 : 'g',
        63 : 'h',
        64 : 'i',
        65 : 'j',
        66 : 'k',
        67 : 'l',
        68 : 'm',
        69 : ',',
        70 : '.',
        71 : '?',
        71 : '/',
        72 : '"',
        73 : "'",
        74 : ':',
        75 : ';',
        76 : '_',
        77 : 'n',
        78 : 'o',
        79 : 'p',
        80 : 'q',
        81 : 'r',
        82 : 's',
        83 : 't',
        84 : 'u',
        85 : 'v',
        86 : 'w',
        87 : 'x',
        88 : 'y',
        89 : 'z',
        90 : ' ',
    }
    # this dictionary will create the random password based on the random number it generates which is a key to a letter , number or punctuation mark
    print('TYPE YOUR PASWORD TO ACCESS THE PERSONAL FILES. \n')
    password_length = random.randint(8, 12)
    # helps to generate a password of unique length
    generated_password = ''
    # creates an empty string for setting the password
    for i in range(password_length):
        # iterates as per the random length of the password
        password_key = random.randint(1, 90)
        # gets a ramdomly generated password key
        generated_password += password_secret_dict[password_key]
        # add a ramdomly selected charecter t the password
    with open('gen_pass.txt', "a") as f:
        # writes this password in a key which the user has the access only
        f.write(generated_password + '\n')
    with open('personal/set_password.txt') as f:
        for line in f:
            # takes the set password which may be set by the user to add an extra layer of security
            set_password = line.strip()

    chances = 3
    # this is total number of chance that a user gonna get to login through the set passwrod

    change_pass_opt = 'raihan_rashid'
    # this is a password set within the program which can't be changed from outside by anymeans. It can also add an extra layer of security and insurance to both the customer and the manufacturer when the user forgets the password
    take_password = input('Type the generated password in the key. \n:')
    # ASks for and takes the generated password from the user

    if take_password == generated_password :
        # this activates a set of program if the password is correct
        print('Your password was correct.')
        take_set_password = input('Type your given password. \n:')
        # asks and takes the set password from the user

        while take_set_password != set_password and chances > 0 and take_set_password != 'forgot password' and take_set_password != 'set new password':
            # this loop starts if the set password given by the user is wrong and it gives the user 3 chances to input the correct password
            print('Your given password was wrong. ')
            print('You have ' + str(chances) + ' chances left before being blocked.')
            # indicates the number of chances that the user has
            print('If you forgot your password. Then please enter the kewwords to change it by accessing the functionality.')
            take_set_password = input('Type your given password. \n:')
            chances -= 1
            # reduce the chances after each iteration 

        if set_password == take_set_password:
            # asks the user to input the filename that he wants to acces in a secured folder
            print('Your password was correct. \n')
            filename = input('ENTER the FILENAME THAT YOU WANT TO ACCESS IN PERSONAL FOLDER. \n')
            with open('personal/' + filename + '.txt') as f:
                # opens and shows the file to the user
                for line in f:
                    print(line.strip())


        elif take_set_password == 'forgot password' or take_set_password == 'set new password':
            # user may use this key like forgot password if he forgets this password or set a new password if he thinks that his password is compromised
            change_pass_checker = input('ENTER THE HINTED PASS WHICH WILL ENABLE YOU TO SET A NEW PASSWORD (your name in python XD). \n')
            # this is where the role of the in built password checker in the program comes into play. Only by knwing this password the user can change the password
            if change_pass_checker == change_pass_opt:
                #helps to change the password
                set_password = input('Enter a new password: \n')
                # takes the password and sets it in the change password file
                with open('personal/set_password.txt', 'a') as f:
                    f.write(set_password + '\n')

            else:
                # if the intruder can't enter the right forgot or checker password then his entry will be blocked and the information about this failed attempt will be stored in a file which only the user has access to
                print('\n UNAUTORIZED ACCESS BLOCKED!')
                chances -= 1
                with open('personal/unauthorized_access_list.txt', 'a') as f:
                    # adds all the information about the entry of the intruder who has tried to invade the system
                    f.write('\n wrong HINTED password, '+ change_pass_checker + ', ' + str(3 - chances) + ' attempts, timestamp, forgot password')


        else:
            # this activates when the intruder fails to give the set password correctly even after giving the generated password correctly
            print('\n UNAUTORIZED ACCESS BLOCKED!')
            chances -= 1
            with open('personal/unauthorized_access_list.txt', 'a') as f:
                # intruders inof in a file
                f.write('\n wrong GIVEN password, ' + take_set_password + ', ' + str(3 - chances) + ' attempts, timestamp, none')

    elif take_password == 'I have lost the key':
        # if the user somehow lost the key/ the access to the file where the randomly generated password are stored
        print('YOU WILL GET ONLY ONE CHANCE TO ENTER YOUR GIVEN PASSWORD. IF YOU FAIL YOUR ENTRY WILL BE BLOCKED!')
        take_set_password = input('Type your given password. \n:')
        # here the user only gets one chance to guve the set password or eklse his entry is blocked

        if set_password == take_set_password:
            # if his set password matches then he can access the files
            filename = input('ENTER the FILENAME THAT YOU WANT TO ACCESS IN PERSONAL FOLDER. \n')
            with open('personal/' + filename + '.txt') as f:
                for line in f:
                    print(line.strip())
        
        else:
            print('\n UNAUTORIZED ACCESS BLOCKED!')
            # if the intruder fails to give the set password correctly even after applying to that special functionality
            chances -= 1
            with open('personal/unauthorized_access_list.txt', 'a') as f:
                f.write('\n wrong GIVEN password, '+ take_set_password + ', ' + str(3 - chances) + ' attempts, timestamp, lost key')
    else:
        # this stores the data of the intruder in a file if he fails to provide the set password correctly
        print('\n UNAUTORIZED ACCESS BLOCKED!')
        chances -= 1
        with open('personal/unauthorized_access_list.txt', 'a') as f:
            f.write('\n wrong GENERATED password, '+ take_password + ', '+ str(3 - chances) +' attempts, timestamp, none')






def sequence_analysis():
    intro1()          #...........prints the introductory lines

    sequence_analysis = input('WHAT SEQUENCE DO YOU WANT TO ANALYSE?(click enter to end)') 
    # it let's the user choose what type of DNA / mRNA / Protein analysis he wants to do

    while sequence_analysis != '':
        if sequence_analysis == '1': 
            mrna_sequence_analyze()           # returns 2 complementary DNA sequence of the mRNA 3 to 5 ends are not shown but maintained
            sequence_analysis = input('WHAT SEQUENCE DO YOU WANT TO ANALYSE?(click enter to end)')
        elif sequence_analysis == '2':
            dna_sequence_analyse()        #returns the mRNA sequence from a given DNA sequence. It takes the DNA as though it has directly synthesized or translated from the DNA
            sequence_analysis = input('WHAT SEQUENCE DO YOU WANT TO ANALYSE?(click enter to end)')
        elif sequence_analysis == '3':
            mrna_to_protein_analysis()     #converts the given mRNA sequence to protein
            sequence_analysis = input('WHAT SEQUENCE DO YOU WANT TO ANALYSE?(click enter to end)')
        elif sequence_analysis == '4':
            protein_to_mrna_analyse()        #convets the given protein sequence to a probabler mRNA sequence. The mRNA sequence might not absolutely be correct as one amino acid may contain several codon as signals
            sequence_analysis = input('WHAT SEQUENCE DO YOU WANT TO ANALYSE?(click enter to end)')
        elif sequence_analysis == '5':
            protein_to_dna_analysis()      #converts a protein sequence to it's original DNA signaling sequence. mRNA has been used as the intermidiate substance.
            sequence_analysis = input('WHAT SEQUENCE DO YOU WANT TO ANALYSE?(click enter to end)')
        elif sequence_analysis == '6':
            dna_to_dna_analysis()         #converts a given DNA sequence to it's complementary sequence of DNA but in an opposite direction.
            sequence_analysis = input('WHAT SEQUENCE DO YOU WANT TO ANALYSE?(click enter to end)')
        elif sequence_analysis == '7':
            protein_sequence_show()       #it shows the full protein sequence and the mRNA sequence of the provided protein. But the protein's information must be stored in a file
            sequence_analysis = input('WHAT SEQUENCE DO YOU WANT TO ANALYSE?(click enter to end)')
        else:
            # This runs if the user inputs some unnecessary keys.
            print('ENTER A CORRECT INPUT. OTERWISE NOTHING WOULD HAPPEN!')
            print('')
            intro()
            sequence_analysis = input('WHAT SEQUENCE DO YOU WANT TO ANALYSE?(click enter to end)')
    print('THE PROGRAM HAS ENDED.')
    #signals the end of program



def intro1():
    #general introduction for the user 
    #this has the information about how to access different types of DNA sequence analysis.
    print('WELCOME TO THE SEQUENCE ANALYSER PROGRAM.')
    print('Input 1 for getting the DNA SEQUENCE of a given mRNA. ')
    print('Input 2 for getting the mRNA sequence of a given DNA sequence.')
    print('Input 3 for getting the protein structure or name from an mRNA sequence.')
    print('Input 4 for getting the mRNA sequence from a protein sequence.')
    print('Input 5 for getting the DNA sequence from a protein sequence.')
    print('Input 6 for getting the DNA sequence from a complementary strand.')
    print("Input 7 in order to input a protein name. It's sequence and probable mRNA sequence will be shown.")
    print('Just click enter to end the program.')
    print('')


def protein_sequence_show():
    """
    THIS function can show all the amino acid sequences as well as the probable mRNA sequence
    of a given protein...
    Although it can now only show the fulll sequence and mRNA of INSULIN. But it's 
    range can be increased by adding more file... As I didb't have all the resources I couldn't do so...
    But by adding for each of the complex protein this program can be constructed which will be able to provide
    perhaps all the protein related information is all of the recources are gathered.
    """
    chain_number = int(input('How many chain are there in the structure of the protein? '))
    #prompts the user to input how many chains does the protein have in it's simplest structure.
    if chain_number == 1:
        #for one chained protein 
        #no information is provided due to lack of resources
        print('No information of such protein has been stored.')
    elif chain_number == 2:
        # for double chained protein connected by cysteine bonds
        protein_name = input('What is the name of the protein? ')
        #takes the name of a protein form the user
        if protein_name == 'insulin':
            #matches the protein name for analysis
            print('THIS IS CHAIN A:')
            #chain A or 1st chain analysis
            chainA = []
            #creates an empty list for the first chain
            with open(protein_name + '/chainA.txt') as f:
                #opens the file where the information of the first chain is provided
                for line in f:
                    #takes in each of the amino acid present in the file as aline
                    line = line.strip()
                    chainA.append(line)
                    #adds the amino acid to the listr
                print(chainA)
                #prints the list
                protein_to_mrna_analysis(chainA)
                # passes the amino acid sequence to this funsction for printing the mRNA sequence
            print('')
            print('THIS IS CHAIN B:')
            #similar operation with chainB or 2nd chain starts
            chainB = []
            #empty list of second chain
            with open(protein_name + '/chainB.txt') as f:
                #opens the file where the information of the chain B is stored
                for line in f:
                    #iterates over each line in the file
                    line = line.strip()
                    chainB.append(line)
                    #strips the line if any space is present or if \n is present 
                print(chainB)
                #prints the list of amino acid sequence of chainB as a list
                protein_to_mrna_analysis(chainB)
                #converts and prints the mRNA sequence through the given function.
    else:
        print('No protein sequence information exists!')
        #extensions can be mae with proper resources


def protein_to_dna_analysis():
    #converts a given protein or amino acid sequence in a translated DNA sequence
    mrna_sequence = protein_to_mrna_analyse()
    #gets the mRNA sequence from the protein sequence
    mrna_sequence_analyse(mrna_sequence)
    #converts and prints the given mRNA sequence to DNA sequence


def dna_to_dna_analysis():
    #this function is used to find the complmentary DNA strand of a given DNA sequence
    dna_sequence = get_dna_sequence()
    # gets a valid DNA sequence form the user 
    complementary_dna_sequence = get_dna_sequence1(dna_sequence)
    #passes the DNA sequnce to a function for converting it into it's compplementary sequence
    print('THE REQUIRED COMPLEMENTARY DNA STRAND IS (direction 3 to 5):')
    print(complementary_dna_sequence)
    #prints the required complementary sequence
    print('')



def protein_to_mrna_analyse():
    #converts a protein to it's mRNA sequence
    amino_acid = get_amino_acid()
    #gets a vaid mRNA sequence from the user 
    mrna_sequence = ''
    #creates a blank mRNA sequence
    amino_acid_mrna_dictionary = {
        'phenylalanine' : 'UUU',
        'leucine' : 'UUG',
        'isoleucine' : 'AUU',
        'valine' : 'GUG',
        'serine' : 'UCA',
        'proline' : 'CCC',
        'Threonine' : 'ACU',
        'alanine' : 'GCU',
        'tyrosine' : 'UAC',
        'histidine' : 'CAU',
        'glutamine' : 'CAG',
        'aspargine' : 'AAC',
        'lysine' : 'AAA',
        'aspartic acid' : 'GAU',
        'glutamic acid' : 'GAG',
        'cysteine' : 'UGC',
        'tryptophan' : 'UGG',
        'arginine' : 'CGC',
        'glycine' : 'GGG'
    }
    #this dictionary has all the information of the AMINO ACID to it's respective codon.
    # DISCLAIMER : AN AMINO ACID MIGHT HAVE SEVERAL CODONS. BUT FOR THIS PURPOSE I HAVE CHOOSEN ONLY ONLE OUT OF 6,4,2 CODONS OF AN AMINO ACID OF PROTEIN. 
    #AN AMINO ACID CAN BE ALSO RE[RESENTED OR IT MIGHT ALSO HAVE A BIT DIFFERENT AMINO ACID SEQUENCE SIGNALING CODONS.
    while amino_acid != '':
        # receives input until the user wants to end the program and simply presses enter
        mrna_sequence += amino_acid_mrna_dictionary[amino_acid]
        #coverts a particular AMINO acid to it's respective signaling codons
        amino_acid = get_amino_acid()
        #gets a valid amino acid
    print('THE REQUIRED MRNA SEQUENCE IS (direction 5 to 3): ')
    print(mrna_sequence)
    #prints the mRNA sequence 
    print('')
    return mrna_sequence
    #returns the mRNA sequence

def protein_to_mrna_analysis(chain):
    #converts a given protein through a file to an mRNA sequence
    amino_acid_mrna_dictionary = {
        'phenylalanine' : 'UUU',
        'leucine' : 'UUG',
        'isoleucine' : 'AUU',
        'valine' : 'GUG',
        'serine' : 'UCA',
        'proline' : 'CCC',
        'Threonine' : 'ACU',
        'alanine' : 'GCU',
        'tyrosine' : 'UAC',
        'histidine' : 'CAU',
        'glutamine' : 'CAG',
        'aspargine' : 'AAC',
        'lysine' : 'AAA',
        'aspartic acid' : 'GAU',
        'glutamic acid' : 'GAG',
        'cysteine' : 'UGC',
        'tryptophan' : 'UGG',
        'arginine' : 'CGC',
        'glycine' : 'GGG'
    }
    #this dictionary has all the information of the AMINO ACID to it's respective codon.
    # DISCLAIMER : AN AMINO ACID MIGHT HAVE SEVERAL CODONS. BUT FOR THIS PURPOSE I HAVE CHOOSEN ONLY ONLE OUT OF 6,4,2 CODONS OF AN AMINO ACID OF PROTEIN. 
    #AN AMINO ACID CAN BE ALSO RE[RESENTED OR IT MIGHT ALSO HAVE A BIT DIFFERENT AMINO ACID SEQUENCE SIGNALING CODONS.
    mrna_sequence = ''
    #creates a blank mRNA sequence
    for i in range(len(chain)):
        #iterates as per the string length
        amino_acid = chain[i]
        #assigns the chain element value to the amino acid
        mrna_sequence += amino_acid_mrna_dictionary[amino_acid]
        #collecs the amino acid mRNA sequence formt eh dictionary according to the amino acid kew and adds to the sequence
    print('THE REQUIRED MRNA SEQUENCE IS (direction 3 to 5): ')
    print(mrna_sequence)
    # prints the mRNA sequence
    print('')

def get_amino_acid():
    #gets a valid amino acid form the user
    amino_acid_dictionary = {
        'plenylalanine' : 'amino acid',
        'leucine' : 'amino acid',
        'isoleucine' : 'amino acid',
        'valine' : 'amino acid',
        'serine' : 'amino acid',
        'proline' : 'amino acid',
        'Threonine' : 'amino acid',
        'alanine' : 'amino acid',
        'tyrosine' : 'amino acid',
        'histidine' : 'amino acid',
        'glutamine' : 'amino acid',
        'aspargine' : 'amino acid',
        'lysine' : 'amino acid',
        'aspartic acid' : 'amino acid',
        'glutamic acid' : 'amino acid',
        'cysteine' : 'amino acid',
        'tryptophan' : 'amino acid',
        'arginine' : 'amino acid',
        'glycine' : 'amino acid'
    }
    # all the amino acid in this dictionary has 'amino acid' as the value. It will be later used to validate if an input is actually an amino acid or not.
    amino_acid = input('Enter an amino acid(click enter to end): ')
    #receives an input as string and stores the value in the amino_acid variable
    if amino_acid == '':
        #returns if the value of the given amino acid is none
            return amino_acid
    while amino_acid_dictionary.get(amino_acid) == None:
        #check if the string given by the user is an amino acid or not bu=y checking the dictionary.
        amino_acid = input('Enter a correct amino acid (click enter to end): ')
        #prompts the user to enter a valid amino acid if they didn't do so.
        if amino_acid == '':
            return amino_acid
    return amino_acid
    #returns a valid amino acid

def mrna_to_protein_analysis():
    # converts the given mRNA sequence to an amino acid according to the specific signalling codons
    protein_dictionary ={
        'UUU' : 'phenaylalanine',
        'UUC' : 'phenaylalanine',
        'UUA' : 'leucine',
        'UUG' : 'leucine',
        'CUU' : 'leucine',
        'CUC' : 'leucine',
        'CUA' : 'leucine',
        'CUG' : 'leucine',
        'AUU' : 'isoleucine',
        'AUC' : 'isoleucine',
        'AUA' : 'isoleucine',
        'AUG' : 'START CODON',
        'GUU' : 'valine',
        'GUC' : 'valine',
        'GUA' : 'valine',
        'GUG' : 'valine',
        'UCU' : 'serine',
        'UCC' : 'serine',
        'UCA' : 'serine',
        'UCG' : 'serine',
        'CCU' : 'proline',
        'CCC' : 'proline',
        'CCA' : 'proline',
        'CCG' : 'proline',
        'ACU' : 'Threonine',
        'ACC' : 'Threonine',
        'ACA' : 'Threonine',
        'ACG' : 'Threonine',
        'GCU' : 'alanine',
        'GCC' : 'alanine',
        'GCA' : 'alanine',
        'GCG' : 'alanine',
        'UAU' : 'tyrosine',
        'UAC' : 'tyrosine',
        'UAA' : 'STOP CODON',
        'UAG' : 'STOP CODON',
        'CAU' : 'histidine',
        'CAC' : 'histidine',
        'CAA' : 'glutamine',
        'CAG' : 'glutamine',
        'AAU' : 'aspargine',
        'AAC' : 'aspargine',
        'AAA' : 'lysine',
        'AAG' : 'lysine',
        'GAU' : 'aspartic acid',
        'GAC' : 'aspartic acid',
        'GAA' : 'glutamic acid',
        'GAG' : 'glutamic acid',
        'UGU' : 'cysteine',
        'UGC' : 'cysteine',
        'UGA' : 'STOP CODON',
        'UGG' : 'tryptophan',
        'CGU' : 'arginine',
        'CGC' : 'arginine',
        'CGA' : 'arginine',
        'CGG' : 'arginine',
        'AGU' : 'serine',
        'AGC' : 'serine',
        'AGA' : 'arginine',
        'AGG' : 'arginine',
        'GGU' : 'glycine',
        'GGC' : 'glycine',
        'GGA' : 'glycine',
        'GGG' : 'glycine'
    }
    #this dictionary contains all the informations about which codon is used for signalling which amino acid
    protein_chain_number = int(input('WHAT IS THE NUMBER OF PROTEIN CHAIN? '))
    #prompts the user to enter the total number of chain present in the protein structure
    for i in range(protein_chain_number):
        #iterates as per the number of the chain
        mrna_sequence = get_mrna_sequence()
        #gets a valid mRNA sequence 
        codon = ''
        #creates a blank string for the codon
        protein_chain = ''
        #creates a blank string for the protein chain
        for i in range(len(mrna_sequence)):
            #iterates as per the length of the mRNA sequence
            codon += mrna_sequence[i]
            #codons gets it's value as string from the mRNA sequence over each iterations
            if len(codon) == 3:
                # if the codon length is 3. THEN it becomes a perfect codon which is definite signalling structure for a particular protein.
                protein_chain = protein_chain + ',' + protein_dictionary[codon]
                #cretaes the protein sequence with the amino acid according the the sequence
                #here the codon basically acts as the kew to the dictionary which gets the value and add it to the protein sequence
                codon = ''
                #th =e codon is again made blank as a codon can have a maximum of 3 sequence of mRNA as values
        print(protein_chain)
        #prints the sequence of protein containing amino acid
    print('')
    #used for creating a gap between lines




def mrna_sequence_analyze():
    # by analysing the mRNA sequence prints the DNA sequence from which it was translated.
    mrna_sequence = get_mrna_sequence()
    #gets a valid mRNA sequence
    dna_sequence1 = get_dna_sequence1(mrna_sequence)
    #gets a valid DNA sequence of the mRNA which actually translates it
    dna_sequence2 = get_dna_sequence2(mrna_sequence)
    #gets the complementary dna sequence of dna_sequence1

    print('THE REQUIRED DNA SEQUENCE IS:')
    print('DNA sequence 1 (direcion 3 to 5): ')
    #shows the actual direction of the DNA sequence
    print(dna_sequence1)
    #prints the DNA sequence 
    print('')
    print('DNA sequence 2 (direction 5 to 3): ')
    print(dna_sequence2)
    print('')

def mrna_sequence_analyse(mrna_sequence):
    dna_sequence1 = get_dna_sequence1(mrna_sequence)
    dna_sequence2 = get_dna_sequence2(mrna_sequence)

    print('THE REQUIRED DNA SEQUENCE IS:')
    print('DNA sequence 1 (direcion 3 to 5): ')
    print(dna_sequence1)
    print('')
    print('DNA sequence 2 (direction 5 to 3): ')
    print(dna_sequence2)
    print('')


def get_mrna_sequence():
    #this functions returns a valid mRNA sequence by taking the input from the user and also by checking if the input was invalid or not.
    mrna_sequence = input('Enter the mRNA sequence (direction 5 to 3): ')
    #receives the input
    for i in range(len(mrna_sequence)):
        while mrna_sequence[i] != 'A' and mrna_sequence[i] != 'C' and mrna_sequence[i] != 'U' and mrna_sequence[i] != 'G' and mrna_sequence[i] != 'a' and mrna_sequence[i] != 'c' and mrna_sequence[i] != 'u' and mrna_sequence[i] != 'g':
            #checks if the user has inputted the correct mRNA sequence or not. IF the user entered wrong sequence, it detects it and
            # puts the user in a loop until the user inputs the correct sequence
            mrna_sequence = input('Enter the correct mRNA sequence(direction 5 to 3): ')
    return mrna_sequence.upper()
    #returns the mRNA sequence in UPPER CASE






def get_dna_sequence1(mrna_sequence):
    #it generates a DNA sequence from the provided mRNA sequence. It is mainly the sequence of the DNA which primarily translates the mRNA. 
    dna_sequence1 = ''
    #creates a blank dna_sequence
    for i in range(len(mrna_sequence)):
        #iterates over as per the length of the mRNA sequence
        if mrna_sequence[i] == 'A' or mrna_sequence[i] == 'a':
            #checks and transforms the sequence likr=e form A ==> T
            dna_sequence1 = dna_sequence1 + 'T'
        elif mrna_sequence[i] == 'C' or mrna_sequence[i] == 'c':
            #transforms the sequence form c to g
            dna_sequence1 += 'G'
        elif mrna_sequence[i] == 'G' or mrna_sequence[i] == 'g':
            #transforms the sequence form g to c
            dna_sequence1 += 'C'
        else:
            #transforms u or t to a
            dna_sequence1 += 'A'
    return dna_sequence1
    #returns dna_sequence1 as string

def get_dna_sequence2(mrna_sequence):
    # it functions as same as the get_dna_sequence1(mrna_sequence)
    dna_sequence2 = ''
    for i in range(len(mrna_sequence)):
        #it analyses the sequence in the same way but doesn,t bring much of a signifiv=cant chage except for changing U to T.
        if mrna_sequence[i] == 'A' or mrna_sequence[i] == 'a':
            dna_sequence2 += 'A'
        elif mrna_sequence[i] == 'C' or mrna_sequence[i] == 'c':
            dna_sequence2 += 'C'
        elif mrna_sequence[i] == 'G' or mrna_sequence[i] == 'g':
            dna_sequence2 += 'G'
        else:
            #coverts U to T
            dna_sequence2 += 'T'
    return dna_sequence2
    #returns the dna_seqeunce 2 to another function

def dna_sequence_analyse():
    #translates an mRNA sequence form a given DNA seqeunce 
    dna_sequence = get_dna_sequence()
    mrna_sequence = analyse_mrna_from_dna(dna_sequence)
    #get an mRNA sequence from a DNA sequence
    print('THE REQUIRED mRNA SEQUENCE IS (direction 3 to 5):')
    print(mrna_sequence)
    #prints the required mRNA sequence
    print('')


def analyse_mrna_from_dna(dna_sequence):
    #translates an mRNA sequencefrom a given dna_sequence. Here the direction of DNA sequence is taken as 3 to 5 
    #the final mRNA returned has the direction 5 to 3.
    mrna_sequence = ''
    for i in range(len(dna_sequence)):
        # analyses the sequence of mRNA as per the DNA sequence.
        if dna_sequence[i] == 'A' or dna_sequence[i] == 'a':
            #coverts all the A/adenine to U/uracil
            mrna_sequence += 'U'
        elif dna_sequence[i] == 'C' or dna_sequence[i] == 'c':
            # converts all the C/cytosine to G/guanine
            mrna_sequence += 'G'
        elif dna_sequence[i] == 'G' or dna_sequence[i] == 'g':
            # converts a Guanine to Cytosine
            mrna_sequence += 'C'
        else:
            mrna_sequence += 'A'
            #converts an adenine to T/thyamine
    return mrna_sequence
    #returns the mRNA sequence


def get_dna_sequence():
    #it is used to get a valid mRNA sequence from the user.
    dna_sequence = input('Enter the DNA Sequence(direction 5 to 3): ')
    for i in range(len(dna_sequence)):
        # checks the whole sequence and prompts the user to inout a valid DNA unitl the user has done so.
        while dna_sequence[i] != 'A' and dna_sequence[i] != 'C' and dna_sequence[i] != 'T' and dna_sequence[i] != 'G' and dna_sequence[i] != 'a' and dna_sequence[i] != 'c' and dna_sequence[i] != 't' and dna_sequence[i] != 'g':
            dna_sequence = input('Enter the correct DNA sequence(direction 5 to 3): ')
    return dna_sequence
    #returns the DNA sequence

if __name__ == '__main__':
    main()
