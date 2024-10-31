#GitHub Toronto Users Analysis

#Project Overview


This project involves analyzing GitHub users based in Toronto with over 100 followers. We used the GitHub API to scrape user and repository data and perform various analyses to understand trends, commonalities, and insights in their usage patterns.

#Key Findings

Top 5 Users by Followers:
aneagoie, ZhangMYihua, susanli2016, thedaviddias, ange-yaghi

Earliest Registered Users:
jamesmacaulay, michaelklishin, myles, nwjsmith, cablehead

Most Popular Licenses:
mit, other, apache-2.0

Company with Majority Representation:
University of Toronto

Most Popular Programming Language:
JavaScript

Second Most Popular Language for Users Joined After 2020:
TypeScript

Language with the Highest Average Stars per Repository:
Cython

Top 5 Users by Leader Strength (followers / (1 + following)):
aneagoie, nayuki, GrapheneOS, hlissner, rspivak

Correlation between Followers and Public Repositories:
0.056 (slightly positive, but very weak correlation)

Additional Followers per Public Repository (Based on Regression):
0.257 (suggesting that each additional repository brings about a 0.26 increase in followers)

Correlation between Projects and Wikis Being Enabled Together:
0.372 (some tendency for users who enable projects to also enable wikis)

Following Difference for Hireable vs. Non-Hireable Users:
-14.869 (hireable users tend to follow fewer people than non-hireable users)

Impact of Bio Word Count on Followers (Based on Regression):
8.127 (indicating that each additional word in the bio is associated with ~8 more followers)

Top 5 Users by Repositories Created on Weekends:
andyw8, QuinntyneBrown, invokethreatguy, rgrinberg, Devang-25

Difference in Email Sharing for Hireable Users:
0.134 (hireable users are more likely to share their emails)

Most Common Surname:
Ahmed

#Explanation of Data Scraping Process

To gather this data, we used the GitHub API, focusing on users in Toronto with more than 100 followers. Our script iterated over user profiles, collecting data such as follower count, registration date, repository information, and activity patterns. We then processed this data using Pandas to calculate metrics and answer specific queries regarding language usage, company affiliation, popular licenses, and more.

#Interesting and Surprising Findings

One surprising insight from our analysis is that users with longer bios tend to have more followers, with each additional word in their bio corresponding to around 8 more followers. This suggests that a well-detailed bio might positively impact engagement and followership on GitHub.

#Actionable Recommendation for Developers

To maximize their reach and engagement on GitHub, developers may benefit from writing a comprehensive bio, sharing contact information (such as an email), and showcasing more repositories. Additionally, enabling wikis and projects on their repositories could create a more engaging profile, as these features are commonly enabled together among popular users.
