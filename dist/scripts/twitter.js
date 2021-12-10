var queryBar = document.querySelectorAll("input[aria-label='Search query']")[0];
var query = queryBar.value;
var tweetsDiv = document.querySelector('div[aria-label="Timeline: Search timeline"]');
var tweets = tweetsDiv.getElementsByTagName("article");
var depressive = "";
var toxic = "";
var sexual = "";
var profanity = "";

var url_d = "https://better-social-media.herokuapp.com/api/depressive";
var url_p = "https://better-social-media.herokuapp.com/api/perspective";

chrome.storage.sync.get("depressive", (res) => {
    depressive = res.depressive;
});
chrome.storage.sync.get("toxic", (res) => {
    toxic = res.toxic;
});
chrome.storage.sync.get("sexual", (res) => {
    sexual = res.sexual;
});
chrome.storage.sync.get("profanity", (res) => {
    profanity = res.profanity;
})

queryBar.addEventListener("change", () => {
    var query = queryBar.value;
    chrome.storage.sync.set({"query": query}, () => {
        console.log("Query set to: " + query);
    });
});

tweetsDiv.addEventListener("DOMSubtreeModified", () => {
    for (let i = 0; i < tweets.length; i++) {
        let tweet = tweets[i].querySelectorAll("div[class='css-1dbjc4n r-18u37iz']")[1];
        fetch(url_d, {
            method: 'post',
            headers: {"content-type": "application/json"},
            body: JSON.stringify({'tweet': tweet.textContent}),
            mode: 'no-cors'
        })
        .then(response => {
            return response.json()
        })
        .then((data) => {
            console.log('Request succeeded with JSON response', data);
        })
        .catch((err) => {
            console.log('Request failed', err);
        });
        if (tweet.textContent.includes("@umich")) {
            tweets[i].style.opacity = 0.1;
        }
    }
});