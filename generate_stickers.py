import os, subprocess

OUTPUT_DIR = "/home/graha/tixdesk-expo-stickers"
SVG_DIR = os.path.join(OUTPUT_DIR, "assets", "svg")
PNG_DIR = os.path.join(OUTPUT_DIR, "assets", "png")
CUTLINE_DIR = os.path.join(OUTPUT_DIR, "assets", "print-ready-cutlines")
PDF_DIR = os.path.join(OUTPUT_DIR, "print-pdfs")

for d in [SVG_DIR, PNG_DIR, CUTLINE_DIR, PDF_DIR]:
    os.makedirs(d, exist_ok=True)

# ==============================================================================
# STICKER 1: THE PURE HERO DIE-CUT (FLAWLESS REVISION)
# Standalone, clean, no description, solid white T, smooth uniform die-cut contour
# ==============================================================================
svg_01 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 450" width="500" height="450">
  <defs>
    <linearGradient id="brandGrad01" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6" />
      <stop offset="50%" stop-color="#1D9BF0" />
      <stop offset="100%" stop-color="#06B6D4" />
    </linearGradient>
  </defs>

  <g transform="translate(250, 210)">
    <!-- 1. SOLID WHITE DIE-CUT BASE CONTOUR -->
    <path d="
      M 0 -110
      L 122 -110
      A 28 28 0 0 1 150 -82
      L 150 -30
      A 20 20 0 0 0 150 10
      L 150 62
      A 28 28 0 0 1 122 90
      L -45 90
      L -72 140
      L -100 90
      L -122 90
      A 28 28 0 0 1 -150 62
      L -150 10
      A 20 20 0 0 0 -150 -30
      L -150 -82
      A 28 28 0 0 1 -122 -110
      Z
    " fill="#FFFFFF" stroke="#FFFFFF" stroke-width="26" stroke-linejoin="round" stroke-linecap="round" />

    <!-- 2. FULL TICKET BODY INCLUDING TAIL (Colored with Blue/Cyan Gradient) -->
    <path d="
      M 0 -110
      L 122 -110
      A 28 28 0 0 1 150 -82
      L 150 -30
      A 20 20 0 0 0 150 10
      L 150 62
      A 28 28 0 0 1 122 90
      L -45 90
      L -72 140
      L -100 90
      L -122 90
      A 28 28 0 0 1 -150 62
      L -150 10
      A 20 20 0 0 0 -150 -30
      L -150 -82
      A 28 28 0 0 1 -122 -110
      Z
    " fill="url(#brandGrad01)" />

    <!-- 3. SOLID WHITE 'T' INSIDE (Floating cleanly, perfectly centered) -->
    <path d="
      M -52 -65
      L 52 -65
      A 17.5 17.5 0 0 1 52 -30
      L 18 -30
      L 18 56
      Q 18 64, 10 64
      L -10 64
      Q -18 64, -18 56
      L -18 -30
      L -52 -30
      A 17.5 17.5 0 0 1 -52 -65
      Z
    " fill="#FFFFFF" />
  </g>
</svg>'''

cutline_01 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 450" width="500" height="450">
  <g id="CutContour" transform="translate(250, 210)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
    <path d="
      M 0 -110
      L 122 -110
      A 28 28 0 0 1 150 -82
      L 150 -30
      A 20 20 0 0 0 150 10
      L 150 62
      A 28 28 0 0 1 122 90
      L -45 90
      L -72 140
      L -100 90
      L -122 90
      A 28 28 0 0 1 -150 62
      L -150 10
      A 20 20 0 0 0 -150 -30
      L -150 -82
      A 28 28 0 0 1 -122 -110
      Z
    " stroke-width="26" />
  </g>
</svg>'''

# ==============================================================================
# STICKER 2: TIXIE THE CYBER-BOT MASCOT (ENHANCED EDITION)
# Standalone, clean, no description, kawaii chibi helpdesk companion
# ==============================================================================
svg_02 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">
  <defs>
    <linearGradient id="headGrad02" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6" />
      <stop offset="50%" stop-color="#1D9BF0" />
      <stop offset="100%" stop-color="#06B6D4" />
    </linearGradient>

    <linearGradient id="screenGrad02" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#080E1E" />
      <stop offset="100%" stop-color="#111C35" />
    </linearGradient>

    <linearGradient id="bodyGrad02" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#E2E8F0" />
    </linearGradient>
  </defs>

  <g transform="translate(300, 290) rotate(-2)">
    <!-- 1. SOLID WHITE DIE-CUT BASE CONTOUR -->
    <g fill="#FFFFFF" stroke="#FFFFFF" stroke-linejoin="round" stroke-linecap="round">
      <rect x="-185" y="-160" width="370" height="240" rx="55" stroke-width="36" />
      <polygon points="-180,40 -180,135 -95,50" stroke-width="36" />
      <line x1="0" y1="-150" x2="0" y2="-235" stroke-width="46" />
      <circle cx="0" cy="-235" r="35" />
      <rect x="-230" y="-75" width="60" height="95" rx="25" stroke-width="28" />
      <rect x="170" y="-75" width="60" height="95" rx="25" stroke-width="28" />
      <path d="M -195 0 C -195 110, -85 135, -45 95" stroke-width="32" />
      <circle cx="-40" cy="95" r="25" />
      <ellipse cx="0" cy="145" rx="110" ry="85" stroke-width="32" />
      <circle cx="-115" cy="90" r="35" stroke-width="28" />
      <rect x="85" y="75" width="75" height="100" rx="15" stroke-width="32" transform="rotate(15 120 125)" />
    </g>

    <!-- 2. ANTENNA -->
    <path d="M 0 -150 L 0 -220" stroke="#64748B" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#10B981" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#6EE7B7" />

    <!-- 3. FLOATING CHIBI BODY -->
    <g transform="translate(0, 140)">
      <polygon points="-25,50 25,50 0,95" fill="#06B6D4" />
      <polygon points="-15,50 15,50 0,80" fill="#FFFFFF" />

      <ellipse cx="0" cy="20" rx="80" ry="58" fill="url(#bodyGrad02)" stroke="#94A3B8" stroke-width="4" />
      
      <path d="M -72 25 Q 0 45 72 25" fill="none" stroke="#0EA5E9" stroke-width="8" stroke-linecap="round" />
      
      <circle cx="0" cy="15" r="18" fill="#2563EB" stroke="#FFFFFF" stroke-width="2.5" />
      <text x="0" y="22" font-family="'Noto Sans', system-ui, sans-serif" font-size="20" font-weight="900" fill="#FFFFFF" text-anchor="middle">T</text>

      <!-- Left Hand Waving -->
      <g transform="translate(-80, -5)">
        <path d="M 0 10 C -25 5, -45 -15, -35 -40" fill="none" stroke="#CBD5E1" stroke-width="22" stroke-linecap="round" />
        <circle cx="-35" cy="-40" r="16" fill="#FFFFFF" stroke="#94A3B8" stroke-width="3.5" />
      </g>

      <!-- Right Hand holding ticket -->
      <g transform="translate(80, 5)">
        <path d="M 0 10 C 25 15, 35 25, 30 40" fill="none" stroke="#CBD5E1" stroke-width="22" stroke-linecap="round" />
        <g transform="translate(35, 15) rotate(15)">
          <rect x="-26" y="-36" width="52" height="72" rx="8" fill="#FEF08A" stroke="#EAB308" stroke-width="3" />
          <circle cx="-26" cy="0" r="8" fill="#CBD5E1" />
          <circle cx="26" cy="0" r="8" fill="#CBD5E1" />
          <line x1="-14" y1="-18" x2="14" y2="-18" stroke="#CA8A04" stroke-width="3" stroke-linecap="round" />
          <line x1="-14" y1="-8" x2="14" y2="-8" stroke="#CA8A04" stroke-width="2.5" stroke-linecap="round" />
          <path d="M -10 12 L -2 20 L 12 6" fill="none" stroke="#16A34A" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" />
        </g>
      </g>
    </g>

    <!-- 4. HEAD -->
    <g>
      <path d="
        M -160 -150
        Q -160 -160, -140 -160
        L 140 -160
        Q 160 -160, 160 -140
        L 160 -40
        A 25 25 0 0 0 160 10
        L 160 50
        Q 160 70, 140 70
        L -90 70
        L -160 120
        L -160 10
        A 25 25 0 0 0 -160 -40
        Z
      " fill="url(#headGrad02)" stroke="#1D4ED8" stroke-width="2.5" />

      <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGrad02)" stroke="#38BDF8" stroke-width="4" />

      <path d="M -115 -105 Q 0 -125 115 -105 L 115 -90 Q 0 -110 -115 -90 Z" fill="#FFFFFF" opacity="0.24" />

      <g transform="translate(-55, -45)">
        <ellipse cx="0" cy="0" rx="24" ry="30" fill="#38BDF8" />
        <ellipse cx="0" cy="0" rx="20" ry="26" fill="#0284C7" />
        <circle cx="-7" cy="-10" r="8" fill="#FFFFFF" />
        <circle cx="8" cy="10" r="4.5" fill="#FFFFFF" />
        <polygon points="-7,4 -5,7 -2,7 -4,9 -3,12 -6,10 -9,12 -8,9 -10,7 -7,7" fill="#E0F2FE" />
      </g>

      <g transform="translate(55, -45)">
        <ellipse cx="0" cy="0" rx="24" ry="30" fill="#38BDF8" />
        <ellipse cx="0" cy="0" rx="20" ry="26" fill="#0284C7" />
        <circle cx="-7" cy="-10" r="8" fill="#FFFFFF" />
        <circle cx="8" cy="10" r="4.5" fill="#FFFFFF" />
        <polygon points="-7,4 -5,7 -2,7 -4,9 -3,12 -6,10 -9,12 -8,9 -10,7 -7,7" fill="#E0F2FE" />
      </g>

      <ellipse cx="-75" cy="-5" rx="14" ry="8" fill="#F43F5E" opacity="0.8" />
      <ellipse cx="75" cy="-5" rx="14" ry="8" fill="#F43F5E" opacity="0.8" />

      <path d="M -16 -4 Q -8 8 0 0 Q 8 8 16 -4" fill="none" stroke="#38BDF8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />
    </g>

    <!-- 5. HEADSET -->
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#1E293B" stroke-width="22" stroke-linecap="round" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#38BDF8" stroke-width="8" stroke-linecap="round" />

    <rect x="-210" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="-200" y="-70" width="25" height="55" rx="12" fill="#1E293B" />

    <rect x="165" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="175" y="-70" width="25" height="55" rx="12" fill="#1E293B" />

    <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke="#1E293B" stroke-width="10" stroke-linecap="round" />
    <circle cx="-70" cy="73" r="14" fill="#10B981" stroke="#FFFFFF" stroke-width="4" />
    <circle cx="-70" cy="73" r="6" fill="#6EE7B7" />
  </g>
</svg>'''

cutline_02 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">
  <g id="CutContour" transform="translate(300, 290) rotate(-2)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
    <rect x="-185" y="-160" width="370" height="240" rx="55" stroke-width="36" />
    <polygon points="-180,40 -180,135 -95,50" stroke-width="36" />
    <line x1="0" y1="-150" x2="0" y2="-235" stroke-width="46" />
    <circle cx="0" cy="-235" r="35" />
    <rect x="-230" y="-75" width="60" height="95" rx="25" stroke-width="28" />
    <rect x="170" y="-75" width="60" height="95" rx="25" stroke-width="28" />
    <path d="M -195 0 C -195 110, -85 135, -45 95" stroke-width="32" />
    <circle cx="-40" cy="95" r="25" />
    <ellipse cx="0" cy="145" rx="110" ry="85" stroke-width="32" />
    <circle cx="-115" cy="90" r="35" stroke-width="28" />
    <rect x="85" y="75" width="75" height="100" rx="15" stroke-width="32" transform="rotate(15 120 125)" />
  </g>
</svg>'''

# ==============================================================================
# STICKER 3: RETRO 16-BIT ARCADE GAMER (ENHANCED EDITION)
# Standalone, clean, no description, uniform pixel grid, 100% SLA hearts & banner
# ==============================================================================
svg_03 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">
  <g transform="translate(300, 300)">
    <!-- 1. DIE-CUT WHITE BACKING CONTOUR -->
    <path d="
      M -200 -195
      L 200 -195
      L 200 -60
      L 165 -60
      L 165 20
      L 200 20
      L 200 135
      L 40 135
      L -40 215
      L -125 215
      L -125 135
      L -200 135
      L -200 20
      L -165 20
      L -165 -60
      L -200 -60
      Z
    " fill="#FFFFFF" stroke="#FFFFFF" stroke-width="45" stroke-linejoin="round" />

    <g fill="#FFFFFF" stroke="#FFFFFF" stroke-width="26" stroke-linejoin="round">
      <rect x="-145" y="-250" width="60" height="55" rx="8" />
      <rect x="-30" y="-260" width="60" height="55" rx="8" />
      <rect x="85" y="-250" width="60" height="55" rx="8" />
    </g>

    <rect x="-185" y="200" width="370" height="60" rx="16" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="28" stroke-linejoin="round" />

    <!-- 2. FLOATING 8-BIT HEARTS -->
    <g transform="translate(-115, -225) scale(3.5)">
      <path d="M -4 -2 H -1 V 1 H -4 Z M 1 -2 H 4 V 1 H 1 Z M -3 1 H 3 V 3 H -3 Z M -2 3 H 2 V 4 H -2 Z M -1 4 H 1 V 5 H -1 Z" fill="#EF4444" />
      <rect x="-3" y="-1" width="1" height="1" fill="#FECACA" />
    </g>
    <g transform="translate(0, -235) scale(4.2)">
      <path d="M -4 -2 H -1 V 1 H -4 Z M 1 -2 H 4 V 1 H 1 Z M -3 1 H 3 V 3 H -3 Z M -2 3 H 2 V 4 H -2 Z M -1 4 H 1 V 5 H -1 Z" fill="#EF4444" />
      <rect x="-3" y="-1" width="1" height="1" fill="#FECACA" />
    </g>
    <g transform="translate(115, -225) scale(3.5)">
      <path d="M -4 -2 H -1 V 1 H -4 Z M 1 -2 H 4 V 1 H 1 Z M -3 1 H 3 V 3 H -3 Z M -2 3 H 2 V 4 H -2 Z M -1 4 H 1 V 5 H -1 Z" fill="#EF4444" />
      <rect x="-3" y="-1" width="1" height="1" fill="#FECACA" />
    </g>

    <!-- 3. MAIN PIXEL TICKET (Dual-tone Blue/Cyan) -->
    <rect x="-175" y="-160" width="350" height="270" fill="#2563EB" />
    <rect x="0" y="-160" width="175" height="270" fill="#06B6D4" />
    <rect x="-35" y="-160" width="35" height="270" fill="#0284C7" />

    <rect x="-205" y="-45" width="55" height="55" fill="#FFFFFF" />
    <rect x="150" y="-45" width="55" height="55" fill="#FFFFFF" />
    
    <polygon points="-160,110 -160,195 -80,110" fill="#2563EB" />
    <polygon points="-130,110 -160,195 -95,110" fill="#1D4ED8" />

    <!-- 4. PIXEL SUNGLASSES ('DEAL WITH IT' RETRO VIBE) -->
    <g transform="translate(0, -50)">
      <rect x="-125" y="-20" width="105" height="45" fill="#0F172A" />
      <rect x="20" y="-20" width="105" height="45" fill="#0F172A" />
      <rect x="-20" y="-10" width="40" height="18" fill="#0F172A" />

      <rect x="-110" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="-92" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="35" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="53" y="4" width="14" height="14" fill="#FFFFFF" />

      <rect x="-20" y="60" width="40" height="12" fill="#0F172A" />
      <rect x="-12" y="72" width="24" height="12" fill="#0F172A" />
      <rect x="-80" y="40" width="24" height="12" fill="#F43F5E" />
      <rect x="56" y="40" width="24" height="12" fill="#F43F5E" />
    </g>

    <!-- 5. RETRO ARCADE BANNER -->
    <g transform="translate(0, 215)">
      <rect x="-170" y="-18" width="340" height="42" fill="#0F172A" stroke="#38BDF8" stroke-width="3" />
      <rect x="-170" y="-18" width="6" height="6" fill="#FFFFFF" />
      <rect x="164" y="-18" width="6" height="6" fill="#FFFFFF" />
      <rect x="-170" y="18" width="6" height="6" fill="#FFFFFF" />
      <rect x="164" y="18" width="6" height="6" fill="#FFFFFF" />

      <text x="0" y="10" font-family="'Noto Sans Mono', monospace" font-size="20" font-weight="900" letter-spacing="3" fill="#38BDF8" text-anchor="middle">★ SLA SAVED: 100% ★</text>
    </g>

    <!-- 6. XP BAR -->
    <g transform="translate(0, 85)">
      <rect x="-85" y="0" width="170" height="12" fill="#0F172A" />
      <rect x="-82" y="2" width="164" height="8" fill="#22C55E" />
    </g>
  </g>
</svg>'''

cutline_03 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">
  <g id="CutContour" transform="translate(300, 300)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round">
    <path d="
      M -200 -195
      L 200 -195
      L 200 -60
      L 165 -60
      L 165 20
      L 200 20
      L 200 135
      L 40 135
      L -40 215
      L -125 215
      L -125 135
      L -200 135
      L -200 20
      L -165 20
      L -165 -60
      L -200 -60
      Z
    " />
    <rect x="-145" y="-250" width="60" height="55" rx="8" />
    <rect x="-30" y="-260" width="60" height="55" rx="8" />
    <rect x="85" y="-250" width="60" height="55" rx="8" />
    <rect x="-185" y="200" width="370" height="60" rx="16" />
  </g>
</svg>'''

items = [
    ("tixdesk-sticker-01-hero-mark", svg_01, cutline_01),
    ("tixdesk-sticker-02-mascot-tixie", svg_02, cutline_02),
    ("tixdesk-sticker-03-retro-pixel-arcade", svg_03, cutline_03),
]

for base_name, svg_content, cutline_content in items:
    # 1. Master SVG
    svg_file = os.path.join(SVG_DIR, f"{base_name}.svg")
    with open(svg_file, "w") as f:
        f.write(svg_content)
    
    # 2. Transparent 300 DPI PNG
    png_file = os.path.join(PNG_DIR, f"{base_name}-300dpi.png")
    subprocess.run(["rsvg-convert", "-z", "2.0", svg_file, "-o", png_file])

    # 3. Cutline SVG
    cutline_file = os.path.join(CUTLINE_DIR, f"{base_name}-cutline.svg")
    with open(cutline_file, "w") as f:
        f.write(cutline_content)

    # 4. Print-ready PDF
    pdf_file = os.path.join(PDF_DIR, f"{base_name}-print.pdf")
    subprocess.run(["rsvg-convert", "-f", "pdf", cutline_file, "-o", pdf_file])

print("Final 3 stickers generated successfully!")
