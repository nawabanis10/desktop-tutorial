questions=[
    {
        "question":"pakistan ka capital kia hai",
        "options":["A.lahore","B.karachi","C.islambad","D.peshawar"],
        "answer":"C"
    },
    {
        "question":"2 + 2 = ?",
        "options":["A.4","B.3","C.7","D.9"],
        "answer":"A"
    },
    {
        "question":"python kes type ke language hai",
        "options":["A.low level","B.Machine","C.high level","D.Assembly"],
        "answer":"C"
    }
]

prize_money=[1000,3000,5000]

amount=0
for i in range (len(questions)):
    print("\n questions",i+1)
    print(questions[i]["question"])

    for option in questions[i]['options']:
        print(option)

    user_answer=input("Apna answer enter karien(A/B/C/D)").upper()
    if user_answer==questions[i]["answer"]:
      amount=prize_money[i]
      print("sahi jawab !")
      print("app ne jeetay: ",amount,"rupees")

    else:
        print("ghalat jawab !")
    
print("\n Game over !")
print("App ghar le ja rahe hai:",amount,"rupees")