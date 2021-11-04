const queryBar = document.querySelectorAll("input[aria-label='Search query']")[0];
let query = document.querySelectorAll("input[aria-label='Search query']")[0].value;
const tweetsDiv = document.querySelector('div[aria-label="Timeline: Search timeline"]');
let tweets = tweetsDiv.getElementsByTagName("article");

queryBar.addEventListener("change", (e) => {
    let query = queryBar.value;
    console.log(query);
})

tweetsDiv.addEventListener("DOMSubtreeModified", (e) => {
    for (let i = 0; i < tweets.length; i++) {
        let tweet = tweets[i].querySelectorAll("div[class='css-1dbjc4n r-18u37iz']")[1];
        if (tweet.textContent.includes("@umich")) {
            tweets[i].style.opacity = 0.1;
        }
    }
})