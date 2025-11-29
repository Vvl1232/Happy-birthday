# app.py
import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="wide")

# --- Clean HTML (no confetti/flakes, no welcome-pets; crown inside the card) ---
html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Happy Birthday!</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body { width:100vw; height:100vh; overflow:hidden; font-family: 'Arial', sans-serif; }

    body {
      background: linear-gradient(135deg, #bfefff 0%, #9edcf7 50%, #6fd0f6 100%);
      transition: background 1.2s cubic-bezier(.2,.9,.2,1);
    }

    /* Welcome banner (neutral, not colorful) */
    .welcome-screen { position: fixed; inset: 0; display:flex; align-items:center; justify-content:center; z-index:10000;
      background: linear-gradient(135deg, rgba(255,255,255,0.02), rgba(255,255,255,0.00));
      animation: welcomeSequence 5s cubic-bezier(.2,.9,.2,1) forwards;
    }
    @keyframes welcomeSequence { 0%{opacity:1} 75%{opacity:1} 100%{opacity:0;visibility:hidden} }
    .welcome-banner { background: rgba(255,255,255,0.06); padding: 18px 36px; border-radius: 28px; box-shadow: 0 10px 30px rgba(0,0,0,0.12); margin-bottom: 18px; text-align:center;}
    .welcome-banner h1 { color:#073642; font-size:2.4rem; font-weight:800; }

    /* Poem card */
    .poem-container { position: fixed; top: 50%; left: 50%; transform: translate(-50%,-50%); z-index:10050; pointer-events:none;
      display:flex; align-items:center; justify-content:center; width:92vw; max-width:820px; animation: poemSequence 42s cubic-bezier(.2,.9,.2,1) forwards; }
    @keyframes poemSequence { 0%{opacity:0} 20%{opacity:1} 93%{opacity:1} 100%{opacity:0} }
    .poem-card { width:100%; padding:20px 28px; border-radius:16px; background: rgba(255,255,255,0.12); backdrop-filter: blur(8px);
      border:1px solid rgba(255,255,255,0.12); box-shadow: 0 10px 40px rgba(0,0,0,0.12); color:#fff; font-weight:600; line-height:1.6; }
    .poem-card p { margin:10px 0; font-size:1.05rem; text-shadow:0 2px 6px rgba(0,0,0,0.18); }

    /* Birthday card (crown is inside this card) */
    .birthday-content {
      position: fixed; top:50%; left:50%; transform:translate(-50%,-50%);
      z-index:10050; text-align:center;
      background: rgba(255,255,255,0.12); backdrop-filter: blur(10px);
      padding: 72px 48px 36px; border-radius:26px;
      border:1px solid rgba(255,255,255,0.14); box-shadow:0 22px 90px rgba(0,0,0,0.18);
      animation: contentSequence 42s cubic-bezier(.2,.9,.2,1) forwards;
      opacity:0; max-width:88%; overflow: visible;
    }
    @keyframes contentSequence { 0%{opacity:0;visibility:hidden} 97%{opacity:0;visibility:hidden} 100%{opacity:1;visibility:visible} }

    /* Crown image (static, fades in with the card) */
    .crown-float {
      position: absolute;
      top: -88px;
      left: 50%;
      transform: translateX(-50%);
      width: 160px;
      height: auto;
      z-index:10060;
      pointer-events:none;
      opacity:0;
      filter: drop-shadow(0 18px 30px rgba(0,0,0,0.28));
      animation: crownFadeIn .75s ease-in-out 0.98s forwards;
    }
    @keyframes crownFadeIn { from { opacity:0; transform: translateX(-50%) translateY(-6px) scale(.98);} to { opacity:1; transform: translateX(-50%) translateY(0) scale(1);} }

    .birthday-content h1 { font-size:2.6rem; margin:0 0 12px 0; font-weight:900; color:#fff; text-shadow:0 6px 18px rgba(0,0,0,0.25); }
    .birthday-content p { color:#fff; margin:10px 0; font-size:1rem; font-weight:600; text-shadow:0 2px 6px rgba(0,0,0,0.12); }

    /* audio hint */
    .audio-hint { position: fixed; left:50%; bottom:12px; transform:translateX(-50%); background:#fff; color:#222; padding:6px 10px; border-radius:8px; box-shadow:0 6px 18px rgba(0,0,0,0.12); z-index:11000; }

    @media (max-width:768px){ .crown-float{ width:120px; top:-68px } .birthday-content{ padding:60px 22px 28px } }
    @media (max-width:420px){ .crown-float{ width:98px; top:-62px } .birthday-content{ padding:48px 14px 20px } }
  </style>
</head>
<body>
  <div class="welcome-screen">
    <div class="welcome-banner"><h1>✨ SOMETHING MAGICAL AWAITS! ✨</h1></div>
  </div>

  <!-- POEM -->
  <div class="poem-container" aria-hidden="true">
    <div class="poem-card" role="article" aria-label="Little Birthday Poem">
      <p>On your special day, let positivity shine ☀️ bright,</p>
      <p>With cheese cakes 🍰 dancing in soft golden light.</p>
      <p>A swirl of warm coffee ☕ makes everything sweet,</p>
      <p>And tiny animals 🐶 bring joy with their little 💙 heartbeat.</p>
      <p>🎶 Songs float around you, inviting your spirit to sing 🎤 along,</p>
      <p>And happy little dances 💃 turn your moments into a cheerful song.</p>
      <p>Wrapped in gentle kindness 😇, your dreams glow true—</p>
      <p>🔮 A day full of magic 🪄 deserves someone like you.</p>
    </div>
  </div>

  <!-- Birthday card (crown placed inside so it only appears with the card) -->
  <div class="birthday-content">
    <!-- Make sure this path matches the file you uploaded into /mnt/data/ -->
    <img class="crown-float" src="file:///mnt/data/05f2f164-6623-4834-bd46-02528ad6fd5d.png" alt="Crown" aria-hidden="true" />
    <h1>🎂🌹✨ Happy Birthday! ✨🌹🎂</h1>
    <p>🌟 May your birthday be as extraordinary and wonderful as you are! 🎉🌟</p>
    <p>💖 Wishing you a day filled with happiness, laughter and as many cupcakes as your heart desires! 🧁</p>
    <p>✨ May your Birthday be filled with the magic of love, joy, and all the things that makes you happy! ✨</p>
  </div>

  <div class="audio-hint" id="audio-hint" role="button" onclick="(window.startAudioInteractive && window.startAudioInteractive());">Click once to play music</div>

  <script>
    // confetti/flakes removed intentionally to avoid stray colorful columns

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
        if(acc==='#') semis+=1; if(acc==='b') semis-=1;
        semis += (octave-4)*12; return 440*Math.pow(2,semis/12);
      }

      function ensureAudio(){ if(audioCtx) return; audioCtx = new (window.AudioContext||window.webkitAudioContext)(); masterGain = audioCtx.createGain(); masterGain.gain.value = 0.45; masterGain.connect(audioCtx.destination); }

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
        const attack = Math.min(0.12, duration*0.35); const release = Math.min(0.28, duration*0.45); const sustain = 0.9;
        env.gain.exponentialRampToValueAtTime(0.1*sustain, time+attack);
        env.gain.setValueAtTime(0.1*sustain, time+attack);
        env.gain.linearRampToValueAtTime(0.0001, time+duration+release);
        noiseGain.gain.linearRampToValueAtTime(0.035, time+attack*0.9);
        noiseGain.gain.linearRampToValueAtTime(0.0, time+duration+release*0.6);
        vib.start(time); osc.start(time); noise.start(time);
        const stopTime = time + duration + release + 0.05; osc.stop(stopTime); noise.stop(stopTime); vib.stop(stopTime+0.02);
      }

      function scheduleMelody(startTime){ let cursor=startTime; for(let i=0;i<melodyNotes.length;i++){ const note=melodyNotes[i]; const durBeats=melodyDurations[i]||1; const durSec=durBeats*beatSec; const freq = noteToFreq(note); playFlute(cursor, freq, durSec*0.95); cursor += durSec; } return cursor-startTime; }

      function startLoopingMelody(){ if(isPlaying) return; ensureAudio(); Promise.resolve().then(()=> audioCtx.resume()).catch(()=>{}).finally(()=>{ if(audioCtx.state==='running'){ const now = audioCtx.currentTime + 0.08; const total = scheduleMelody(now); loopTimer = setInterval(()=>{ const s = audioCtx.currentTime + 0.06; scheduleMelody(s); }, Math.max(100, (total*1000)-40)); isPlaying = true; try { const h = document.getElementById('audio-hint'); if(h) h.style.display = 'none'; } catch(e){} } }); }

      function stopLoopingMelody(){ if(loopTimer){ clearInterval(loopTimer); loopTimer=null; } isPlaying=false; if(masterGain && audioCtx){ const t=audioCtx.currentTime; masterGain.gain.cancelScheduledValues(t); masterGain.gain.setValueAtTime(masterGain.gain.value,t); masterGain.gain.exponentialRampToValueAtTime(0.0001,t+0.8); setTimeout(()=>{ if(masterGain) masterGain.gain.value=0.0; },900); } }

      window.addEventListener('load', ()=>{ try{ ensureAudio(); startLoopingMelody(); }catch(e){} });
      function gestureStart(){ try { ensureAudio(); audioCtx.resume().then(()=>{ startLoopingMelody(); try { const h = document.getElementById('audio-hint'); if(h) h.style.display = 'none'; } catch(e){} }).catch(()=>{}); } catch(e){} window.removeEventListener('pointerdown', gestureStart); window.removeEventListener('keydown', gestureStart); window.removeEventListener('touchstart', gestureStart); }
      window.startAudioInteractive = gestureStart; window.addEventListener('pointerdown', gestureStart, {passive:true}); window.addEventListener('keydown', gestureStart, {passive:true}); window.addEventListener('touchstart', gestureStart, {passive:true});
      document.addEventListener('visibilitychange', () => { if(document.hidden){ stopLoopingMelody(); } else { startLoopingMelody(); } });
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

# Optional visual effects (safe-guarded)
try:
    st.balloons()
    st.snow()
except Exception:
    pass
