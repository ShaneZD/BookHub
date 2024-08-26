// Toggle content visibility
function toggleContent(buttonId, contentId) {
    const button = document.getElementById(buttonId);
    const content = document.getElementById(contentId);
    if (content.style.display === 'none' || content.style.display === '') {
        content.style.display = 'block';
        button.textContent = 'Hide Details';
    } else {
        content.style.display = 'none';
        button.textContent = 'Show Details';
    }
}

// Add an event listener to a button to scroll smoothly to the top
function scrollToTop(buttonId) {
    const button = document.getElementById(buttonId);
    button.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// Add a hover effect to change the background colour of an element
function addHoverEffect(elementId, hoverColor, originalColor) {
    const element = document.getElementById(elementId);
    element.addEventListener('mouseover', function() {
        element.style.backgroundColor = hoverColor;
    });
    element.addEventListener('mouseout', function() {
        element.style.backgroundColor = originalColor;
    });
}

// Call functions on page load
document.addEventListener('DOMContentLoaded', function() {
    // Example usage
    toggleContent('toggleDetailsButton', 'profileDetails');
    scrollToTop('scrollTopButton');
    addHoverEffect('profileCard', '#f8f9fa', '#ffffff');
});
