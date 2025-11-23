from interview_engine import InterviewEngine

def choose_role():
    roles = {
        "1": "software_engineer",
        "2": "sales",
        "3": "retail_associate"
    }
    print("Choose a role to practice for:")
    for k, v in roles.items():
        print(f"{k}. {v.replace('_',' ').title()}")
    choice = input("Enter number (1-3): ").strip()
    return roles.get(choice, "software_engineer")

def main():
    role = choose_role()
    engine = InterviewEngine(role=role, max_questions=5)
    engine.run()

if __name__ == "__main__":
    main()
