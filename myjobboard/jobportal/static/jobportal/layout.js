document.addEventListener("DOMContentLoaded", function() {
    // Get the current URL
    const currentURL = window.location.href;
    
    // Get all anchor tags
    const anchorTags = document.getElementsByTagName("a");
    
    // Loop through all anchor tags to find the one with the href matching the current URL
    for (let i = 0; i < anchorTags.length; i++) {
        if (anchorTags[i].href === currentURL) {
            // Add the "active" class to the parent li tag of the anchor tag
            const parentLi = anchorTags[i].parentNode;
            if (parentLi.tagName.toLowerCase() === 'li') {
                // Remove "active" class from all li tags with the class name "jobNavElement"
                const allLiElements = document.getElementsByClassName("jobNavElement");
                for (let j = 0; j < allLiElements.length; j++) {
                    allLiElements[j].classList.remove("active");
                }
                // Add "active" class to the parent li tag of the anchor tag
                parentLi.classList.add("active");
            }
            break; // Exit the loop once the matching anchor tag is found
        }
    }
});
