# student_inquiry_categorizer_lightblue_fixed.py

# -------------------------------
# ANSI color codes
# -------------------------------
LIGHT_BLUE_BG = "\033[104m"  # Light blue background
RESET = "\033[0m"
WHITE_TEXT = "\033[97m"

# -------------------------------
# Expanded Keywords for departments
# -------------------------------
DEPARTMENTS = {
    "Registrar": [
        "register", "enroll", "enrollment", "transcript", "class", "course", "semester",
        "schedule", "add/drop", "curriculum", "grading", "drop", "withdraw", "subject", "classlist"
    ],
    "Accounting": [
        "tuition", "fee", "fees", "payment", "pay", "bill", "billing", "invoice", "refund",
        "balance", "due", "scholarship", "financial aid", "payment plan", "overpayment", "charges"
    ],
    "IT": [
        "password", "reset password", "computer", "login", "email", "portal", "account",
        "system", "issue", "technical", "wifi", "internet", "laptop", "network", "access",
        "credentials", "server", "website", "login problem", "software", "hardware"
    ]
}

# -------------------------------
# Responses per department
# -------------------------------
DEPARTMENT_RESPONSES = {
    "Registrar": "This inquiry is related to academic registration, classes, or schedules. Contact the Registrar office.",
    "Accounting": "This is a financial or tuition-related issue. Contact the Accounting office for help.",
    "IT": "This seems technical, such as login or system problems. Reach out to the IT support team.",
    "Uncategorized": "I'm not sure which department this belongs to. Could you provide more details?"
}

# -------------------------------
# Analyze inquiry and detect keywords
# -------------------------------
def analyze_inquiry(message):
    message_lower = message.lower()
    found_departments = {}
    for dept, keywords in DEPARTMENTS.items():
        matched_keywords = [word for word in keywords if word in message_lower]
        if matched_keywords:
            found_departments[dept] = matched_keywords
    if not found_departments:
        found_departments["Uncategorized"] = []
    return found_departments

# -------------------------------
# Main program
# -------------------------------
def main():
    # Light-blue background header
    print(LIGHT_BLUE_BG + WHITE_TEXT)
    print("University Inquiry Assistant".center(80))
    print(RESET)

    while True:
        # Use plain input prompt for compatibility
        user_input = input("Enter your inquiry (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        departments = analyze_inquiry(user_input)

        # Display results on light-blue background
        print(LIGHT_BLUE_BG + WHITE_TEXT)
        for dept, keywords in departments.items():
            print(f"Department: {dept}")
            if keywords:
                print(f"Keywords detected: {', '.join(keywords)}")
            print(DEPARTMENT_RESPONSES[dept])
            print("-" * 60)
        print(RESET)

if __name__ == "__main__":
    main()
