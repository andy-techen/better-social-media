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

function norm_to_range(val, from_min=0, from_max=1, to_min=1, to_max=10) {
    from_delta = from_max - from_min;
    to_delta = to_max - to_min;

    return ((val - from_min) * to_delta / from_delta) + to_min;
}

chrome.storage.sync.get("depressive", (res) => {
    depressive = res.depressive;
});
chrome.storage.sync.get("toxic", (res) => {
    toxic = norm_to_range(res.toxic);
});
chrome.storage.sync.get("sexual", (res) => {
    sexual = norm_to_range(res.sexual);
});
chrome.storage.sync.get("profanity", (res) => {
    profanity = norm_to_range(res.profanity);
})

queryBar.addEventListener("change", () => {
    var query = queryBar.value;
    chrome.storage.sync.set({"query": query}, () => {
        console.log("Query set to: " + query);
    });
});

function fetch_depressive(tweet) {
    let pred = 0;

    return fetch(url_d, {
        method: 'post',
        body: JSON.stringify({"tweet": tweet.textContent}),
        mode: 'cors'
    })
    .then(res => {
        return res.text();
    })
    .then(data => {
        pred = data ? JSON.parse(data).prediction : 0;
        return pred;
    })
    .catch(err => {
        console.log('Depressive request failed', err);
    });
}

function fetch_perspective(tweet) {
    let pred = {};
    let pred_prof = 0;
    let pred_sex = 0;
    let pred_toxic = 0;

    return fetch(url_p, {
        method: 'post',
        body: JSON.stringify({"tweet": tweet.textContent}),
        mode: 'cors'
    })
    .then(res => {
        return res.text();
    })
    .then(data => {
        pred = data ? JSON.parse(data) : {"profanity": 0, "sexually": 0, "toxicity": 0};
        pred_prof = pred.profanity;
        pred_sex = pred.sexually;
        pred_toxic = pred.toxicity;
        return {'prof': pred_prof, 'sex': pred_sex, 'toxic': pred_toxic};
    })
    .catch(err => {
        console.log('Perspective request failed', err);
    });
}

tweetsDiv.addEventListener("DOMSubtreeModified", () => {
    tweets = tweetsDiv.getElementsByTagName("article");
    for (let i = 0; i < tweets.length; i++) {
        try {
            let tweet = tweets[i].querySelectorAll("div[class*='r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0']")[0];
            let tweet_id = tweet.id;

            // fetch depressive predictions
            let promise_d = fetch_depressive(tweet);
            // fetch perspective api predictions
            let promise_p = fetch_perspective(tweet);
    
            Promise.all([promise_d, promise_p])
            .then(preds => {
                let pred_d = preds[0];
                let pred_p = preds[1];
                // if any category exceeds slider settings
                if (pred_d > (1 - depressive) || pred_p['prof'] > (10 - profanity) || pred_p['sex'] > (10 - sexual) || pred_p['toxic'] > (10 - toxic)) {
                    console.log(`Tweet ${i} depressive: ${pred_d}`);
                    console.log(`Tweet ${i} profanity: ${pred_p['prof']}`);
                    console.log(`Tweet ${i} sexually: ${pred_p['sex']}`);
                    console.log(`Tweet ${i} toxicity: ${pred_p['toxic']}`);
                    console.log(`Tweet ${tweet_id} filtered out!`);
                    document.getElementById(tweet_id).style.opacity = 0.1;
                }
            });
        } catch (err) {
            console.log(err);
        }
    }
});