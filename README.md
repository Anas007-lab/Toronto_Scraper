#GitHub Toronto Users Analysis

#Project Overview


This project involves analyzing GitHub users based in Toronto with over 100 followers. We used the GitHub API to scrape user and repository data and perform various analyses to understand trends, commonalities, and insights in their usage patterns.

#Key Findings

1-Top 5 Users by Followers:
aneagoie, ZhangMYihua, susanli2016, thedaviddias, ange-yaghi

2-Earliest Registered Users:
jamesmacaulay, michaelklishin, myles, nwjsmith, cablehead

3-Most Popular Licenses:
mit, other, apache-2.0

4-Company with Majority Representation:
University of Toronto

5-Most Popular Programming Language:
JavaScript

6-Second Most Popular Language for Users Joined After 2020:
TypeScript

7-Language with the Highest Average Stars per Repository:
Cython

8-Top 5 Users by Leader Strength (followers / (1 + following)):
aneagoie, nayuki, GrapheneOS, hlissner, rspivak

9-Correlation between Followers and Public Repositories:
0.056 (slightly positive, but very weak correlation)

10-Additional Followers per Public Repository (Based on Regression):
0.257 (suggesting that each additional repository brings about a 0.26 increase in followers)

11-Correlation between Projects and Wikis Being Enabled Together:
0.372 (some tendency for users who enable projects to also enable wikis)

12-Following Difference for Hireable vs. Non-Hireable Users:
-14.869 (hireable users tend to follow fewer people than non-hireable users)

13-Impact of Bio Word Count on Followers (Based on Regression):
8.127 (indicating that each additional word in the bio is associated with ~8 more followers)

14-Top 5 Users by Repositories Created on Weekends:
andyw8, QuinntyneBrown, invokethreatguy, rgrinberg, Devang-25

15-Difference in Email Sharing for Hireable Users:
0.134 (hireable users are more likely to share their emails)

16-Most Common Surname:
Ahmed

Q1- #Explanation of Data Scraping Process

To gather this data, we used the GitHub API, focusing on users in Toronto with more than 100 followers. Our script iterated over user profiles, collecting data such as follower count, registration date, repository information, and activity patterns. We then processed this data using Pandas to calculate metrics and answer specific queries regarding language usage, company affiliation, popular licenses, and more.

Q2- #Interesting and Surprising Findings

One surprising insight from our analysis is that users with longer bios tend to have more followers, with each additional word in their bio corresponding to around 8 more followers. This suggests that a well-detailed bio might positively impact engagement and followership on GitHub.

Q3- #Actionable Recommendation for Developers

To maximize their reach and engagement on GitHub, developers may benefit from writing a comprehensive bio, sharing contact information (such as an email), and showcasing more repositories. Additionally, enabling wikis and projects on their repositories could create a more engaging profile, as these features are commonly enabled together among popular users.
