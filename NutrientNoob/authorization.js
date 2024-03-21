// Store user info for login
const userInfoMap = new Map();

// Function to validate the password requirements: 
// 8 Characters Long, At least 1 Capital Letter, At least 1 Number
function validatePassword(password) {
  return password.length >= 8 && /[A-Z]/.test(password) && /\d/.test(password);
}

// Sign Up Function
function handleSignUp(event) {
  event.preventDefault();

  // Adjusting selectors to match the HTML class and type attributes
  const username = document.querySelector('.signup .input[type="text"]').value; // Assuming this is the username
  const password = document.querySelector('.signup .input[type="password"]:nth-of-type(1)').value; // First password input
  const confirmPassword = document.querySelector('.signup .input[type="password"]:nth-of-type(2)').value; // Second password input

  if (!validatePassword(password)) {
    alert('Password must be at least 8 characters long, contain a number, and an uppercase letter.');
    return;
  }

  if (password !== confirmPassword) {
    alert('Passwords do not match.');
    return;
  }

  // Store the user information with username as key
  userInfoMap.set(username, { password: password });

  // Here you would normally handle the AJAX request to submit the form data to the server.
  console.log('Sign Up Success:', { username, password });
}

// Function to handle the login
function handleLogin(event) {
  event.preventDefault();

  // Adjusting selectors to match the HTML class and type attributes
  const username = document.querySelector('.login .input[type="text"]').value; // Assuming this is the username
  const password = document.querySelector('.login .input[type="password"]').value; // Assuming this is the password

  // Check if the user exists and password matches
  if (userInfoMap.has(username) && userInfoMap.get(username).password === password) {
    console.log('Login Success:', { username });
  } else {
    alert('Login Failed: Incorrect username or password.');
  }
}

// Wait for the DOM to fully load before attaching event handlers
document.addEventListener("DOMContentLoaded", function() {
  // Attach the event handler for the sign-up form
  const signUpForm = document.querySelector('.signup form');
  signUpForm.addEventListener('submit', handleSignUp);

  // Attach the event handler for the login form
  const loginForm = document.querySelector('.login form');
  loginForm.addEventListener('submit', handleLogin);
});
