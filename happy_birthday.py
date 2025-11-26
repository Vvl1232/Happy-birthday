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
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body, html {
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      font-family: 'Arial', sans-serif;
      position: fixed;
      top: 0;
      left: 0;
    }

    body {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
      transition: background 1.2s cubic-bezier(.2,.9,.2,1);
    }

    /* Mobile responsive */
    @media (max-width: 768px) {
      .welcome-banner h1 {
          font-size: 2.5em !important;
      }
      .welcome-banner {
          padding: 25px 40px !important;
      }
      .pet {
          font-size: 6em !important;
      }
      .welcome-pets {
          gap: 60px !important;
      }
      .peacock {
          font-size: 12em !important;
      }
      .peacock-poem {
          font-size: 1.1em !important;
          padding: 12px 16px !important;
      }
      .krishna-image {
          width: 150px !important;
          height: 150px !important;
      }
      .countdown {
          font-size: 10em !important;
      }
      .birthday-content {
          padding: 25px 30px !important;
          width: 90% !important;
          max-width: 90% !important;
      }
      .birthday-content h1 {
          font-size: 2em !important;
      }
      .birthday-content p {
          font-size: 1em !important;
          margin: 10px 0 !important;
      }
      .floating-animal {
          font-size: 2.5em !important;
      }
      .snowflake, .confetti, .sparkle {
          font-size: 1.5em !important;
      }
      .firework {
          font-size: 2.5em !important;
      }
    }

    @media (max-width: 480px) {
      .welcome-banner h1 {
          font-size: 1.8em !important;
      }
      .welcome-banner {
          padding: 20px 30px !important;
      }
      .pet {
          font-size: 4em !important;
      }
      .peacock {
          font-size: 8em !important;
      }
      .peacock-poem {
          font-size: 0.95em !important;
          padding: 10px 12px !important;
      }
      .krishna-image {
          width: 120px !important;
          height: 120px !important;
      }
      .countdown {
          font-size: 8em !important;
      }
      .birthday-content {
          padding: 20px 25px !important;
      }
      .birthday-content h1 {
          font-size: 1.5em !important;
      }
      .birthday-content p {
          font-size: 0.85em !important;
          margin: 8px 0 !important;
      }
    }

    /* Animations (smoother easing and subtle transitions) */
    @keyframes float {
      0%, 100% { transform: translateY(0px) rotate(0deg); }
      50% { transform: translateY(-24px) rotate(3deg); }
    }

    @keyframes bounce {
      0%, 100% { transform: translateY(0) scale(1); }
      50% { transform: translateY(-28px) scale(1.03); }
    }

    @keyframes slideIn {
      from { transform: translateX(-110%); opacity: 0; }
      to { transform: translateX(0); opacity: 1; }
    }

    @keyframes sparkle {
      0%, 100% { opacity: 1; transform: scale(1) rotate(0deg); }
      50% { opacity: 0.4; transform: scale(1.35) rotate(160deg); }
    }

    @keyframes fall {
      0% { transform: translateY(-110vh) rotate(0deg); opacity: 1; }
      100% { transform: translateY(100vh) rotate(360deg); opacity: 0.45; }
    }

    @keyframes firework {
      0% { transform: scale(0); opacity: 1; }
      50% { transform: scale(1); opacity: 1; }
      100% { transform: scale(1.8); opacity: 0; }
    }

    @keyframes flutePlay {
      0%, 100% { transform: rotate(-5deg); }
      50% { transform: rotate(5deg); }
    }

    @keyframes glow {
      0%, 100% { filter: drop-shadow(0 0 18px rgba(255, 215, 0, 0.7)); }
      50% { filter: drop-shadow(0 0 36px rgba(255, 215, 0, 1)); }
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
      animation: welcomeSequence 3s cubic-bezier(.2,.9,.2,1) forwards; /* reduced from 6s -> 3s */
      transition: opacity .8s cubic-bezier(.2,.9,.2,1), visibility .8s;
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
      box-shadow: 0 20px 60px rgba(0,0,0,0.28);
      animation: bounce 2.6s cubic-bezier(.25,.9,.35,1) infinite;
      margin-bottom: 50px;
      transition: transform .9s cubic-bezier(.2,.9,.2,1);
    }

    .welcome-banner h1 {
      color: white;
      font-size: 5em;
      text-align: center;
      margin: 0;
      text-shadow: 4px 4px 10px rgba(0,0,0,0.35);
      font-weight: bold;
    }

    .welcome-pets {
      display: flex;
      gap: 120px;
      animation: slideIn 1.5s cubic-bezier(.2,.9,.2,1) ease-out;
    }

    .pet {
      font-size: 10em;
      animation: bounce 1.6s cubic-bezier(.25,.9,.35,1) infinite;
      filter: drop-shadow(0 10px 20px rgba(0,0,0,0.28));
    }

    .pet:nth-child(2) {
      animation-delay: 0.3s;
    }

    /* Peacock animation
       Reduced duration by 30%: 39s -> 27s (approx)
       Smooth cubic-bezier easing, fade/transform transitions for gentle feel.
    */
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
      animation: peacockSequence 27s cubic-bezier(.2,.9,.2,1) forwards; /* reduced from 39s -> 27s */
      pointer-events: none;
      transition: opacity 1.0s cubic-bezier(.2,.9,.2,1), transform 1.0s cubic-bezier(.2,.9,.2,1);
    }

    @keyframes peacockSequence {
      0% { opacity: 0; visibility: hidden; pointer-events: none; transform: translateX(0) scale(1); }
      25% { opacity: 0; visibility: hidden; pointer-events: none; transform: translateX(0) scale(1); }
      26% { opacity: 1; visibility: visible; }
      86% { opacity: 1; visibility: visible; }
      100% { opacity: 0; visibility: hidden; pointer-events: none; transform: translateY(-6px) scale(0.98); }
    }

    .peacock {
      font-size: 20em;
      filter: drop-shadow(0 20px 40px rgba(0,0,0,0.45));
      animation: peacockFlyStop 27s cubic-bezier(.2,.9,.2,1) forwards; /* match 27s */
      margin-right: 18px;
      transition: transform 1.0s cubic-bezier(.2,.9,.2,1), opacity 0.9s cubic-bezier(.2,.9,.2,1);
    }

    @keyframes peacockFlyStop {
      0% { transform: translateX(0) scale(1.5); opacity: 0; }
      25% { transform: translateX(0) scale(1.5); opacity: 0; }
      26% { transform: translateX(-150%) scale(1.4); opacity: 1; }
      60% { transform: translateX(-8%) scale(1.35) rotate(6deg); opacity: 1; }
      86% { transform: translateX(-8%) scale(1.25) rotate(0deg); opacity: 1; }
      100% { transform: translateX(-8%) scale(1.2); opacity: 0; }
    }

    /* New: Peacock Poem card that enters with the same flow as the peacock.
       emojis inline, extended visible time reduced to 27s, smoother transitions and higher z-index.
    */
    .peacock-poem {
      max-width: 560px;
      min-width: 320px;
      border-radius: 18px;
      padding: 18px 24px;
      backdrop-filter: blur(10px);
      background: linear-gradient(135deg, rgba(255,255,255,0.10), rgba(255,255,255,0.04));
      border: 1px solid rgba(255,255,255,0.20);
      box-shadow: 0 14px 50px rgba(0,0,0,0.28);
      color: #fff;
      text-align: left;
      font-size: 1.12em;
      line-height: 1.55;
      z-index: 10050; /* raised so nothing overlaps */
      animation: peacockSequence 27s cubic-bezier(.2,.9,.2,1) forwards, poemFloat 3.6s ease-in-out infinite; /* poem float slightly faster */
      animation-fill-mode: forwards;
      transform-origin: center;
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.9s cubic-bezier(.2,.9,.2,1), transform 0.9s cubic-bezier(.2,.9,.2,1);
      will-change: transform, opacity;
      border-left: 4px solid rgba(255,255,255,0.12);
    }

    @keyframes poemFloat {
      0% { transform: translateY(0) rotate(0deg); }
      50% { transform: translateY(-6px) rotate(0.6deg); }
      100% { transform: translateY(0) rotate(0deg); }
    }

    /* Make sure poem becomes fully opaque when peacockSequence shows it */
    .peacock-container .peacock-poem {
      opacity: 1;
    }

    .peacock-poem p {
      margin: 8px 0;
      color: #ffffff;
      text-shadow: 1px 1px 6px rgba(0,0,0,0.35);
      font-weight: 500;
    }

    /* Countdown Timer */
    .countdown {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      font-size: 15em;
      font-weight: bold;
      color: #ff6b6b;
      text-shadow: 0 0 30px rgba(255, 107, 107, 0.8), 0 0 60px rgba(255, 107, 107, 0.6);
      z-index: 10001;
      transition: opacity 0.6s cubic-bezier(.2,.9,.2,1), transform 0.6s cubic-bezier(.2,.9,.2,1);
    }

    .countdown.show {
      animation: countdownNumber 1s ease-in-out;
    }

    @keyframes countdownNumber {
      0% { opacity: 0; transform: translate(-50%, -50%) scale(0.7); }
      15% { opacity: 1; transform: translate(-50%, -50%) scale(1.06); }
      25% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
      85% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
      100% { opacity: 0; transform: translate(-50%, -50%) scale(0.7); }
    }

    /* Main content
       Delayed so peacock+poem finish first — adjusted so main content appears after the 27s peacock/poem:
       was 42s, now 30s to keep a short buffer.
       Smooth fade/scale in to feel like "more to come"
    */
    .birthday-content {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      text-align: center;
      z-index: 10000;
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(15px);
      padding: 40px 50px;
      border-radius: 30px;
      box-shadow: 0 25px 100px rgba(0,0,0,0.4);
      border: 2px solid rgba(255,255,255,0.3);
      /* start later so content doesn't overlap peacock/poem */
      animation: contentSequence 30s cubic-bezier(.2,.9,.2,1) forwards; /* reduced from 42s -> 30s */
      max-width: 85%;
      max-height: 85vh;
      overflow-y: auto;
      opacity: 0;
      transform-origin: center;
      transition: opacity 1.1s cubic-bezier(.2,.9,.2,1), transform 1.1s cubic-bezier(.2,.9,.2,1);
    }

    @keyframes contentSequence {
      0% { opacity: 0; visibility: hidden; transform: translate(-50%, -50%) scale(0.5); }
      99% { opacity: 0; visibility: hidden; transform: translate(-50%, -50%) scale(0.5); }
      100% { opacity: 1; visibility: visible; transform: translate(-50%, -50%) scale(1); }
    }

    /* Celebration burst effects */
    .celebration-burst {
      position: fixed;
      width: 100vw;
      height: 100vh;
      top: 0;
      left: 0;
      z-index: 9999;
      pointer-events: none;
      animation: burstSequence 17s linear forwards;
    }

    @keyframes burstSequence {
      0% { opacity: 0; }
      99% { opacity: 0; }
      100% { opacity: 1; }
    }

    .burst-confetti, .burst-balloon, .burst-snow, .burst-firework {
      position: absolute;
      animation: burstEffect 1s ease-out;
    }

    @keyframes burstEffect {
      0% { transform: scale(0) translateY(0); opacity: 0; }
      50% { transform: scale(1.5) translateY(-20px); opacity: 1; }
      100% { transform: scale(1) translateY(0); opacity: 1; }
    }

    .birthday-content h1 {
      font-size: 3em;
      background: linear-gradient(45deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: 20px;
      animation: bounce 3s cubic-bezier(.25,.9,.35,1) infinite;
      font-weight: bold;
    }

    .birthday-content p {
      font-size: 1.3em;
      color: white;
      text-shadow: 2px 2px 6px rgba(0,0,0,0.45);
      margin: 15px 0;
      line-height: 1.6;
      font-weight: 500;
    }

    /* Floating animals */
    .floating-animal {
      position: fixed;
      font-size: 4em;
      animation: float 4.4s cubic-bezier(.2,.9,.2,1) infinite;
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
      animation: firework 2.2s cubic-bezier(.2,.9,.2,1) infinite;
    }

    .sparkle {
      font-size: 2.5em;
      animation: sparkle 2.2s cubic-bezier(.2,.9,.2,1) infinite;
    }

    @media (prefers-reduced-motion: reduce) {
      .welcome-banner, .pet, .peacock, .countdown, .floating-animal, .celebration-burst { animation: none !important; transition: none !important; }
    }
  </style>
</head>
<body>
  <!-- Welcome Screen -->
  <div class="welcome-screen">
      <div class="welcome-banner">
          <h1>✨ SOMETHING MAGICAL AWAITS! ✨</h1>
      </div>
      <div class="welcome-pets">
          <div class="pet">🐱</div>
          <div class="pet">🐶</div>
      </div>
  </div>

  <!-- Peacock Animation + Poem (poem enters with the peacock, now 27s visible) -->
  <div class="peacock-container" aria-hidden="true">
      <div class="peacock" role="img" aria-label="Peacock">🦚</div>

      <!-- Poem card beside the peacock — emojis inline inside poem, heading removed -->
      <div class="peacock-poem" aria-hidden="true">
        <p>☀️ On your special day, let positivity shine bright,</p>
        <p>🍰 With cheese cakes dancing in soft golden light.</p>
        <p>☕ A swirl of warm coffee makes everything sweet,</p>
        <p>🐶 And tiny animals bring joy with their little heartbeat.</p>
        <p>🎶 Songs float around you, inviting your spirit to sing along,</p>
        <p>💃 And happy little dances turn your moments into a cheerful song.</p>
        <p>😇 Wrapped in gentle kindness, your dreams glow true—</p>
        <p>🔮 A day full of magic deserves someone like you.</p>
      </div>
  </div>

  <!-- Countdown Timer -->
  <div class="countdown" id="countdown"></div>

  <!-- Celebration Burst Effects -->
  <div class="celebration-burst">
      <!-- Decorative burst placeholders (removed emoji glyphs so they don't float over poem) -->
      <div class="burst-confetti" style="top: 20%; left: 15%; font-size: 3em; animation-delay: 0s;"></div>
      <div class="burst-confetti" style="top: 25%; right: 20%; font-size: 3em; animation-delay: 0.1s;"></div>
      <div class="burst-confetti" style="top: 30%; left: 30%; font-size: 3em; animation-delay: 0.2s;"></div>
      <div class="burst-confetti" style="top: 35%; right: 35%; font-size: 3em; animation-delay: 0.3s;"></div>
      <div class="burst-confetti" style="bottom: 30%; left: 25%; font-size: 3em; animation-delay: 0.4s;"></div>
      <div class="burst-confetti" style="bottom: 35%; right: 30%; font-size: 3em; animation-delay: 0.5s;"></div>

      <!-- Balloons burst placeholders -->
      <div class="burst-balloon" style="top: 40%; left: 20%; font-size: 3em; animation-delay: 0.2s;"></div>
      <div class="burst-balloon" style="top: 45%; right: 25%; font-size: 3em; animation-delay: 0.3s;"></div>
      <div class="burst-balloon" style="bottom: 40%; left: 30%; font-size: 3em; animation-delay: 0.4s;"></div>
      <div class="burst-balloon" style="bottom: 45%; right: 28%; font-size: 3em; animation-delay: 0.5s;"></div>

      <!-- Fireworks burst placeholders -->
      <div class="burst-firework" style="top: 15%; left: 40%; font-size: 4em; animation-delay: 0.1s;"></div>
      <div class="burst-firework" style="top: 20%; right: 40%; font-size: 4em; animation-delay: 0.3s;"></div>
      <div class="burst-firework" style="bottom: 20%; left: 35%; font-size: 4em; animation-delay: 0.5s;"></div>
      <div class="burst-firework" style="bottom: 25%; right: 38%; font-size: 4em; animation-delay: 0.6s;"></div>

      <!-- Snowflakes burst placeholders -->
      <div class="burst-snow" style="top: 10%; left: 50%; font-size: 2.5em; animation-delay: 0.2s;"></div>
      <div class="burst-snow" style="top: 18%; right: 50%; font-size: 2.5em; animation-delay: 0.4s;"></div>
      <div class="burst-snow" style="top: 28%; left: 45%; font-size: 2.5em; animation-delay: 0.6s;"></div>
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
  <div class="snowflake" style="left: 10%; animation-duration: 8s; animation-delay: 0s;">❄</div>
  <div class="snowflake" style="left: 20%; animation-duration: 10s; animation-delay: 1s;">❄</div>
  <div class="snowflake" style="left: 30%; animation-duration: 9s; animation-delay: 2s;">❄</div>
  <div class="snowflake" style="left: 40%; animation-duration: 11s; animation-delay: 0.5s;">❄</div>
  <div class="snowflake" style="left: 50%; animation-duration: 8.5s; animation-delay: 1.5s;">❄</div>
  <div class="snowflake" style="left: 60%; animation-duration: 10.5s; animation-delay: 2.5s;">❄</div>
  <div class="snowflake" style="left: 70%; animation-duration: 9.5s; animation-delay: 0.8s;">❄</div>
  <div class="snowflake" style="left: 80%; animation-duration: 11.5s; animation-delay: 1.8s;">❄</div>
  <div class="snowflake" style="left: 90%; animation-duration: 10s; animation-delay: 3s;">❄</div>

  <!-- Confetti -->
  <div class="confetti" style="left: 15%; animation-duration: 7s; animation-delay: 0s; color: #ff6b6b;"></div>
  <div class="confetti" style="left: 25%; animation-duration: 8s; animation-delay: 1s; color: #feca57;"></div>
  <div class="confetti" style="left: 35%; animation-duration: 6s; animation-delay: 2s; color: #48dbfb;"></div>
  <div class="confetti" style="left: 45%; animation-duration: 9s; animation-delay: 0.5s; color: #ff9ff3;"></div>
  <div class="confetti" style="left: 55%; animation-duration: 7.5s; animation-delay: 1.5s; color: #ff6b6b;"></div>
  <div class="confetti" style="left: 65%; animation-duration: 8.5s; animation-delay: 2.5s; color: #feca57;"></div>
  <div class="confetti" style="left: 75%; animation-duration: 6.5s; animation-delay: 0.8s; color: #48dbfb;"></div>
  <div class="confetti" style="left: 85%; animation-duration: 9.5s; animation-delay: 1.8s; color: #ff9ff3;"></div>

  <!-- Fireworks -->
  <div class="firework" style="top: 15%; left: 20%; animation-delay: 0s;"></div>
  <div class="firework" style="top: 20%; right: 25%; animation-delay: 0.6s;"></div>
  <div class="firework" style="top: 30%; left: 30%; animation-delay: 1.2s;"></div>
  <div class="firework" style="top: 35%; right: 35%; animation-delay: 1.8s;"></div>
  <div class="firework" style="bottom: 30%; left: 25%; animation-delay: 0.4s;"></div>
  <div class="firework" style="bottom: 35%; right: 30%; animation-delay: 1s;"></div>

  <!-- Sparkles -->
  <div class="sparkle" style="top: 12%; left: 40%; animation-delay: 0s;"></div>
  <div class="sparkle" style="top: 18%; right: 45%; animation-delay: 0.5s;"></div>
  <div class="sparkle" style="top: 80%; left: 25%; animation-delay: 1s;"></div>
  <div class="sparkle" style="top: 85%; right: 28%; animation-delay: 1.5s;"></div>
  <div class="sparkle" style="top: 45%; left: 8%; animation-delay: 2s;"></div>
  <div class="sparkle" style="top: 50%; right: 10%; animation-delay: 2.5s;"></div>


<!-- Flute Happy Birthday: WebAudio script (autoplay attempt; falls back to first user gesture) -->
<script>
(function(){
  // Happy Birthday melody notes and durations
  const melodyNotes = [
    "G4","G4","A4","G4","C5","B4",
    "G4","G4","A4","G4","D5","C5",
    "G4","G4","G5","E5","C5","B4","A4",
    "F5","F5","E5","C5","D5","C5"
  ];
  const melodyDurations = [
    0.5,0.5,1,1,1,2,
    0.5,0.5,1,1,1,2,
    0.5,0.5,1,1,1,1,1,
    0.5,0.5,1,1,2,2
  ];
  const tempo = 88; // BPM
  const beatSec = 60 / tempo;

  let audioCtx = null;
  let masterGain = null;
  let isPlaying = false;
  let loopTimer = null;

  // Convert note like "C#4" to frequency, A4 = 440Hz
  function noteToFreq(note){
    const re = /^([A-Ga-g])([#b]?)(\d+)$/;
    const m = re.exec(note);
    if(!m) return 440;
    const name = m[1].toUpperCase();
    const acc = m[2];
    const octave = parseInt(m[3],10);
    const semitoneMap = { 'C': -9, 'D': -7, 'E': -5, 'F': -4, 'G': -2, 'A': 0, 'B': 2 };
    let semis = semitoneMap[name];
    if(acc === '#') semis += 1;
    if(acc === 'b') semis -= 1;
    semis += (octave - 4) * 12;
    return 440 * Math.pow(2, semis / 12);
  }

  function ensureAudio(){
    if(audioCtx) return;
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    masterGain = audioCtx.createGain();
    masterGain.gain.value = 0.45; // background volume (adjust 0-1)
    masterGain.connect(audioCtx.destination);
  }

  // Play a single flute-like note at given time
  function playFlute(time, freq, duration){
    const osc = audioCtx.createOscillator();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(freq, time);

    // vibrato
    const vib = audioCtx.createOscillator();
    vib.type = 'sine';
    vib.frequency.value = 5.0;
    const vibGain = audioCtx.createGain();
    vibGain.gain.value = freq * 0.0025;
    vib.connect(vibGain);
    vibGain.connect(osc.frequency);

    // breath noise
    const buffer = audioCtx.createBuffer(1, Math.floor(audioCtx.sampleRate * 0.3), audioCtx.sampleRate);
    const data = buffer.getChannelData(0);
    for(let i=0;i<data.length;i++){
      data[i] = (Math.random()*2 - 1) * Math.exp(-i / (audioCtx.sampleRate * 0.08));
    }
    const noise = audioCtx.createBufferSource();
    noise.buffer = buffer;

    const noiseGain = audioCtx.createGain();
    noiseGain.gain.value = 0.0;

    const bp = audioCtx.createBiquadFilter();
    bp.type = 'bandpass';
    bp.frequency.value = freq * 2.2;
    bp.Q.value = 8;

    const env = audioCtx.createGain();
    env.gain.setValueAtTime(0.0001, time);

    osc.connect(env);
    noise.connect(noiseGain);
    noiseGain.connect(bp);
    bp.connect(env);
    env.connect(masterGain);

    const attack = Math.min(0.12, duration * 0.35);
    const release = Math.min(0.28, duration * 0.45);
    const sustain = 0.9;

    // small initial level then ramp to sustain
    env.gain.exponentialRampToValueAtTime(0.1 * sustain, time + attack);
    env.gain.setValueAtTime(0.1 * sustain, time + attack);
    env.gain.linearRampToValueAtTime(0.0001, time + duration + release);

    noiseGain.gain.linearRampToValueAtTime(0.035, time + attack * 0.9);
    noiseGain.gain.linearRampToValueAtTime(0.0, time + duration + release * 0.6);

    vib.start(time);
    osc.start(time);
    noise.start(time);

    const stopTime = time + duration + release + 0.05;
    osc.stop(stopTime);
    noise.stop(stopTime);
    vib.stop(stopTime + 0.02);
  }

  function scheduleMelody(startTime){
    let cursor = startTime;
    for(let i=0;i<melodyNotes.length;i++){
      const note = melodyNotes[i];
      const durBeats = melodyDurations[i] || 1;
      const durSec = durBeats * beatSec;
      const freq = noteToFreq(note);
      playFlute(cursor, freq, durSec * 0.95);
      cursor += durSec;
    }
    return cursor - startTime;
  }

  function startLoopingMelody(){
    if(isPlaying) return;
    ensureAudio();
    // Attempt to resume (may require user gesture in some browsers)
    Promise.resolve()
      .then(()=> audioCtx.resume())
      .catch(()=>{})
      .finally(()=>{
        // schedule first run if running
        if(audioCtx.state === 'running'){
          const now = audioCtx.currentTime + 0.08;
          const total = scheduleMelody(now);
          // schedule periodic scheduling slightly before the melody ends
          loopTimer = setInterval(()=>{
            const s = audioCtx.currentTime + 0.06;
            scheduleMelody(s);
          }, Math.max(100, (total * 1000) - 40));
          isPlaying = true;
        } else {
          // attempt again later when user interacts
        }
      });
  }

  function stopLoopingMelody(){
    if(loopTimer){ clearInterval(loopTimer); loopTimer = null; }
    isPlaying = false;
    if(masterGain && audioCtx){
      const t = audioCtx.currentTime;
      masterGain.gain.cancelScheduledValues(t);
      masterGain.gain.setValueAtTime(masterGain.gain.value, t);
      masterGain.gain.exponentialRampToValueAtTime(0.0001, t + 0.8);
      setTimeout(()=> { if(masterGain) masterGain.gain.value = 0.0; }, 900);
    }
  }

  // Attempt autoplay on load and ensure loop continues
  window.addEventListener('load', () => {
    try {
      ensureAudio();
      startLoopingMelody();
    } catch (e) {
      // ignore; gesture fallback will handle it
    }
  });

  // Fallback: resume on first user gesture if autoplay was blocked.
  function gestureStart(){
    try {
      ensureAudio();
      audioCtx.resume().then(()=>{
        startLoopingMelody();
      }).catch(()=>{});
    } catch(e){}
    window.removeEventListener('pointerdown', gestureStart);
    window.removeEventListener('keydown', gestureStart);
    window.removeEventListener('touchstart', gestureStart);
  }

  window.addEventListener('pointerdown', gestureStart, {passive:true});
  window.addEventListener('keydown', gestureStart, {passive:true});
  window.addEventListener('touchstart', gestureStart, {passive:true});

  // Keep audio tidy: stop when page hidden, restart when visible again
  document.addEventListener('visibilitychange', () => {
    if(document.hidden){
      stopLoopingMelody();
    } else {
      startLoopingMelody();
    }
  });

})();
</script>
</body>
</html>
"""

# Hide Streamlit chrome so the page is fullscreen and immersive
st.markdown("""
<style>
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  header {visibility: hidden;}
  .stApp > header {visibility: hidden;}
  [data-testid="stHeader"] {display: none;}
  [data-testid="stToolbar"] {display: none;}
  .stDeployButton {display: none;}
  .block-container { padding: 0 !important; max-width: 100% !important; }
  iframe { border: none !important; display: block; position: fixed; top: 0; left: 0; width: 100vw !important; height: 100vh !important; }
</style>
""", unsafe_allow_html=True)

# Render full-screen HTML
components.html(html_code, height=1000, scrolling=False)

# Optional visual effects from Streamlit (keeps fun)
st.balloons()
st.snow()
