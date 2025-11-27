import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="wide")

html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Happy Birthday!</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body { width:100vw; height:100vh; overflow:hidden; font-family: 'Arial', sans-serif; position:fixed; top:0; left:0; }

    /* Pink -> Blurry Blue bottom */
    body {
      background: linear-gradient(
        to bottom,
        #ffb6d9 0%,
        #f48ab3 45%,
        rgba(135,206,250,0.55) 90%,
        rgba(135,206,250,0.4) 100%
      );
      transition: background 1.2s;
    }

    /* Floating Celebration & Peacock Emojis */
    .floating-emojis {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      display: none; /* invisible in welcome */
      grid-template-columns: repeat(5, 1fr);
      grid-template-rows: repeat(3, 1fr);
      align-items: center;
      justify-items: center;
      pointer-events: none;
      opacity: 0;
      z-index: 15;
      animation: emojiFadeIn 6s ease-in forwards;
    }
    .floating-emojis span {
      font-size: 3.5rem;
      animation: slowBounce 4.5s ease-in-out infinite;
      filter: drop-shadow(0 6px 12px rgba(0,0,0,0.25));
    }

    @keyframes emojiFadeIn {
      0% { opacity: 0; }
      100% { opacity: 0.45; }
    }
    @keyframes slowBounce {
      0%,100% { transform: translateY(0); }
      50% { transform: translateY(-14px); }
    }

    /* Welcome */
    .welcome-screen {
      position: fixed; top:0; left:0; width:100vw; height:100vh;
      display:flex; flex-direction:column; align-items:center; justify-content:center;
      z-index:10000;
      background: transparent;
      animation: welcomeSequence 5s forwards;
    }
    @keyframes welcomeSequence {
      0%, 75% { opacity:1; }
      100% { opacity:0; visibility:hidden; pointer-events:none; }
    }

    .welcome-banner {
      background: linear-gradient(45deg,#ff6b6b,#feca57,#48dbfb,#ff9ff3);
      padding: 30px 60px; border-radius: 48px;
      animation: bounce 2s infinite;
      box-shadow:0 18px 50px rgba(0,0,0,0.35);
    }
    .welcome-banner h1 { color:white; font-size:3rem; text-shadow:3px 3px 10px black; font-weight:800; }

    .welcome-pets { display:flex; gap:80px; }
    .pet { font-size:5rem; animation:bounce 1.6s infinite; filter:drop-shadow(0 10px 20px rgba(0,0,0,0.28)); }
    @keyframes bounce { 50%{transform:translateY(-18px);} }

    /* Poem */
    .poem-container {
      position: fixed; top: 50%; left: 50%; transform: translate(-50%,-50%);
      z-index: 10050; width: 90vw; max-width: 700px;
      animation: poemSequence 35s forwards;
      visibility:hidden;
    }
    @keyframes poemSequence {
      0%,14% { visibility:hidden; opacity:0; }
      15% { visibility:visible; opacity:1; }
      98% { opacity:1; }
      100% { opacity:0; }
    }
    .poem-card {
      background: rgba(255,255,255,0.12); padding:22px; border-radius: 18px;
      box-shadow:0 14px 50px rgba(0,0,0,0.25); backdrop-filter: blur(10px);
      color:white; font-size:1.12rem;
    }

    /* Main Birthday Content */
    .birthday-content {
      position: fixed; top:50%; left:50%; transform:translate(-50%,-50%);
      background: rgba(255,255,255,0.14); backdrop-filter: blur(20px);
      padding: 38px 48px; border-radius: 26px;
      animation: contentSequence 40s forwards;
      text-align:center; opacity:0;
      z-index:10000;
    }
    @keyframes contentSequence {
      0%,97% { opacity:0; visibility:hidden; }
      100% { opacity:1; visibility:visible; }
    }
    .birthday-content h1 {
      font-size:2.6rem; font-weight:900; color:#fff;
      text-shadow:0 0 10px black, 0 0 25px black;
      margin-bottom:12px;
    }
    .birthday-content p {
      color:white; text-shadow:1px 1px 4px black; margin:10px 0;
    }
  </style>
</head>
<body>

<!-- Background Floating Emojis (activated after welcome) -->
<div class="floating-emojis" id="emojiBG">
  <span>🎉</span><span>🦚</span><span>🎊</span><span>🦚</span><span>🎉</span>
  <span>🦚</span><span>🎊</span><span>🎉</span><span>🦚</span><span>🎊</span>
  <span>🎉</span><span>🦚</span><span>🎊</span><span>🦚</span><span>🎉</span>
</div>

<script>
setTimeout(()=>{document.getElementById("emojiBG").style.display="grid";}, 5000);
</script>

<!-- Welcome -->
<div class="welcome-screen">
  <div class="welcome-banner">
    <h1>✨ SOMETHING MAGICAL AWAITS! ✨</h1>
  </div>
  <div class="welcome-pets">
    <div class="pet">🐱</div>
    <div class="pet">🐶</div>
  </div>
</div>

<!-- POEM -->
<div class="poem-container">
  <div class="poem-card">
    <p>On your special day, let positivity shine ☀️ bright,</p>
    <p>With cheese cakes 🍰 dancing in golden light.</p>
    <p>A swirl of warm coffee ☕ makes everything sweet,</p>
    <p>And tiny animals 🐶 bring joy with each heartbeat.</p>
    <p>🎶 Songs float around, inviting you to sing along,</p>
    <p>Happy dances 💃 turning moments into a cheerful song.</p>
    <p>Kindness 😇 warms your dreams through and through—</p>
    <p>🔮 Magic and joy belong to someone like you.</p>
  </div>
</div>

<!-- MAIN -->
<div class="birthday-content">
  <h1>🎂🌹✨ Happy Birthday! ✨🌹🎂</h1>
  <p>🌟 May your day be as extraordinary as you are! 🎉🌟</p>
  <p>💖 Wishing you happiness, laughter & cupcakes! 🧁</p>
  <p>✨ May your life always be filled with magic! ✨</p>
</div>

</body>
</html>
"""

components.html(html_code, height=1000, scrolling=False)
