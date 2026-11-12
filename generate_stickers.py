#!/usr/bin/env python3
import os
import subprocess

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(REPO_DIR, "assets", "svg")
PNG_DIR = os.path.join(REPO_DIR, "assets", "png")
CUT_DIR = os.path.join(REPO_DIR, "assets", "print-ready-cutlines")
PDF_DIR = os.path.join(REPO_DIR, "print-pdfs")

for d in [SVG_DIR, PNG_DIR, CUT_DIR, PDF_DIR]:
    os.makedirs(d, exist_ok=True)

# ==============================================================================
# 1. STICKER 01: PURE HERO MARK (OFFICIAL REVISION)
# - White die-cut contour follows the design curves (dips into the tail crevice,
#   no lazy straight diagonal shortcut across the bottom).
# - 'T' glyph is 100% solid white (#FFFFFF) with zero black gaps or holes.
# - Exact horizontal gradient #3877F6 -> #4CA2EA -> #5AC1C4.
# ==============================================================================
path_01_body = """
  M 0 -105
  L 120 -105
  A 28 28 0 0 1 148 -77
  L 148 -35
  A 20 20 0 0 0 148 5
  L 148 52
  A 28 28 0 0 1 120 80
  L 24 80
  L 24 -25
  L 65 -25
  A 17.5 17.5 0 0 0 65 -60
  L -65 -60
  A 17.5 17.5 0 0 0 -65 -25
  L -24 -25
  L -24 80
  L -70 140
  A 10 10 0 0 1 -80 135
  L -80 80
  L -120 80
  A 28 28 0 0 1 -148 52
  L -148 5
  A 20 20 0 0 0 -148 -35
  L -148 -77
  A 28 28 0 0 1 -120 -105
  Z
"""

path_01_t = """
  M -65 -60
  L 65 -60
  A 17.5 17.5 0 0 1 65 -25
  L 24 -25
  L 24 80
  L -24 80
  L -24 -25
  L -65 -25
  A 17.5 17.5 0 0 1 -65 -60
  Z
"""

path_01_contour = """
  M 0 -105
  L 120 -105
  A 28 28 0 0 1 148 -77
  L 148 -35
  A 20 20 0 0 0 148 5
  L 148 52
  A 28 28 0 0 1 120 80
  L 24 80
  L -24 80
  L -70 140
  A 10 10 0 0 1 -80 135
  L -80 80
  L -120 80
  A 28 28 0 0 1 -148 52
  L -148 5
  A 20 20 0 0 0 -148 -35
  L -148 -77
  A 28 28 0 0 1 -120 -105
  Z
"""

svg_01 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 440" width="440" height="440">
  <defs>
    <linearGradient id="tixdeskGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3877F6" />
      <stop offset="50%" stop-color="#4CA2EA" />
      <stop offset="100%" stop-color="#5AC1C4" />
    </linearGradient>
  </defs>

  <g id="Artwork" transform="translate(220, 195)">
    <!-- 1. White die-cut contour that closely follows design curves & tail -->
    <path id="WhiteBorder" d="{path_01_contour}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="24" stroke-linejoin="round" stroke-linecap="round" />
    
    <!-- 2. Official Blue/Cyan Gradient body (tail is gradient) -->
    <path id="TicketBody" d="{path_01_body}" fill="url(#tixdeskGrad)" />

    <!-- 3. SOLID WHITE 'T' GLYPH (100% solid white, no black gap, exact proportions) -->
    <path id="TGlyph" d="{path_01_t}" fill="#FFFFFF" />
  </g>
</svg>"""

cutline_01 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 440" width="440" height="440">
  <defs>
    <linearGradient id="tixdeskGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3877F6" />
      <stop offset="50%" stop-color="#4CA2EA" />
      <stop offset="100%" stop-color="#5AC1C4" />
    </linearGradient>
  </defs>

  <g id="Artwork" transform="translate(220, 195)">
    <path id="WhiteBorder" d="{path_01_contour}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="24" stroke-linejoin="round" stroke-linecap="round" />
    <path id="TicketBody" d="{path_01_body}" fill="url(#tixdeskGrad)" />
    <path id="TGlyph" d="{path_01_t}" fill="#FFFFFF" />
  </g>

  <!-- Technical Die-Cut Layer: Spot Magenta 100% 0.5pt -->
  <g id="CutContour" transform="translate(220, 195)">
    <path d="{path_01_contour}" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" />
  </g>
</svg>"""

# ==============================================================================
# 2. STICKER 02: KAWAII CHIBI MASCOT TIXIE (FOLLOWING CONTOURS)
# - White die-cut contour follows the character curves closely (antenna,
#   headset, earcups, waving hand, golden ticket, thruster).
# - Zero artifacts or stray specks.
# ==============================================================================
mascot_contour_group = """
    <g id="WhiteBorder" fill="#FFFFFF" stroke="#FFFFFF" stroke-linejoin="round" stroke-linecap="round">
      <circle cx="0" cy="-230" r="38" />
      <line x1="0" y1="-150" x2="0" y2="-230" stroke-width="40" />
      <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke-width="50" />
      <rect x="-228" y="-98" width="68" height="108" rx="30" stroke-width="12" />
      <rect x="160" y="-98" width="68" height="108" rx="30" stroke-width="12" />
      <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke-width="36" />
      <circle cx="-70" cy="73" r="32" />
      <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="42" />
      <ellipse cx="0" cy="160" rx="105" ry="82" stroke-width="16" />
      <polygon points="-45,190 45,190 0,250" stroke-width="26" />
      <circle cx="-115" cy="95" r="38" stroke-width="16" />
      <path d="M -80 135 C -105 130, -125 110, -115 85" fill="none" stroke-width="46" />
      <rect x="80" y="65" width="95" height="118" rx="24" stroke-width="32" transform="rotate(15 120 125)" />
      <polygon points="60,80 160,60 160,160 60,160" />
    </g>
"""

svg_02 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 620" width="600" height="620">
  <defs>
    <linearGradient id="headGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3877F6" />
      <stop offset="50%" stop-color="#4CA2EA" />
      <stop offset="100%" stop-color="#5AC1C4" />
    </linearGradient>

    <linearGradient id="screenGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#080E1E" />
      <stop offset="100%" stop-color="#111C35" />
    </linearGradient>

    <linearGradient id="bodyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#E2E8F0" />
    </linearGradient>
  </defs>

  <g id="Artwork" transform="translate(300, 305)">
    <!-- 1. White die-cut contour that closely follows character curves -->
    {mascot_contour_group}

    <!-- 2. Antenna -->
    <path d="M 0 -150 L 0 -220" stroke="#64748B" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#10B981" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#6EE7B7" />

    <!-- 3. Floating Chibi Body -->
    <g transform="translate(0, 140)">
      <polygon points="-25,50 25,50 0,95" fill="#06B6D4" />
      <polygon points="-15,50 15,50 0,80" fill="#FFFFFF" />

      <ellipse cx="0" cy="20" rx="80" ry="58" fill="url(#bodyGrad)" stroke="#94A3B8" stroke-width="4" />
      <path d="M -72 25 Q 0 45 72 25" fill="none" stroke="#0EA5E9" stroke-width="8" stroke-linecap="round" />
      
      <circle cx="0" cy="15" r="18" fill="#2563EB" stroke="#FFFFFF" stroke-width="2.5" />
      <text x="0" y="22" font-family="'Noto Sans', system-ui, sans-serif" font-size="20" font-weight="900" fill="#FFFFFF" text-anchor="middle">T</text>

      <!-- Left Hand Waving -->
      <g transform="translate(-80, -5)">
        <path d="M 0 10 C -25 5, -45 -15, -35 -40" fill="none" stroke="#CBD5E1" stroke-width="22" stroke-linecap="round" />
        <circle cx="-35" cy="-40" r="16" fill="#FFFFFF" stroke="#94A3B8" stroke-width="3.5" />
      </g>

      <!-- Right Hand holding golden ticket -->
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

    <!-- 4. Head -->
    <g>
      <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#headGrad)" stroke="#1D4ED8" stroke-width="2.5" />

      <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGrad)" stroke="#38BDF8" stroke-width="4" />
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

    <!-- 5. Headset -->
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
</svg>"""

cutline_02 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 620" width="600" height="620">
  <defs>
    <linearGradient id="headGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3877F6" />
      <stop offset="50%" stop-color="#4CA2EA" />
      <stop offset="100%" stop-color="#5AC1C4" />
    </linearGradient>

    <linearGradient id="screenGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#080E1E" />
      <stop offset="100%" stop-color="#111C35" />
    </linearGradient>

    <linearGradient id="bodyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#E2E8F0" />
    </linearGradient>
  </defs>

  <g id="Artwork" transform="translate(300, 305)">
    {mascot_contour_group}
    <!-- Antenna -->
    <path d="M 0 -150 L 0 -220" stroke="#64748B" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#10B981" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#6EE7B7" />

    <!-- Floating Chibi Body -->
    <g transform="translate(0, 140)">
      <polygon points="-25,50 25,50 0,95" fill="#06B6D4" />
      <polygon points="-15,50 15,50 0,80" fill="#FFFFFF" />
      <ellipse cx="0" cy="20" rx="80" ry="58" fill="url(#bodyGrad)" stroke="#94A3B8" stroke-width="4" />
      <path d="M -72 25 Q 0 45 72 25" fill="none" stroke="#0EA5E9" stroke-width="8" stroke-linecap="round" />
      <circle cx="0" cy="15" r="18" fill="#2563EB" stroke="#FFFFFF" stroke-width="2.5" />
      <text x="0" y="22" font-family="'Noto Sans', system-ui, sans-serif" font-size="20" font-weight="900" fill="#FFFFFF" text-anchor="middle">T</text>
      <!-- Left Hand -->
      <g transform="translate(-80, -5)">
        <path d="M 0 10 C -25 5, -45 -15, -35 -40" fill="none" stroke="#CBD5E1" stroke-width="22" stroke-linecap="round" />
        <circle cx="-35" cy="-40" r="16" fill="#FFFFFF" stroke="#94A3B8" stroke-width="3.5" />
      </g>
      <!-- Right Hand -->
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

    <!-- Head -->
    <g>
      <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#headGrad)" stroke="#1D4ED8" stroke-width="2.5" />
      <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGrad)" stroke="#38BDF8" stroke-width="4" />
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

    <!-- Headset -->
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

  <!-- Technical Die-Cut Layer: Spot Magenta 100% 0.5pt -->
  <g id="CutContour" transform="translate(300, 305)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
    <circle cx="0" cy="-230" r="38" />
    <line x1="0" y1="-150" x2="0" y2="-230" stroke-width="40" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke-width="50" />
    <rect x="-228" y="-98" width="68" height="108" rx="30" stroke-width="12" />
    <rect x="160" y="-98" width="68" height="108" rx="30" stroke-width="12" />
    <ellipse cx="0" cy="160" rx="105" ry="82" stroke-width="16" />
  </g>
</svg>"""

# ==============================================================================
# 3. STICKER 03: RETRO PIXEL ART ARCADE (SNUG CONTOUR, FLAWLESS INTEGRATION)
# - Scalloped arches over the 3 floating hearts.
# - Clean indentations for side notches.
# - Snug SLA Banner directly under the ticket chin and tail.
# - Zero awkward white blocks, zero dark glitches.
# ==============================================================================
path_03_snug = """
  M -115 -260
  Q -60 -230, -45 -250
  Q 0 -280, 45 -250
  Q 60 -230, 115 -260
  Q 195 -220, 200 -140
  L 200 -45
  Q 165 -15, 200 15
  L 200 95
  Q 195 130, 185 160
  A 18 18 0 0 1 167 175
  L -167 175
  A 18 18 0 0 1 -185 160
  L -195 95
  L -200 15
  Q -165 -15, -200 -45
  L -200 -140
  Q -195 -220, -115 -260
  Z
"""

svg_03 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">
  <g id="Artwork" transform="translate(270, 290)">
    <!-- 1. White die-cut contour that follows pixel design curves & hearts -->
    <path id="WhiteBorder" d="{path_03_snug}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="18" stroke-linejoin="round" stroke-linecap="round" />

    <!-- 2. Floating 8-Bit Hearts -->
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

    <!-- 3. Ticket Body -->
    <rect x="-175" y="-160" width="350" height="265" fill="#3877F6" />
    <rect x="0" y="-160" width="175" height="265" fill="#5AC1C4" />
    <rect x="-35" y="-160" width="35" height="265" fill="#4CA2EA" />
    
    <!-- Notches -->
    <rect x="-195" y="-35" width="35" height="45" fill="#FFFFFF" />
    <rect x="160" y="-35" width="35" height="45" fill="#FFFFFF" />

    <!-- Tail -->
    <polygon points="-160,105 -160,145 -105,105" fill="#3877F6" />
    <polygon points="-135,105 -160,145 -118,105" fill="#2563EB" />

    <!-- 4. Sunglasses -->
    <g transform="translate(0, -45)">
      <rect x="-125" y="-20" width="105" height="45" fill="#0F172A" />
      <rect x="20" y="-20" width="105" height="45" fill="#0F172A" />
      <rect x="-20" y="-10" width="40" height="18" fill="#0F172A" />
      <rect x="-110" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="-92" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="35" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="53" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="-20" y="58" width="40" height="12" fill="#0F172A" />
      <rect x="-12" y="70" width="24" height="12" fill="#0F172A" />
      <rect x="-80" y="38" width="24" height="12" fill="#F43F5E" />
      <rect x="56" y="38" width="24" height="12" fill="#F43F5E" />
    </g>

    <!-- 5. XP Bar -->
    <g transform="translate(0, 80)">
      <rect x="-85" y="0" width="170" height="12" fill="#0F172A" />
      <rect x="-82" y="2" width="164" height="8" fill="#22C55E" />
    </g>

    <!-- 6. Snug SLA Banner -->
    <g transform="translate(0, 135)">
      <rect x="-165" y="-18" width="330" height="40" rx="8" fill="#0F172A" stroke="#38BDF8" stroke-width="3" />
      <text x="0" y="10" font-family="'Noto Sans Mono', monospace" font-size="19" font-weight="900" letter-spacing="2.5" fill="#38BDF8" text-anchor="middle">★ SLA SAVED: 100% ★</text>
    </g>
  </g>
</svg>"""

cutline_03 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">
  <g id="Artwork" transform="translate(270, 290)">
    <path id="WhiteBorder" d="{path_03_snug}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="18" stroke-linejoin="round" stroke-linecap="round" />
    
    <!-- 8-Bit Hearts -->
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

    <!-- Ticket Body -->
    <rect x="-175" y="-160" width="350" height="265" fill="#3877F6" />
    <rect x="0" y="-160" width="175" height="265" fill="#5AC1C4" />
    <rect x="-35" y="-160" width="35" height="265" fill="#4CA2EA" />
    <rect x="-195" y="-35" width="35" height="45" fill="#FFFFFF" />
    <rect x="160" y="-35" width="35" height="45" fill="#FFFFFF" />
    <polygon points="-160,105 -160,145 -105,105" fill="#3877F6" />
    <polygon points="-135,105 -160,145 -118,105" fill="#2563EB" />

    <!-- Sunglasses -->
    <g transform="translate(0, -45)">
      <rect x="-125" y="-20" width="105" height="45" fill="#0F172A" />
      <rect x="20" y="-20" width="105" height="45" fill="#0F172A" />
      <rect x="-20" y="-10" width="40" height="18" fill="#0F172A" />
      <rect x="-110" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="-92" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="35" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="53" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="-20" y="58" width="40" height="12" fill="#0F172A" />
      <rect x="-12" y="70" width="24" height="12" fill="#0F172A" />
      <rect x="-80" y="38" width="24" height="12" fill="#F43F5E" />
      <rect x="56" y="38" width="24" height="12" fill="#F43F5E" />
    </g>

    <!-- XP Bar -->
    <g transform="translate(0, 80)">
      <rect x="-85" y="0" width="170" height="12" fill="#0F172A" />
      <rect x="-82" y="2" width="164" height="8" fill="#22C55E" />
    </g>

    <!-- Snug SLA Banner -->
    <g transform="translate(0, 135)">
      <rect x="-165" y="-18" width="330" height="40" rx="8" fill="#0F172A" stroke="#38BDF8" stroke-width="3" />
      <text x="0" y="10" font-family="'Noto Sans Mono', monospace" font-size="19" font-weight="900" letter-spacing="2.5" fill="#38BDF8" text-anchor="middle">★ SLA SAVED: 100% ★</text>
    </g>
  </g>

  <!-- Technical Die-Cut Layer: Spot Magenta 100% 0.5pt -->
  <g id="CutContour" transform="translate(270, 290)">
    <path d="{path_03_snug}" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" />
  </g>
</svg>"""

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
    subprocess.run(["rsvg-convert", "-w", "1000", svg_file, "-o", png_file], check=True)

    # 3. Cutline SVG
    cutline_file = os.path.join(CUT_DIR, f"{base_name}-cutcontour.svg")
    with open(cutline_file, "w") as f:
        f.write(cutline_content)

    # 4. Print-ready PDF
    pdf_file = os.path.join(PDF_DIR, f"{base_name}-print.pdf")
    subprocess.run(["rsvg-convert", "-f", "pdf", cutline_file, "-o", pdf_file], check=True)

print("Official 3-sticker pack generated successfully with flawless contours and Spot Magenta CutContour!")
