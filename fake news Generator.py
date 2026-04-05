import random

subjects=[
    "Rizwan",
    "babar azam",
    "hamid mir",
    "nouman ijaz",
    "a group of dogs",
    "Army chief",
    "pakistan",
    "imran khan",
    "shahbaz sharif",
    "A famous actor",
    "A cricket fan",
    "A minister",
    "A journalist",

]

actions=[
    "launches a mesile",
    "win the match",
    "shoot drama",
    "dance with",
    "eats",
    "declare war on",
    "shuts down",
    "celebrates with",
    "discovers",
    "invites",
    "calls",
    "meets",
    "helps",
    "teaches",
    "writes about",
    "plays with"
]

objects=[
    "at sea view",
    "in islambad motorway",
    "at ghadafi stadium",
    "in parlimant",
    "near Minar-e-Pakistan",
    "during a press conference",
    "on social media",
    "at airport",
    "at a tea stall",
    "at a wedding hall",
    "inside a school"
]

while True:
    sub=random.choice(subjects)
    act=random.choice(actions)
    obj=random.choice(objects)

    headline=f"Breaking news: {sub} {act} {obj}"

    print("\n" + headline)

    user=input("\n do you want another headline ?(yes/no) ").strip().lower()

    if user == "no":
        break
        # print("generate another headlines")
        
    # else:
    #     print("\n no need of headlines")
               
print("\n Thanks for using the fake generator!! have a fun")



