import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="wide")

# ---------------------------------------
# Minimal-edits version of your original HTML
# (only small targeted changes — see comments)
# ---------------------------------------
html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* ---------- Minimal visual fixes & original styles kept ---------- */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body, html { width: 100vw; height: 100vh; overflow: hidden; font-family: 'Arial', sans-serif; position: fixed; top: 0; left: 0; }

        /* BACKGROUND: changed to light sky powder blue as requested */
        body {
            background: linear-gradient(135deg, #bfe9ff 0%, #cfefff 50%, #e9f8ff 100%);
        }

        /* small mobile responsive tweaks preserved */
        @media (max-width: 768px) {
            .welcome-banner h1 { font-size: 2.5em !important; }
            .welcome-banner { padding: 25px 40px !important; }
            .pet { font-size: 6em !important; }
            .welcome-pets { gap: 60px !important; }
            .peacock { font-size: 12em !important; }
            .countdown { font-size: 10em !important; }
            .birthday-content { padding: 25px 30px !important; width: 90% !important; max-width: 90% !important; }
            .birthday-content h1 { font-size: 2em !important; }
            .birthday-content p { font-size: 1em !important; margin: 10px 0 !important; }
            .floating-animal { font-size: 2.5em !important; }
            .snowflake, .confetti, .sparkle { font-size: 1.5em !important; }
            .firework { font-size: 2.5em !important; }
        }

        @media (max-width: 480px) {
            .welcome-banner h1 { font-size: 1.8em !important; }
            .welcome-banner { padding: 20px 30px !important; }
            .pet { font-size: 4em !important; }
            .peacock { font-size: 8em !important; }
            .countdown { font-size: 8em !important; }
            .birthday-content { padding: 20px 25px !important; }
            .birthday-content h1 { font-size: 1.5em !important; }
            .birthday-content p { font-size: 0.85em !important; margin: 8px 0 !important; }
        }

        /* Animations (kept original, slight timing tweak on float) */
        @keyframes float { 0%, 100% { transform: translateY(0px) rotate(0deg); } 50% { transform: translateY(-20px) rotate(4deg); } }
        @keyframes bounce { 0%, 100% { transform: translateY(0) scale(1); } 50% { transform: translateY(-32px) scale(1.05); } }
        @keyframes slideIn { from { transform: translateX(-100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
        @keyframes sparkle { 0%, 100% { opacity: 1; transform: scale(1) rotate(0deg); } 50% { opacity: 0.3; transform: scale(1.5) rotate(180deg); } }
        @keyframes fall { 0% { transform: translateY(-100vh) rotate(0deg); opacity: 1; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0.5; } }
        @keyframes firework { 0% { transform: scale(0); opacity: 1; } 50% { transform: scale(1.2); opacity: 1; } 100% { transform: scale(2); opacity: 0; } }
        @keyframes flutePlay { 0%, 100% { transform: rotate(-5deg); } 50% { transform: rotate(5deg); } }
        @keyframes glow { 0%, 100% { filter: drop-shadow(0 0 20px rgba(255, 215, 0, 0.8)); } 50% { filter: drop-shadow(0 0 40px rgba(255, 215, 0, 1)); } }

        /* ---------- Welcome screen: reduced time so main appears sooner ---------- */
        .welcome-screen {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            z-index: 10000;
            background: linear-gradient(135deg, rgba(191,233,255,0.06) 0%, rgba(207,239,255,0.06) 50%, rgba(233,248,255,0.06) 100%);
            /* REDUCED: shorter welcome duration */
            animation: welcomeSequence 1.05s ease-in-out forwards;
        }
        @keyframes welcomeSequence {
            0% { opacity: 1; visibility: visible; }
            85% { opacity: 1; visibility: visible; }
            100% { opacity: 0; visibility: hidden; pointer-events: none; }
        }

        .welcome-banner {
            background: linear-gradient(45deg, #ffebee, #fff9e6, #dff7ff, #fff0fb);
            padding: 28px 68px;
            border-radius: 50px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.06);
            animation: bounce 1.8s ease-in-out infinite;
            margin-bottom: 30px;
        }
        .welcome-banner h1 { color: #073542; font-size: 3.2rem; text-align: center; margin: 0; font-weight: 800; }

        .welcome-pets { display: flex; gap: 60px; animation: slideIn 1.2s ease-out; }
        .pet { font-size: 6.2rem; animation: bounce 1.5s ease-in-out infinite; filter: drop-shadow(0 10px 20px rgba(0,0,0,0.05)); }

        /* Countdown (slightly smaller & faster) */
        .countdown {
            position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
            font-size: 6.6rem; font-weight: 900; color: #ff6b6b;
            text-shadow: 0 0 30px rgba(255,107,107,0.8);
            z-index: 10001; transition: opacity 0.3s ease, transform 0.3s ease;
        }
        .countdown.show { animation: countdownNumber 0.9s ease-in-out; }
        @keyframes countdownNumber {
            0% { opacity: 0; transform: translate(-50%, -50%) scale(0.8); }
            20% { opacity: 1; transform: translate(-50%, -50%) scale(1.05); }
            60% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
            100% { opacity: 0; transform: translate(-50%, -50%) scale(0.8); }
        }

        /* Main content: increased transparency & blur kept (user requested blur/transparent look earlier) */
        .birthday-content {
            position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
            text-align: center; z-index: 10000;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(16px);
            padding: 34px 44px; border-radius: 22px;
            box-shadow: 0 25px 80px rgba(0,0,0,0.06);
            border: 1px solid rgba(255,255,255,0.12);
            animation: contentSequence 2.8s ease-in forwards; /* kept short so content appears after welcome */
            max-width: 84%; max-height: 84vh; overflow-y: auto;
        }
        @keyframes contentSequence { 0% { opacity: 0; visibility: hidden; transform: translate(-50%, -50%) scale(0.95); } 99% { opacity: 0; } 100% { opacity: 1; visibility: visible; transform: translate(-50%, -50%) scale(1); } }

        .birthday-content h1 { font-size: 2.1rem; background: linear-gradient(45deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 14px; font-weight: 900; }
        .birthday-content p { font-size: 1.1rem; color: #052a30; margin: 10px 0; line-height: 1.6; font-weight: 600; }

        /* Floating animals: slightly reduced size and more spacing to avoid overlap */
        .floating-animal {
            position: fixed; font-size: 3.2rem; animation: float 4.2s ease-in-out infinite; z-index: 50; filter: drop-shadow(0 6px 12px rgba(0,0,0,0.05));
        }

        /* Effects (kept) */
        .snowflake, .confetti, .firework, .sparkle {
            position: fixed; font-size: 2rem; z-index: 10; will-change: transform, opacity;
        }
        .snowflake { animation: fall linear infinite; }
        .confetti { animation: fall linear infinite; }
        .firework { font-size: 3.6rem; animation: firework 2s ease-out infinite; }
        .sparkle { font-size: 2.2rem; animation: sparkle 2s ease-in-out infinite; }

        @media (prefers-reduced-motion: reduce) {
            .welcome-banner, .pet, .peacock, .countdown, .floating-animal, .celebration-burst { animation: none !important; transition: none !important; }
        }

        /* small visual nudge: ensure emojis don't overlap too closely by default */
        .burst-confetti, .burst-balloon, .burst-snow, .burst-firework { transform-origin: center; will-change: transform; margin: 6px; }
    </style>
</head>
<body>
    <!-- Welcome Screen (short) -->
    <div class="welcome-screen">
        <div class="welcome-banner">
            <h1>✨ SOMETHING MAGICAL AWAITS! ✨</h1>
        </div>
        <div class="welcome-pets">
            <div class="pet">🐱</div>
            <div class="pet">🐶</div>
        </div>
    </div>

    <!-- Removed separate peacock-container entry earlier per your requests, peacock now placed among floating animals -->

    <!-- Countdown Timer -->
    <div class="countdown" id="countdown"></div>

    <!-- Celebration Burst Effects (kept your placements) -->
    <div class="celebration-burst">
        <div class="burst-confetti" style="top: 20%; left: 15%; font-size: 3em; animation-delay: 0s;">🎊</div>
        <div class="burst-confetti" style="top: 25%; right: 20%; font-size: 3em; animation-delay: 0.1s;">🎉</div>
        <div class="burst-confetti" style="top: 30%; left: 30%; font-size: 3em; animation-delay: 0.2s;">🎊</div>
        <div class="burst-confetti" style="top: 35%; right: 35%; font-size: 3em; animation-delay: 0.3s;">🎉</div>
        <div class="burst-confetti" style="bottom: 30%; left: 25%; font-size: 3em; animation-delay: 0.4s;">🎊</div>
        <div class="burst-confetti" style="bottom: 35%; right: 30%; font-size: 3em; animation-delay: 0.5s;">🎉</div>

        <div class="burst-balloon" style="top: 40%; left: 20%; font-size: 3em; animation-delay: 0.2s;">🎈</div>
        <div class="burst-balloon" style="top: 45%; right: 25%; font-size: 3em; animation-delay: 0.3s;">🎈</div>
        <div class="burst-balloon" style="bottom: 40%; left: 30%; font-size: 3em; animation-delay: 0.4s;">🎈</div>
        <div class="burst-balloon" style="bottom: 45%; right: 28%; font-size: 3em; animation-delay: 0.5s;">🎈</div>

        <div class="burst-firework" style="top: 15%; left: 40%; font-size: 4em; animation-delay: 0.1s;">💥</div>
        <div class="burst-firework" style="top: 20%; right: 40%; font-size: 4em; animation-delay: 0.3s;">🎆</div>
        <div class="burst-firework" style="bottom: 20%; left: 35%; font-size: 4em; animation-delay: 0.5s;">✨</div>
        <div class="burst-firework" style="bottom: 25%; right: 38%; font-size: 4em; animation-delay: 0.6s;">💫</div>

        <div class="burst-snow" style="top: 10%; left: 50%; font-size: 2.5em; animation-delay: 0.2s;">❄️</div>
        <div class="burst-snow" style="top: 18%; right: 50%; font-size: 2.5em; animation-delay: 0.4s;">❄️</div>
        <div class="burst-snow" style="top: 28%; left: 45%; font-size: 2.5em; animation-delay: 0.6s;">❄️</div>
    </div>

    <!-- Audio for celebration sound (kept your WebAudio flute; slightly increased clarity) -->
    <script>
        /* Minimal change: slightly increase the master gain and adjust some bandpass Q to make flute clearer
           The rest of your original audio scheduling logic is preserved. */

        (function(){
          // NOTES/PHRASE are left as before (your original melody variables).
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
          const tempo = 88;
          const beatSec = 60 / tempo;

          let audioCtx = null;
          let masterGain = null;
          let isPlaying = false;
          let loopTimer = null;

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

            // Slightly higher master volume for clarity (but still moderate)
            masterGain = audioCtx.createGain();
            masterGain.gain.value = 0.50; // changed from 0.45 -> 0.50 for a touch more clarity
            masterGain.connect(audioCtx.destination);
          }

          function playFlute(time, freq, duration){
            const osc = audioCtx.createOscillator();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(freq, time);

            const vib = audioCtx.createOscillator();
            vib.type = 'sine';
            vib.frequency.value = 5.0;
            const vibGain = audioCtx.createGain();
            vibGain.gain.value = freq * 0.0025;
            vib.connect(vibGain);
            vibGain.connect(osc.frequency);

            const buffer = audioCtx.createBuffer(1, audioCtx.sampleRate * 0.28, audioCtx.sampleRate);
            const data = buffer.getChannelData(0);
            for(let i=0;i<data.length;i++){
              data[i] = (Math.random()*2 - 1) * Math.exp(-i / (audioCtx.sampleRate * 0.08));
            }
            const noise = audioCtx.createBufferSource();
            noise.buffer = buffer;

            const noiseGain = audioCtx.createGain();
            noiseGain.gain.value = 0.0;

            // Slightly adjusted Q for the bandpass to emphasize flute harmonics a bit more
            const bp = audioCtx.createBiquadFilter();
            bp.type = 'bandpass';
            bp.frequency.value = freq * 2.25; // tiny boost
            bp.Q.value = 9; // slightly higher Q for clarity

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

            env.gain.exponentialRampToValueAtTime(0.11 * sustain, time + attack);
            env.gain.setValueAtTime(0.11 * sustain, time + attack);
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
            audioCtx.resume().catch(()=>{}).finally(()=>{
              const now = audioCtx.currentTime + 0.08;
              const total = scheduleMelody(now);
              loopTimer = setInterval(()=>{
                const s = audioCtx.currentTime + 0.06;
                scheduleMelody(s);
              }, Math.max(100, (total * 1000) - 40));
              isPlaying = true;
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

          // Attempt autoplay (will resume on first gesture if blocked)
          try {
            ensureAudio();
            startLoopingMelody();
          } catch (e) {}

          function userStartHandler(){
            try {
              ensureAudio();
              audioCtx.resume().then(()=> {
                startLoopingMelody();
              }).catch(()=>{});
            } catch(e){}
            window.removeEventListener('pointerdown', userStartHandler);
            window.removeEventListener('keydown', userStartHandler);
            window.removeEventListener('touchstart', userStartHandler);
          }

          window.addEventListener('pointerdown', userStartHandler, {passive:true});
          window.addEventListener('keydown', userStartHandler, {passive:true});
          window.addEventListener('touchstart', userStartHandler, {passive:true});

          // small click chime on pointerdown (kept)
          window.addEventListener('pointerdown', function(){
            if(!audioCtx || audioCtx.state !== 'running') return;
            const now = audioCtx.currentTime;
            const osc = audioCtx.createOscillator(); osc.type = 'sine';
            const g = audioCtx.createGain(); g.gain.value = 0.0001;
            osc.frequency.setValueAtTime(880, now);
            osc.frequency.exponentialRampToValueAtTime(1500, now + 0.06);
            g.gain.setValueAtTime(0.0001, now);
            g.gain.exponentialRampToValueAtTime(0.12, now + 0.02);
            g.gain.exponentialRampToValueAtTime(0.0001, now + 0.24);
            osc.connect(g).connect(masterGain);
            osc.start(now); osc.stop(now + 0.26);
          }, {passive:true});

        })();
    </script>

    <!-- Main Birthday Content -->
    <div class="birthday-content" role="main" aria-label="Birthday message">
        <h1>🎂🌹✨ Happy Birthday! ✨🌹🎂</h1>
        <p>🌟 May your birthday be as extraordinary and wonderful as you are! 🎉🌟</p>
        <p>💖 Wishing you a day filled with happiness, laughter and as many cupcakes as your heart desires! 🧁</p>
        <p>✨ May your Birthday be filled with the magic of love, joy, and all the things that make you happy! ✨</p>
    </div>

    <!-- Floating Animals & emojis with slightly more spacing (no overlap) -->
    <div class="floating-animal" style="top: 6%; left: 5%; animation-delay: 0s; animation-duration: 3s;">🐶</div>
    <div class="floating-animal" style="top: 11%; right: 8%; animation-delay: 0.5s; animation-duration: 3.5s;">🐱</div>
    <!-- peacock is now just a floating emoji among others and entrance effectively faster since welcome is shorter -->
    <div class="floating-animal" style="top: 16%; left: 18%; animation-delay: 0.2s; animation-duration: 2s; font-size: 4.8rem;">🦚</div>
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

    <!-- Quick JS to show shorter countdown and remove welcome faster -->
    <script>
      (function(){
        const countdown = document.getElementById('countdown');

        function showNumber(number, delay) {
            setTimeout(() => {
                countdown.textContent = number;
                countdown.classList.remove('show');
                void countdown.offsetWidth;
                countdown.classList.add('show');
            }, delay);
        }

        // START: shorter timeline (was longer in the original)
        showNumber('3', 450); // show 3 at 0.45s
        showNumber('2', 600); // 2 at 0.6s
        showNumber('1', 730); // 1 at 0.73s

        // clear countdown sooner
        setTimeout(() => {
            countdown.style.opacity = '0';
            setTimeout(() => { countdown.textContent = ''; }, 300);
        }, 950);

        // remove welcome earlier so content is interactive quickly
        setTimeout(() => {
            const w = document.querySelector('.welcome-screen');
            if (w) w.remove();
        }, 920);
      })();
    </script>
</body>
</html>
"""

# Hide Streamlit's default UI elements (keeps original style from your file)
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp > header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    [data-testid="stToolbar"] {display: none;}
    .stDeployButton {display: none;}
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    .main .block-container {
        padding-top: 0 !important;
    }
    iframe {
        border: none !important;
        display: block;
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw !important;
        height: 100vh !important;
    }
</style>
""", unsafe_allow_html=True)

# Render the HTML using Streamlit components - fullscreen, no border
components.html(html_code, height=1000, scrolling=False)

# Keep Streamlit effects as you had them
st.balloons()
st.snow()
