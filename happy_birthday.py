import streamlit as st
from datetime import datetime
import time

# Page config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="wide")

# Custom CSS for animations
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Full page background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        overflow: hidden;
    }
    
    /* Animations */
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-30px) rotate(5deg); }
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-40px); }
    }
    
    @keyframes slideIn {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: scale(0.5); }
        to { opacity: 1; transform: scale(1); }
    }
    
    @keyframes peacockEnter {
        0% { transform: translateX(150%) scale(0.5); opacity: 0; }
        50% { transform: translateX(50%) scale(1.5); opacity: 1; }
        100% { transform: translateX(50%) scale(1); opacity: 1; }
    }
    
    @keyframes peacockExit {
        0% { transform: translateX(50%) scale(1); opacity: 1; }
        100% { transform: translateX(150%) scale(0.5); opacity: 0; }
    }
    
    @keyframes sparkle {
        0%, 100% { opacity: 1; transform: scale(1) rotate(0deg); }
        50% { opacity: 0.3; transform: scale(1.5) rotate(180deg); }
    }
    
    @keyframes fall {
        0% { transform: translateY(-100vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0.5; }
    }
    
    @keyframes firework {
        0% { transform: scale(0); opacity: 1; }
        50% { transform: scale(1); opacity: 1; }
        100% { transform: scale(1.5); opacity: 0; }
    }
    
    /* Welcome screen */
    .welcome-screen {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 1000;
        animation: fadeIn 1s ease-in;
    }
    
    .welcome-banner {
        background: linear-gradient(45deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3);
        padding: 30px 60px;
        border-radius: 50px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        animation: bounce 2s ease-in-out infinite;
        margin-bottom: 40px;
    }
    
    .welcome-banner h1 {
        color: white;
        font-size: 4em;
        text-align: center;
        margin: 0;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
    }
    
    .welcome-pets {
        display: flex;
        gap: 100px;
        animation: slideIn 1.5s ease-out;
    }
    
    .pet {
        font-size: 8em;
        animation: bounce 1.5s ease-in-out infinite;
    }
    
    .pet:nth-child(2) {
        animation-delay: 0.3s;
    }
    
    /* Peacock animation */
    .peacock-container {
        position: fixed;
        top: 50%;
        left: 0;
        width: 100vw;
        height: auto;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 999;
        pointer-events: none;
    }
    
    .peacock {
        font-size: 15em;
        animation: peacockEnter 3s ease-out forwards;
    }
    
    .peacock.exit {
        animation: peacockExit 2s ease-in forwards;
    }
    
    /* Main content */
    .birthday-content {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        z-index: 100;
        animation: fadeIn 2s ease-in;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 50px;
        border-radius: 30px;
        box-shadow: 0 20px 80px rgba(0,0,0,0.3);
    }
    
    .birthday-content h1 {
        font-size: 5em;
        color: #ff6b6b;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        margin-bottom: 30px;
        animation: bounce 3s ease-in-out infinite;
    }
    
    .birthday-content p {
        font-size: 1.8em;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin: 20px 0;
        line-height: 1.6;
    }
    
    /* Floating animals */
    .floating-animal {
        position: fixed;
        font-size: 4em;
        animation: float 3s ease-in-out infinite;
        z-index: 50;
    }
    
    /* Snowflakes */
    .snowflake {
        position: fixed;
        color: white;
        font-size: 2em;
        animation: fall linear infinite;
        z-index: 10;
    }
    
    /* Confetti */
    .confetti {
        position: fixed;
        font-size: 2em;
        animation: fall linear infinite;
        z-index: 10;
    }
    
    /* Fireworks */
    .firework {
        position: fixed;
        font-size: 4em;
        animation: firework 2s ease-out infinite;
        z-index: 10;
    }
    
    /* Sparkles */
    .sparkle {
        position: fixed;
        font-size: 2em;
        animation: sparkle 2s ease-in-out infinite;
        z-index: 10;
    }
</style>
""", unsafe_allow_html=True)

# Create the animated HTML
st.markdown("""
<div id="app">
    <!-- Welcome Screen (shows first) -->
    <div class="welcome-screen" id="welcomeScreen">
        <div class="welcome-banner">
            <h1>🎉 WELCOME! 🎉</h1>
        </div>
        <div class="welcome-pets">
            <div class="pet">🐱</div>
            <div class="pet">🐶</div>
        </div>
    </div>
    
    <!-- Peacock Animation -->
    <div class="peacock-container" id="peacockContainer" style="display: none;">
        <div class="peacock" id="peacock">🦚</div>
    </div>
    
    <!-- Main Birthday Content (shows after peacock) -->
    <div class="birthday-content" id="birthdayContent" style="display: none;">
        <h1>🎂🌹✨ Happy Birthday! ✨🌹🎂</h1>
        <p>🌟 May your birthday be as extraordinary and wonderful as you are! 🎉🌟</p>
        <p>💖 Wishing you a day filled with happiness, laughter and as many cupcakes as your heart desires! 🧁</p>
        <p>✨ May your Birthday be filled with the magic of love, joy, and all the things that make you happy! ✨</p>
    </div>
    
    <!-- Floating Animals scattered everywhere -->
    <div class="floating-animal" style="top: 5%; left: 5%; animation-delay: 0s;">🐶</div>
    <div class="floating-animal" style="top: 10%; right: 8%; animation-delay: 0.5s;">🐱</div>
    <div class="floating-animal" style="top: 20%; left: 15%; animation-delay: 1s;">🐕</div>
    <div class="floating-animal" style="top: 25%; right: 20%; animation-delay: 1.5s;">🐈</div>
    <div class="floating-animal" style="top: 40%; left: 3%; animation-delay: 2s;">🐩</div>
    <div class="floating-animal" style="top: 45%; right: 5%; animation-delay: 2.5s;">🐈‍⬛</div>
    <div class="floating-animal" style="bottom: 20%; left: 10%; animation-delay: 0.3s;">🦮</div>
    <div class="floating-animal" style="bottom: 25%; right: 12%; animation-delay: 0.8s;">🐕‍🦺</div>
    <div class="floating-animal" style="bottom: 10%; left: 20%; animation-delay: 1.3s;">🐾</div>
    <div class="floating-animal" style="bottom: 15%; right: 18%; animation-delay: 1.8s;">🐾</div>
    <div class="floating-animal" style="top: 30%; left: 45%; animation-delay: 2.2s;">🐶</div>
    <div class="floating-animal" style="top: 60%; right: 30%; animation-delay: 2.7s;">🐱</div>
    <div class="floating-animal" style="top: 70%; left: 35%; animation-delay: 3s;">🐕</div>
    <div class="floating-animal" style="bottom: 40%; right: 40%; animation-delay: 0.6s;">🐈</div>
    
    <!-- Snowflakes -->
    <div class="snowflake" style="left: 10%; animation-duration: 8s; animation-delay: 0s;">❄️</div>
    <div class="snowflake" style="left: 20%; animation-duration: 10s; animation-delay: 1s;">❄️</div>
    <div class="snowflake" style="left: 30%; animation-duration: 9s; animation-delay: 2s;">❄️</div>
    <div class="snowflake" style="left: 40%; animation-duration: 11s; animation-delay: 0.5s;">❄️</div>
    <div class="snowflake" style="left: 50%; animation-duration: 8.5s; animation-delay: 1.5s;">❄️</div>
    <div class="snowflake" style="left: 60%; animation-duration: 10.5s; animation-delay: 2.5s;">❄️</div>
    <div class="snowflake" style="left: 70%; animation-duration: 9.5s; animation-delay: 0.8s;">❄️</div>
    <div class="snowflake" style="left: 80%; animation-duration: 11.5s; animation-delay: 1.8s;">❄️</div>
    <div class="snowflake" style="left: 90%; animation-duration: 10s; animation-delay: 3s;">❄️</div>
    <div class="snowflake" style="left: 5%; animation-duration: 9s; animation-delay: 2.2s;">❄️</div>
    
    <!-- Confetti -->
    <div class="confetti" style="left: 15%; animation-duration: 7s; animation-delay: 0s; color: #ff6b6b;">🎊</div>
    <div class="confetti" style="left: 25%; animation-duration: 8s; animation-delay: 1s; color: #feca57;">🎉</div>
    <div class="confetti" style="left: 35%; animation-duration: 6s; animation-delay: 2s; color: #48dbfb;">🎊</div>
    <div class="confetti" style="left: 45%; animation-duration: 9s; animation-delay: 0.5s; color: #ff9ff3;">🎉</div>
    <div class="confetti" style="left: 55%; animation-duration: 7.5s; animation-delay: 1.5s; color: #ff6b6b;">🎊</div>
    <div class="confetti" style="left: 65%; animation-duration: 8.5s; animation-delay: 2.5s; color: #feca57;">🎉</div>
    <div class="confetti" style="left: 75%; animation-duration: 6.5s; animation-delay: 0.8s; color: #48dbfb;">🎊</div>
    <div class="confetti" style="left: 85%; animation-duration: 9.5s; animation-delay: 1.8s; color: #ff9ff3;">🎉</div>
    <div class="confetti" style="left: 95%; animation-duration: 7s; animation-delay: 3s; color: #ff6b6b;">🎊</div>
    
    <!-- Fireworks -->
    <div class="firework" style="top: 15%; left: 20%; animation-delay: 0s;">💥</div>
    <div class="firework" style="top: 20%; right: 25%; animation-delay: 0.5s;">✨</div>
    <div class="firework" style="top: 30%; left: 30%; animation-delay: 1s;">🎆</div>
    <div class="firework" style="top: 35%; right: 35%; animation-delay: 1.5s;">💫</div>
    <div class="firework" style="bottom: 30%; left: 25%; animation-delay: 0.3s;">🎇</div>
    <div class="firework" style="bottom: 35%; right: 30%; animation-delay: 0.8s;">💥</div>
    <div class="firework" style="top: 50%; left: 15%; animation-delay: 2s;">✨</div>
    <div class="firework" style="top: 55%; right: 20%; animation-delay: 2.5s;">🎆</div>
    
    <!-- Sparkles -->
    <div class="sparkle" style="top: 12%; left: 40%; animation-delay: 0s;">⭐</div>
    <div class="sparkle" style="top: 18%; right: 45%; animation-delay: 0.4s;">✨</div>
    <div class="sparkle" style="top: 80%; left: 25%; animation-delay: 0.8s;">🌟</div>
    <div class="sparkle" style="top: 85%; right: 28%; animation-delay: 1.2s;">💫</div>
    <div class="sparkle" style="top: 45%; left: 8%; animation-delay: 1.6s;">⭐</div>
    <div class="sparkle" style="top: 50%; right: 10%; animation-delay: 2s;">✨</div>
</div>

<script>
    // Animation sequence
    setTimeout(() => {
        // Hide welcome screen
        document.getElementById('welcomeScreen').style.display = 'none';
        
        // Show peacock
        document.getElementById('peacockContainer').style.display = 'flex';
        
        // After 3 seconds, peacock exits and content shows
        setTimeout(() => {
            document.getElementById('peacock').classList.add('exit');
            
            setTimeout(() => {
                document.getElementById('peacockContainer').style.display = 'none';
                document.getElementById('birthdayContent').style.display = 'block';
            }, 2000);
        }, 3000);
    }, 3000);
</script>
""", unsafe_allow_html=True)

# Add Streamlit balloons and snow effects
st.balloons()
st.snow()
