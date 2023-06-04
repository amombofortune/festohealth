export const validateRegistration = (
  email,
  password,
  confirmPassword,
  user_type
) => {
  const errors = {};

  if (!user_type) {
    errors.userTypeError = "User type is required";
  }

  // Validate email
  if (!email) {
    errors.emailError = "Email is required";
  } else if (!isValidEmail(email)) {
    errors.emailError = "Invalid email format";
  }

  if (!password) {
    errors.passwordError = "Password is required";
  } else if (password.length < 8) {
    errors.passwordError = "Password must be at least 8 characters long";
  } else if (!/\d/.test(password)) {
    errors.passwordError = "Password must contain at least one digit";
  } else if (!/[a-z]/.test(password)) {
    errors.passwordError =
      "Password must contain at least one lowercase letter";
  } else if (!/[A-Z]/.test(password)) {
    errors.passwordError =
      "Password must contain at least one uppercase letter";
  } else if (!/[!@#$%^&*]/.test(password)) {
    errors.passwordError =
      "Password must contain at least one special character (!@#$%^&*)";
  }

  if (password !== confirmPassword) {
    errors.confirmPasswordError = "Password and Confirm Password do not match";
  }

  return errors;
};

// Helper function to validate email format
const isValidEmail = (email) => {
  // Basic email format validation
  const emailRegex = /^\S+@\S+\.\S+$/;
  return emailRegex.test(email);
};
