Questions=[
    {
        "question":"python use for",
        "options":["a.datascience","b.cybersecurity","c.App development"],
        "answer":"a"
    },
    {
        "question":"Python me kaunsa data type immutable hota hai?",
        "options":["a.list","b.tupple","c.dict"],
        "answer":"b"

    },
    {
        "question":"Python me # ka use kis liye hota hai?",
        "options":["a.docs","b.comment","c.variable"],
        "answer":"b"
    }
]
score=0

for q in Questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

        user_answer=input("enter your answer(a/b/c)")
        if user_answer==q["answer"]:
            print("✅ Sahi jawab")
            score +=10
        else:
            print("❌ Ghalat jawab")

print("\nYour total score is:", score)

             
