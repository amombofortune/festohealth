export const validateLogin = (email, password) => {
  const errors = {};

  // Validate email
  if (!email) {
    errors.emailError = "Email is required";
  } else if (!isValidEmail(email)) {
    errors.emailError = "Invalid email format";
  }

  // Validate password
  if (!password) {
    errors.passwordError = "Password is required";
  }

  return errors;
};

// Helper function to validate email format
const isValidEmail = (email) => {
  // Basic email format validation
  const emailRegex = /^\S+@\S+\.\S+$/;
  return emailRegex.test(email);
};
