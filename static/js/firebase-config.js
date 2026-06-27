// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyABId0rWfT9BVwmGBqgjkhwe0w87fubEnI",
  authDomain: "silkworm-e707c.firebaseapp.com",
  projectId: "silkworm-e707c",
  storageBucket: "silkworm-e707c.firebasestorage.app",
  messagingSenderId: "103074914437",
  appId: "1:103074914437:web:3fd9d72e8109e203fa49ec",
  measurementId: "G-M5SYFWCXV2"
};

// Initialize Firebase
let auth;
if (typeof firebase !== 'undefined') {
  try {
    // Check if Firebase is already initialized
    if (!firebase.apps || firebase.apps.length === 0) {
      firebase.initializeApp(firebaseConfig);
    }
    
    // Initialize Firebase Authentication and get a reference to the service
    auth = firebase.auth();
    
    console.log('Firebase initialized successfully');
  } catch (error) {
    console.error('Firebase initialization error:', error);
  }
} else {
  console.error('Firebase SDK not loaded!');
}

