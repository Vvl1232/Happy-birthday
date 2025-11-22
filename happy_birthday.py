# app.py
import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

st.set_page_config(page_title="🎉 Happy Birthday!", layout="wide", initial_sidebar_state="collapsed")

# ---------- Inputs in main area (no sidebar) ----------
name = st.text_input("Who are we celebrating today?", value="Friend", max_chars=60)
birthday = datetime.strptime('13/11/2005', '%d/%m/%Y')

today = datetime.today()
age = today.year - birthday.year - ((today.month, today.day) <= (birthday.month, birthday.day)) + 1

# top header
st.markdown(
    f"<div style='text-align:center; margin-top:8px'>"
    f"<h1 style='margin:0; font-size:2.2rem;'>🎂 Happy Birthday, <span id='celebrant'>{name}</span>! 🎂</h1>"
    f"<h3 style='margin:6px 0 18px 0; color:#FF4FA3'>🥳 {age} years young! 🥳</h3>"
    f"</div>",
    unsafe_allow_html=True
)

# Keep main area wide and occupy top area
st.markdown("<div id='appContainer' style='width:100%; height:calc(100vh - 150px);'></div>", unsafe_allow_html=True)

# High-level JS + HTML injected via components.html
# Replace kittyGif and puppyGif with preferred GIFs if you like.
kittyGif = "https://media.giphy.com/media/12PA1eI8FBqEBa/giphy.gif"
puppyGif = "https://media.giphy.com/media/26FPqut4dLh8q6Jqg/giphy.gif"

html = f"""
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    :root {{
      --bg1: #fff7fb;
      --bg2: #f2fffb;
      --accent: #ff6fa3;
      --accent-2: #6f7bff;
    }}
    html,body{{margin:0;padding:0;height:100%;overflow:hidden;font-family:Inter,Roboto,Arial,Helvetica,sans-serif}}
    #stage {{
      position:relative;
      width:100%;
      height:100%;
      background: linear-gradient(125deg, var(--bg1) 0%, var(--bg2) 100%);
      overflow:hidden;
    }}

    /* central greeting card (transparent so animation can be seen) */
    .greeting-card {{
      position:absolute;
      left:50%;
      top:6%;
      transform:translateX(-50%);
      z-index:40;
      width:min(980px,92%);
      background: rgba(255,255,255,0.85);
      border-radius:18px;
      padding:14px 20px;
      box-shadow:0 12px 36px rgba(0,0,0,0.12);
      text-align:center;
      pointer-events:none;
    }}
    .greeting-card h2{{margin:4px 0; font-size:1.6rem; color:#3b1b3b}}
    .greeting-card p{{margin:2px 0; color:#4a2d4a}}

    /* runner characters container */
    .runner {{
      position:absolute;
      z-index:20;
      display:flex;
      align-items:flex-end;
      pointer-events:auto;
      user-select:none;
    }}
    .runner .char {{
      width:96px;
      height:96px;
      display:block;
      transform-origin:center bottom;
      will-change: transform, left;
      filter: drop-shadow(0 8px 18px rgba(0,0,0,0.18));
      border-radius:12px;
      background-size:cover;
      background-position:center;
    }}
    .runner.small .char {{ width:72px; height:72px; }}
    .runner.tiny .char {{ width:56px; height:56px; }}
    .runner .balloon {{
      position:absolute;
      left:50%;
      transform:translateX(-50%);
      bottom:110%;
      width:48px;
      height:64px;
      pointer-events:none;
      display:flex;
      align-items:center;
      justify-content:center;
    }}
    /* balloon shape using simple svg via background */
    .balloon .string {{
      position:absolute;
      bottom:-14px;
      left:50%;
      width:2px;
      height:28px;
      transform:translateX(-50%);
      background:rgba(80,80,80,0.35);
    }}

    /* keyframe: runner bobbing (creates running illusion with subtle vertical movement) */
    @keyframes bob {{
      0% {{ transform: translateY(0) rotate(-1deg); }}
      50% {{ transform: translateY(-10px) rotate(1deg); }}
      100% {{ transform: translateY(0) rotate(-1deg); }}
    }}

    /* balloon float */
    @keyframes floatBalloon {{
      0% {{ transform: translateY(0) translateX(0) rotate(0deg); }}
      50% {{ transform: translateY(-8px) translateX(4px) rotate(2deg); }}
      100% {{ transform: translateY(0) translateX(0) rotate(0deg); }}
    }}

    /* subtle scale/tilt to give motion */
    .char {{ animation: bob 0.85s ease-in-out infinite; }}

    /* small hover pop */
    .runner:hover .balloon {{ transform: translateY(-12px) translateX(0); }}

    /* decorative top-left & top-right fireworks icons */
    .corner {{
      position:absolute;
      z-index:45;
      width:48px;height:48px;
      top:12px;
      border-radius:12px;
      opacity:0.95;
      pointer-events:none;
    }}
    .corner.left {{ left:12px; }}
    .corner.right {{ right:12px; }}

    /* performance control overlays (hidden) */
    .hidden-controls{{display:none}}

    /* responsive */
    @media(max-width:600px) {{
      .greeting-card h2{{font-size:1.2rem}}
      .runner .char{{width:64px;height:64px}}
    }}
  </style>
</head>
<body>
  <div id="stage" aria-hidden="false">
    <div class="greeting-card" id="gcard" style="pointer-events:none;">
      <h2 id="greeting">Hey <span id="nameSpan">{name}</span> — furry friends are here to celebrate!</h2>
      <p id="ageText">We made this just for you — enjoy the running kitties & puppies with balloons!</p>
    </div>

    <div class="corner left" aria-hidden="true">
      <!-- small svg spark -->
      <svg width="48" height="48" viewBox="0 0 64 64"><circle cx="32" cy="32" r="14" fill="#ffd38b"></circle></svg>
    </div>
    <div class="corner right" aria-hidden="true">
      <svg width="48" height="48" viewBox="0 0 64 64"><circle cx="32" cy="32" r="14" fill="#ff9ad6"></circle></svg>
    </div>
  </div>

  <script>
    /*******************************
     * High-level JS animation:
     * - Spawns kitties and puppies that run horizontally across the stage
     * - Each character has a balloon (varied colors) attached that bobs independently
     * - Characters are recycled (DOM pooled) to limit element counts
     * - Movement uses requestAnimationFrame and transforms for smoothness
     *******************************/

    // Config
    const kittyGif = "{kittyGif}";
    const puppyGif = "{puppyGif}";
    const maxRunners = 12; // active characters at a time
    const spawnInterval = 900; // ms between spawn attempts
    const stage = document.getElementById('stage');
    const stageBounds = () => ({ w: stage.clientWidth, h: stage.clientHeight });

    // name linking (streamlit input updates)
    const nameSpan = document.getElementById('nameSpan');

    // Streamlit will update the displayed top name on rerun but we also add listener for dynamic text
    // (Note: Streamlit re-injects HTML between runs, but this keeps name inline for client interactions)

    // Utility: random number
    function rnd(min, max) { return Math.random() * (max - min) + min; }

    // Pre-create a pool of DOM nodes to recycle
    const pool = [];
    const active = new Set();

    function makeRunnerElement() {{
      const el = document.createElement('div');
      el.className = 'runner';
      // structure: runner -> balloon + char img
      const balloon = document.createElement('div');
      balloon.className = 'balloon';
      balloon.style.animation = `floatBalloon ${2 + Math.random()*2}s ease-in-out infinite`;
      // balloon fill (simple circle)
      balloon.innerHTML = `
        <svg width="48" height="64" viewBox="0 0 48 64" xmlns="http://www.w3.org/2000/svg">
          <ellipse cx="24" cy="22" rx="18" ry="22" fill="${chooseBalloonColor()}" />
        </svg>
        <div class="string"></div>
      `;
      const char = document.createElement('div');
      char.className = 'char';
      el.appendChild(balloon);
      el.appendChild(char);
      // meta
      el._meta = {{
        vx:0, x:0, y:0, direction: 'right', speed:1, size:1, type:'kitty'
      }};
      // make clickable interaction
      el.addEventListener('click', () => {{
        // small burst effect: scale character briefly
        char.animate([
          {{ transform: 'scale(1)' }},
          {{ transform: 'scale(1.15)' }},
          {{ transform: 'scale(1)' }}
        ], {{duration:350, easing:'cubic-bezier(.2,.8,.2,1)'}});
      }});
      el.style.pointerEvents = 'auto';
      return el;
    }}

    function chooseBalloonColor() {{
      const cols = ['#FF7AB6','#FFD38B','#9AFFC9','#9BD3FF','#D7B2FF','#FFB3B3','#BDA6FF'];
      return cols[Math.floor(rnd(0, cols.length))];
    }}

    // initialize pool
    for (let i=0;i<maxRunners;i++) pool.push(makeRunnerElement());

    // spawn logic: configure runner meta and place on stage
    function spawnRunner() {{
      if (active.size >= maxRunners) return;
      const el = pool.pop();
      if (!el) return;
      // randomize type
      const type = Math.random() < 0.52 ? 'kitty' : 'puppy';
      el._meta.type = type;
      // set background image
      const char = el.querySelector('.char');
      char.style.backgroundImage = `url(${type === 'kitty' ? kittyGif : puppyGif})`;

      // random vertical lane (avoid top greeting card area)
      const bounds = stageBounds();
      const topArea = Math.max(120, bounds.h * 0.08); // keep characters below header a bit
      const bottomPad = 28;
      const y = rnd(topArea, bounds.h - 120 - bottomPad);

      // direction left->right or right->left randomly
      const direction = Math.random() < 0.5 ? 'right' : 'left';
      el._meta.direction = direction;

      // speed varies slightly
      const baseSpeed = rnd(0.06, 0.16); // px per ms
      el._meta.speed = baseSpeed;

      // size variations
      const scaleClass = Math.random();
      el.classList.remove('small','tiny');
      if (scaleClass < 0.15) { el.classList.add('tiny'); el._meta.size = 0.7; }
      else if (scaleClass < 0.45) { el.classList.add('small'); el._meta.size = 0.85; }
      else { el._meta.size = 1; }

      // initial x offscreen
      if (direction === 'right') {{
        el._meta.x = -140 - rnd(0,200);
      }} else {{
        el._meta.x = bounds.w + 140 + rnd(0,200);
      }}
      el._meta.y = y;

      // set transform
      el.style.transform = `translate3d(${el._meta.x}px, ${el._meta.y}px, 0) scale(${el._meta.size})`;
      el.style.opacity = '1';

      // attach to DOM
      stage.appendChild(el);
      active.add(el);
    }}

    // movement / recycle logic
    function step(timestamp) {{
      // move each active runner
      for (const el of Array.from(active)) {{
        const meta = el._meta;
        // direction movement
        const sign = meta.direction === 'right' ? 1 : -1;
        // vary speed slightly for a natural effect
        const jitter = Math.sin((performance.now() + (el._jitter||0)) / (1200 + (meta.speed*1000))) * 0.02;
        meta.x += sign * (meta.speed * (1 + jitter)) * 20; // scaling factor

        // update transforms
        el.style.transform = `translate3d(${meta.x}px, ${meta.y}px, 0) scale(${meta.size})`;

        // if offscreen beyond threshold, recycle
        const bounds = stageBounds();
        if ((meta.direction === 'right' && meta.x > bounds.w + 200) || (meta.direction === 'left' && meta.x < -260)) {{
          // remove from DOM and recycle
          active.delete(el);
          try {{ stage.removeChild(el); }} catch(e){}
          // reset some props and push back to pool
          pool.push(el);
        }}
      }}

      // occasionally spawn new runner
      if (!step._lastSpawn) step._lastSpawn = performance.now();
      if (performance.now() - step._lastSpawn > spawnInterval) {{
        // spawn multiple sometimes
        const toSpawn = Math.random() < 0.2 ? 2 : 1;
        for (let i=0;i<toSpawn;i++) spawnRunner();
        step._lastSpawn = performance.now() + rnd(-120, 120);
      }}

      requestAnimationFrame(step);
    }}

    // initial warm-up spawns
    for (let i=0;i<4;i++) setTimeout(spawnRunner, i*220);

    requestAnimationFrame(step);

    // update name text on every short interval (this allows Streamlit re-running to update the nameInput)
    function syncNameFromDOM() {{
      const streamlitName = document.querySelector('#root .stTextInput [role="textbox"]');
      if (streamlitName && streamlitName.value !== undefined) {{
        const val = streamlitName.value.trim() || "{name}";
        nameSpan.textContent = val;
        // also update greeting small text
        const ageText = document.getElementById('ageText');
        if (ageText) ageText.textContent = `Make a wish for ${val} — kitties and puppies are running with balloons!`;
      }}
    }}
    setInterval(syncNameFromDOM, 700);

    // responsive: when stage is resized, reposition existing elements proportionally (simple approach)
    window.addEventListener('resize', () => {{
      // nothing heavy — active elements will continue to animate relative to new width
    }});

    /********* Clean up advice for deployers *********/
    // If you need to reduce activity for low-power devices, reduce `maxRunners` in Python or lower `spawnInterval`.
  </script>
</body>
</html>
"""

components.html(html, height=820, scrolling=False)

# No footer, no extra controls (user requested removal of sidebar & footer)
# Keep a short usage hint just for convenience (displayed as a single small line)
st.markdown(
    "<div style='text-align:center; margin-top:10px; color:#6b2a6f; font-size:0.95rem;'>"
    "Tip: change the character GIFs inside <code>app.py</code> (kittyGif / puppyGif) to use your preferred sprites."
    "</div>",
    unsafe_allow_html=True
)
