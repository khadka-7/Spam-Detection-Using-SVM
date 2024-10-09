def clean_user_input(text):
  def tokenize(text):
    return nltk.word_tokenize(text) # Use nltk.word_tokenize

  return text



# Function to classify user input as spam or ham
def predict_spam(user_input):
    cleaned_input = clean_user_input(user_input)
    input_tfidf = vectorizer.transform([cleaned_input])  # Vectorize the input
    prediction = "path_to_svm_model" #svm_model.predict(input_tfidf)

    if prediction == 0:
        return "Ham"
    else:
        return "Spam"

# Ask for user input and make prediction
user_input = input("Enter the email text to classify as spam or ham: ")
result = predict_spam(user_input)
print(f"The email is classified as: {result}")