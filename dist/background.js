chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({"depressive": 0.8});
  chrome.storage.sync.set({"toxic": 0.5});
  chrome.storage.sync.set({"sexual": 0.25});
  chrome.storage.sync.set({"profanity": 0.1});
  chrome.storage.sync.set({"query": ""});
});

chrome.declarativeContent.onPageChanged.removeRules(() => {
  chrome.declarativeContent.onPageChanged.addRules([{
    conditions: [new chrome.declarativeContent.PageStateMatcher({
      pageUrl: {hostEquals: 'twitter.com'}
    })
  ],
    actions: [new chrome.declarativeContent.ShowPageAction()]
  }]);
});