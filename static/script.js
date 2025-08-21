const password = document.getElementById("password");
const toggle = document.getElementById("toggle-pass");
const email = document.getElementById("email");

toggle.addEventListener("click", () => {
  if (password.type === "password") {
    password.type = "text";
    toggle.textContent = "Hide";
  } else {
    password.type = "password";
    toggle.textContent = "Show";
  }
});

document.getElementById("login").addEventListener("submit", (e) => {
  let valid = true;

  if (!email.value.includes("@")) {
    document.getElementById("email-error").textContent = "Enter a valid email.";
    valid = false;
  } else {
    document.getElementById("email-error").textContent = "";
  }

  if (password.value.length < 8) {
    document.getElementById("pw-error").textContent = "Password must be at least 8 characters.";
    valid = false;
  } else {
    document.getElementById("pw-error").textContent = "";
  }

  if (!valid) e.preventDefault();
});
