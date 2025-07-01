// Modal Functionality
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.style.display = 'flex';
  }
  
  function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.style.display = 'none';
  }
  
  document.querySelectorAll('.close').forEach(button => {
    button.addEventListener('click', () => {
      const modal = button.closest('.modal');
      modal.style.display = 'none';
    });
  });
  
  window.addEventListener('click', (event) => {
    if (event.target.classList.contains('modal')) {
      event.target.style.display = 'none';
    }
  });
  
  // Function to update navbar based on login status
  function updateNavbar() {
    const navButtons = document.getElementById('nav-buttons');
    const user = JSON.parse(localStorage.getItem('user'));
  
    if (user) {
      navButtons.innerHTML = `
        <a href="./profile.html" class="profile-btn">Profile</a>
      `;
    } else {
      navButtons.innerHTML = `
        <button class="login-btn" onclick="openModal('loginModal')">Login</button>
        <button class="signup-btn" onclick="openModal('signupModal')">Sign up</button>
      `;
    }
  }
  
  // Handle Login Form Submission
  document.getElementById('loginForm').addEventListener('submit', (event) => {
    event.preventDefault();
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
  
    // For simplicity, we're not validating the password here
    // In a real app, you'd verify credentials with a backend
    const user = {
      username: email.split('@')[0] || email, // Use part of email or phone as username for login
      email: email
    };
  
    localStorage.setItem('user', JSON.stringify(user));
    updateNavbar();
    closeModal('loginModal');
    window.location.href = './index.html'; // Redirect to home page
  });
  
  // Handle Signup Form Submission
  document.getElementById('signupForm').addEventListener('submit', (event) => {
    event.preventDefault();
    const username = document.getElementById('signupUsername').value;
    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    
    if (password !== confirmPassword) {
      alert('Passwords do not match!');
      return;
    }
    
    const user = {
      username: username,
      email: email
    };
  
    localStorage.setItem('user', JSON.stringify(user));
    updateNavbar();
    closeModal('signupModal');
    window.location.href = './index.html'; // Redirect to home page
  });
  
  // Chat Functionality (only applies to chat.html)
  if (document.getElementById('input-field')) {
    const inputField = document.getElementById('input-field');
    const outputContainer = document.getElementById('output');
    const detectedValue = document.getElementById('detected-value');
  
    inputField.addEventListener('keypress', function(event) {
      if (event.key === 'Enter') {
        const inputValue = inputField.value.trim();
        
        if (inputValue) {
          outputContainer.style.display = 'block';
          detectedValue.textContent = 'nan';
        } else {
          outputContainer.style.display = 'none';
        }
      }
    });
  }
  
  // Profile Page Functionality (only applies to profile.html)
  if (document.getElementById('profile-username')) {
    const user = JSON.parse(localStorage.getItem('user'));
    if (user) {
      document.getElementById('profile-username').textContent = user.username;
      document.getElementById('profile-email').textContent = user.email;
    }
  }
  
  // Logout Functionality
  function logout() {
    localStorage.removeItem('user');
    updateNavbar();
    window.location.href = './index.html'; // Redirect to home page
  }
  
  // Update navbar on page load
  document.addEventListener('DOMContentLoaded', () => {
    updateNavbar();
  });