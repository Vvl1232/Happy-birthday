import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="wide")

# Complete HTML with modifications: darker H1, autoplay attempt, and no click sound.
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Happy Birthday!</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body, html {
      width: 100vw; height: 100vh; overflow: hidden;
      font-family: 'Arial', sans-serif;
      position: fixed; top: 0; left: 0;
    }

    /* Powder sky blue background */
    body {
      background: linear-gradient(135deg, #dff6ff 0%, #cfefff 50%, #e9f8ff 100%);
    }

    /* Responsive */
    @media (max-width: 768px) { .welcome-banner h1 { font-size: 2.5em !important; } .welcome-banner { padding: 25px 40px !important; } .pet { font-size: 6em !important; } .welcome-pets { gap: 60px !important; } .peacock { font-size: 12em !important; } .countdown { font-size: 10em !important; } .birthday-content { padding: 25px 30px !important; width: 90% !important; max-width: 90% !important; } .birthday-content h1 { font-size: 2em !important; } .birthday-content p { font-size: 1em !important; margin: 10px 0 !important; } .floating-animal { font-size: 2.5em !important; } .snowflake, .confetti, .sparkle { font-size: 1.5em !important; } .firework { font-size: 2.5em !important; } }
    @media (max-width: 480px) { .welcome-banner h1 { font-size: 1.8em !important; } .welcome-banner { padding: 20px 30px !important; } .pet { font-size: 4em !important; } .peacock { font-size: 8em !important; } .countdown { font-size: 8em !important; } .birthday-content { padding: 20px 25px !important; } .birthday-content h1 { font-size: 1.5em !important; } .birthday-content p { font-size: 0.85em !important; margin: 8px 0 !important; } }

    /* Animations */
    @keyframes float { 0%,100%{transform:translateY(0) rotate(0)} 50%{transform:translateY(-30px) rotate(5deg)} }
    @keyframes bounce { 0%,100%{transform:translateY(0) scale(1)} 50%{transform:translateY(-20px) scale(1.03)} }
    @keyframes slideIn { from{transform:translateX(-100%);opacity:0} to{transform:translateX(0);opacity:1} }
    @keyframes sparkle { 0%,100%{opacity:1;transform:scale(1) rotate(0deg)} 50%{opacity:0.3;transform:scale(1.5) rotate(180deg)} }
    @keyframes fall { 0%{transform:translateY(-100vh) rotate(0)} 100%{transform:translateY(100vh) rotate(360deg)} }
    @keyframes firework { 0%{transform:scale(0);opacity:1} 50%{transform:scale(1.2);opacity:1} 100%{transform:scale(2);opacity:0} }
    @keyframes peacockFlyStop { 0%{transform:translateX(-120%) scale(1.2);opacity:0} 10%{transform:translateX(-120%) scale(1.2);opacity:0} 11%{transform:translateX(-10%) scale(1.2);opacity:1} 70%{transform:translateX(5%) scale(1.1);opacity:1} 100%{transform:translateX(5%) scale(1.1);opacity:0} }
    @keyframes countdownNumber { 0%{opacity:0;transform:translate(-50%,-50%) scale(0.75)} 20%{opacity:1;transform:translate(-50%,-50%) scale(1.08)} 60%{opacity:1;transform:translate(-50%,-50%) scale(1)} 100%{opacity:0;transform:translate(-50%,-50%) scale(0.75)} }

    /* Welcome */
    .welcome-screen { position:fixed; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:center; z-index:10000; background:linear-gradient(135deg, rgba(223,246,255,0.06) 0%, rgba(207,239,255,0.06) 50%, rgba(233,248,255,0.06) 100%); animation: welcomeSequence 1.05s ease-in-out forwards; }
    @keyframes welcomeSequence { 0%{opacity:1} 83%{opacity:1} 100%{opacity:0;visibility:hidden;pointer-events:none} }
    .welcome-banner { background: linear-gradient(45deg,#ff6b6b,#feca57,#48dbfb,#ff9ff3); padding:40px 80px; border-radius:50px; box-shadow:0 20px 60px rgba(0,0,0,0.12); animation:bounce 2s infinite; margin-bottom:28px; }
    .welcome-banner h1 { color:white; font-size:3.2rem; text-align:center; margin:0; text-shadow:2px 2px 6px rgba(11,59,68,0.12); font-weight:800; }

    .welcome-pets { display:flex; gap:80px; animation:slideIn 1.5s ease-out; }
    .pet { font-size:6.8rem; animation:bounce 1.6s infinite; filter:drop-shadow(0 6px 10px rgba(11,59,68,0.06)); }

    /* Peacock container (shorter entrance) */
    .peacock-container { position:fixed; inset:0; display:flex; align-items:center; justify-content:center; z-index:9999; animation: peacockSequence 3s ease-in-out forwards; background:linear-gradient(135deg, rgba(223,246,255,0.04), rgba(207,239,255,0.04)); }
    @keyframes peacockSequence { 0%{opacity:0;visibility:hidden} 10%{opacity:1;visibility:visible} 60%{opacity:1} 100%{opacity:0;visibility:hidden} }
    .peacock { font-size:6.6rem; filter:drop-shadow(0 12px 20px rgba(11,59,68,0.08)); animation:peacockFlyStop 3s ease-out forwards; }

    /* Countdown */
    .countdown { position:fixed; top:50%; left:50%; transform:translate(-50%,-50%); font-size:4.8rem; font-weight:800; color:#ff6b6b; text-shadow:0 0 12px rgba(255,107,107,0.5); z-index:10001; transition:opacity 0.3s, transform 0.3s; }
    .countdown.show { animation: countdownNumber 0.9s ease-in-out; }

    /* Main content (lighter, cute, readable) */
    .birthday-content { position:fixed; top:50%; left:50%; transform:translate(-50%,-50%); text-align:center; z-index:10000; background:rgba(255,255,255,0.14); backdrop-filter: blur(8px); padding:28px 38px; border-radius:20px; box-shadow:0 20px 60px rgba(11,59,68,0.06); border:1px solid rgba(255,255,255,0.18); animation:contentSequence 1.2s ease-in forwards; max-width:88%; max-height:85vh; overflow-y:auto; }
    @keyframes contentSequence { 0%{opacity:0; transform:translate(-50%,-50%) scale(0.98)} 100%{opacity:1; transform:translate(-50%,-50%) scale(1)} }

    /* H1: same style + darker for better visibility + bounce */
    .birthday-content h1 {
      font-size:2.0rem;
      background: linear-gradient(45deg, #c63b3b, #e68a2e, #2f8fbf, #c85aa8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom:14px;
      animation: bounce 2.6s ease-in-out infinite;
      font-weight:900;
      text-shadow: 0 4px 12px rgba(11,59,68,0.18); /* darker shadow to increase contrast */
    }

    /* paragraphs slightly darker color for readability */
    .birthday-content p { font-size:1.02rem; color:#04454b; margin:10px 0; line-height:1.6; font-weight:600; }

    /* floating animals */
    .floating-animal { position:fixed; font-size:2.8rem; animation:float 4s ease-in-out infinite; z-index:50; filter:drop-shadow(0 6px 10px rgba(11,59,68,0.05)); }

    /* small effects sizes */
    .snowflake, .confetti, .firework, .sparkle { position:fixed; font-size:1.6rem; z-index:10; }
    .firework { font-size:2.6rem; animation:firework 1.6s ease-out infinite; }
    .sparkle { font-size:1.9rem; animation:sparkle 2s ease-in-out infinite; }

    @media (prefers-reduced-motion: reduce) {
      .welcome-banner, .pet, .peacock, .countdown, .floating-animal, .celebration-burst { animation: none !important; transition: none !important; }
    }

  </style>
</head>
<body>
  <!-- Welcome Screen -->
  <div class="welcome-screen" role="region" aria-label="Welcome">
    <div class="welcome-banner">
      <h1>✨ SOMETHING MAGICAL AWAITS! ✨</h1>
    </div>
    <div class="welcome-pets">
      <div class="pet">🐱</div>
      <div class="pet">🐶</div>
    </div>
  </div>

  <!-- Peacock animation (short entrance) -->
  <div class="peacock-container" aria-hidden="true">
    <div class="peacock">🦚</div>
  </div>

  <!-- Countdown area -->
  <div class="countdown" id="countdown" aria-hidden="true"></div>

  <!-- Celebration burst (decorative) -->
  <div class="celebration-burst" aria-hidden="true">
    <div class="burst-confetti" style="top:20%; left:15%; font-size:2.6rem; animation-delay:0s;">🎊</div>
    <div class="burst-confetti" style="top:25%; right:20%; font-size:2.6rem; animation-delay:0.1s;">🎉</div>
    <div class="burst-firework" style="top:15%; left:40%; font-size:3rem; animation-delay:0.1s;">💥</div>
    <div class="burst-snow" style="top:10%; left:50%; font-size:2rem; animation-delay:0.2s;">❄</div>
  </div>

  <!-- Main Birthday Content -->
  <div class="birthday-content" role="main" aria-label="Birthday message">
    <h1>🎂🌹✨ Happy Birthday! ✨🌹🎂</h1>
    <p>🌟 May your birthday be as extraordinary and wonderful as you are! 🎉🌟</p>
    <p>💖 Wishing you a day filled with happiness, laughter and as many cupcakes as your heart desires! 🧁</p>
    <p>✨ May your Birthday be filled with the magic of love, joy, and all the things that make you happy! ✨</p>
  </div>

  <!-- Floating Animals (spaced to avoid overlapping) -->
  <div class="floating-animal" style="top:6%; left:6%; animation-delay:0s;">🐶</div>
  <div class="floating-animal" style="top:10%; right:8%; animation-delay:0.6s;">🐱</div>
  <div class="floating-animal" style="top:22%; left:16%; animation-delay:1.1s;">🐕</div>
  <div class="floating-animal" style="top:30%; right:22%; animation-delay:1.6s;">🐈</div>
  <div class="floating-animal" style="top:44%; left:4%; animation-delay:2.1s;">🐩</div>
  <div class="floating-animal" style="top:52%; right:6%; animation-delay:2.6s;">🐈‍⬛</div>
  <div class="floating-animal" style="bottom:22%; left:12%; animation-delay:0.4s;">🦮</div>
  <div class="floating-animal" style="bottom:30%; right:14%; animation-delay:0.9s;">🐕‍🦺</div>
  <div class="floating-animal" style="bottom:14%; left:22%; animation-delay:1.4s;">🐾</div>
  <div class="floating-animal" style="bottom:20%; right:20%; animation-delay:1.9s;">🐾</div>

  <!-- Minimal decorative flakes / confetti spaced out -->
  <div class="snowflake" style="left:12%; animation-duration:8.2s;">❄</div>
  <div class="snowflake" style="left:28%; animation-duration:9.0s;">❄</div>
  <div class="confetti" style="left:42%; animation-duration:7.5s; color:#ff9ff3;">🎉</div>
  <div class="confetti" style="left:62%; animation-duration:8.7s; color:#48dbfb;">🎊</div>
  <div class="sparkle" style="top:18%; right:44%;">✨</div>

  <!-- Flute background music: autoplay attempt on load; will still resume on gesture if blocked -->
  <script>
    (function(){
      const notes = [
        "G4","G4","A4","G4","C5","B4",
        "G4","G4","A4","G4","D5","C5",
        "G4","G4","G5","E5","C5","B4","A4",
        "F5","F5","E5","C5","D5","C5"
      ];
      const durations = [0.5,0.5,1,1,1,2,0.5,0.5,1,1,1,2,0.5,0.5,1,1,1,1,1,0.5,0.5,1,1,2,2];
      const tempo = 88;
      const beat = 60/tempo;

      let audioCtx = null;
      let master = null;
      let loopHandle = null;
      let playing = false;

      function noteToFreq(n){
        const m = /^([A-G])([#b]?)(\\d+)$/.exec(n);
        if(!m) return 440;
        const map = {'C':-9,'D':-7,'E':-5,'F':-4,'G':-2,'A':0,'B':2};
        let semis = map[m[1]] + (parseInt(m[3],10)-4)*12;
        if(m[2] === '#') semis++;
        if(m[2] === 'b') semis--;
        return 440 * Math.pow(2, semis/12);
      }

      function ensure(){
        if(audioCtx) return;
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        master = audioCtx.createGain();
        master.gain.value = 0.55; // slightly stronger for clarity
        master.connect(audioCtx.destination);
      }

      function playNoteAt(t, freq, dur){
        const osc = audioCtx.createOscillator(); osc.type='sine';
        osc.frequency.setValueAtTime(freq, t);

        const vib = audioCtx.createOscillator(); vib.type='sine'; vib.frequency.value = 5.1;
        const vg = audioCtx.createGain(); vg.gain.value = freq * 0.0024;
        vib.connect(vg); vg.connect(osc.frequency);

        const buf = audioCtx.createBuffer(1, audioCtx.sampleRate * 0.28, audioCtx.sampleRate);
        const data = buf.getChannelData(0);
        for(let i=0;i<data.length;i++) data[i] = (Math.random()*2 - 1) * Math.exp(-i/(audioCtx.sampleRate*0.08));
        const noise = audioCtx.createBufferSource(); noise.buffer = buf;
        const noiseG = audioCtx.createGain(); noiseG.gain.value = 0;
        const bp = audioCtx.createBiquadFilter(); bp.type='bandpass'; bp.frequency.value = freq*2.2; bp.Q.value = 8.5;

        const env = audioCtx.createGain(); env.gain.setValueAtTime(0.0001, t);

        osc.connect(env);
        noise.connect(noiseG); noiseG.connect(bp); bp.connect(env);
        env.connect(master);

        const attack = Math.min(0.12, dur * 0.35);
        const release = Math.min(0.28, dur * 0.45);

        env.gain.exponentialRampToValueAtTime(0.11, t + attack);
        env.gain.linearRampToValueAtTime(0.0001, t + dur + release);

        noiseG.gain.linearRampToValueAtTime(0.035, t + attack * 0.9);
        noiseG.gain.linearRampToValueAtTime(0.0, t + dur + release * 0.6);

        vib.start(t); osc.start(t); noise.start(t);
        const stopT = t + dur + release + 0.05;
        osc.stop(stopT); noise.stop(stopT); vib.stop(stopT + 0.02);
      }

      function scheduleOnce(start){
        let cur = start;
        for(let i=0;i<notes.length;i++){
          const dur = (durations[i] || 1) * beat;
          const freq = noteToFreq(notes[i]);
          playNoteAt(cur, freq, dur * 0.95);
          cur += dur;
        }
        return cur - start;
      }

      function startLoop(){
        if(playing) return;
        ensure();
        // If the context is suspended, try to resume first
        audioCtx.resume().catch(()=>{}).finally(()=>{
          const now = audioCtx.currentTime + 0.06;
          const total = scheduleOnce(now);
          loopHandle = setInterval(()=> scheduleOnce(audioCtx.currentTime + 0.04), Math.max(60, (total*1000) - 30));
          playing = true;
        });
      }

      function stopLoop(){
        if(loopHandle){ clearInterval(loopHandle); loopHandle = null; }
        playing = false;
      }

      // Aggressively attempt autoplay immediately and also on load.
      try { ensure(); startLoop(); } catch(e){ /* ignore */ }

      window.addEventListener('load', function(){
        try { ensure(); startLoop(); } catch(e){}
      }, {passive:true});

      // Also resume if the user interacts (in case browser blocked autoplay)
      function resumeOnGesture(){
        try { ensure(); audioCtx.resume().then(()=> startLoop()).catch(()=>{}); } catch(e){}
        window.removeEventListener('pointerdown', resumeOnGesture);
        window.removeEventListener('keydown', resumeOnGesture);
        window.removeEventListener('touchstart', resumeOnGesture);
      }
      window.addEventListener('pointerdown', resumeOnGesture, {passive:true});
      window.addEventListener('keydown', resumeOnGesture, {passive:true});
      window.addEventListener('touchstart', resumeOnGesture, {passive:true});

      // NOTE: click sound removed as requested (no pointerdown chime).
    })();
  </script>

  <script>
    // Shortened countdown timing to make main content appear quickly
    const countdown = document.getElementById('countdown');
    function showNumber(number, delay) {
      setTimeout(()=> {
        countdown.textContent = number;
        countdown.classList.remove('show');
        void countdown.offsetWidth;
        countdown.classList.add('show');
      }, delay);
    }
    showNumber('3', 600);
    showNumber('2', 760);
    showNumber('1', 920);
    setTimeout(()=> { countdown.style.opacity = '0'; setTimeout(()=> countdown.textContent = '', 300); }, 1250);
  </script>
</body>
</html>
"""

# Hide Streamlit chrome for fullscreen
st.markdown("""
<style>
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  header {visibility: hidden;}
  .stApp > header {visibility: hidden;}
  [data-testid="stHeader"] {display: none;}
  [data-testid="stToolbar"] {display: none;}
  .block-container { padding: 0 !important; max-width: 100% !important; }
  iframe { border: none !important; display: block; position: fixed; top: 0; left: 0; width: 100vw !important; height: 100vh !important; }
</style>
""", unsafe_allow_html=True)

# Render and optional visuals
components.html(html_code, height=1000, scrolling=False)
st.balloons()
st.snow()
