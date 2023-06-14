def chatbot_survey():
    print("Welcome to the Survey Chatbot!")
    name = input("Q1. What is your name? ")
    print("Hello!",name)
    age = input("Q2. What is your age? ")
    print("Almost same age as my granny")
    print("haha")
    print("Just Kidding")
    employment_status = input("Q3. Are you currently working? (Yes/No) ").lower()
    
    if employment_status == "yes":
        job_status = input("Q4. What is your job status? ")
        print("Thank you for sharing your employment details!")
    elif employment_status == "no":
        school_name = input("Q4. If you are a student, what is the name of your school? ")
        print("Thank you for sharing your school information!")
    else:
        print("Invalid response. Please try again.")
        return

    favorite_sport = input("Q5. What is your favorite sport? ")
    print("Damn I also like playing",favorite_sport,"very much")
    favorite_programming_language = input("Q6. What is your favorite programming language? ")
    print("Fun fact: I was writted in Python and my creator doesn't likes me")
    favorite_music = input("Q7. What type of music do you like? ")
    print("A lot of people like that kind of music")
    print("Thank you for completing the survey, {}!".format(name))

chatbot_survey()
