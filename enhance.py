#!/usr/bin/env python3
"""
enhance.py — SGS IA & Conformité
Refonte visuelle : glassmorphism, icônes géantes, correction des débordements.
"""
import re

with open('ia-conformite-presentation.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ════════════════════════════════════════════════════════════
# 1. REMPLACE le bloc <style> entier par une version améliorée
# ════════════════════════════════════════════════════════════

OLD_STYLE_END = """/* --- 3D and Animations Added --- */
.card, .flip-card {
  transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.4s ease, border-color 0.2s, background 0.2s;
}
.card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 15px 35px rgba(0,0,0,0.4);
  border-color: var(--accent);
}
.flip-card:hover .fci {
  box-shadow: 0 15px 35px rgba(0,0,0,0.4);
  border-color: var(--accent);
}

.slide.active .card, .slide.active .flip-card, .slide.active .timeline-item {
  animation: slideFadeUp 0.6s cubic-bezier(0.2, 0.8, 0.2, 1) both;
}

/* Staggering based on simple DOM order */
.slide.active > div:nth-child(1) { animation-delay: 0.05s; }
.slide.active > div:nth-child(2) { animation-delay: 0.1s; }
.slide.active > div:nth-child(3) { animation-delay: 0.15s; }
.slide.active .flip-grid-2 > div:nth-child(even), 
.slide.active .flip-grid-3 > div:nth-child(3n+2),
.slide.active .grid-2 > div:nth-child(even) { animation-delay: 0.15s; }
.slide.active .flip-grid-3 > div:nth-child(3n+3) { animation-delay: 0.25s; }

@keyframes slideFadeUp {
  0% { opacity: 0; transform: translateY(30px) scale(0.97); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}

/* 3D Image styling */
.img-3d {
  width: 100%;
  max-width: 450px;
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.1);
  animation: float 6s ease-in-out infinite;
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-12px); }
  100% { transform: translateY(0px); }
}


/* --- 3D and Animations Added --- */
.card, .flip-card {
  transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.4s ease, border-color 0.2s, background 0.2s;
}
.card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 15px 35px rgba(0,0,0,0.4);
  border-color: var(--accent);
}
.flip-card:hover .fci {
  box-shadow: 0 15px 35px rgba(0,0,0,0.4);
  border-color: var(--accent);
}

.slide.active .card, .slide.active .flip-card, .slide.active .timeline-item {
  animation: slideFadeUp 0.6s cubic-bezier(0.2, 0.8, 0.2, 1) both;
}

/* Staggering based on simple DOM order */
.slide.active > div:nth-child(1) { animation-delay: 0.05s; }
.slide.active > div:nth-child(2) { animation-delay: 0.1s; }
.slide.active > div:nth-child(3) { animation-delay: 0.15s; }
.slide.active .flip-grid-2 > div:nth-child(even), 
.slide.active .flip-grid-3 > div:nth-child(3n+2),
.slide.active .grid-2 > div:nth-child(even) { animation-delay: 0.15s; }
.slide.active .flip-grid-3 > div:nth-child(3n+3) { animation-delay: 0.25s; }

@keyframes slideFadeUp {
  0% { opacity: 0; transform: translateY(30px) scale(0.97); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}

/* 3D Image styling */
.img-3d {
  width: 100%;
  max-width: 450px;
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.1);
  animation: float 6s ease-in-out infinite;
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-12px); }
  100% { transform: translateY(0px); }
}

</style>"""

NEW_STYLE_END = """/* ══════════════════════════════════════════════
   WOW EFFECTS — Glassmorphism + 3D + Animations
   ══════════════════════════════════════════════ */

/* Card & flip-card transitions */
.card, .flip-card {
  transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1),
              box-shadow 0.35s ease, border-color 0.2s, background 0.2s;
}
.card:hover {
  transform: translateY(-6px) scale(1.015);
  box-shadow: 0 18px 40px rgba(0,0,0,0.45), 0 0 0 1px rgba(243,112,33,0.2);
  border-color: rgba(243,112,33,0.4);
}
.flip-card:hover .fc-front {
  box-shadow: 0 18px 40px rgba(0,0,0,0.45), 0 0 20px rgba(243,112,33,0.08);
}

/* Slide entry animation */
.slide.active .card,
.slide.active .flip-card,
.slide.active .timeline-item,
.slide.active .kpi-card,
.slide.active .norm-card,
.slide.active .flow-step,
.slide.active .rm-phase {
  animation: slideFadeUp 0.5s cubic-bezier(0.2, 0.8, 0.2, 1) both;
}
.slide.active > *:nth-child(1) { animation-delay: 0.00s; }
.slide.active > *:nth-child(2) { animation-delay: 0.06s; }
.slide.active > *:nth-child(3) { animation-delay: 0.12s; }
.slide.active > *:nth-child(4) { animation-delay: 0.18s; }
.slide.active .flip-grid-2 > *:nth-child(1),
.slide.active .flip-grid-3 > *:nth-child(1),
.slide.active .grid-2 > *:nth-child(1),
.slide.active .grid-3 > *:nth-child(1),
.slide.active .grid-4 > *:nth-child(1) { animation-delay: 0.04s; }
.slide.active .flip-grid-2 > *:nth-child(2),
.slide.active .flip-grid-3 > *:nth-child(2),
.slide.active .grid-2 > *:nth-child(2),
.slide.active .grid-3 > *:nth-child(2),
.slide.active .grid-4 > *:nth-child(2) { animation-delay: 0.10s; }
.slide.active .flip-grid-3 > *:nth-child(3),
.slide.active .grid-3 > *:nth-child(3),
.slide.active .grid-4 > *:nth-child(3) { animation-delay: 0.16s; }
.slide.active .grid-4 > *:nth-child(4) { animation-delay: 0.22s; }

@keyframes slideFadeUp {
  0%   { opacity: 0; transform: translateY(24px) scale(0.97); }
  100% { opacity: 1; transform: translateY(0)   scale(1); }
}

/* ── Glassmorphism on flip-card front ── */
.fc-front {
  background: linear-gradient(
    145deg,
    rgba(29, 35, 64, 0.95) 0%,
    rgba(22, 27, 46, 0.85) 100%
  ) !important;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.08) !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.07),
    0 8px 32px rgba(0,0,0,0.3);
}
.fc-front:hover {
  background: linear-gradient(
    145deg,
    rgba(32, 40, 72, 0.98) 0%,
    rgba(26, 32, 58, 0.92) 100%
  ) !important;
  border-color: rgba(243,112,33,0.25) !important;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.10),
    0 12px 40px rgba(0,0,0,0.4),
    0 0 30px rgba(243,112,33,0.06);
}

/* ── Giant circular icon with glow-pulse ── */
.fc-icon {
  width: 90px !important;
  height: 90px !important;
  border-radius: 50% !important;
  background: rgba(243,112,33,0.12) !important;
  border: 1.5px solid rgba(243,112,33,0.25) !important;
  box-shadow: 0 0 20px rgba(243,112,33,0.2), inset 0 0 15px rgba(243,112,33,0.05) !important;
  font-size: 2rem !important;
  color: var(--accent) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-shrink: 0 !important;
  animation: iconGlow 3s ease-in-out infinite !important;
  transition: transform 0.3s ease, box-shadow 0.3s ease !important;
  margin-bottom: 4px;
}
.fc-front:hover .fc-icon {
  transform: scale(1.08) translateY(-2px);
  box-shadow: 0 0 30px rgba(243,112,33,0.35), inset 0 0 20px rgba(243,112,33,0.08) !important;
}

/* Icon color variants */
[style*="color:var(--amber)"] ~ .fc-icon,
.fc-icon[style*="color:var(--amber)"] {
  background: rgba(245,158,11,0.12) !important;
  border-color: rgba(245,158,11,0.25) !important;
  box-shadow: 0 0 20px rgba(245,158,11,0.2), inset 0 0 15px rgba(245,158,11,0.05) !important;
}
.fc-icon[style*="color:var(--green)"] {
  background: rgba(16,185,129,0.12) !important;
  border-color: rgba(16,185,129,0.25) !important;
  box-shadow: 0 0 20px rgba(16,185,129,0.2) !important;
}
.fc-icon[style*="color:var(--red)"] {
  background: rgba(239,68,68,0.12) !important;
  border-color: rgba(239,68,68,0.25) !important;
  box-shadow: 0 0 20px rgba(239,68,68,0.2) !important;
}
.fc-icon[style*="color:var(--cyan)"] {
  background: rgba(6,182,212,0.12) !important;
  border-color: rgba(6,182,212,0.25) !important;
  box-shadow: 0 0 20px rgba(6,182,212,0.2) !important;
}

@keyframes iconGlow {
  0%, 100% { box-shadow: 0 0 20px rgba(243,112,33,0.20), inset 0 0 15px rgba(243,112,33,0.05); }
  50%       { box-shadow: 0 0 35px rgba(243,112,33,0.38), inset 0 0 22px rgba(243,112,33,0.10); }
}

/* ── Shimmer sweep on card hover ── */
.fc-front::after, .card::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(
    105deg,
    transparent 35%,
    rgba(255,255,255,0.04) 50%,
    transparent 65%
  );
  background-size: 200% 100%;
  background-position: -100% 0;
  transition: background-position 0.6s ease;
  pointer-events: none;
}
.fc-front:hover::after, .card:hover::after {
  background-position: 200% 0;
}
.fc-front { position: relative; overflow: hidden; }
.card      { position: relative; overflow: hidden; }

/* ── KPI card glassmorphism ── */
.kpi-card {
  background: linear-gradient(135deg, rgba(22,27,46,0.9) 0%, rgba(17,21,32,0.8) 100%) !important;
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,0.07) !important;
  border-top: 2px solid var(--accent) !important;
  box-shadow: 0 4px 24px rgba(0,0,0,0.25);
  transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}
.kpi-card:hover {
  transform: translateY(-4px) scale(1.02);
  box-shadow: 0 12px 32px rgba(0,0,0,0.4), 0 0 0 1px rgba(243,112,33,0.15);
}

/* ── 3D Image float ── */
.img-3d {
  width: 100%;
  max-width: 450px;
  border-radius: 16px;
  box-shadow: 0 20px 50px rgba(0,0,0,0.6), inset 0 0 0 1px rgba(255,255,255,0.08);
  animation: float 6s ease-in-out infinite;
  transition: box-shadow 0.3s ease;
}
.img-3d:hover {
  box-shadow: 0 28px 60px rgba(0,0,0,0.7), 0 0 40px rgba(243,112,33,0.12);
}
@keyframes float {
  0%   { transform: translateY(0px) rotate(0deg); }
  33%  { transform: translateY(-8px) rotate(0.3deg); }
  66%  { transform: translateY(-4px) rotate(-0.3deg); }
  100% { transform: translateY(0px) rotate(0deg); }
}

/* ── Cover particle canvas ── */
#particleCanvas {
  position: absolute; inset: 0; z-index: 0;
  pointer-events: none; opacity: 0.5;
}

/* ── KPI counter animation ── */
.kpi-val { transition: transform 0.3s ease; }
.kpi-val.updating { transform: scale(1.15); color: var(--accent); }

/* ── Slide fc-back glassmorphism ── */
.fc-back {
  background: linear-gradient(
    145deg,
    rgba(25, 31, 56, 0.97) 0%,
    rgba(19, 24, 42, 0.93) 100%
  ) !important;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(243,112,33,0.20) !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.06), 0 8px 32px rgba(0,0,0,0.4) !important;
}

/* ── Norm card glow on hover ── */
.norm-card:hover {
  box-shadow: 0 8px 30px rgba(0,0,0,0.4), 0 0 0 1px rgba(243,112,33,0.15);
  border-color: rgba(243,112,33,0.3) !important;
  transform: translateY(-3px);
}

/* ── Flow step premium ── */
.flow-step {
  background: linear-gradient(135deg, rgba(22,27,46,0.9), rgba(17,21,32,0.8)) !important;
  backdrop-filter: blur(6px);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.flow-step:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 28px rgba(0,0,0,0.4);
}

</style>"""

if OLD_STYLE_END in html:
    html = html.replace(OLD_STYLE_END, NEW_STYLE_END)
    print("✅ Bloc CSS WOW remplacé avec succès")
else:
    print("❌ ERREUR: bloc CSS non trouvé (attention aux espaces/sauts de ligne)")

# ════════════════════════════════════════════════════════════
# 2. RÉDUIT le padding de .slide-area
# ════════════════════════════════════════════════════════════
html = html.replace(
    '.slide-area { flex: 1; overflow-y: auto; padding: 36px 48px 48px; }',
    '.slide-area { flex: 1; overflow-y: auto; padding: 18px 30px 22px; }'
)
print("✅ Padding slide-area réduit")

# ════════════════════════════════════════════════════════════
# 3. RÉDUIT la marge du .slide-header
# ════════════════════════════════════════════════════════════
html = html.replace(
    '.slide-header { margin-bottom: 28px; }',
    '.slide-header { margin-bottom: 12px; }'
)
print("✅ Marge slide-header réduite")

# ════════════════════════════════════════════════════════════
# 4. RÉDUIT min-height des flip-cards globalement
# ════════════════════════════════════════════════════════════
html = html.replace(
    """.flip-card {
  cursor: pointer;
  perspective: 1200px;
  min-height: 440px;
}
.flip-card .fci {
  position: relative;
  width: 100%; min-height: 440px;
  transition: transform 0.55s cubic-bezier(0.4,0,0.2,1);
  transform-style: preserve-3d;
}""",
    """.flip-card {
  cursor: pointer;
  perspective: 1200px;
  min-height: 280px;
}
.flip-card .fci {
  position: relative;
  width: 100%; min-height: 280px;
  transition: transform 0.55s cubic-bezier(0.4,0,0.2,1);
  transform-style: preserve-3d;
}"""
)
print("✅ min-height flip-card réduit (440 -> 280)")

html = html.replace(
    """.fc-front, .fc-back {
  position: absolute; top: 0; left: 0;
  width: 100%; min-height: 440px;""",
    """.fc-front, .fc-back {
  position: absolute; top: 0; left: 0;
  width: 100%; min-height: 280px;"""
)
print("✅ min-height fc-front/fc-back réduit")

# Grille 2 colonnes
html = html.replace(
    '.flip-grid-2 .flip-card,\n.flip-grid-2 .flip-card .fci,\n.flip-grid-2 .fc-front,\n.flip-grid-2 .fc-back { min-height: 398px; }',
    '.flip-grid-2 .flip-card,\n.flip-grid-2 .flip-card .fci,\n.flip-grid-2 .fc-front,\n.flip-grid-2 .fc-back { min-height: 300px; }'
)
print("✅ min-height flip-grid-2 réduit (398 -> 300)")

# Grille 3 colonnes
html = html.replace(
    '.flip-grid-3 .flip-card,\n.flip-grid-3 .flip-card .fci,\n.flip-grid-3 .fc-front,\n.flip-grid-3 .fc-back { min-height: 420px; }',
    '.flip-grid-3 .flip-card,\n.flip-grid-3 .flip-card .fci,\n.flip-grid-3 .fc-front,\n.flip-grid-3 .fc-back { min-height: 260px; }'
)
print("✅ min-height flip-grid-3 réduit (420 -> 260)")

# ════════════════════════════════════════════════════════════
# 5. COVER: réduire min-height et amélioration
# ════════════════════════════════════════════════════════════
html = html.replace(
    '.cover-hero {\n  min-height: 75vh; display: flex; align-items: center; justify-content: space-between; gap: 40px;\n  position: relative;\n}',
    '.cover-hero {\n  min-height: auto; display: flex; align-items: center; justify-content: space-between; gap: 32px;\n  position: relative; padding: 8px 0 16px;\n}'
)
print("✅ Cover-hero hauteur réduite")

# Réduire couverture title
html = html.replace(
    '.cover-h1 {\n  font-family: \'Montserrat\', sans-serif; font-size: var(--fs-54); font-weight: 700; line-height: 1.08;\n  color: var(--text); margin-bottom: 20px;\n}',
    '.cover-h1 {\n  font-family: \'Montserrat\', sans-serif; font-size: var(--fs-42); font-weight: 700; line-height: 1.1;\n  color: var(--text); margin-bottom: 14px;\n}'
)
print("✅ Cover-h1 taille réduite")

html = html.replace(
    '.cover-sub { font-size: var(--fs-17); color: var(--text2); max-width: 640px; line-height: 1.65; margin-bottom: 30px; }',
    '.cover-sub { font-size: var(--fs-14); color: var(--text2); max-width: 600px; line-height: 1.55; margin-bottom: 18px; }'
)
print("✅ Cover-sub taille réduite")

html = html.replace(
    '.cover-tags { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 36px; }',
    '.cover-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; }'
)
print("✅ Cover-tags marge réduite")

# ════════════════════════════════════════════════════════════
# 6. SLIDE 02: Supprimer l'image qui fait déborder
# ════════════════════════════════════════════════════════════
old_img_slide02 = """      <div style="margin-top:20px; text-align:center;">
        <img src="9ljjUGl0.jpg" alt="Vision AR en usine" class="img-3d" style="width:100%; max-width:800px; max-height:350px; object-fit:cover;">
      </div>

    </div>

    <!-- SLIDE 03 -->"""

new_img_slide02 = """
    </div>

    <!-- SLIDE 03 -->"""

if old_img_slide02 in html:
    html = html.replace(old_img_slide02, new_img_slide02)
    print("✅ Image débordante slide 02 supprimée")
else:
    print("⚠️  Image slide 02 non trouvée (possiblement déjà supprimée)")

# ════════════════════════════════════════════════════════════
# 7. SLIDE 03: Réduire les min-height inline 630px -> 420px
# ════════════════════════════════════════════════════════════
html = html.replace(
    'style="min-height: 630px"',
    'style="min-height: 420px"'
)
print("✅ Inline min-height 630px réduit à 420px")

# ════════════════════════════════════════════════════════════
# 8. SLIDE 10 (Audit): Réduire min-height dos inline 630px
# ════════════════════════════════════════════════════════════
html = html.replace(
    'style="min-height: 630px;border-color',
    'style="min-height: 340px;border-color'
)
print("✅ Inline min-height dos cartes LLM/Code réduit à 340px")

# ════════════════════════════════════════════════════════════
# 9. SLIDE-h1 font réduite légèrement pour éviter overflow
# ════════════════════════════════════════════════════════════
html = html.replace(
    '.slide-h1 {\n  font-family: \'Montserrat\', sans-serif;\n  font-size: var(--fs-42); font-weight: 700;\n  color: var(--text); line-height: 1.1;\n  margin-bottom: 10px;\n}',
    '.slide-h1 {\n  font-family: \'Montserrat\', sans-serif;\n  font-size: var(--fs-30); font-weight: 700;\n  color: var(--text); line-height: 1.1;\n  margin-bottom: 8px;\n}'
)
print("✅ slide-h1 réduit (--fs-42 -> --fs-30)")

html = html.replace(
    '.slide-desc { font-size: var(--fs-14); color: var(--text2); max-width: 720px; line-height: 1.65; }',
    '.slide-desc { font-size: var(--fs-13); color: var(--text2); max-width: 720px; line-height: 1.55; margin-bottom: 2px; }'
)
print("✅ slide-desc taille réduite")

# ════════════════════════════════════════════════════════════
# 10. Ajouter canvas particules dans le header cover
# ════════════════════════════════════════════════════════════
html = html.replace(
    '      <div class="cover-hero">\n        <div class="cover-bg"></div>',
    '      <div class="cover-hero">\n        <canvas id="particleCanvas"></canvas>\n        <div class="cover-bg"></div>'
)
print("✅ Canvas particules ajouté sur la couverture")

# ════════════════════════════════════════════════════════════
# 11. AJOUT JS: Particules + compteur KPI animé
# ════════════════════════════════════════════════════════════
OLD_JS_END = """navItems.forEach((item, i) => item.addEventListener('click', () => goTo(i)));

document.addEventListener('keydown', e => {"""

NEW_JS_END = """navItems.forEach((item, i) => item.addEventListener('click', () => goTo(i)));

/* ── Particle canvas on cover slide ── */
(function initParticles() {
  const canvas = document.getElementById('particleCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const particles = [];
  const COUNT = 55;

  function resize() {
    canvas.width  = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  for (let i = 0; i < COUNT; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      r: Math.random() * 1.8 + 0.4,
      dx: (Math.random() - 0.5) * 0.4,
      dy: (Math.random() - 0.5) * 0.4,
      alpha: Math.random() * 0.5 + 0.1
    });
  }

  function drawParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(243,112,33,${p.alpha})`;
      ctx.fill();
      p.x += p.dx; p.y += p.dy;
      if (p.x < 0 || p.x > canvas.width)  p.dx *= -1;
      if (p.y < 0 || p.y > canvas.height) p.dy *= -1;
    });
    // Draw faint lines between nearby particles
    for (let i = 0; i < COUNT; i++) {
      for (let j = i+1; j < COUNT; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const d  = Math.sqrt(dx*dx + dy*dy);
        if (d < 100) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(243,112,33,${0.08 * (1 - d/100)})`;
          ctx.lineWidth = 0.5;
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(drawParticles);
  }
  drawParticles();
})();

/* ── KPI counter animation ── */
function animateCounters(slideEl) {
  slideEl.querySelectorAll('.kpi-val').forEach(el => {
    const text = el.textContent.trim();
    const match = text.match(/^([×\\-+]?)(\\d+(?:\\.\\d+)?)(.*)/);
    if (!match) return;
    const prefix = match[1], num = parseFloat(match[2]), suffix = match[3];
    let start = null;
    const duration = 900;
    function step(ts) {
      if (!start) start = ts;
      const progress = Math.min((ts - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.round(eased * num * 10) / 10;
      el.textContent = prefix + (Number.isInteger(num) ? Math.round(current) : current.toFixed(1)) + suffix;
      if (progress < 1) requestAnimationFrame(step);
      else el.textContent = text;
    }
    requestAnimationFrame(step);
  });
}

const _origGoTo = goTo;
function goTo(n) {
  _origGoTo(n);
  const slide = slides[n];
  setTimeout(() => animateCounters(slide), 120);
}
// Animate on first load
setTimeout(() => animateCounters(slides[0]), 300);

document.addEventListener('keydown', e => {"""

if OLD_JS_END in html:
    html = html.replace(OLD_JS_END, NEW_JS_END)
    print("✅ JS particules + compteur KPI ajouté")
else:
    print("❌ JS target non trouvé")

# ════════════════════════════════════════════════════════════
# 12. Fix fc-icon dans la fc-back : icônes alignées dans les listes
# ════════════════════════════════════════════════════════════
# Enlever le ::before arrow sur les check-lists dans fc-back si une icône FA est déjà là
html = html.replace(
    'ul.check-list li::before { content: \'→\'; color: var(--accent); font-weight: 700; flex-shrink: 0; margin-top: 1px; }',
    'ul.check-list li::before { content: \'→\'; color: var(--accent); font-weight: 700; flex-shrink: 0; margin-top: 1px; }\n.fc-back ul.check-list li::before { display: none; }'
)
print("✅ Arrow supprimé dans fc-back check-list (icônes FA déjà présentes)")

# ════════════════════════════════════════════════════════════
# 13. Réduire quelques gaps dans les grilles pour gagner de la hauteur
# ════════════════════════════════════════════════════════════
html = html.replace(
    '.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }',
    '.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }'
)
html = html.replace(
    '.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }',
    '.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }'
)
html = html.replace(
    '.grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }',
    '.grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }'
)
html = html.replace(
    '.flip-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }',
    '.flip-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }'
)
html = html.replace(
    '.flip-grid-3 { display: grid; grid-template-columns: repeat(3,1fr); gap: 14px; }',
    '.flip-grid-3 { display: grid; grid-template-columns: repeat(3,1fr); gap: 10px; }'
)
print("✅ Gaps de grilles réduits")

# ════════════════════════════════════════════════════════════
# Écriture du fichier final
# ════════════════════════════════════════════════════════════
with open('ia-conformite-presentation.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n🎉 Fichier ia-conformite-presentation.html mis à jour avec succès !")
