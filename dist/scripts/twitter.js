var queryBar = document.querySelectorAll("input[aria-label='Search query']")[0];
var query = queryBar.value;
var tweetsDiv = document.querySelector('div[aria-label="Timeline: Search timeline"]');
var tweets = tweetsDiv.getElementsByTagName("article");

queryBar.addEventListener("change", () => {
    var query = queryBar.value;
    chrome.storage.sync.set({"query": query}, () => {
        console.log("Query set to: " + query);
    });
});

tweetsDiv.addEventListener("DOMSubtreeModified", () => {
    for (let i = 0; i < tweets.length; i++) {
        let tweet = tweets[i].querySelectorAll("div[class='css-1dbjc4n r-18u37iz']")[1];
        if (tweet.textContent.includes("@umich")) {
            tweets[i].style.opacity = 0.1;
        }
    }
});