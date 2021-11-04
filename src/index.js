// Initialize button with user's preferred color
let queryTerm = document.getElementById("query-term");
const button = document.getElementsByClassName("filter-button");
const depressive = document.getElementById("depressive");
const toxic = document.getElementById("toxic");
const sexual = document.getElementById("sexual");
const profanity = document.getElementById("profanity");

chrome.storage.sync.get("depressive", (res) => {
  depressive.value = res.depressive;
  console.log(res.depressive);
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

// get query from search bar
chrome.storage.sync.get("query", (res) => {
  queryTerm.textContent = res.query;
  console.log("Query is currently " + res.query);
})

button.addEventListener("click", () => {
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
})