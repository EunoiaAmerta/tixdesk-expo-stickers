import os, subprocess

OUTPUT_DIR = "/home/graha/tixdesk-expo-stickers"
SVG_DIR = os.path.join(OUTPUT_DIR, "assets", "svg")
PNG_DIR = os.path.join(OUTPUT_DIR, "assets", "png")
CUTLINE_DIR = os.path.join(OUTPUT_DIR, "assets", "print-ready-cutlines")
PDF_DIR = os.path.join(OUTPUT_DIR, "print-pdfs")

for d in [SVG_DIR, PNG_DIR, CUTLINE_DIR, PDF_DIR]:
    os.makedirs(d, exist_ok=True)

# ==============================================================================
# STICKER 1: THE PURE HERO DIE-CUT (Approved by Darling)
# ==============================================================================
path_d = ("M106.07 258.81 L104.23 262.5 L103.61 264.65 L103.61 265.87 L103.31 266.18 "
          "L103.31 293.52 L103 293.83 L103 296.29 L103.31 297.21 L106.69 298.13 "
          "L109.76 299.66 L110.99 300.59 L114.98 304.89 L117.13 309.8 L117.13 311.03 "
          "L117.44 311.34 L117.44 315.64 L117.13 315.94 L117.13 317.48 L116.52 319.32 "
          "L114.06 323.62 L110.68 327 L109.76 327.31 L108.22 328.54 L105.46 329.46 "
          "L104.54 329.46 L103.31 330.08 L103.31 360.49 L103.61 360.79 L103.92 363.25 "
          "L105.76 367.55 L107.61 370.01 L110.68 372.77 L116.21 375.54 L119.59 375.84 "
          "L119.89 376.15 L144.78 376.15 L145.39 376.46 L146.01 377.38 L146.01 405.03 "
          "L147.23 406.56 L149.08 406.87 L150.92 405.95 L177.34 379.22 L180.1 376.15 "
          "L180.72 374.92 L180.72 301.81 L179.79 300.28 L144.78 300.28 L143.24 299.66 "
          "L142.63 299.05 L142.01 297.51 L142.01 279.7 L142.63 278.16 L143.55 277.24 "
          "L144.47 277.24 L144.78 276.93 L245.22 276.93 L245.53 277.24 L246.45 277.24 "
          "L247.68 278.47 L247.68 279.39 L247.99 279.7 L247.99 297.82 L247.68 298.74 "
          "L246.15 299.97 L244.61 299.97 L244.3 300.28 L209.9 300.28 L208.98 301.51 "
          "L208.98 374.92 L209.59 375.84 L210.51 376.15 L270.72 376.15 L271.03 375.84 "
          "L272.87 375.84 L277.48 374 L280.55 371.85 L283.62 368.47 L285.46 365.09 "
          "L286.69 360.79 L286.69 330.08 L286.08 329.46 L282.09 328.54 L278.4 326.08 "
          "L275.63 323.32 L274.1 320.86 L272.87 317.79 L272.87 316.25 L272.56 315.94 "
          "L272.56 311.03 L272.87 310.72 L272.87 309.8 L274.1 306.42 L275.63 303.96 "
          "L280.24 299.66 L283.31 298.13 L286.08 297.51 L286.69 296.9 L286.69 265.57 "
          "L285.46 261.57 L283.62 258.2 L282.39 256.66 L279.32 253.89 L275.02 251.74 "
          "L274.1 251.74 L272.87 251.13 L271.03 251.13 L270.72 250.82 L120.51 250.82 "
          "L120.2 251.13 L117.74 251.13 L113.14 252.67 L109.76 254.82 Z")

svg_sticker_01 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 260" width="300" height="260">
  <defs>
    <linearGradient id="tixGrad01" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6" />
      <stop offset="60%" stop-color="#0EA5E9" />
      <stop offset="100%" stop-color="#06B6D4" />
    </linearGradient>
  </defs>
  <g transform="translate(150, 130) scale(1.15) translate(-194.845, -328.845)">
    <!-- White Die-Cut Contour -->
    <path d="{path_d}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="26" stroke-linejoin="round" stroke-linecap="round" />
    <!-- Official Master Logo Path -->
    <path d="{path_d}" fill="url(#tixGrad01)" />
  </g>
</svg>'''

# ==============================================================================
# STICKER 2: MASCOT CHIBI BOT - "TIXIE THE SUPPORT BOT"
# ==============================================================================
svg_sticker_02 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">
  <defs>
    <linearGradient id="headGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6" />
      <stop offset="50%" stop-color="#1D9BF0" />
      <stop offset="100%" stop-color="#06B6D4" />
    </linearGradient>

    <linearGradient id="visorGrad2" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#070D1E" />
      <stop offset="100%" stop-color="#131F38" />
    </linearGradient>

    <linearGradient id="bodyGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#E2E8F0" />
    </linearGradient>
  </defs>

  <g transform="translate(300, 290) rotate(-3)">
    <!-- WHITE DIE-CUT BASE CONTOUR -->
    <g fill="#FFFFFF" stroke="#FFFFFF" stroke-linejoin="round" stroke-linecap="round">
      <rect x="-185" y="-165" width="370" height="245" rx="55" stroke-width="36" />
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

    <!-- ANTENNA -->
    <path d="M 0 -150 L 0 -220" stroke="#64748B" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#10B981" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#6EE7B7" />

    <!-- FLOATING CHIBI BODY -->
    <g transform="translate(0, 140)">
      <!-- Thruster flame -->
      <polygon points="-25,50 25,50 0,95" fill="#06B6D4" />
      <polygon points="-15,50 15,50 0,80" fill="#FFFFFF" />

      <!-- Body Pod with subtle shadow border -->
      <ellipse cx="0" cy="20" rx="80" ry="58" fill="url(#bodyGrad2)" stroke="#94A3B8" stroke-width="4" />
      
      <!-- Cyan belly stripe -->
      <path d="M -72 25 Q 0 45 72 25" fill="none" stroke="#0EA5E9" stroke-width="8" stroke-linecap="round" />
      
      <!-- Center Emblem: T logo -->
      <circle cx="0" cy="15" r="18" fill="#2563EB" stroke="#FFFFFF" stroke-width="2" />
      <text x="0" y="22" font-family="'Noto Sans', system-ui, sans-serif" font-size="20" font-weight="900" fill="#FFFFFF" text-anchor="middle">T</text>

      <!-- Left Hand Waving -->
      <g transform="translate(-80, -5)">
        <path d="M 0 10 C -25 5, -45 -15, -35 -40" fill="none" stroke="#CBD5E1" stroke-width="22" stroke-linecap="round" />
        <circle cx="-35" cy="-40" r="16" fill="#FFFFFF" stroke="#94A3B8" stroke-width="3" />
      </g>

      <!-- Right Hand holding ticket -->
      <g transform="translate(80, 5)">
        <path d="M 0 10 C 25 15, 35 25, 30 40" fill="none" stroke="#CBD5E1" stroke-width="22" stroke-linecap="round" />
        <!-- Golden Resolved Ticket -->
        <g transform="translate(35, 15) rotate(15)">
          <rect x="-25" y="-35" width="50" height="70" rx="8" fill="#FEF08A" stroke="#EAB308" stroke-width="3" />
          <circle cx="-25" cy="0" r="8" fill="#CBD5E1" />
          <circle cx="25" cy="0" r="8" fill="#CBD5E1" />
          <line x1="-12" y1="-18" x2="12" y2="-18" stroke="#CA8A04" stroke-width="3" stroke-linecap="round" />
          <path d="M -10 12 L -2 20 L 12 6" fill="none" stroke="#16A34A" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />
        </g>
      </g>
    </g>

    <!-- HEAD (TixDesk Ticket Hybrid Shape) -->
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
      " fill="url(#headGrad2)" stroke="#1D4ED8" stroke-width="2" />

      <!-- Inner Visor Screen -->
      <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#visorGrad2)" stroke="#38BDF8" stroke-width="4" />

      <!-- Gloss highlight -->
      <path d="M -115 -105 Q 0 -125 115 -105 L 115 -90 Q 0 -110 -115 -90 Z" fill="#FFFFFF" opacity="0.22" />

      <!-- ADORABLE BIG EYES -->
      <g transform="translate(-55, -45)">
        <ellipse cx="0" cy="0" rx="24" ry="30" fill="#38BDF8" />
        <ellipse cx="0" cy="0" rx="20" ry="26" fill="#0284C7" />
        <circle cx="-7" cy="-10" r="8" fill="#FFFFFF" />
        <circle cx="8" cy="10" r="4" fill="#FFFFFF" />
      </g>

      <g transform="translate(55, -45)">
        <ellipse cx="0" cy="0" rx="24" ry="30" fill="#38BDF8" />
        <ellipse cx="0" cy="0" rx="20" ry="26" fill="#0284C7" />
        <circle cx="-7" cy="-10" r="8" fill="#FFFFFF" />
        <circle cx="8" cy="10" r="4" fill="#FFFFFF" />
      </g>

      <!-- Blush -->
      <ellipse cx="-75" cy="-5" rx="14" ry="8" fill="#F43F5E" opacity="0.75" />
      <ellipse cx="75" cy="-5" rx="14" ry="8" fill="#F43F5E" opacity="0.75" />

      <!-- Cheerful Cat-Mouth -->
      <path d="M -16 -6 Q -8 6 0 -2 Q 8 6 16 -6" fill="none" stroke="#38BDF8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />
    </g>

    <!-- HEADSET -->
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

# ==============================================================================
# STICKER 3: CYBER MECHA TACTICAL DECAL - "UNIT-016 // ZERO OVERDUE"
# ==============================================================================
svg_sticker_03 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">
  <defs>
    <linearGradient id="cyanGlow3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" />
      <stop offset="100%" stop-color="#3B82F6" />
    </linearGradient>

    <linearGradient id="mechaBase3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#090D1A" />
      <stop offset="100%" stop-color="#111827" />
    </linearGradient>

    <pattern id="hazard3" width="20" height="20" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <rect width="10" height="20" fill="#F59E0B" />
      <rect x="10" width="10" height="20" fill="#1E293B" />
    </pattern>
  </defs>

  <g transform="translate(300, 300)">
    <!-- WHITE DIE-CUT BASE CONTOUR (Chamfered Tactical Shield) -->
    <polygon points="
      -190,-250 190,-250
      250,-190 250,190
      190,250 -190,250
      -250,190 -250,-190
    " fill="#FFFFFF" stroke="#FFFFFF" stroke-width="38" stroke-linejoin="round" />

    <!-- MAIN DARK TACTICAL PLATE -->
    <polygon points="
      -180,-240 180,-240
      240,-180 240,180
      180,240 -180,240
      -240,180 -240,-180
    " fill="url(#mechaBase3)" stroke="#00F0FF" stroke-width="3.5" />

    <!-- INNER NEON ACCENT LINES -->
    <polygon points="
      -165,-225 165,-225
      225,-165 225,165
      165,225 -165,225
      -225,165 -225,-165
    " fill="none" stroke="#1E3A8A" stroke-width="2" stroke-dasharray="8 4" />

    <!-- TOP HEADER: TELEMETRY & UNIT DESIGNATION -->
    <g transform="translate(0, -195)">
      <text x="-150" y="0" font-family="'Noto Sans Mono', monospace" font-size="14" font-weight="900" fill="#00F0FF" letter-spacing="3">TIXDESK // TACTICAL</text>
      <text x="150" y="0" font-family="'Noto Sans Mono', monospace" font-size="13" font-weight="700" fill="#94A3B8" text-anchor="end">UNIT-016 // TIM-A3</text>
      <line x1="-155" y1="10" x2="155" y2="10" stroke="#334155" stroke-width="2" />
    </g>

    <!-- HAZARD STRIPE ACCENT (TOP RIGHT CORNER) -->
    <polygon points="170,-230 230,-170 215,-170 170,-215" fill="url(#hazard3)" />

    <!-- CENTER EMBLEM: MECHA TIXDESK LOGO -->
    <g transform="translate(0, -10)">
      <!-- Glow backing -->
      <path d="M -85 -70 L 85 -70 Q 110 -70 110 -45 L 110 -15 A 18 18 0 0 0 110 20 L 110 50 Q 110 75 85 75 L -45 75 L -95 110 L -95 20 A 18 18 0 0 0 -95 -15 L -95 -45 Q -95 -70 -70 -70 Z"
            fill="none" stroke="#00F0FF" stroke-width="12" opacity="0.25" />

      <!-- Main Mecha Ticket -->
      <path d="M -85 -70 L 85 -70 Q 110 -70 110 -45 L 110 -15 A 18 18 0 0 0 110 20 L 110 50 Q 110 75 85 75 L -45 75 L -95 110 L -95 20 A 18 18 0 0 0 -95 -15 L -95 -45 Q -95 -70 -70 -70 Z"
            fill="url(#cyanGlow3)" stroke="#FFFFFF" stroke-width="2.5" />

      <!-- Internal T Negative Cutout with Cyber Traces -->
      <path d="M -50 -50 L 50 -50 L 50 -25 L 20 -25 L 20 50 L -20 50 L -20 -25 L -50 -25 Z" fill="#090D1A" stroke="#00F0FF" stroke-width="2" />

      <!-- Circuit Nodes inside T -->
      <circle cx="0" cy="-37" r="4.5" fill="#00F0FF" />
      <circle cx="0" cy="15" r="4.5" fill="#00F0FF" />
      <line x1="0" y1="-33" x2="0" y2="11" stroke="#00F0FF" stroke-width="2.5" />

      <!-- Crosshairs on corners -->
      <line x1="-125" y1="-10" x2="-105" y2="-10" stroke="#00F0FF" stroke-width="2" />
      <line x1="105" y1="-10" x2="125" y2="-10" stroke="#00F0FF" stroke-width="2" />
    </g>

    <!-- STATUS DISPLAY BOX -->
    <g transform="translate(0, 135)">
      <rect x="-160" y="-18" width="320" height="36" rx="6" fill="#0F172A" stroke="#00F0FF" stroke-width="2" />
      <circle cx="-135" cy="0" r="6" fill="#10B981" />
      <text x="-115" y="6" font-family="'Noto Sans Mono', monospace" font-size="14" font-weight="900" fill="#FFFFFF" letter-spacing="2">PROTOCOL: RESOLVED</text>
      <text x="135" y="6" font-family="'Noto Sans Mono', monospace" font-size="14" font-weight="900" fill="#10B981" text-anchor="end">[200 OK]</text>
    </g>

    <!-- BOTTOM SPECS FOOTER -->
    <g transform="translate(0, 195)">
      <line x1="-155" y1="-8" x2="155" y2="-8" stroke="#334155" stroke-width="2" />
      <text x="-150" y="12" font-family="'Noto Sans Mono', monospace" font-size="12" font-weight="700" fill="#38BDF8" letter-spacing="2">SLA: ZERO OVERDUE</text>
      <text x="150" y="12" font-family="'Noto Sans Mono', monospace" font-size="12" font-weight="900" fill="#F59E0B" text-anchor="end">SYS.VER // v1.0.0</text>
    </g>

    <!-- CORNER BRACKETS -->
    <path d="M -170 -220 L -170 -235 L -155 -235" fill="none" stroke="#00F0FF" stroke-width="3" />
    <path d="M 170 -220 L 170 -235 L 155 -235" fill="none" stroke="#00F0FF" stroke-width="3" />
    <path d="M -170 220 L -170 235 L -155 235" fill="none" stroke="#00F0FF" stroke-width="3" />
    <path d="M 170 220 L 170 235 L 155 235" fill="none" stroke="#00F0FF" stroke-width="3" />
  </g>
</svg>'''

# ==============================================================================
# STICKER 4: RETRO 16-BIT ARCADE GAMER - "LEVEL UP // 100% SLA"
# ==============================================================================
svg_sticker_04 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">
  <g transform="translate(300, 300)">
    <!-- WHITE DIE-CUT BASE CONTOUR -->
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

    <!-- HEARTS BASE OUTLINE -->
    <g fill="#FFFFFF" stroke="#FFFFFF" stroke-width="26" stroke-linejoin="round">
      <rect x="-145" y="-250" width="60" height="55" rx="8" />
      <rect x="-30" y="-260" width="60" height="55" rx="8" />
      <rect x="85" y="-250" width="60" height="55" rx="8" />
    </g>

    <!-- BANNER BASE OUTLINE -->
    <rect x="-185" y="200" width="370" height="60" rx="16" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="28" stroke-linejoin="round" />

    <!-- ================= PIXEL GRAPHICS ================= -->

    <!-- FLOATING 8-BIT HEARTS -->
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

    <!-- MAIN TICKET BODY (Pixel Blocks) -->
    <rect x="-175" y="-160" width="350" height="270" fill="#2563EB" />
    <rect x="0" y="-160" width="175" height="270" fill="#06B6D4" />
    <rect x="-35" y="-160" width="35" height="270" fill="#0284C7" />

    <!-- Notches -->
    <rect x="-205" y="-45" width="55" height="55" fill="#FFFFFF" />
    <rect x="150" y="-45" width="55" height="55" fill="#FFFFFF" />
    
    <!-- Bubble Tail -->
    <polygon points="-160,110 -160,195 -80,110" fill="#2563EB" />
    <polygon points="-130,110 -160,195 -95,110" fill="#1D4ED8" />

    <!-- PIXEL SUNGLASSES ('DEAL WITH IT' RETRO VIBE) -->
    <g transform="translate(0, -50)">
      <rect x="-125" y="-20" width="105" height="45" fill="#0F172A" />
      <rect x="20" y="-20" width="105" height="45" fill="#0F172A" />
      <rect x="-20" y="-10" width="40" height="18" fill="#0F172A" />

      <rect x="-110" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="-92" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="35" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="53" y="4" width="14" height="14" fill="#FFFFFF" />

      <!-- Smile -->
      <rect x="-20" y="60" width="40" height="12" fill="#0F172A" />
      <rect x="-12" y="72" width="24" height="12" fill="#0F172A" />
      <!-- Cheeks -->
      <rect x="-80" y="40" width="24" height="12" fill="#F43F5E" />
      <rect x="56" y="40" width="24" height="12" fill="#F43F5E" />
    </g>

    <!-- RETRO ARCADE BANNER -->
    <g transform="translate(0, 215)">
      <rect x="-170" y="-18" width="340" height="42" fill="#0F172A" stroke="#38BDF8" stroke-width="3" />
      <rect x="-170" y="-18" width="6" height="6" fill="#FFFFFF" />
      <rect x="164" y="-18" width="6" height="6" fill="#FFFFFF" />
      <rect x="-170" y="18" width="6" height="6" fill="#FFFFFF" />
      <rect x="164" y="18" width="6" height="6" fill="#FFFFFF" />

      <text x="0" y="10" font-family="'Noto Sans Mono', monospace" font-size="20" font-weight="900" letter-spacing="3" fill="#38BDF8" text-anchor="middle">★ SLA SAVED: 100% ★</text>
    </g>

    <!-- XP BAR -->
    <g transform="translate(0, 85)">
      <rect x="-85" y="0" width="170" height="12" fill="#0F172A" />
      <rect x="-82" y="2" width="164" height="8" fill="#22C55E" />
    </g>
  </g>
</svg>'''

# Save files
files = {
    "tixdesk-sticker-01-hero-mark.svg": svg_sticker_01,
    "tixdesk-sticker-02-mascot-tixie.svg": svg_sticker_02,
    "tixdesk-sticker-03-cyber-mecha-decal.svg": svg_sticker_03,
    "tixdesk-sticker-04-retro-pixel-arcade.svg": svg_sticker_04,
}

for name, content in files.items():
    svg_path = os.path.join(SVG_DIR, name)
    with open(svg_path, "w") as f:
        f.write(content)
    
    base_name = name.replace(".svg", "")
    png_path = os.path.join(PNG_DIR, f"{base_name}-300dpi.png")
    subprocess.run(["rsvg-convert", "-z", "2.0", svg_path, "-o", png_path])

print("All 4 SVGs and 300 DPI PNGs generated!")
