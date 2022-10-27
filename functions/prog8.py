import random  # importing dependencies


def score():
    """
    PROTOTYPE:
        score()
        Arguments -> None
        Return values -> (int) scorevalue
    DESCRIPTION:
        Simulates a GK quiz and returns the score of the user.
    """
    scorevalue = 0
    # Format for questions: {question_id: [question, [option1, option2 ...], answer]}
    questions = {
        1: [
            "ISRO is to set up its second launch port in Tamilnadu for SSLV. What does SSLV stand for?",
            [
                "Space Satellite Launch Vehicle",
                "Speed Satellite Launch Vehicle",
                "Small Satellite Launch Vehicle",
                "Solar Satellite Launch Vehicle"
             ],
            "Small Satellite Launch Vehicle"
        ],
        2: [
            "Which global tele-communication company’s arm has recently launched a new privacy-focused search engine called ‘OneSearch’?",
            [
                "AT&T",
                "Verizon",
                "Vodaphone",
                "China Mobile"
            ],
            "Verizon"
        ],
        3 : [
            "What is the name of the humanoid robot, which was recently unveiled by the Indian Space Research Organisation (ISRO)?",
            [
                "Vyom Mitra",
                "Gagan Mitra",
                "Vayu Mitra",
                "Agni Mitra"
            ],
            "Vyom Mitra"
        ],
        4 : [
            "As per the recent study by the Institute of Advanced Study in Science and Technology (IASST), the ‘Endophytic Actinobacteria’ could reduce chemical inputs in which plant?",
            [
                "Coffee",
                "Jute",
                "Tea",
                "Cotton"
            ],
            "Tea"
        ],
        5: [
            "The Union Home ministry has flagged which video-conferencing software as vulnerable to cyber-crimes?",
            [
                "Zoom",
                "Teams",
                "Skype",
                "Duo"
            ],
            "Zoom"
        ],
        6: [
            "Which famous platform has introduced a feature called ‘bedtime reminder’, as a part of its wellness and screen time tools?",
            [
                "WhatsApp",
                "Facebook",
                "Twitter",
                "Youtube"
            ],
            "Youtube"
        ],
        7: [
            "As per ICMR, which vaccine is found to be effective in neutralizing double mutant strain of SARS-CoV-2?",
            [
                "Sputnik V",
                "Covaxin",
                "Covishield",
                "Oxford Astra Zeneca"
            ],
            "Covaxin"
        ],
        7: [
            "What is the name of the NASA Mission, which aims to measure Earth’s global electric potential?",
            [
                "Endurance",
                "Ambition",
                "Perseverance",
                "Dedication"
            ],
            "Endurance"
        ],
        8: [
            "Which country’s scientists have grown plants in lunar soil for the first time?",
            [
                "India",
                "Japan",
                "UK",
                "USA"
            ],
            "USA"
        ],
        9: [
            "Which company has signed a deal with TikTok to be a trusted technology provider in USA?",
            [
                "Microsoft",
                "Intel",
                "Oracle",
                "Infosys"
            ],
            "Oracle"
        ],
        10: [
            "‘Unicorn’ is the name of which space body, that was recently discovered at 1,500 light-years away from the Earth?",
            [
                "Exo-planet",
                "Asteroid",
                "Black hole",
                "Satellite"
            ],
            "Endurance"
        ]
    }

    count = 0
    asked = []
    while count < 5:
        question_id = random.randint(1,max(questions.keys()))
        if question_id not in asked:
            print(f"{questions[question_id][0]} ")
            options =  ["A","B","C","D"]
            for i in options:
                print(f"{i}. {questions[question_id][1][options.index(i)]}")

            user_input = input("\n-> ")
            print()

            if user_input.lower().strip() == questions[question_id][2].lower().strip():
                print("Correct answer.")
                scorevalue += 1
            else:
                print("Incorrect answer.")
            print()
            asked.append(question_id)
        else:
            continue
        count += 1

    return scorevalue


def remark(scorevalue):
    """
    PROTOTYPE:
        remark
        Arguments -> (int) scorevalue
        Return values -> None
    DESCRIPTION:
        Prints a message to the console depending on the value of the input parameter.
    USAGE:
        remark(5)
        ->  Outstanding
            FINAL SCORE: 5 out of 5
        remark(0)
        -> General knowledge will always help you. Take it seriously.
            FINAL SCORE: O out of 0
    """
    remarks = [
        "General knowledge will always help you. Take it seriously. 📰",
        "Needs to take interest 🧑‍💻",
        "Read more to score more 📚",
        "Good 👍",
        "Excellent 👏",
        "Outstanding 💯"
    ]
    print(remarks[scorevalue])
    print("FINAL SCORE:", scorevalue, "out of 5")

def main():
    usr_score = score()
    remark(usr_score)

# print(score.__doc__)
# print(remark.__doc__)

if __name__ == "__main__":
    main()
