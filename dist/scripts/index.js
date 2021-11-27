// Initialize button with user's preferred color
let queryTerm = document.getElementById("query-term");
const button = document.getElementById("filter-button");
const depressive = document.getElementById("depressive");
const toxic = document.getElementById("toxic");
const sexual = document.getElementById("sexual");
const profanity = document.getElementById("profanity");

// executing twitter.js
chrome.tabs.query({
  active: true,
  currentWindow: true
}, (tabs) => {
  chrome.scripting.executeScript({
    target: {tabId: tabs[0].id},
    files: ['scripts/twitter.js']
  });
});

// get query from search bar
chrome.storage.onChanged.addListener(() => {
  chrome.storage.sync.get("query", (res) => {
    queryTerm.textContent = res.query;
  });
});

chrome.storage.sync.get("depressive", (res) => {
  depressive.value = res.depressive;
});
chrome.storage.sync.get("toxic", (res) => {
  toxic.value = res.toxic;
});
chrome.storage.sync.get("sexual", (res) => {
  sexual.value = res.sexual;
});
chrome.storage.sync.get("profanity", (res) => {
  profanity.value = res.profanity;
});
chrome.storage.sync.get("query", (res) => {
  queryTerm.textContent = res.query;
});

// save settings in storage
button.addEventListener("click", (e) => {
  e.preventDefault();
  chrome.storage.sync.set({"depressive": depressive.value}, () => {
    console.log("Depressive set to: " + depressive.value);
  });
  chrome.storage.sync.set({"toxic": toxic.value}, () => {
    console.log("Toxic set to: " + toxic.value);
  });
  chrome.storage.sync.set({"sexual": sexual.value}, () => {
    console.log("Sexual set to: " + sexual.value);
  });
  chrome.storage.sync.set({"profanity": profanity.value}, () => {
    console.log("Profanity set to: " + profanity.value);
  });
  console.log("Abracadabra!");
});