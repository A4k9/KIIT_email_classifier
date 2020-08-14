# Project Overview

Aren't you tired of the constant buzzing of your phone form the mail notifications, only for them to turn out to be spam mails promoting the next big event you didn't want in your memory? Try out this simple spam classifier personalized for KIIT DU!

Check it out: [KIIT spam mail classifier](https://kiit-spam-classifier.herokuapp.com/)

# Table of Contents

- Data Collection
  - All the mails were collected from the [official KIIT DU mail id.](http://mail.google.com/a/kiit.ac.in)
  - The data was stored in an .xlsx file along with their labels.
  - A total of 100 hand-picked mails were chosen for the purpose of this project
- Data Cleaning
  - The text contained data irrelevant to the actual predictions such as images and emojis, which were filtered out by hand for simplicity.
- Feature Extraction
  - The words were converted into usable features with the help of [sci-kitlearn's CountVectorizer() functionality.](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)
  
- Model Selection
  - The [sci-kitlearn's in-built SVM model](https://scikit-learn.org/stable/modules/svm.html) was used for the purpose of binary classification: Spam OR Ham.
  
- Model Validation
  - The data was split into two parts: [Training and Testing](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) for the purpose of validation.

- Model Training & Accuracy
  - The model was trained on 80% of the total data and then validated against the testing data with 95% accuracy metric.

- Deployment
  - A client facing API using flask and CSS ([Tailwind + Tailblocks](https://mertjf.github.io/tailblocks/)) was then deployed on the [Heroku cloud platform.](https://www.heroku.com/)
