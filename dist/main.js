(()=>{const e=document.getElementsByClassName("filter-button");chrome.storage.sync.get("query",(({query:e})=>{document.querySelectorAll("input[aria-label='Search query']")[0].value=e,console.log("Query is currently "+e)})),e.addEventListener("click",(()=>{console.log("Abracadabra!")}))})();