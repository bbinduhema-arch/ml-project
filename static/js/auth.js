// Authentication functions

// Wait for auth to be ready
function waitForAuth() {
    return new Promise((resolve) => {
        if (typeof auth !== 'undefined' && auth) {
            resolve(auth);
        } else {
            // Wait a bit and try again
            setTimeout(() => {
                if (typeof auth !== 'undefined' && auth) {
                    resolve(auth);
                } else {
                    console.error('Auth not initialized');
                    resolve(null);
                }
            }, 100);
        }
    });
}

// Sign up function
async function signUp(email, password) {
    const authInstance = await waitForAuth();
    if (!authInstance) {
        return { success: false, error: 'Firebase Authentication not initialized. Please refresh the page.' };
    }
    
    return authInstance.createUserWithEmailAndPassword(email, password)
        .then((userCredential) => {
            // Signed up successfully
            const user = userCredential.user;
            console.log('User signed up:', user);
            return { success: true, user: user };
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            console.error('Sign up error:', errorCode, errorMessage);
            
            // User-friendly error messages
            let friendlyMessage = errorMessage;
            if (errorCode === 'auth/email-already-in-use') {
                friendlyMessage = 'This email is already registered. Please sign in instead.';
            } else if (errorCode === 'auth/invalid-email') {
                friendlyMessage = 'Please enter a valid email address.';
            } else if (errorCode === 'auth/weak-password') {
                friendlyMessage = 'Password should be at least 6 characters.';
            }
            
            return { success: false, error: friendlyMessage };
        });
}

// Sign in function
async function signIn(email, password) {
    const authInstance = await waitForAuth();
    if (!authInstance) {
        return { success: false, error: 'Firebase Authentication not initialized. Please refresh the page.' };
    }
    
    return authInstance.signInWithEmailAndPassword(email, password)
        .then((userCredential) => {
            // Signed in successfully
            const user = userCredential.user;
            console.log('User signed in:', user);
            return { success: true, user: user };
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            console.error('Sign in error:', errorCode, errorMessage);
            
            // User-friendly error messages
            let friendlyMessage = errorMessage;
            if (errorCode === 'auth/user-not-found') {
                friendlyMessage = 'No account found with this email. Please sign up first.';
            } else if (errorCode === 'auth/wrong-password') {
                friendlyMessage = 'Incorrect password. Please try again.';
            } else if (errorCode === 'auth/invalid-email') {
                friendlyMessage = 'Please enter a valid email address.';
            } else if (errorCode === 'auth/user-disabled') {
                friendlyMessage = 'This account has been disabled.';
            }
            
            return { success: false, error: friendlyMessage };
        });
}

// Sign out function
async function signOut() {
    const authInstance = await waitForAuth();
    if (!authInstance) {
        return { success: false, error: 'Firebase Authentication not initialized.' };
    }
    
    return authInstance.signOut()
        .then(() => {
            console.log('User signed out');
            return { success: true };
        })
        .catch((error) => {
            console.error('Sign out error:', error);
            return { success: false, error: error.message };
        });
}

// Get current user
function getCurrentUser() {
    if (typeof auth !== 'undefined' && auth) {
        return auth.currentUser;
    }
    return null;
}

// Auth state observer - wait for auth to be ready
setTimeout(() => {
    if (typeof auth !== 'undefined' && auth) {
        auth.onAuthStateChanged((user) => {
            if (user) {
                // User is signed in
                console.log('User is signed in:', user.email);
            } else {
                // User is signed out
                console.log('User is signed out');
            }
        });
    }
}, 500);

