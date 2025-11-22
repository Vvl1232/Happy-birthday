# app.py
import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

st.set_page_config(page_title="🎉 Happy Birthday!", layout="wide", initial_sidebar_state="expanded")

# ---------- User inputs ----------
name = st.sidebar.text_input("Enter name to celebrate", value="Friend")
birthday = datetime.strptime('13/11/2005', '%d/%m/%Y')

today = datetime.today()
age = today.year - birthday.year - ((today.month, today.day) <= (birthday.month, birthday.day)) + 1

# ---------- Top message ----------
st.markdown(
    f"<h1 style='text-align:center; margin-top:10px;'>🎂🌹🦚✨ Happy Birthday, {name}! ✨🦚🌹🎂</h1>",
    unsafe_allow_html=True,
)
st.markdown(f"<h3 style='text-align:center; color:#FF1493;'>🥳 {age} years young today! 🥳</h3>", unsafe_allow_html=True)

# Keep Streamlit balloons as fallback
st.balloons()

# ---------- Embedded interactive HTML/CSS/JS ----------
# NOTE: replace kitty_img and puppy_img URLs if you want different ones.
kitty_img = "https://media.giphy.com/media/MLpW0m2fJp7u8/giphy.gif"
puppy_img = "https://media.giphy.com/media/3oEduSbSGpGaRX2Vri/giphy.gif"

html = f"""
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    html, body {{
      margin:0; padding:0; height:100%; overflow:hidden;
      font-family: Inter, Roboto, Arial, sans-serif;
      background: linear-gradient(135deg, #FFF7FB 0%, #F0FFFF 100%);
    }}

    /* central card */
    .card {{
      position: relative;
      z-index: 10;
      max-width: 900px;
      margin: 20px auto;
      background: rgba(255,255,255,0.85);
      border-radius: 18px;
      padding: 28px;
      box-shadow: 0 8px 40px rgba(0,0,0,0.12);
      text-align:center;
    }}
    .message {{
      font-size:1.15rem;
      color:#6b2a6f;
      line-height:1.5;
    }}
    .cta {{
      display:inline-block;
      margin-top:14px;
      padding:10px 18px;
      border-radius:12px;
      background:linear-gradient(90deg,#FF7AB6,#FFB86C);
      color:white;
      font-weight:600;
      cursor:pointer;
      box-shadow: 0 6px 18px rgba(255,122,182,0.25);
    }}

    /* Greeters (kitty/puppy) */
    .greeter {{
      position: fixed;
      z-index: 25;
      width:90px;
      height:90px;
      pointer-events: auto;
      transform-origin: center;
      -webkit-user-select:none;
    }}
    .greeter img {{
      width:100%; height:100%; border-radius:12px;
      box-shadow:0 6px 20px rgba(0,0,0,0.18);
    }}
    .left-bottom {{ left: 12px; bottom: 12px; animation: floaty 4s ease-in-out infinite; }}
    .right-bottom {{ right: 12px; bottom: 12px; animation: floaty 4.2s ease-in-out infinite; }}

    @keyframes floaty {{
      0% {{ transform: translateY(0px) rotate(-3deg); }}
      50% {{ transform: translateY(-12px) rotate(3deg); }}
      100% {{ transform: translateY(0px) rotate(-3deg); }}
    }}

    /* small welcome text bubble */
    .bubble {{
      position: fixed;
      z-index: 26;
      bottom: 110px;
      left: 110px;
      background: rgba(255,255,255,0.92);
      color:#2b2b2b;
      padding:10px 14px;
      border-radius:12px;
      box-shadow:0 6px 18px rgba(0,0,0,0.12);
      font-weight:600;
      display:none;
    }}

    /* make canvas cover full screen but behind UI */
    #fireworksCanvas {{
      position: fixed;
      left:0; top:0; width:100%; height:100%;
      z-index: 1;
      pointer-events: none; /* keep clicks for page */
    }}

    /* little corner 'sparkle' elements for firecrackers icons */
    .corner-spark {{
      position: fixed;
      width: 42px;
      height: 42px;
      z-index: 24;
      opacity: 0.9;
      filter: drop-shadow(0 6px 12px rgba(0,0,0,0.16));
      animation: pop 1.2s ease-in-out infinite;
    }}
    .corner-spark.top-left {{ left: 8px; top: 8px; animation-delay: 0s; }}
    .corner-spark.top-right {{ right: 8px; top: 8px; animation-delay: 0.3s; }}
    .corner-spark.bottom-left {{ left: 8px; bottom: 8px; animation-delay: 0.6s; }}
    .corner-spark.bottom-right {{ right: 8px; bottom: 8px; animation-delay: 0.9s; }}

    @keyframes pop {{
      0% {{ transform: scale(0.82) rotate(-8deg); opacity:.9; }}
      50% {{ transform: scale(1.15) rotate(8deg); opacity:1; }}
      100% {{ transform: scale(0.82) rotate(-8deg); opacity:.9; }}
    }}

    /* confetti strip styles for extra cheer */
    .confetti-piece {{
      position: absolute;
      width: 10px; height: 18px;
      background: linear-gradient(180deg,#fff 0%, #ffd1e6 100%);
      opacity: 0.95;
      transform-origin:center;
      z-index: 5;
      pointer-events:none;
    }}

    /* responsive tweaks */
    @media (max-width: 700px) {{
      .card {{ margin: 10px; padding:18px; }}
      .greeter {{ width:68px; height:68px; }}
    }}
  </style>
</head>
<body>
  <canvas id="fireworksCanvas"></canvas>

  <div class="corner-spark top-left">
    <!-- small SVG firecracker icon -->
    <svg viewBox="0 0 64 64" width="42" height="42">
      <circle cx="32" cy="32" r="14" fill="#ffcd38" />
      <path d="M28 20 L36 12" stroke="#ff6b6b" stroke-width="3" stroke-linecap="round" />
      <path d="M36 52 L28 44" stroke="#ff6b6b" stroke-width="3" stroke-linecap="round" />
    </svg>
  </div>
  <div class="corner-spark top-right">
    <svg viewBox="0 0 64 64" width="42" height="42">
      <circle cx="32" cy="32" r="14" fill="#ff8bd6" />
      <path d="M28 20 L36 12" stroke="#7ad3ff" stroke-width="3" stroke-linecap="round" />
    </svg>
  </div>
  <div class="corner-spark bottom-left">
    <svg viewBox="0 0 64 64" width="42" height="42">
      <circle cx="32" cy="32" r="14" fill="#9affc9" />
      <path d="M36 20 L28 12" stroke="#ff8b5c" stroke-width="3" stroke-linecap="round" />
    </svg>
  </div>
  <div class="corner-spark bottom-right">
    <svg viewBox="0 0 64 64" width="42" height="42">
      <circle cx="32" cy="32" r="14" fill="#ffd38b" />
      <path d="M36 20 L28 12" stroke="#c27bff" stroke-width="3" stroke-linecap="round" />
    </svg>
  </div>

  <!-- kitty and puppy greeters -->
  <div class="greeter left-bottom" id="kitty">
    <img src="{kitty_img}" alt="kitty" />
  </div>
  <div class="greeter right-bottom" id="puppy">
    <img src="{puppy_img}" alt="puppy" />
  </div>

  <div class="bubble" id="bubble">Hi {name}! We're so happy — tap the cake! 🎉</div>

  <div class="card" id="card">
    <h2 style="margin-bottom:6px;">Surprise! 🎊</h2>
    <p class="message">
      Today is your day — we filled the corners with fireworks, and some furry friends came to say hello.
      Click <span class="cta" id="speakBtn">🎂 Play Greeting</span> to hear a short message.
    </p>
  </div>

  <script>
    // ---------- Canvas fireworks (continuous at edges/corners) ----------
    const canvas = document.getElementById('fireworksCanvas');
    const ctx = canvas.getContext('2d');
    let W = canvas.width = window.innerWidth;
    let H = canvas.height = window.innerHeight;
    window.addEventListener('resize', () => {{
      W = canvas.width = window.innerWidth;
      H = canvas.height = window.innerHeight;
    }});

    // particles array
    const particles = [];

    function rand(min, max) {{ return Math.random()*(max-min)+min; }}
    function hueRandom() {{ return Math.floor(rand(0, 360)); }}

    // particle constructor
    function Particle(x, y, vx, vy, hue) {{
      this.x = x; this.y = y;
      this.vx = vx; this.vy = vy;
      this.life = 60 + Math.floor(rand(0,80));
      this.age = 0;
      this.hue = hue;
      this.size = rand(1.6, 4.2);
    }}

    Particle.prototype.update = function() {{
      this.x += this.vx;
      this.y += this.vy;
      this.vy += 0.04; // gravity
      this.vx *= 0.995;
      this.vy *= 0.995;
      this.age++;
    }}

    Particle.prototype.draw = function(ctx) {{
      ctx.beginPath();
      ctx.globalCompositeOperation = 'lighter';
      ctx.fillStyle = 'hsla(' + this.hue + ', 85%, 60%, ' + (1 - this.age/this.life) + ')';
      ctx.arc(this.x, this.y, this.size, 0, Math.PI*2);
      ctx.fill();
    }}

    function spawnFireworkFromEdge(edge) {{
      // edges: "top","bottom","left","right","topleft","topright","bottomleft","bottomright"
      let x, y;
      const padding = 30;
      switch(edge) {{
        case 'top': x = rand(0, W); y = -padding; break;
        case 'bottom': x = rand(0, W); y = H + padding; break;
        case 'left': x = -padding; y = rand(0, H); break;
        case 'right': x = W + padding; y = rand(0, H); break;
        case 'topleft': x = -padding; y = -padding; break;
        case 'topright': x = W + padding; y = -padding; break;
        case 'bottomleft': x = -padding; y = H + padding; break;
        case 'bottomright': x = W + padding; y = H + padding; break;
        default: x = rand(0, W); y = -padding;
      }}
      // aim roughly toward center with some variation
      const cx = W/2 + rand(-W*0.12, W*0.12);
      const cy = H/2 + rand(-H*0.12, H*0.12);
      const dx = cx - x, dy = cy - y;
      const dist = Math.sqrt(dx*dx + dy*dy);
      const speed = rand(3.6, 6.4);
      const vx = (dx/dist)*speed + rand(-0.6,0.6);
      const vy = (dy/dist)*speed + rand(-0.6,0.6);

      // create 'explosion' leader: travel then explode into many particles
      const leader = {{
        x, y, vx, vy, hue: hueRandom(), travel: 20 + Math.floor(rand(0,30)), step:0
      }};
      leaders.push(leader);
    }}

    const leaders = [];

    function step() {{
      ctx.clearRect(0,0,W,H);
      // spawn occasional leaders from random edges/corners
      if (Math.random() < 0.16) {{
        const edges = ['top','bottom','left','right','topleft','topright','bottomleft','bottomright'];
        spawnFireworkFromEdge(edges[Math.floor(rand(0, edges.length))]);
      }}

      // update leaders
      for (let i = leaders.length-1; i >=0; i--) {{
        const L = leaders[i];
        L.x += L.vx; L.y += L.vy;
        L.vx *= 0.995; L.vy *= 0.995;
        L.step++;
        // draw leader spark
        ctx.beginPath();
        ctx.fillStyle = 'hsla('+L.hue+', 90%, 60%, 1)';
        ctx.arc(L.x, L.y, 2.6, 0, Math.PI*2);
        ctx.fill();

        // trail effect
        for (let t = 0; t < 2; t++) {{
          particles.push(new Particle(L.x + rand(-2,2), L.y + rand(-2,2), (Math.random()-0.5)*0.8, (Math.random()-0.5)*0.8, L.hue));
        }}

        if (L.step > L.travel) {{
          // explode into many particles
          const count = 28 + Math.floor(rand(0,40));
          for (let k=0;k<count;k++) {{
            const angle = Math.random()*Math.PI*2;
            const speed = rand(1.6, 6.6);
            const vx = Math.cos(angle)*speed;
            const vy = Math.sin(angle)*speed;
            particles.push(new Particle(L.x, L.y, vx, vy, L.hue + rand(-30,30)));
          }}
          leaders.splice(i,1);
        }}
      }}

      // update and draw particles
      for (let i = particles.length-1; i >=0; i--) {{
        const p = particles[i];
        p.update();
        p.draw(ctx);
        if (p.age > p.life) particles.splice(i,1);
      }}

      requestAnimationFrame(step);
    }}
    step();

    // ---------- confetti pieces (light decorative falling confetti) ----------
    (function createConfetti(){{
      const colours = ['#FF7AB6','#FFD38B','#9AFFC9','#9BD3FF','#D7B2FF'];
      for (let i=0; i<32; i++) {{
        const el = document.createElement('div');
        el.className = 'confetti-piece';
        el.style.left = Math.random()*100 + '%';
        el.style.top = (-Math.random()*30 - 5) + 'vh';
        el.style.width = (8 + Math.random()*8) + 'px';
        el.style.height = (12 + Math.random()*12) + 'px';
        el.style.background = colours[Math.floor(Math.random()*colours.length)];
        el.style.transform = 'rotate(' + (Math.random()*360) + 'deg)';
        document.body.appendChild(el);
        // animate falling
        const duration = 8000 + Math.random()*12000;
        el.animate([
          {{ transform: 'translateY(0) rotate(0deg)', opacity: 1 }},
          {{ transform: 'translateY(120vh) rotate(540deg)', opacity: 0.1 }}
        ], {{
          duration: duration,
          iterations: Infinity,
          delay: Math.random()*4000
        }});
      }}
    }})();

    // ---------- Kitty & Puppy interactions ----------
    const kitty = document.getElementById('kitty');
    const puppy = document.getElementById('puppy');
    const bubble = document.getElementById('bubble');

    kitty.addEventListener('mouseenter', ()=>{{ bubble.style.display = 'block'; bubble.textContent = 'Meow! Happy Birthday, {name}! 🐱' }});
    kitty.addEventListener('mouseleave', ()=>{{ bubble.style.display = 'none'; }});
    puppy.addEventListener('mouseenter', ()=>{{ bubble.style.display = 'block'; bubble.textContent = 'Woof! Hugs and cake for {name}! 🐶' }});
    puppy.addEventListener('mouseleave', ()=>{{ bubble.style.display = 'none'; }});

    // ---------- Play greeting audio + speak using Web Speech API ----------
    document.getElementById('speakBtn').addEventListener('click', async ()=>{{
      // a short TTS greeting (if browser supports)
      const message = `Happy Birthday, {name}! Wishing you a day full of joy, cake, and unforgettable moments.`;
      if ('speechSynthesis' in window) {{
        const u = new SpeechSynthesisUtterance(message);
        u.rate = 1;
        u.pitch = 1;
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(u);
      }} else {{
        alert('Happy Birthday, {name}! (Your browser does not support speech synthesis.)');
      }}
      // show spark burst at center
      for (let i=0;i<18;i++) {{
        const hue = Math.floor(Math.random()*360);
        for (let k=0;k<10;k++) {{
          particles.push(new Particle(window.innerWidth/2 + rand(-10,10), window.innerHeight/2 + rand(-10,10), rand(-6,6), rand(-6,6), hue));
        }}
      }}
    }});

    // allow clicking the kitty or puppy to trigger small bursts
    [kitty, puppy].forEach(node => {{
      node.addEventListener('click', ()=>{{
        for (let i=0;i<10;i++) {{
          const sx = node.getBoundingClientRect().left + node.offsetWidth/2;
          const sy = node.getBoundingClientRect().top + node.offsetHeight/2;
          for (let k=0;k<12;k++) {{
            particles.push(new Particle(sx + rand(-6,6), sy + rand(-6,6), rand(-6,6), rand(-6,6), hueRandom()));
          }}
        }}
      }});
    }});

    // small helper used in event handlers
    function rand(min,max){{ return Math.random()*(max-min)+min; }}
    function hueRandom(){{ return Math.floor(rand(0,360)); }}

  </script>
</body>
</html>
"""

components.html(html, height=820, scrolling=False)

# ---------- Extra footer text and tips ----------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#6b2a6f;'>"
    "Tip: replace kitty/puppy GIF URLs in the script if you want different ones. "
    "To publish, push this file to your GitHub and deploy on Streamlit Cloud or run locally with <code>streamlit run app.py</code>."
    "</div>", unsafe_allow_html=True
)
