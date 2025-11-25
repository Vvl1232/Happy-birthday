import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="wide")

html_code = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Happy Birthday!</title>
<style>
  :root{
    --bg-a: #0f172a;
    --grad-1: #6b8ef6;
    --grad-2: #8b5cf6;
    --glass: rgba(255,255,255,0.08);
    --glass-2: rgba(255,255,255,0.06);
    --text: #ffffff;
    --muted: rgba(255,255,255,0.75);
    --ease: cubic-bezier(.22,.98,.38,.98); /* smooth */
  }
  html,body,#root{height:100%;margin:0;}
  body{
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    background: radial-gradient(1200px 700px at 10% 10%, rgba(139,92,246,0.12), transparent 12%),
                radial-gradient(900px 600px at 90% 90%, rgba(107,142,246,0.12), transparent 12%),
                linear-gradient(135deg,#09112a 0%, #0f172a 100%);
    color:var(--text);
    overflow:hidden;
  }

  /* Layout */
  .stage{
    position:relative;
    width:100vw;
    height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    padding:6vh 6vw;
    box-sizing:border-box;
    --card-w: min(920px, 92%);
  }

  .hero {
    width:var(--card-w);
    max-height:84vh;
    border-radius:20px;
    padding:48px;
    box-sizing:border-box;
    background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
    border: 1px solid rgba(255,255,255,0.04);
    backdrop-filter: blur(8px) saturate(1.05);
    box-shadow: 0 15px 50px rgba(3,7,18,0.6);
    display:grid;
    grid-template-columns: 1fr 420px;
    gap:32px;
    align-items:center;
    transform: translate3d(0,40px,0);
    opacity:0;
    transition: transform 900ms var(--ease), opacity 900ms var(--ease);
  }

  /* reveal */
  .hero.ready{ transform: translate3d(0,0,0); opacity:1; }

  .content h1{
    margin:0 0 16px 0;
    font-size: clamp(28px, 4.8vw, 44px);
    line-height:1.02;
    letter-spacing:-0.02em;
    background: linear-gradient(90deg,var(--grad-1),var(--grad-2));
    -webkit-background-clip:text; background-clip:text; color:transparent;
    font-weight:800;
  }
  .content p.lead{
    margin:0 0 18px 0;
    color:var(--muted);
    font-size: clamp(14px, 1.7vw, 18px);
    max-width: 54ch;
  }
  .content .cta{
    display:inline-flex;
    gap:12px;
    align-items:center;
    margin-top:6px;
  }
  .btn{
    background: linear-gradient(90deg,var(--grad-1),var(--grad-2));
    color:white;
    padding:10px 16px;
    border-radius:12px;
    border:none;
    font-weight:600;
    cursor:pointer;
    transform: translateZ(0);
    transition: transform 180ms ease, box-shadow 180ms ease;
    box-shadow: 0 6px 24px rgba(107,92,246,0.18);
  }
  .btn:active{ transform: translateY(1px) scale(0.997); box-shadow: 0 4px 14px rgba(107,92,246,0.12); }

  /* Right panel - hero illustration and countdown */
  .panel{
    width:100%;
    height:100%;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    gap:18px;
    position:relative;
  }
  .card{
    width:100%;
    border-radius:16px;
    padding:20px;
    box-sizing:border-box;
    background: linear-gradient(180deg,var(--glass), var(--glass-2));
    border:1px solid rgba(255,255,255,0.03);
    display:flex;
    align-items:center;
    justify-content:center;
    min-height:220px;
  }

  /* countdown number */
  .count{
    font-weight:900;
    font-size: clamp(46px, 9.5vw, 94px);
    color: var(--grad-2);
    -webkit-text-stroke: 0px rgba(0,0,0,0.1);
    transform-origin:center;
    transition: transform 450ms var(--ease);
    will-change: transform;
  }

  /* small caption */
  .muted{
    color:var(--muted);
    font-size:13px;
  }

  /* canvas covers stage for particles, pointer events none */
  #particle-canvas{
    position:fixed;
    left:0; top:0;
    width:100vw; height:100vh;
    pointer-events:none;
    z-index:8;
    mix-blend-mode: screen;
  }

  /* subtle parallax layer for hero icon */
  .hero-figure{
    width:100%;
    height:100%;
    display:flex;
    align-items:center;
    justify-content:center;
    transform: translate3d(0,0,0);
    will-change: transform;
    pointer-events:none;
  }

  /* small responsive tweaks */
  @media (max-width:980px){
    .hero{ grid-template-columns: 1fr; padding:28px; gap:18px; }
    .panel{ order:-1; }
  }
  @media (max-width:520px){
    .hero{ padding:18px; border-radius:12px; }
    .card{ min-height:160px; padding:14px; }
  }

  /* Reduce motion respect */
  @media (prefers-reduced-motion: reduce){
    .hero{ transition:none; }
    .count{ transition:none; }
    #particle-canvas{ display:none; }
  }
</style>
</head>
<body>
<canvas id="particle-canvas"></canvas>

<div class="stage">
  <div class="hero" id="hero">
    <div class="content">
      <h1>🎂 Happy Birthday — a tiny surprise just for you</h1>
      <p class="lead">Wishing you a day of sweet moments and joyful memories. This page focuses on smooth motion, subtle depth and crisp visuals — optimized to feel fluid like modern product sites.</p>
      <div class="cta">
        <button class="btn" id="openBtn">Open Surprise</button>
        <div class="muted">Tap anywhere to pause the particles</div>
      </div>
    </div>

    <div class="panel">
      <div class="card" id="card">
        <!-- centerpiece: crisp SVG + graceful gradient -->
        <div class="hero-figure" id="figure">
          <svg width="240" height="220" viewBox="0 0 240 220" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden>
            <defs>
              <linearGradient id="g1" x1="0" x2="1" y1="0" y2="1">
                <stop offset="0" stop-color="#6b8ef6" />
                <stop offset="1" stop-color="#8b5cf6" />
              </linearGradient>
              <filter id="glow" x="-40%" y="-40%" width="200%" height="200%">
                <feGaussianBlur stdDeviation="8" result="b"/>
                <feBlend in="SourceGraphic" in2="b"/>
              </filter>
            </defs>

            <!-- stylized cake (SVG) -->
            <g filter="url(#glow)">
              <rect x="32" y="88" width="176" height="60" rx="12" fill="url(#g1)" opacity="0.95"/>
              <rect x="48" y="62" width="144" height="32" rx="10" fill="#fff" opacity="0.06"/>
              <g transform="translate(0,-8)">
                <path d="M120 30c-10 0-18 8-18 18h36c0-10-8-18-18-18z" fill="#ffd6e8" opacity="0.9" />
                <!-- candles -->
                <g transform="translate(84,28)">
                  <rect x="6" y="-18" width="4" height="18" rx="2" fill="#ffdd57"/>
                  <rect x="34" y="-18" width="4" height="18" rx="2" fill="#ffdd57"/>
                </g>
              </g>
            </g>

            <!-- small stars -->
            <g opacity="0.9">
              <circle cx="38" cy="36" r="3" fill="#fff" opacity="0.7"/>
              <circle cx="210" cy="42" r="4" fill="#fff" opacity="0.6"/>
            </g>
          </svg>
        </div>
      </div>

      <div style="display:flex; flex-direction:column; align-items:center; gap:8px; margin-top:6px;">
        <div class="count" id="count">✨</div>
        <div class="muted">Get ready…</div>
      </div>
    </div>
  </div>
</div>

<script>
  // Wait until DOM paint; reveal hero with smooth transform
  requestAnimationFrame(()=> {
    document.getElementById('hero').classList.add('ready');
  });

  // ===== Smooth particle/confetti using canvas + requestAnimationFrame =====
  const canvas = document.getElementById('particle-canvas');
  const ctx = canvas.getContext('2d');
  let W = canvas.width = innerWidth;
  let H = canvas.height = innerHeight;
  let particles = [];
  let running = true;

  function rand(min,max){ return Math.random()*(max-min)+min; }

  class P {
    constructor(){
      this.reset();
    }
    reset(){
      this.x = rand(0, W);
      this.y = rand(-H*0.2, H);
      this.vx = rand(-0.3, 0.3);
      this.vy = rand(0.6, 2.6);
      this.size = rand(6,18);
      this.h = rand(0,360);
      this.a = rand(0.6, 1);
      this.life = rand(80, 320);
      this.t = 0;
      this.swing = rand(0.5, 2);
    }
    step(){
      this.t++;
      this.x += this.vx + Math.sin(this.t/20)*this.swing*0.3;
      this.y += this.vy;
      if(this.y > H+40 || this.t > this.life){ this.reset(); this.y = -20; }
    }
    draw(ctx){
      ctx.save();
      ctx.translate(this.x, this.y);
      ctx.rotate(this.t/100);
      // subtle gradient fill for depth
      const g = ctx.createLinearGradient(-this.size/2, -this.size/2, this.size/2, this.size/2);
      g.addColorStop(0, `hsla(${this.h},75%,60%, ${this.a})`);
      g.addColorStop(1, `hsla(${(this.h+40)%360},70%,40%, ${this.a*0.9})`);
      ctx.fillStyle = g;
      // use rounded rectangle for confetti-like shape (fast)
      const s = this.size;
      ctx.beginPath();
      ctx.roundRect = ctx.roundRect || function(x,y,w,h,r){
        if (w < 2*r) r = w/2;
        if (h < 2*r) r = h/2;
        this.moveTo(x+r,y);
        this.arcTo(x+w,y,x+w,y+h,r);
        this.arcTo(x+w,y+h,x,y+h,r);
        this.arcTo(x,y+h,x,y,r);
        this.arcTo(x,y,x+w,y,r);
      };
      ctx.roundRect(-s/2, -s/2, s, s, 3);
      ctx.fill();
      ctx.restore();
    }
  }

  function initParticles(n=90){
    particles = [];
    for(let i=0;i<n;i++) particles.push(new P());
  }
  initParticles(110);

  function step(){
    if(!running) return;
    ctx.clearRect(0,0,W,H);
    for(let i=0;i<particles.length;i++){
      const p = particles[i];
      p.step();
      p.draw(ctx);
    }
    requestAnimationFrame(step);
  }
  step();

  // resize
  window.addEventListener('resize', ()=> {
    W = canvas.width = innerWidth;
    H = canvas.height = innerHeight;
  });

  // toggle animation on click/tap
  window.addEventListener('pointerdown', ()=>{
    running = !running;
    if(running) step();
  });

  // small parallax on mouse move for the SVG hero
  const heroFigure = document.getElementById('figure');
  window.addEventListener('mousemove', (e)=>{
    const x = (e.clientX - innerWidth/2) / innerWidth;
    const y = (e.clientY - innerHeight/2) / innerHeight;
    heroFigure.style.transform = `translate3d(${x*8}px, ${y*8}px, 0) rotate(${x*2}deg) scale(1.01)`;
  });

  // simple countdown effect: 3..2..1 then reveal message
  const count = document.getElementById('count');
  const openBtn = document.getElementById('openBtn');

  function playCountdown(){
    const seq = ['3','2','1','🎉'];
    let idx = 0;
    const tick = ()=> {
      count.style.transform = 'scale(1.15) translateZ(0)';
      count.textContent = seq[idx++];
      setTimeout(()=>{
        count.style.transform = 'scale(1) translateZ(0)';
      }, 320);
      if(idx < seq.length) setTimeout(tick, 900);
      else {
        // small confetti blast: boost particle velocities briefly
        particles.forEach(p => { p.vy *= 0.6; p.vx += (Math.random()-0.5)*2; p.h = Math.random()*360; });
      }
    };
    tick();
  }

  // event handlers
  openBtn.addEventListener('click', playCountdown);
  // also auto-trigger once the page is ready, with slight delay for reveal
  setTimeout(playCountdown, 1600);

  // accessibility: stop animation on reduce-motion
  if(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    running = false;
    canvas.style.display = 'none';
  }
</script>
</body>
</html>
"""

# Hide Streamlit UI like before, but simplified and compatible
st.markdown("""
<style>
    #MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stHeader"] {visibility: hidden !important;}
    .block-container{padding:0 !important;max-width:100% !important;}
    iframe{border:none !important; display:block; position:fixed; top:0; left:0; width:100vw !important; height:100vh !important;}
</style>
""", unsafe_allow_html=True)

# Render full-screen HTML
components.html(html_code, height=900, scrolling=False)

# keep a Streamlit visual effect (optional)
st.snow()
