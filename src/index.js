// Initialize button with user's preferred color
// let queryTerm = document.getElementById("query-term");
const button = document.getElementsByClassName("filter-button");

// get query from search bar
chrome.storage.sync.get("query", ({ query }) => {
  document.querySelectorAll("input[aria-label='Search query']")[0].value = query;
  console.log("Query is currently " + query);
  // queryTerm.value = query;
})

button.addEventListener("click", () => {
  console.log("Abracadabra!");
})