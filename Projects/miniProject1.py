def quizanswers():
    print("welcome to your quiz")
    quiz = [ 1+1 , 2+2 , 3+3 , 4+4, 5+5]
    answer = []
    answer = input("type your answer please")
    while answer != "quit":
        question = int(answer)
        quiz.append(question)
        print(quiz)
        answer = input("type in a answer")
        if input == 2:
            print("correct")
    else:
        x = sum(answer)
        print(x)


quizanswers()
