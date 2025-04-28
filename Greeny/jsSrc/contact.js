document.getElementById("contactForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent actual form submission
    // Here you can add AJAX call or validation
    document.getElementById("successMessage").classList.remove("hidden");
    this.reset(); // Clear the form
});