import re

file_path = "c:/Users/Mounir/Downloads/SGS_IA4NORM/ia-conformite-presentation.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Colors Contrast
content = content.replace("--text2: #8b91a8", "--text2: #b0b5cc")
content = content.replace("--text3: #5a6080", "--text3: #8a93bb")

# 2. Extract font sizes into var(--fs-XX)
# Gather all sizes
sizes = set()

def fs_repl(match):
    size = int(match.group(1))
    sizes.add(size)
    return f"font-size: var(--fs-{size})"

# Process font-size definitions
content = re.sub(r'font-size:\s*(\d+)px', fs_repl, content)

# Process shorthand 'font: 800 30px/1' kinds of definitions
# Example: font: 800 30px/1 'Montserrat',sans-serif;
def font_shorthand_repl(match):
    weight = match.group(1)
    size = int(match.group(2))
    line_height = match.group(3)
    family = match.group(4)
    sizes.add(size)
    return f"font-weight: {weight}; font-size: var(--fs-{size}); line-height: {line_height}; font-family: {family}"

content = re.sub(r'font:\s*(\w+)\s*(\d+)px/(\S+)\s*([^;]+)', font_shorthand_repl, content)

# 3. Generate the CSS Variables for root
var_lines = []
for s in sorted(sizes):
    # Scale algorithm: increase by ~35%
    new_s = int(round(s * 1.35))
    var_lines.append(f"  --fs-{s}: {new_s}px;")

css_vars = "\n".join(var_lines)
root_add = f"\n  /* Centralized Typography Sizes */\n{css_vars}\n"

# Insert inside :root {
content = content.replace(":root {", f":root {{{root_add}")

# 4. Handle min-height to use more space
def mh_repl(match):
    size = int(match.group(1))
    new_size = int(size * 1.45) # Increase height 45%
    return f"min-height: {new_size}px"

content = re.sub(r'min-height:\s*(\d+)px', mh_repl, content)

# Also explicitly override chart height restriction
content = content.replace("canvas { max-height: 220px !important; }", "canvas { max-height: 280px !important; }")

# 5. Add custom CSS for 3D anims and hover effects
custom_css = """
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
"""
content = content.replace("</style>", custom_css + "\n</style>")

# 6. Insert 3D images where appropriate (e.g. Slide 05 / Architectures hybrides and Slide 01 / Cover)
# Let's insert the AI core image in SLIDE 5 (Architectures hybrides) by changing the grid to accommodate it, or just place it above/below.
# We will inject the images using replace. Let's do it after the script runs or carefully here.

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("HTML Transformation Complete!")
