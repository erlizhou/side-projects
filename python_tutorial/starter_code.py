def level_one():
    print "####################################################"
    print "STARTING LEVEL ONE"
    print "####################################################"
    print "### Initializing various Python types ###"
    a_number = 42 
    a_string = "hello world"
    foo = 3.1415 # I am a float

    # "You can print them too!"
    print a_number
    print a_string
    print foo
    print foo + a_number
    print a_string + ' ' + str(a_number)
    
    print "### Lists are a fundamental part of the Python toolkit ###"
    my_list = [a_number, a_string, foo] # lists can hold a variety of things
    my_other_list = [5, 1, 6, 2, 8, 3] 
    
    # On Sorting
    # Can YOU guess what will be printed out?
    print sorted(my_other_list)
    print my_other_list
    my_other_list.sort()
    print my_other_list
    
def level_two():
    print "####################################################"
    print "STARTING LEVEL TWO"
    print "####################################################"
    
    # On If Statements
    my_college = "Stanford"
    if my_college == "Stanford":
        print "You go to " + my_college + ". You're awesome!"
    elif my_college == "Berkeley":
        print "You're a hippie."
    else:
        print "Depends on your personality"

    print "####################################################"
    # On Dictionaries
    d1 = {}
    d1["A"] = 23
    d1["B"] = 34
    
    d2 = {"C": 45, "D": 56, "E": [1, 2, 3]}

    print d1["C"] # You should see None
    if "C" in d1:
        print "He who shall not be named."
    elif "A" in d1:
        print "A was in d1"
        print "Key:","A", "Value:",d1["A"]
    else:
        print "A was not in d1"

    print "####################################################"
    # On For Loops
    for i in range(5):
        print i

    print "####################################################"
    emotions = ["Happy", "Fine", "Okay", "Meh", "Sad"]
    for i, word in enumerate(emotions):
        print i, word

    print "####################################################"
    for key in d1.keys():
        print key

    print d2.items()
    for k,v in d2.items():
        print k,v

    print "####################################################"
    # On Sets
    s1 = set([1,2,2,2,2,3,3,4,5])
    print s1
    if 4 in s1:
        print "hooray!"

def level_three():
    print "####################################################"
    print "STARTING LEVEL THREE"
    print "####################################################"
    
    my_list = ["Stanford", "Cal Tech", "MIT", "Berkeley", "Princeton"]
    another_list = [school.upper() for school in my_list if school != "Berkeley"]
    print another_list

    words = open("words.txt", "r")
    my_words = []
    for i, line in enumerate(words):
        my_words.append(line.strip('\n'))
        if i > 10:
            break
    print my_words
        
if __name__ == "__main__":
    #level_one()
    #level_two()
    level_three()
