document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const roll = document.getElementById("roll").value.trim();
    const course = document.getElementById("course").value;

    if (!name || !email || !roll || !course) {
        document.getElementById("message").textContent = "Please fill all fields.";
        return;
    }

    document.getElementById("message").textContent =
        "Registration successful for " + name + "!";
    this.reset();
});
