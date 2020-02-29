# Konnect

### Problem
A lot of small local businesses often lack the visibility and support that they need from customers in order to grow and remain relevant in their community. Advertisements are expensive; small businesses hardly receive the coverage they need on bigger sites such as yelp. For this project, we aim to serve as a microinfuencer for multiple businesses that register with us. the main problem we found is that people are often steered away from patronizing these local businesses because they can not ascertain the quality of their services

### Solution
We are utilizing trend culture, the easiest and the fastest way to gain coverage about anything in this age, as our means of businesses promotion. As our company is based around trends, we encourage users and businesses to use trends in their tweets, posts etc. We also  utilize these trends ourself as a means of constant promotion for our businesses in popular websites. Also, as substantial reviews are not available for the smaller businesses, we utilize sentimental analysis AI, to anaylze reactions, tags, opinions, reviews scrapped from the main platforms of the internet such as facebook, twitter, reddit etc. 
To solve this problem, we had to rely on the twi. We realized that although people are unwilling to give reviews on Google or Yelp, they would readily post about their experiences on the twitter, reddit, .

### Detailed Technical Breakdown of Solution
Twitter X Reddit
* Have small businesses register with us and give us keywords/”sentiments” that can be associated with their businesses.
* The businesses would also do their part by encouraging users to use those hashtags/keywords when tweeting about the services received
* Search multiple online forums, twitter, reddit for reviews. 
* Generate a score/rating for those businesses based on those reviews by utilizing sentiment analysis
* Use generated ratings to also promote events on the "For you" page
* Allow users to search for businesses based on tags
* Display business profile with generated rating and tweets
* Encourage people to go to these small businesses
* Web/iOS/Android app for people to register or search for businesses around them
* Users can know how their business is doing based on their ratings

### Roadmap
* Twitter Implementation Backend
* Twitter bot to search all tweets for specific APIs
* Compile all tweets and store into csv file
* Pass each field into MonkeyLearn sentiment analytics
* Generate a rating that is featured on a profile page.
* Based on the generated ratings of local businesses, and location of user, display these tweets/posts.


### Moving Forward/Known Isssues
* Check for bots
* Scrape instagram for images for the businesses with location pins
* Improve sentiment analysis to accurately differentiate slangs from their literal meanings

