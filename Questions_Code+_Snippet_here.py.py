# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R0TygF1zojOkY51Hn1ig46KMlpCCp8xG
"""

#Question1
import pandas as pd

# Load the users CSV file
file_path = r'C:\Users\91735\OneDrive\Desktop\users.csv'
users_df = pd.read_csv(file_path)

# Filter users from Toronto and sort by followers in descending order
top_users = users_df[users_df['location'] == 'Toronto'].nlargest(5, 'followers')

# Get the logins of the top users
top_user_logins = top_users['login'].tolist()

# Print the logins as a comma-separated string
print(', '.join(top_user_logins))

"""Solution: aneagoie,ZhangMYihua,susanli2016,thedaviddias,ange-yaghi"""

#Question2
import pandas as pd

# Load the users CSV file
file_path = r'C:\Users\91735\OneDrive\Desktop\users.csv'
users_df = pd.read_csv(file_path)

# Filter users from Toronto and sort by created_at in ascending order
earliest_users = users_df[users_df['location'] == 'Toronto'].nsmallest(5, 'created_at')

# Get the logins of the earliest users
earliest_user_logins = earliest_users['login'].tolist()

# Print the logins as a comma-separated string
print(', '.join(earliest_user_logins))

"""Solution: jamesmacaulay,michaelklishin,myles,nwjsmith,cablehead"""

#Question3
import pandas as pd

# Load the repositories CSV file
file_path = r'C:\Users\91735\OneDrive\Desktop\repositories.csv'
repos_df = pd.read_csv(file_path)

# Drop rows with missing license names
licenses = repos_df['license_name'].dropna()

# Get the top 3 most common licenses
popular_licenses = licenses.value_counts().nlargest(3)

# List the license names in order
popular_license_names = popular_licenses.index.tolist()

# Print the license names as a comma-separated string
print(', '.join(popular_license_names))

"""Solution; mit,other,apache-2.0"""

#Question4
import pandas as pd

# Load the users CSV file
file_path = r'C:\Users\91735\OneDrive\Desktop\users.csv'
users_df = pd.read_csv(file_path)

# Drop rows with missing company names and count occurrences
company_counts = users_df['company'].dropna().value_counts()

# Get the company with the highest count
most_common_company = company_counts.idxmax()
most_common_count = company_counts.max()

# Print the result
print(f"The majority of developers work at: {most_common_company} (Count: {most_common_count})")

"""Solution: UNIVERSITY OF TORONTO"""

#Question5
import pandas as pd

# Load the users CSV file
file_path = r'C:\Users\91735\OneDrive\Desktop\users.csv'
users_df = pd.read_csv(file_path)

# Drop rows with missing language data and count occurrences
language_counts = users_df['language'].dropna().value_counts()

# Get the most popular programming language
most_popular_language = language_counts.idxmax()
most_popular_count = language_counts.max()

# Print the result
print(f"The most popular programming language is: {most_popular_language} (Count: {most_popular_count})")

"""Solution: JavaScript"""

#Question6
import pandas as pd

# Load the users CSV file
file_path = r'C:\Users\91735\OneDrive\Desktop\users.csv'
users_df = pd.read_csv(file_path)

# Convert 'created_at' to datetime and filter users who joined after 2020
users_df['created_at'] = pd.to_datetime(users_df['created_at'])
recent_users = users_df[users_df['created_at'] > '2020-01-01']

# Count occurrences of each language
language_counts = recent_users['language'].dropna().value_counts()

# Get the second most popular programming language
if len(language_counts) >= 2:
    second_most_popular_language = language_counts.index[1]
    second_most_popular_count = language_counts.iloc[1]
    print(f"The second most popular programming language is: {second_most_popular_language} (Count: {second_most_popular_count})")
else:
    print("Not enough languages to determine the second most popular.")

"""Solution: TypeScript"""

#Question7
import pandas as pd

# Load the repositories CSV file
repos_file_path = r'C:\Users\91735\OneDrive\Desktop\repositories.csv'
repos_df = pd.read_csv(repos_file_path)

# Group by 'language' and calculate average stars per repository
average_stars = repos_df.groupby('language')['stargazers_count'].mean().reset_index()

# Find the language with the highest average
highest_avg_language = average_stars.loc[average_stars['stargazers_count'].idxmax()]

print(f"Language with the highest average stars: {highest_avg_language['language']} (Average Stars: {highest_avg_language['stargazers_count']})")

"""Solution: Cython"""

#Question8
import pandas as pd

# Load the users CSV file
users_file_path = r'C:\Users\91735\OneDrive\Desktop\users.csv'
users_df = pd.read_csv(users_file_path)

# Calculate leader_strength
users_df['leader_strength'] = users_df['followers'] / (1 + users_df['following'])

# Get the top 5 users by leader_strength
top_leaders = users_df.nlargest(5, 'leader_strength')[['login', 'leader_strength']]

# Create a comma-separated list of logins
top_logins = ', '.join(top_leaders['login'].tolist())

print(f"Top 5 users in terms of leader_strength: {top_logins}")

"""Solution: aneagoie,nayuki,GrapheneOS,hlissner,rspivak"""

#Question9
import pandas as pd

# Load the users CSV file
users_file_path = r'C:\Users\91735\OneDrive\Desktop\users.csv'
users_df = pd.read_csv(users_file_path)

# Calculate the correlation
correlation = users_df['followers'].corr(users_df['public_repos'])

print(f"The correlation between followers and public repositories is: {correlation:.2f}")

"""Solution: 0.056"""

#Question10
import pandas as pd
import statsmodels.api as sm

# Load the users CSV file
users_file_path = r'C:\Users\91735\OneDrive\Desktop\users.csv'
users_df = pd.read_csv(users_file_path)

# Define the independent variable (X) and dependent variable (y)
X = users_df['public_repos']
y = users_df['followers']

# Add a constant to the independent variable
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the regression results
print(model.summary())

# Estimate the additional followers per additional public repository
additional_followers_per_repo = model.params['public_repos']
print(f"Estimated additional followers per public repository: {additional_followers_per_repo:.2f}")

"""Solution: 0.257"""

#Question11
import pandas as pd

# Load the repositories CSV file
repos_file_path = r'C:\Users\91735\OneDrive\Desktop\repositories.csv'
repos_df = pd.read_csv(repos_file_path)

# Calculate the correlation between 'has_projects' and 'has_wiki'
correlation = repos_df['has_projects'].corr(repos_df['has_wiki'])
print(f"Correlation between having projects and having wiki enabled: {correlation:.2f}")

"""Solution: 0.372"""

#Question12
import pandas as pd

# Load the users CSV file
users_file_path = r'C:\Users\91735\OneDrive\Desktop\users.csv'
users_df = pd.read_csv(users_file_path)

# Calculate average following for hireable and non-hireable users
avg_following_hireable = users_df[users_df['hireable'] == True]['following'].mean()
avg_following_non_hireable = users_df[users_df['hireable'] == False]['following'].mean()

# Calculate the difference
difference = avg_following_hireable - avg_following_non_hireable

# Print the result rounded to 3 decimal places
print(f"Average following difference: {difference:.3f}")

"""Solution: -14.869"""

#Question13
import pandas as pd
import statsmodels.api as sm

# Load the users CSV file
users_file_path = r'C:\Users\91735\OneDrive\Desktop\users.csv'
users_df = pd.read_csv(users_file_path)

# Remove users without bios
users_df = users_df[users_df['bio'].notnull()]

# Calculate the bio word count
users_df['bio_word_count'] = users_df['bio'].apply(lambda x: len(x.split()))

# Prepare the regression data
X = users_df['bio_word_count']  # Independent variable
y = users_df['followers']        # Dependent variable
X = sm.add_constant(X)          # Add constant term for intercept

# Perform regression
model = sm.OLS(y, X).fit()

# Get the slope (coefficient of bio_word_count)
slope = model.params['bio_word_count']

# Print the result rounded to 3 decimal places
print(f"Regression slope of followers on bio word count: {slope:.3f}")

"""Solution: 8.127"""

#Question14
import pandas as pd

# Load the repositories CSV file
repos_file_path = r'C:\Users\91735\OneDrive\Desktop\repositories.csv'
repos_df = pd.read_csv(repos_file_path)

# Convert created_at to datetime
repos_df['created_at'] = pd.to_datetime(repos_df['created_at'])

# Filter for weekend entries (Saturday=5, Sunday=6)
repos_df['day_of_week'] = repos_df['created_at'].dt.dayofweek
weekend_repos = repos_df[repos_df['day_of_week'].isin([5, 6])]

# Count repositories per user
top_weekend_users = weekend_repos['login'].value_counts().head(5)

# Get the top 5 users' logins in order
top_user_logins = ', '.join(top_weekend_users.index)
print(f"Top 5 users who created the most repositories on weekends: {top_user_logins}")

"""Solution: andyw8,QuinntyneBrown,invokethreatguy,rgrinberg,Devang-25"""

#Question15
import pandas as pd

# Load the users CSV file
users_file_path = r'C:\Users\91735\OneDrive\Desktop\users.csv'
users_df = pd.read_csv(users_file_path)

# Calculate fractions
total_hireable = users_df[users_df['hireable'] == True].shape[0]
total_non_hireable = users_df[users_df['hireable'] == False].shape[0]

users_with_email_hireable = users_df[users_df['hireable'] == True]['email'].notnull().sum()
users_with_email_non_hireable = users_df[users_df['hireable'] == False]['email'].notnull().sum()

fraction_hireable = users_with_email_hireable / total_hireable if total_hireable > 0 else 0
fraction_non_hireable = users_with_email_non_hireable / total_non_hireable if total_non_hireable > 0 else 0

# Calculate the difference
difference = round(fraction_hireable - fraction_non_hireable, 3)

print(f"Difference in email sharing: {difference}")

"""Solution: 0.134"""

#Question16
import pandas as pd
from collections import Counter

# Load the users CSV file
users_file_path = r'C:\Users\91735\OneDrive\Desktop\users.csv'
users_df = pd.read_csv(users_file_path)

# Extract surnames
surnames = users_df['name'].dropna().str.split().str[-1].str.strip()
surnames_count = Counter(surnames)

# Find the most common surname(s)
most_common_surnames = surnames_count.most_common()

# Get the highest count
max_count = most_common_surnames[0][1]

# Filter for surnames with the highest count
common_surnames = [surname for surname, count in most_common_surnames if count == max_count]

# Sort alphabetically
common_surnames.sort()

# Output
print(f"Most common surname(s): {', '.join(common_surnames)}")

"""Solution: Ahmed"""