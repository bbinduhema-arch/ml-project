# Firebase Authentication Setup Guide

## Steps to Configure Firebase

1. **Create a Firebase Project**
   - Go to [Firebase Console](https://console.firebase.google.com/)
   - Click "Add project" or select an existing project
   - Follow the setup wizard

2. **Enable Authentication**
   - In your Firebase project, go to "Authentication" in the left sidebar
   - Click "Get started"
   - Go to the "Sign-in method" tab
   - Enable "Email/Password" authentication
   - Click "Save"

3. **Get Your Firebase Configuration**
   - In Firebase Console, click the gear icon ⚙️ next to "Project Overview"
   - Select "Project settings"
   - Scroll down to "Your apps" section
   - If you don't have a web app, click the web icon `</>` to add one
   - Copy the Firebase configuration object

4. **Update Firebase Configuration**
   - Open `static/js/firebase-config.js`
   - Replace the placeholder values with your actual Firebase configuration:
     ```javascript
     const firebaseConfig = {
       apiKey: "YOUR_API_KEY",
       authDomain: "YOUR_AUTH_DOMAIN",
       projectId: "YOUR_PROJECT_ID",
       storageBucket: "YOUR_STORAGE_BUCKET",
       messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
       appId: "YOUR_APP_ID"
     };
     ```

## Routes Added

- `/signin` - Sign in page
- `/signup` - Sign up page

## Features

- Email/Password authentication
- Form validation
- Error handling
- Success messages
- Automatic redirects after authentication
- Responsive design
- Modern UI with animations

## Usage

1. Navigate to `/signup` to create a new account
2. Navigate to `/signin` to sign in with existing credentials
3. After successful sign in, users are redirected to the home page

