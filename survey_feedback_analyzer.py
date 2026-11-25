
# Project: Survey Feedback Analyzer

# Step 1: Preloaded Feedbacks

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': [
        'Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
        'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'
    ],

    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


# Step 2: Add More Feedbacks

print("Welcome to Survey Feedback Analyzer!")

while True:
    try:
        number = int(input("How many more feedbacks do you want to add? "))

        if number >= 0:
            break
        else:
            print("Please enter zero or a positive number.")

    except ValueError:
        print("Please enter a valid whole number.")


for i in range(number):

    print(f"\nEnter feedback {i + 1}")

    # Automatically generate serial number
    s_no = len(feedback_data['S_No']) + 1

    name = input("Enter your name: ")

    feedback = input("Enter your feedback: ")

    # Validate rating
    while True:
        try:
            rating = int(input("Enter rating (1-5): "))

            if 1 <= rating <= 5:
                break
            else:
                print("Rating must be between 1 and 5.")

        except ValueError:
            print("Please enter a valid whole number.")

    # Append new values to the dictionary
    feedback_data['S_No'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)


# Step 3: Clean All Feedback Text

def clean_feedback(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    for punctuation in ['.', ',', '!', '?']:
        text = text.replace(punctuation, '')

    # Remove extra spaces
    text = ' '.join(text.split())

    return text


# Clean every feedback using a loop
for i in range(len(feedback_data['Feedback'])):

    feedback_data['Feedback'][i] = clean_feedback(
        feedback_data['Feedback'][i]
    )


# Step 4: Word Count Insights

def count_word_in_feedbacks(word):

    count = 0

    # Check every feedback
    for feedback in feedback_data['Feedback']:

        words = feedback.split()

        # Count a feedback only once if it contains the word
        if word.lower() in words:
            count += 1

    return count


print("\n--- Word Count Insights ---")

print("Feedbacks containing 'good':",
      count_word_in_feedbacks("good"))

print("Feedbacks containing 'poor':",
      count_word_in_feedbacks("poor"))

print("Feedbacks containing 'excellent':",
      count_word_in_feedbacks("excellent"))


# Step 5: Final Summary and Insights

print("\n--- Final Cleaned Feedback Data ---")

print(feedback_data)


# Calculate average rating

total_rating = sum(feedback_data['Rating'])

total_feedbacks = len(feedback_data['Rating'])

average_rating = total_rating / total_feedbacks

print("\nAverage Rating:", round(average_rating, 2))


# Find the feedback with the longest comment

longest_feedback = ""
maximum_words = 0

for feedback in feedback_data['Feedback']:

    words = feedback.split()

    word_count = len(words)

    if word_count > maximum_words:
        maximum_words = word_count
        longest_feedback = feedback


print("\n--- Longest Feedback ---")

print("Feedback:", longest_feedback)

print("Word Count:", maximum_words)


# Find unique words across all feedbacks

unique_words = []

for feedback in feedback_data['Feedback']:

    words = feedback.split()

    for word in words:

        if word not in unique_words:
            unique_words.append(word)


unique_words.sort()

print("\n--- Unique Words ---")

print(unique_words)


# Optional: Sort feedbacks by rating (highest to lowest)

sorted_feedbacks = sorted(
    zip(
        feedback_data['S_No'],
        feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']
    ),
    key=lambda x: x[3],
    reverse=True
)


print("\n--- Feedbacks Sorted by Rating ---")

for s_no, name, feedback, rating in sorted_feedbacks:

    print(
        f"S_No: {s_no}, Name: {name}, "
        f"Feedback: {feedback}, Rating: {rating}"
    )
