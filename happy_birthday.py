import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="wide")

# Create the complete HTML with embedded CSS and animations
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body, html {
            width: 100%;
            height: 100%;
            overflow: hidden;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        }
        
        /* Animations */
        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-30px) rotate(5deg); }
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0) scale(1); }
            50% { transform: translateY(-40px) scale(1.05); }
        }
        
        @keyframes slideIn {
            from { transform: translateX(-100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
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
            50% { transform: scale(1.2); opacity: 1; }
            100% { transform: scale(2); opacity: 0; }
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
            z-index: 10000;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            animation: welcomeSequence 6s ease-in-out forwards;
        }
        
        @keyframes welcomeSequence {
            0% { opacity: 1; visibility: visible; }
            83% { opacity: 1; visibility: visible; }
            100% { opacity: 0; visibility: hidden; pointer-events: none; }
        }
        
        .welcome-banner {
            background: linear-gradient(45deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3);
            padding: 40px 80px;
            border-radius: 50px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.4);
            animation: bounce 2s ease-in-out infinite;
            margin-bottom: 50px;
        }
        
        .welcome-banner h1 {
            color: white;
            font-size: 5em;
            text-align: center;
            margin: 0;
            text-shadow: 4px 4px 8px rgba(0,0,0,0.4);
            font-weight: bold;
        }
        
        .welcome-pets {
            display: flex;
            gap: 120px;
            animation: slideIn 1.5s ease-out;
        }
        
        .pet {
            font-size: 10em;
            animation: bounce 1.5s ease-in-out infinite;
            filter: drop-shadow(0 10px 20px rgba(0,0,0,0.3));
        }
        
        .pet:nth-child(2) {
            animation-delay: 0.3s;
        }
        
        /* Peacock animation */
        .peacock-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            animation: peacockSequence 13s ease-in-out forwards;
        }
        
        @keyframes peacockSequence {
            0% { opacity: 0; visibility: hidden; pointer-events: none; }
            46% { opacity: 0; visibility: hidden; pointer-events: none; }
            50% { opacity: 1; visibility: visible; }
            92% { opacity: 1; visibility: visible; }
            100% { opacity: 0; visibility: hidden; pointer-events: none; }
        }
        
        .peacock {
            font-size: 20em;
            filter: drop-shadow(0 20px 40px rgba(0,0,0,0.5));
            animation: peacockFly 13s ease-out forwards;
        }
        
        @keyframes peacockFly {
            0% { transform: translateX(150%) scale(0.3) rotate(0deg); }
            46% { transform: translateX(150%) scale(0.3) rotate(0deg); }
            54% { transform: translateX(50%) scale(1.8) rotate(10deg); }
            69% { transform: translateX(50%) scale(1.5) rotate(0deg); }
            92% { transform: translateX(50%) scale(1.5) rotate(0deg); }
            100% { transform: translateX(-150%) scale(0.3) rotate(-20deg); }
        }
        
        /* Main content */
        .birthday-content {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            z-index: 9998;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(15px);
            padding: 60px 80px;
            border-radius: 40px;
            box-shadow: 0 25px 100px rgba(0,0,0,0.4);
            border: 2px solid rgba(255,255,255,0.3);
            animation: contentSequence 15s ease-in forwards;
        }
        
        @keyframes contentSequence {
            0% { opacity: 0; visibility: hidden; transform: translate(-50%, -50%) scale(0.5); }
            86% { opacity: 0; visibility: hidden; transform: translate(-50%, -50%) scale(0.5); }
            100% { opacity: 1; visibility: visible; transform: translate(-50%, -50%) scale(1); }
        }
        
        .birthday-content h1 {
            font-size: 4.5em;
            background: linear-gradient(45deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 30px;
            animation: bounce 3s ease-in-out infinite;
            font-weight: bold;
        }
        
        .birthday-content p {
            font-size: 1.6em;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            margin: 25px 0;
            line-height: 1.8;
            font-weight: 500;
        }
        
        /* Floating animals */
        .floating-animal {
            position: fixed;
            font-size: 4em;
            animation: float 4s ease-in-out infinite;
            z-index: 50;
            filter: drop-shadow(0 5px 10px rgba(0,0,0,0.3));
        }
        
        /* Effects */
        .snowflake, .confetti, .firework, .sparkle {
            position: fixed;
            font-size: 2em;
            z-index: 10;
        }
        
        .snowflake {
            animation: fall linear infinite;
        }
        
        .confetti {
            animation: fall linear infinite;
        }
        
        .firework {
            font-size: 4em;
            animation: firework 2s ease-out infinite;
        }
        
        .sparkle {
            font-size: 2.5em;
            animation: sparkle 2s ease-in-out infinite;
        }
    </style>
</head>
<body>
    <!-- Welcome Screen -->
    <div class="welcome-screen">
        <div class="welcome-banner">
            <h1>🎉 WELCOME! 🎉</h1>
        </div>
        <div class="welcome-pets">
            <div class="pet">🐱</div>
            <div class="pet">🐶</div>
        </div>
    </div>
    
    <!-- Peacock Animation -->
    <div class="peacock-container">
        <div class="peacock">🦚</div>
    </div>
    
    <!-- Main Birthday Content -->
    <div class="birthday-content">
        <h1>🎂🌹✨ Happy Birthday! ✨🌹🎂</h1>
        <p>🌟 May your birthday be as extraordinary and wonderful as you are! 🎉🌟</p>
        <p>💖 Wishing you a day filled with happiness, laughter and as many cupcakes as your heart desires! 🧁</p>
        <p>✨ May your Birthday be filled with the magic of love, joy, and all the things that make you happy! ✨</p>
    </div>
    
    <!-- Floating Animals -->
    <div class="floating-animal" style="top: 8%; left: 5%; animation-delay: 0s; animation-duration: 3s;">🐶</div>
    <div class="floating-animal" style="top: 12%; right: 8%; animation-delay: 0.5s; animation-duration: 3.5s;">🐱</div>
    <div class="floating-animal" style="top: 22%; left: 15%; animation-delay: 1s; animation-duration: 4s;">🐕</div>
    <div class="floating-animal" style="top: 28%; right: 20%; animation-delay: 1.5s; animation-duration: 3.2s;">🐈</div>
    <div class="floating-animal" style="top: 42%; left: 3%; animation-delay: 2s; animation-duration: 3.8s;">🐩</div>
    <div class="floating-animal" style="top: 48%; right: 5%; animation-delay: 2.5s; animation-duration: 4.2s;">🐈‍⬛</div>
    <div class="floating-animal" style="bottom: 22%; left: 10%; animation-delay: 0.3s; animation-duration: 3.3s;">🦮</div>
    <div class="floating-animal" style="bottom: 28%; right: 12%; animation-delay: 0.8s; animation-duration: 3.7s;">🐕‍🦺</div>
    <div class="floating-animal" style="bottom: 12%; left: 20%; animation-delay: 1.3s; animation-duration: 4.1s;">🐾</div>
    <div class="floating-animal" style="bottom: 18%; right: 18%; animation-delay: 1.8s; animation-duration: 3.4s;">🐾</div>
    <div class="floating-animal" style="top: 35%; left: 45%; animation-delay: 2.2s; animation-duration: 3.9s;">🐶</div>
    <div class="floating-animal" style="top: 65%; right: 30%; animation-delay: 2.7s; animation-duration: 3.6s;">🐱</div>
    <div class="floating-animal" style="top: 75%; left: 35%; animation-delay: 3s; animation-duration: 4.3s;">🐕</div>
    <div class="floating-animal" style="bottom: 45%; right: 40%; animation-delay: 0.6s; animation-duration: 3.5s;">🐈</div>
    
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
    
    <!-- Confetti -->
    <div class="confetti" style="left: 15%; animation-duration: 7s; animation-delay: 0s; color: #ff6b6b;">🎊</div>
    <div class="confetti" style="left: 25%; animation-duration: 8s; animation-delay: 1s; color: #feca57;">🎉</div>
    <div class="confetti" style="left: 35%; animation-duration: 6s; animation-delay: 2s; color: #48dbfb;">🎊</div>
    <div class="confetti" style="left: 45%; animation-duration: 9s; animation-delay: 0.5s; color: #ff9ff3;">🎉</div>
    <div class="confetti" style="left: 55%; animation-duration: 7.5s; animation-delay: 1.5s; color: #ff6b6b;">🎊</div>
    <div class="confetti" style="left: 65%; animation-duration: 8.5s; animation-delay: 2.5s; color: #feca57;">🎉</div>
    <div class="confetti" style="left: 75%; animation-duration: 6.5s; animation-delay: 0.8s; color: #48dbfb;">🎊</div>
    <div class="confetti" style="left: 85%; animation-duration: 9.5s; animation-delay: 1.8s; color: #ff9ff3;">🎉</div>
    
    <!-- Fireworks -->
    <div class="firework" style="top: 15%; left: 20%; animation-delay: 0s;">💥</div>
    <div class="firework" style="top: 20%; right: 25%; animation-delay: 0.6s;">✨</div>
    <div class="firework" style="top: 30%; left: 30%; animation-delay: 1.2s;">🎆</div>
    <div class="firework" style="top: 35%; right: 35%; animation-delay: 1.8s;">💫</div>
    <div class="firework" style="bottom: 30%; left: 25%; animation-delay: 0.4s;">🎇</div>
    <div class="firework" style="bottom: 35%; right: 30%; animation-delay: 1s;">💥</div>
    
    <!-- Sparkles -->
    <div class="sparkle" style="top: 12%; left: 40%; animation-delay: 0s;">⭐</div>
    <div class="sparkle" style="top: 18%; right: 45%; animation-delay: 0.5s;">✨</div>
    <div class="sparkle" style="top: 80%; left: 25%; animation-delay: 1s;">🌟</div>
    <div class="sparkle" style="top: 85%; right: 28%; animation-delay: 1.5s;">💫</div>
    <div class="sparkle" style="top: 45%; left: 8%; animation-delay: 2s;">⭐</div>
    <div class="sparkle" style="top: 50%; right: 10%; animation-delay: 2.5s;">✨</div>
</body>
</html>
"""

# Render the HTML using Streamlit components
components.html(html_code, height=800, scrolling=False)

# Add Streamlit effects
st.balloons()
st.snow()
