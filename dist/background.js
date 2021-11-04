chrome.runtime.onInstalled.addListener(function() {
  chrome.storage.sync.set({hide: true}, function() {
    console.log("Hide image is on");
  });
});

chrome.tabs.onActivated.addListener(tab => {
  chrome.tabs.get(tab.tabId, tab_info => {
    if(/^https:\/\/twitter\.com\/search/.test(tab_info.url)) {
      chrome.tabs.executeScript(null, {file: 'main.js'}, () => console.log("Retrieved query!"))
    }
  })
});