"""
Task-03: Phishing Email Detection
Assesses whether an email message looks suspicious based on common phishing
red flags such as urgent language, suspicious links, generic greetings,
requests for sensitive information, and unexpected attachments. Provides
clear feedback.
"""

import re


def check_phishing_email(email_text):
    """
    Evaluate whether an email appears suspicious.

    Criteria:
        - Urgent or threatening language         → +1 point
        - Suspicious links or raw URLs           → +1 point
        - Generic greeting                       → +1 point
        - Requests for sensitive info            → +1 point
        - Grammar/spelling red flags             → +1 point
        - Attachment mention                     → +1 point

    Args:
        email_text (str): The email content to analyze

    Returns:
        dict: Score, risk label, and feedback list
    """
    score = 0
    feedback = []
    text = email_text.lower()

    urgent_patterns = [
        r"urgent", r"immediately", r"act now", r"verify now", r"suspended",
        r"limited time", r"your account will be closed", r"warning", r"final notice"
    ]
    link_patterns = [r"http[s]?://", r"www\.", r"bit\.ly", r"tinyurl", r"click here"]
    generic_greetings = [r"dear customer", r"dear user", r"dear valued customer", r"hello user"]
    sensitive_requests = [
        r"password", r"otp", r"bank account", r"credit card", r"ssn",
        r"verify your account", r"login credentials", r"security code"
    ]
    grammar_flags = [r"won prize", r"congratulation", r"kindly revert", r"update immediately"]
    attachment_patterns = [r"attachment", r"attached file", r"download file", r"invoice attached"]

    if any(re.search(pattern, text) for pattern in urgent_patterns):
        score += 1
        feedback.append("⚠️ Urgent or threatening language detected.")

    if any(re.search(pattern, text) for pattern in link_patterns):
        score += 1
        feedback.append("⚠️ Suspicious link or raw URL found in the email.")

    if any(re.search(pattern, text) for pattern in generic_greetings):
        score += 1
        feedback.append("⚠️ Generic greeting detected. Legitimate emails often use your real name.")

    if any(re.search(pattern, text) for pattern in sensitive_requests):
        score += 1
        feedback.append("⚠️ Email requests sensitive information such as passwords or banking details.")

    if any(re.search(pattern, text) for pattern in grammar_flags):
        score += 1
        feedback.append("⚠️ Possible grammar or phrasing red flags detected.")

    if any(re.search(pattern, text) for pattern in attachment_patterns):
        score += 1
        feedback.append("⚠️ Email mentions an attachment. Unexpected attachments can be risky.")

    if score == 0:
        risk = "🟢 Low Risk"
        feedback.append("✅ No major phishing indicators were detected, but always verify the sender.")
    elif score <= 2:
        risk = "🟡 Moderate Risk"
    elif score <= 4:
        risk = "🟠 Suspicious"
    else:
        risk = "🔴 High Phishing Risk"

    return {
        "score": score,
        "max_score": 6,
        "risk": risk,
        "feedback": feedback,
    }


def display_result(result, email_length):
    """Pretty-print the phishing analysis result."""
    print("\n" + "=" * 50)
    print(f"  Email Length    : {email_length} characters")
    print(f"  Score           : {result['score']} / {result['max_score']}")
    print(f"  Risk Level      : {result['risk']}")
    print("-" * 50)
    print("  Feedback:")
    for line in result['feedback']:
        print(f"    {line}")
    print("=" * 50)


def main():
    print("=" * 50)
    print("        Phishing Email Detection Tool")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Check an email")
        print("  2. Exit")

        choice = input("\nEnter your choice (1/2): ").strip()

        if choice == '1':
            print("\nPaste the email content below.")
            print("Type END on a new line when finished:\n")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == 'END':
                    break
                lines.append(line)
            email_text = "\n".join(lines)
            result = check_phishing_email(email_text)
            display_result(result, len(email_text))

        elif choice == '2':
            print("\nGoodbye! 👋")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
