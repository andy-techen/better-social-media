# Better Social Media
**Better Social Media** is a project that attempts to build a Chrome extension that can filter out content across various categories on a user’s Twitter feed. The categories -- severe toxicity, profanity, depressiveness, and sexual explicitness -- represent sentiment or rhetorical properties that we consider the most salient and addressable problems within text analysis. The goal of this project is to address what we consider to be a large part of what makes current social media platforms toxic: echo chambers of negativity, anger, and despair.

## Chrome Extension
To allow our models to interact with our actual Twitter feeds, we created a Chrome extension as our interface to do so. Users can use sliders to adjust the strictness of the filters, and the tweets with predicted scores that exceed the thresholds in any category will get whited out.
<p>
  <img src="../images/filters.png" width="400">
  <img src="../images/whiteout.png" width="400">
</p>

## Models
Our tweets were mainly collected using the [tweepy](https://www.tweepy.org/) package and partially annotated by ourselves. For our models, we used TF-IDF as a feature vector for each of the tweets.

## Deployed API
After we determined our final models, we packaged each of the TF-IDF vectorizers as well as the models into Pickle files to prepare them for reuse. Using Flask, we built a RESTful API that can be called in our Chrome extension. The API was then deployed on Heroku. There are two endpoints available for POST requests.
### Depressiveness
Predictions for a tweet's depressiveness can be retrieved using a POST request: `POST https://better-social-media.herokuapp.com/api/depressive`
#### Sample Input
```json
{"tweet": "todays energy feels so depressive and ugly ugh I can’t wait the day to be over"}
```
#### Sample Output
Returns prediction scaled from 0 to 1.
```json
{
    "prediction": "0.98030853"
}
```

### Toxicity, Profanity, and Sexually Explicitness
Predictions for a tweet's toxicity, profanity, and sexually explicitness can be retrieved using a POST request: `POST https://better-social-media.herokuapp.com/api/depressive`
#### Sample Input
```json
{"tweet": "3 stages in life 1.birth 2.the fuck is this? 3.death"}
```
#### Sample Output
Returns prediction scaled from 1 to 10.
```json
{
    "profanity": "10.0",
    "sexually": "7.0",
    "toxicity": "9.0"
}
```

## Requirements
In order to run the api and models locally, install the required python packages using `pip install -r requirements.txt` after cloning the repository.

## Project Authors
- Andy Chen
- Saurabh Budholiya
- Cameron Milne
