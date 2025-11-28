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

    body {
      background: linear-gradient(135deg, #b3e5fc 0%, #81d4fa 50%, #4fc3f7 100%);
      transition: background 1.2s cubic-bezier(.2,.9,.2,1);
    }

    /* -- Responsive: poem-first, mobile-friendly -- */
    .welcome-screen {
      position: fixed; top:0; left:0; width:100vw; height:100vh;
      display:flex; flex-direction:column; align-items:center; justify-content:center; z-index:10000;
      background: linear-gradient(135deg, #b3e5fc 0%, #81d4fa 50%, #4fc3f7 100%);
      animation: welcomeSequence 5s cubic-bezier(.2,.9,.2,1) forwards;
    }

    @keyframes welcomeSequence {
      0% { opacity:1; visibility:visible; }
      75% { opacity:1; visibility:visible; }
      100% { opacity:0; visibility:hidden; pointer-events:none; }
    }

    .welcome-banner {
      background: linear-gradient(45deg,#ff6b6b,#feca57,#48dbfb,#ff9ff3);
      padding: 30px 60px; border-radius: 48px; box-shadow: 0 18px 50px rgba(0,0,0,0.28);
      animation: bounce 2.6s cubic-bezier(.25,.9,.35,1) infinite;
      margin-bottom: 34px;
    }
    .welcome-banner h1 { color:white; font-size:3.2rem; text-align:center; text-shadow:4px 4px 10px rgba(0,0,0,0.35); font-weight:800; }

    .welcome-pets { display:flex; gap:80px; animation: slideIn 1.2s cubic-bezier(.2,.9,.2,1) ease-out; }
    .pet { font-size:6rem; animation:bounce 1.6s cubic-bezier(.25,.9,.35,1) infinite; filter:drop-shadow(0 10px 20px rgba(0,0,0,0.28)); }

    @keyframes float { 0%,100%{transform:translateY(0)}50%{transform:translateY(-16px)} }
    @keyframes bounce { 0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(-22px) scale(1.02)} }
    @keyframes slideIn { from{transform:translateX(-110%);opacity:0} to{transform:translateX(0);opacity:1} }

    /* POEM card */
    .poem-container {
      position: fixed; top: 50%; left: 50%; transform: translate(-50%,-50%);
      z-index: 10050; pointer-events: none;
      display: flex; align-items: center; justify-content: center;
      width: 92vw; max-width: 720px;
      animation: poemSequence 35s cubic-bezier(.2,.9,.2,1) forwards;
    }

    @keyframes poemSequence {
      0% { opacity: 0; }
      14% { opacity: 0; }
      15% { opacity: 1; }
      98% { opacity: 1; }
      100% { opacity: 0; }
    }

    .poem-card {
      width: 100%;
      padding: 20px 28px;
      border-radius: 16px;
      background: rgba(255,255,255,0.14);
      backdrop-filter: blur(14px);
      border: 1.6px solid rgba(255,255,255,0.24);
      box-shadow: 0 14px 60px rgba(0,0,0,0.28);
      color: #fff;
      text-align: left;
      font-weight: 500;
      line-height: 1.55;
      pointer-events: none;
      transform-origin: center;
      transition: transform .9s cubic-bezier(.2,.9,.2,1), opacity .9s ease;
    }

    .poem-card p { margin: 8px 0; font-size: 1.12rem; text-shadow: 1px 1px 6px rgba(0,0,0,0.35); }

    /* Confetti for poem transition - BEHIND content */
    .confetti-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 10045;
      animation: confettiTiming 35s linear forwards;
      opacity: 0;
      filter: blur(2px);
    }

    @keyframes confettiTiming {
      0% { opacity: 0; }
      14% { opacity: 0; }
      15% { opacity: 1; }
      98% { opacity: 1; }
      100% { opacity: 0; }
    }

    .confetti {
      position: absolute;
      width: 12px;
      height: 12px;
      background: #f0f;
      opacity: 0.25;
      animation: confettiFall 4s linear infinite;
    }

    @keyframes confettiFall {
      to {
        transform: translateY(120vh) rotate(360deg);
      }
    }

    /* Color flakes for birthday content transition - BEHIND content */
    .flakes-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 9995;
      animation: flakesTiming 38s linear forwards;
      opacity: 0;
      filter: blur(2px);
    }

    @keyframes flakesTiming {
      0% { opacity: 0; }
      96% { opacity: 0; }
      97% { opacity: 1; }
      100% { opacity: 1; }
    }

    .flake {
      position: absolute;
      width: 10px;
      height: 10px;
      background: #ff0;
      border-radius: 50%;
      opacity: 0.3;
      animation: flakeFall 5s linear infinite;
    }

    @keyframes flakeFall {
      to {
        transform: translateY(120vh) rotate(180deg);
        opacity: 0.1;
      }
    }

    @media (max-width: 768px) {
      .welcome-banner h1 { font-size: 2.2rem; padding: 14px 24px; }
      .pet { font-size: 4.2rem; }
      .poem-card { padding: 16px 18px; border-radius: 14px; }
      .poem-card p { font-size: 1rem; }
    }

    @media (max-width: 420px) {
      .poem-card { padding: 12px 14px; }
      .poem-card p { font-size: 0.95rem; line-height: 1.45; }
      .welcome-banner h1 { font-size: 1.6rem; padding: 10px 18px; }
      .pet { font-size: 3.4rem; }
    }

    .countdown { position: fixed; top:50%; left:50%; transform:translate(-50%,-50%); font-size:12rem; font-weight:bold; color:#ff6b6b; text-shadow:0 0 30px rgba(255,107,107,0.8); z-index:10001; transition:opacity .6s, transform .6s; }

    .birthday-content {
      position: fixed; top:50%; left:50%; transform:translate(-50%,-50%);
      z-index:10000; text-align:center;
      background: rgba(255,255,255,0.14); backdrop-filter: blur(14px);
      padding: 36px 44px; border-radius: 26px; border:1.6px solid rgba(255,255,255,0.24);
      box-shadow: 0 22px 90px rgba(0,0,0,0.36);
      animation: contentSequence 38s cubic-bezier(.2,.9,.2,1) forwards;
      opacity:0;
      max-width: 90%;
    }

    @keyframes contentSequence {
      0% { opacity:0; visibility:hidden; }
      97% { opacity:0; visibility:hidden; }
      100% { opacity:1; visibility:visible; }
    }

    .birthday-content h1 {
      font-size: 2.6rem;
      margin-bottom: 14px;
      font-weight: 900;
      color: #ffffff;
      text-shadow:
        0 0 10px rgba(0, 0, 0, 0.55),
        0 0 20px rgba(0, 0, 0, 0.40),
        0 4px 14px rgba(0, 0, 0, 0.55);
    }

    .birthday-content p {
      color:#fff;
      font-size:1rem;
      margin:10px 0;
      text-shadow:1px 1px 6px rgba(0,0,0,0.35);
    }

    .celebration-burst { position: fixed; width:100vw; height:100vh; top:0; left:0; z-index:9990; pointer-events:none; }
    .burst-confetti, .burst-balloon, .burst-firework, .burst-snow { position:absolute; width:auto; height:auto; font-size:0; }

    .floating-animal { position: fixed; font-size:3.6rem; animation: float 4.4s cubic-bezier(.2,.9,.2,1) infinite; z-index:50; filter: drop-shadow(0 5px 10px rgba(0,0,0,0.3)); }

    .audio-hint {
      position: fixed;
      left: 50%;
      bottom: 8px;
      transform: translateX(-50%);
      font-size: 11px;
      color: #000;
      background: rgba(255,255,255,0.92);
      padding: 4px 8px;
      border-radius: 8px;
      box-shadow: 0 6px 18px rgba(0,0,0,0.12);
      cursor: pointer;
      z-index: 11000;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
    }

    @media (max-width:420px){
      .audio-hint { font-size:10px; padding:3px 6px; bottom:6px; }
    }

    @media (prefers-reduced-motion: reduce) {
      .welcome-banner, .pet, .poem-container, .countdown, .floating-animal, .celebration-burst, .confetti, .flake {
        animation:none !important; transition:none !important;
      }
    }
  </style>
</head>
<body>
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

  <!-- Confetti for poem transition -->
  <div class="confetti-container" id="confettiContainer"></div>

  <!-- Color flakes for birthday content transition -->
  <div class="flakes-container" id="flakesContainer"></div>

  <!-- POEM ONLY -->
  <div class="poem-container" aria-hidden="true">
    <div class="poem-card" role="article" aria-label="Little Birthday Poem">
      <p> On your special day, let positivity shine ☀️ bright,</p>
      <p> With cheese cakes 🍰 dancing in soft golden light.</p>
      <p> A swirl of warm coffee ☕ makes everything sweet,</p>
      <p> And tiny animals 🐶 bring joy with their little 💙 heartbeat.</p>
      <p>🎶 Songs float around you, inviting your spirit to sing along,</p>
      <p> And happy little dances 💃 turn your moments into a cheerful song.</p>
      <p> Wrapped in gentle kindness 😇, your dreams glow true—</p>
      <p>🔮 A day full of magic 🪄 deserves someone like you.</p>
    </div>
  </div>

  <!-- Countdown Timer -->
  <div class="countdown" id="countdown"></div>

  <!-- Celebration Burst placeholders -->
  <div class="celebration-burst" aria-hidden="true">
    <div class="burst-confetti" style="top:20%; left:15%;"></div>
    <div class="burst-confetti" style="top:25%; right:20%;"></div>
    <div class="burst-balloon" style="top:40%; left:20%;"></div>
    <div class="burst-firework" style="top:15%; left:40%;"></div>
    <div class="burst-snow" style="top:10%; left:50%;"></div>
  </div>

  <!-- Main Birthday Content -->
  <div class="birthday-content">
    <h1>🎂🌹✨ Happy Birthday! ✨🌹🎂</h1>
    <p>🌟 May your birthday be as extraordinary and wonderful as you are! 🎉🌟</p>
    <p>💖 Wishing you a day filled with happiness, laughter and as many cupcakes as your heart desires! 🧁</p>
    <p>✨ May your Birthday be filled with the magic of love, joy, and all the things that makes you happy! ✨</p>
  </div>

  <!-- Snowflakes minimal -->
  <div class="burst-snow" style="left:10%; top:6%;"></div>

  <!-- Audio hint -->
  <div id="audio-hint" class="audio-hint" role="button" aria-label="Play music" onclick="(window.startAudioInteractive && window.startAudioInteractive());">
    Click once to play music
  </div>

  <script>
  // Create confetti particles
  (function(){
    const confettiContainer = document.getElementById('confettiContainer');
    const colors = ['#ff6b6b', '#feca57', '#48dbfb', '#ff9ff3', '#1dd1a1', '#f368e0'];
    
    for(let i = 0; i < 50; i++) {
      const confetti = document.createElement('div');
      confetti.className = 'confetti';
      confetti.style.left = Math.random() * 100 + '%';
      confetti.style.background = colors[Math.floor(Math.random() * colors.length)];
      confetti.style.animationDelay = Math.random() * 3 + 's';
      confetti.style.animationDuration = (Math.random() * 2 + 2) + 's';
      confettiContainer.appendChild(confetti);
    }
  })();

  // Create color flakes
  (function(){
    const flakesContainer = document.getElementById('flakesContainer');
    const colors = ['#ff6b6b', '#feca57', '#48dbfb', '#ff9ff3', '#1dd1a1', '#f368e0', '#5f27cd'];
    
    for(let i = 0; i < 60; i++) {
      const flake = document.createElement('div');
      flake.className = 'flake';
      flake.style.left = Math.random() * 100 + '%';
      flake.style.background = colors[Math.floor(Math.random() * colors.length)];
      flake.style.animationDelay = Math.random() * 4 + 's';
      flake.style.animationDuration = (Math.random() * 3 + 3) + 's';
      flake.style.width = (Math.random() * 6 + 6) + 'px';
      flake.style.height = flake.style.width;
      flakesContainer.appendChild(flake);
    }
  })();

  // Audio code
  (function(){
    const melodyNotes = ["G4","G4","A4","G4","C5","B4","G4","G4","A4","G4","D5","C5","G4","G4","G5","E5","C5","B4","A4","F5","F5","E5","C5","D5","C5"];
    const melodyDurations = [0.5,0.5,1,1,1,2,0.5,0.5,1,1,1,2,0.5,0.5,1,1,1,1,1,0.5,0.5,1,1,2,2];
    const tempo = 88; const beatSec = 60/tempo;
    let audioCtx=null, masterGain=null, isPlaying=false, loopTimer=null;

    function noteToFreq(note){
      const re=/^([A-Ga-g])([#b]?)(\d+)$/; const m=re.exec(note);
      if(!m) return 440;
      const name=m[1].toUpperCase(); const acc=m[2]; const octave=parseInt(m[3],10);
      const semitoneMap={ 'C':-9,'D':-7,'E':-5,'F':-4,'G':-2,'A':0,'B':2 };
      let semis=semitoneMap[name];
      if(acc==='#') semis+=1;
      if(acc==='b') semis-=1;
      semis += (octave-4)*12;
      return 440*Math.pow(2,semis/12);
    }

    function ensureAudio(){
      if(audioCtx) return;
      audioCtx = new (window.AudioContext||window.webkitAudioContext)();
      masterGain = audioCtx.createGain();
      masterGain.gain.value = 0.45;
      masterGain.connect(audioCtx.destination);
    }

    function playFlute(time,freq,duration){
      const osc=audioCtx.createOscillator(); osc.type='sine'; osc.frequency.setValueAtTime(freq,time);
      const vib=audioCtx.createOscillator(); vib.type='sine'; vib.frequency.value=5.0;
      const vibGain=audioCtx.createGain(); vibGain.gain.value = freq*0.0025;
      vib.connect(vibGain); vibGain.connect(osc.frequency);

      const buffer = audioCtx.createBuffer(1, Math.floor(audioCtx.sampleRate*0.28), audioCtx.sampleRate);
      const data = buffer.getChannelData(0);
      for(let i=0;i<data.length;i++){ data[i] = (Math.random()*2-1) * Math.exp(-i/(audioCtx.sampleRate*0.08)); }
      const noise = audioCtx.createBufferSource(); noise.buffer = buffer;

      const noiseGain = audioCtx.createGain(); noiseGain.gain.value = 0.0;
      const bp = audioCtx.createBiquadFilter(); bp.type='bandpass'; bp.frequency.value = freq*2.2; bp.Q.value=8;
      const env = audioCtx.createGain(); env.gain.setValueAtTime(0.0001,time);

      osc.connect(env); noise.connect(noiseGain); noiseGain.connect(bp); bp.connect(env); env.connect(masterGain);

      const attack = Math.min(0.12, duration*0.35); const release = Math.min(0.28, duration*0.45);
      const sustain = 0.9;
      env.gain.exponentialRampToValueAtTime(0.1*sustain, time+attack);
      env.gain.setValueAtTime(0.1*sustain, time+attack);
      env.gain.linearRampToValueAtTime(0.0001, time+duration+release);

      noiseGain.gain.linearRampToValueAtTime(0.035, time+attack*0.9);
      noiseGain.gain.linearRampToValueAtTime(0.0, time+duration+release*0.6);

      vib.start(time); osc.start(time); noise.start(time);
      const stopTime = time + duration + release + 0.05;
      osc.stop(stopTime); noise.stop(stopTime); vib.stop(stopTime+0.02);
    }

    function scheduleMelody(startTime){
      let cursor=startTime;
      for(let i=0;i<melodyNotes.length;i++){
        const note=melodyNotes[i];
        const durBeats=melodyDurations[i]||1;
        const durSec=durBeats*beatSec;
        const freq = noteToFreq(note);
        playFlute(cursor, freq, durSec*0.95);
        cursor += durSec;
      }
      return cursor-startTime;
    }

    function startLoopingMelody(){
      if(isPlaying) return;
      ensureAudio();
      Promise.resolve().then(()=> audioCtx.resume()).catch(()=>{}).finally(()=>{
        if(audioCtx.state==='running'){
          const now = audioCtx.currentTime + 0.08;
          const total = scheduleMelody(now);
          loopTimer = setInterval(()=>{ const s = audioCtx.currentTime + 0.06; scheduleMelody(s); }, Math.max(100, (total*1000)-40));
          isPlaying = true;
          try { const h = document.getElementById('audio-hint'); if(h) h.style.display = 'none'; } catch(e){}
        }
      });
    }

    function stopLoopingMelody(){
      if(loopTimer){ clearInterval(loopTimer); loopTimer=null; }
      isPlaying=false;
      if(masterGain && audioCtx){
        const t=audioCtx.currentTime;
        masterGain.gain.cancelScheduledValues(t);
        masterGain.gain.setValueAtTime(masterGain.gain.value,t);
        masterGain.gain.exponentialRampToValueAtTime(0.0001,t+0.8);
        setTimeout(()=>{ if(masterGain) masterGain.gain.value=0.0; },900);
      }
    }

    window.addEventListener('load', ()=>{ try{ ensureAudio(); startLoopingMelody(); }catch(e){} });

    function gestureStart(){
      try {
        ensureAudio();
        audioCtx.resume().then(()=>{
          startLoopingMelody();
          try { const h = document.getElementById('audio-hint'); if(h) h.style.display = 'none'; } catch(e){}
        }).catch(()=>{});
      } catch(e){}
      window.removeEventListener('pointerdown', gestureStart);
      window.removeEventListener('keydown', gestureStart);
      window.removeEventListener('touchstart', gestureStart);
    }

    window.startAudioInteractive = gestureStart;

    window.addEventListener('pointerdown', gestureStart, {passive:true});
    window.addEventListener('keydown', gestureStart, {passive:true});
    window.addEventListener('touchstart', gestureStart, {passive:true});

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

# Hide Streamlit chrome
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

# Optional visual effects
st.balloons()
st.snow()
