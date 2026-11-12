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
# 1. STICKER 01: PURE HERO MARK (LOCKED PERMANENT - DO NOT MODIFY)
# ==============================================================================
path_01_body = """
  M 0 -105
  L 120 -105
  A 28 28 0 0 1 148 -77
  L 148 -35
  A 20 20 0 0 0 148 5
  L 148 52
  A 28 28 0 0 1 120 80
  L 20 80
  L 20 -24
  L 66 -24
  A 20 20 0 0 0 66 -64
  L -66 -64
  A 20 20 0 0 0 -66 -24
  L -20 -24
  L -20 80
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
  M -66 -64
  L 66 -64
  A 20 20 0 0 1 66 -24
  L 20 -24
  L 20 80
  L -20 80
  L -20 -24
  L -66 -24
  A 20 20 0 0 1 -66 -64
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
  L 20 80
  L -20 80
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
    <path id="WhiteBorder" d="{path_01_contour}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="24" stroke-linejoin="round" stroke-linecap="round" />
    <path id="TicketBody" d="{path_01_body}" fill="url(#tixdeskGrad)" />
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

  <g id="CutContour" transform="translate(220, 195)">
    <path d="{path_01_contour}" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" />
  </g>
</svg>"""

# ==============================================================================
# 2. STICKER 02: KAWAII CHIBI MASCOT HEAD (LOCKED PERMANENT - DO NOT MODIFY)
# ==============================================================================
svg_02 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">
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
  </defs>

  <g id="Artwork" transform="translate(260, 275)">
    <!-- 1. Tight White Die-Cut Contour matching Sticker 01 (Clean seamless contour) -->
    <g id="WhiteBorder" fill="#FFFFFF" stroke="#FFFFFF" stroke-linejoin="round" stroke-linecap="round">
      <circle cx="0" cy="-230" r="22" stroke-width="24" />
      <line x1="0" y1="-150" x2="0" y2="-230" stroke-width="32" />
      <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke-width="46" />
      <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
      <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke-width="26" />
      <circle cx="-70" cy="73" r="14" stroke-width="24" />
      <!-- Solid White Bridge filling the gap between mic wire and speech body -->
      <path d="M -190 -10 C -190 60, -160 70, -160 70 L -160 10 L -160 -10 Z" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="12" stroke-linejoin="round" />
    </g>

    <!-- 2. Solid White Gap Fills inside the ticket notches (stroke=none, cleanly behind earcups) -->
    <path d="M 160 -40 A 25 25 0 0 0 160 10 L 175 10 L 175 -40 Z" fill="#FFFFFF" stroke="none" />
    <path d="M -160 -40 A 25 25 0 0 1 -160 10 L -175 10 L -175 -40 Z" fill="#FFFFFF" stroke="none" />

    <!-- 3. Antenna -->
    <path d="M 0 -150 L 0 -220" stroke="#64748B" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#10B981" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#6EE7B7" />

    <!-- 4. Head Ticket Shell (Preserves iconic ticket notches!) -->
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#headGrad)" stroke="#1D4ED8" stroke-width="2.5" />

    <!-- 5. Screen Visor -->
    <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGrad)" stroke="#38BDF8" stroke-width="4" />
    <path d="M -115 -105 Q 0 -125 115 -105 L 115 -90 Q 0 -110 -115 -90 Z" fill="#FFFFFF" opacity="0.24" />

    <!-- 6. Eyes & Expression -->
    <g transform="translate(-55, -45)">
      <ellipse cx="0" cy="0" rx="24" ry="30" fill="#38BDF8" />
      <ellipse cx="0" cy="0" rx="20" ry="26" fill="#0284C7" />
      <circle cx="-7" cy="-10" r="8" fill="#FFFFFF" />
      <circle cx="8" cy="10" r="4.5" fill="#FFFFFF" />
    </g>
    <g transform="translate(55, -45)">
      <ellipse cx="0" cy="0" rx="24" ry="30" fill="#38BDF8" />
      <ellipse cx="0" cy="0" rx="20" ry="26" fill="#0284C7" />
      <circle cx="-7" cy="-10" r="8" fill="#FFFFFF" />
      <circle cx="8" cy="10" r="4.5" fill="#FFFFFF" />
    </g>
    <ellipse cx="-75" cy="-5" rx="14" ry="8" fill="#F43F5E" opacity="0.8" />
    <ellipse cx="75" cy="-5" rx="14" ry="8" fill="#F43F5E" opacity="0.8" />
    <path d="M -16 -4 Q -8 8 0 0 Q 8 8 16 -4" fill="none" stroke="#38BDF8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />

    <!-- 7. Headset -->
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#1E293B" stroke-width="22" stroke-linecap="round" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#38BDF8" stroke-width="8" stroke-linecap="round" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="-200" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <rect x="165" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="175" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke="#1E293B" stroke-width="10" stroke-linecap="round" />
    <circle cx="-70" cy="73" r="14" fill="#10B981" stroke="#FFFFFF" stroke-width="4" />
  </g>
</svg>"""

cutline_02 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">
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
  </defs>

  <g id="Artwork" transform="translate(260, 275)">
    <g id="WhiteBorder" fill="#FFFFFF" stroke="#FFFFFF" stroke-linejoin="round" stroke-linecap="round">
      <circle cx="0" cy="-230" r="22" stroke-width="24" />
      <line x1="0" y1="-150" x2="0" y2="-230" stroke-width="32" />
      <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke-width="46" />
      <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
      <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke-width="26" />
      <circle cx="-70" cy="73" r="14" stroke-width="24" />
      <path d="M -190 -10 C -190 60, -160 70, -160 70 L -160 10 L -160 -10 Z" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="12" stroke-linejoin="round" />
    </g>

    <path d="M 160 -40 A 25 25 0 0 0 160 10 L 175 10 L 175 -40 Z" fill="#FFFFFF" stroke="none" />
    <path d="M -160 -40 A 25 25 0 0 1 -160 10 L -175 10 L -175 -40 Z" fill="#FFFFFF" stroke="none" />

    <path d="M 0 -150 L 0 -220" stroke="#64748B" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#10B981" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#6EE7B7" />

    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#headGrad)" stroke="#1D4ED8" stroke-width="2.5" />

    <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGrad)" stroke="#38BDF8" stroke-width="4" />
    <path d="M -115 -105 Q 0 -125 115 -105 L 115 -90 Q 0 -110 -115 -90 Z" fill="#FFFFFF" opacity="0.24" />

    <g transform="translate(-55, -45)">
      <ellipse cx="0" cy="0" rx="24" ry="30" fill="#38BDF8" />
      <ellipse cx="0" cy="0" rx="20" ry="26" fill="#0284C7" />
      <circle cx="-7" cy="-10" r="8" fill="#FFFFFF" />
      <circle cx="8" cy="10" r="4.5" fill="#FFFFFF" />
    </g>
    <g transform="translate(55, -45)">
      <ellipse cx="0" cy="0" rx="24" ry="30" fill="#38BDF8" />
      <ellipse cx="0" cy="0" rx="20" ry="26" fill="#0284C7" />
      <circle cx="-7" cy="-10" r="8" fill="#FFFFFF" />
      <circle cx="8" cy="10" r="4.5" fill="#FFFFFF" />
    </g>
    <ellipse cx="-75" cy="-5" rx="14" ry="8" fill="#F43F5E" opacity="0.8" />
    <ellipse cx="75" cy="-5" rx="14" ry="8" fill="#F43F5E" opacity="0.8" />
    <path d="M -16 -4 Q -8 8 0 0 Q 8 8 16 -4" fill="none" stroke="#38BDF8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />

    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#1E293B" stroke-width="22" stroke-linecap="round" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#38BDF8" stroke-width="8" stroke-linecap="round" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="-200" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <rect x="165" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="175" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke="#1E293B" stroke-width="10" stroke-linecap="round" />
    <circle cx="-70" cy="73" r="14" fill="#10B981" stroke="#FFFFFF" stroke-width="4" />
  </g>

  <!-- Technical Die-Cut Layer: Spot Magenta 100% 0.5pt -->
  <g id="CutContour" transform="translate(260, 275)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
    <circle cx="0" cy="-230" r="22" stroke-width="24" />
    <line x1="0" y1="-150" x2="0" y2="-230" stroke-width="32" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" stroke-width="46" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
    <circle cx="-70" cy="73" r="14" stroke-width="24" />
  </g>
</svg>"""

# ==============================================================================
# 3. STICKER 03: RETRO PIXEL ART ARCADE (LOCKED PERMANENT - DO NOT MODIFY)
# ==============================================================================
contour_03_smooth = """
  M -130 -135
  L 130 -135
  Q 150 -135, 150 -115
  L 150 75
  Q 150 95, 130 95
  L -75 95
  L -135 140
  Q -150 145, -150 130
  L -150 75
  L -150 -115
  Q -150 -135, -130 -135
  Z
"""

path_03_body_left = """
  M -130 -135
  L 0 -135
  L 0 95
  L -90 95
  L -140 135
  L -140 95
  L -150 95
  L -150 20
  L -125 20
  L -125 -25
  L -150 -25
  L -150 -115
  Q -150 -135, -130 -135
  Z
"""

path_03_body_right = """
  M 0 -135
  L 130 -135
  Q 150 -135, 150 -115
  L 150 -25
  L 125 -25
  L 125 20
  L 150 20
  L 150 75
  Q 150 95, 130 95
  L 0 95
  Z
"""

svg_03 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 440" width="440" height="440">
  <g id="Artwork" transform="translate(220, 205)">
    <!-- 1. Soft, Slim, Uniform White die-cut contour -->
    <path id="WhiteBorder" d="{contour_03_smooth}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" />

    <!-- 2. Ticket Body with Authentic Inward Punch Notches -->
    <path d="{path_03_body_left}" fill="#3877F6" />
    <path d="{path_03_body_right}" fill="#5AC1C4" />
    <polygon points="-120,95 -140,135 -102,95" fill="#2563EB" />

    <!-- 3. Pixel Sunglasses & Face -->
    <g transform="translate(0, -20)">
      <rect x="-115" y="-20" width="95" height="45" fill="#0F172A" />
      <rect x="20" y="-20" width="95" height="45" fill="#0F172A" />
      <rect x="-20" y="-10" width="40" height="18" fill="#0F172A" />
      <rect x="-100" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="-82" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="35" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="53" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="-20" y="58" width="40" height="12" fill="#0F172A" />
      <rect x="-12" y="70" width="24" height="12" fill="#0F172A" />
      <rect x="-75" y="38" width="24" height="12" fill="#F43F5E" />
      <rect x="51" y="38" width="24" height="12" fill="#F43F5E" />
    </g>
  </g>
</svg>"""

cutline_03 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 440" width="440" height="440">
  <g id="Artwork" transform="translate(220, 205)">
    <path id="WhiteBorder" d="{contour_03_smooth}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" />
    <path d="{path_03_body_left}" fill="#3877F6" />
    <path d="{path_03_body_right}" fill="#5AC1C4" />
    <polygon points="-120,95 -140,135 -102,95" fill="#2563EB" />

    <g transform="translate(0, -20)">
      <rect x="-115" y="-20" width="95" height="45" fill="#0F172A" />
      <rect x="20" y="-20" width="95" height="45" fill="#0F172A" />
      <rect x="-20" y="-10" width="40" height="18" fill="#0F172A" />
      <rect x="-100" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="-82" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="35" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="53" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="-20" y="58" width="40" height="12" fill="#0F172A" />
      <rect x="-12" y="70" width="24" height="12" fill="#0F172A" />
      <rect x="-75" y="38" width="24" height="12" fill="#F43F5E" />
      <rect x="51" y="38" width="24" height="12" fill="#F43F5E" />
    </g>
  </g>

  <!-- Technical Die-Cut Layer: Spot Magenta 100% 0.5pt -->
  <g id="CutContour" transform="translate(220, 205)">
    <path d="{contour_03_smooth}" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" />
  </g>
</svg>"""

# ==============================================================================
# 4. STICKER 04: TIXIE NIGHT SHIFT / POWERED BY CAFFEINE
# ==============================================================================
svg_04 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">
  <defs>
    <linearGradient id="headGrad4" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3877F6" />
      <stop offset="50%" stop-color="#4CA2EA" />
      <stop offset="100%" stop-color="#5AC1C4" />
    </linearGradient>
    <linearGradient id="screenGrad4" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#080E1E" />
      <stop offset="100%" stop-color="#111C35" />
    </linearGradient>
    <linearGradient id="mugGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="coffeeGrad4" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#78350F" />
      <stop offset="100%" stop-color="#451A03" />
    </linearGradient>
  </defs>

  <g id="Artwork" transform="translate(260, 270)">
    <!-- 1. White Die-Cut Contour -->
    <g id="WhiteBorder" fill="#FFFFFF" stroke="#FFFFFF" stroke-linejoin="round" stroke-linecap="round">
      <circle cx="0" cy="-230" r="22" stroke-width="24" />
      <line x1="0" y1="-150" x2="0" y2="-230" stroke-width="32" />
      <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke-width="46" />
      <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
      <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke-width="26" />
      <circle cx="-70" cy="73" r="14" stroke-width="24" />
      <path d="M -190 -10 C -190 60, -160 70, -160 70 L -160 10 L -160 -10 Z" stroke-width="12" />
      <rect x="-45" y="35" width="90" height="75" rx="18" stroke-width="24" />
      <path d="M 40 45 C 68 45, 68 85, 40 85" fill="none" stroke-width="22" />
      <path d="M -20 25 C -25 10, -15 -5, -20 -20" fill="none" stroke-width="18" />
      <path d="M 0 25 C -5 5, 10 -10, 0 -25" fill="none" stroke-width="20" />
      <path d="M 20 25 C 15 10, 25 -5, 20 -20" fill="none" stroke-width="18" />
    </g>

    <path d="M 160 -40 A 25 25 0 0 0 160 10 L 175 10 L 175 -40 Z" fill="#FFFFFF" stroke="none" />
    <path d="M -160 -40 A 25 25 0 0 1 -160 10 L -175 10 L -175 -40 Z" fill="#FFFFFF" stroke="none" />

    <!-- Antenna with Warm Amber Beacon -->
    <path d="M 0 -150 L 0 -220" stroke="#64748B" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#F59E0B" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#FCD34D" />

    <!-- Head Ticket Shell -->
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#headGrad4)" stroke="#1D4ED8" stroke-width="2.5" />

    <!-- Visor -->
    <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGrad4)" stroke="#38BDF8" stroke-width="4" />
    <path d="M -115 -105 Q 0 -125 115 -105 L 115 -90 Q 0 -110 -115 -90 Z" fill="#FFFFFF" opacity="0.24" />

    <!-- Night Shift Sleepy-Cute Eyes & Smile -->
    <path d="M -75 -42 Q -55 -22, -35 -42" fill="none" stroke="#38BDF8" stroke-width="8" stroke-linecap="round" />
    <path d="M -65 -30 Q -55 -22, -45 -30" fill="none" stroke="#38BDF8" stroke-width="4" stroke-linecap="round" />
    
    <path d="M 35 -42 Q 55 -22, 75 -42" fill="none" stroke="#38BDF8" stroke-width="8" stroke-linecap="round" />
    <path d="M 45 -30 Q 55 -22, 65 -30" fill="none" stroke="#38BDF8" stroke-width="4" stroke-linecap="round" />

    <ellipse cx="-70" cy="-15" rx="16" ry="9" fill="#F43F5E" opacity="0.85" />
    <ellipse cx="70" cy="-15" rx="16" ry="9" fill="#F43F5E" opacity="0.85" />
    <path d="M -16 -12 Q -8 0 0 -8 Q 8 0 16 -12" fill="none" stroke="#38BDF8" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />

    <!-- Headset -->
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#1E293B" stroke-width="22" stroke-linecap="round" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#38BDF8" stroke-width="8" stroke-linecap="round" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="-200" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <rect x="165" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="175" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke="#1E293B" stroke-width="10" stroke-linecap="round" />
    <circle cx="-70" cy="73" r="14" fill="#F59E0B" stroke="#FFFFFF" stroke-width="4" />

    <!-- Steaming Coffee Mug -->
    <path d="M -18 22 C -23 10, -13 -2, -18 -15" fill="none" stroke="#E2E8F0" stroke-width="4.5" stroke-linecap="round" opacity="0.75" />
    <path d="M 0 20 C -6 6, 8 -6, 0 -20" fill="none" stroke="#E2E8F0" stroke-width="5.5" stroke-linecap="round" opacity="0.85" />
    <path d="M 18 22 C 13 10, 23 -2, 18 -15" fill="none" stroke="#E2E8F0" stroke-width="4.5" stroke-linecap="round" opacity="0.75" />

    <rect x="-42" y="38" width="84" height="70" rx="16" fill="url(#mugGrad4)" stroke="#38BDF8" stroke-width="4" />
    <path d="M 40 48 C 65 48, 65 80, 40 80" fill="none" stroke="#38BDF8" stroke-width="7" stroke-linecap="round" />
    
    <ellipse cx="0" cy="38" rx="36" ry="8" fill="url(#coffeeGrad4)" stroke="#38BDF8" stroke-width="3" />
    <path d="M 0 34 C -6 38, -6 44, 0 45 C 6 44, 6 38, 0 34 Z" fill="#FEF08A" />

    <polygon points="0,58 12,65 12,79 0,86 -12,79 -12,65" fill="#F59E0B" />
    <text x="0" y="77" font-family="'Noto Sans', sans-serif" font-size="14" font-weight="900" fill="#FFFFFF" text-anchor="middle">T</text>

    <circle cx="-42" cy="72" r="13" fill="#3877F6" stroke="#FFFFFF" stroke-width="3" />
    <circle cx="42" cy="72" r="13" fill="#5AC1C4" stroke="#FFFFFF" stroke-width="3" />
  </g>
</svg>"""

cutline_04 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">
  {svg_04.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">', '').replace('</svg>', '')}
  <g id="CutContour" transform="translate(260, 270)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
    <circle cx="0" cy="-230" r="22" stroke-width="24" />
    <line x1="0" y1="-150" x2="0" y2="-230" stroke-width="32" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" stroke-width="46" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
    <circle cx="-70" cy="73" r="14" stroke-width="24" />
    <rect x="-45" y="35" width="90" height="75" rx="18" stroke-width="24" />
  </g>
</svg>"""

# ==============================================================================
# ==============================================================================
# 5. STICKER 05: TIXIE ON FIRE (BURNING MASCOT // PROD ON FIRE)
# ==============================================================================
svg_05 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">
  <defs>
    <!-- Ticket Head Gradient (Heated Red-Orange) -->
    <linearGradient id="fireHeadGrad" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#DC2626" />
      <stop offset="60%" stop-color="#EA580C" />
      <stop offset="100%" stop-color="#F59E0B" />
    </linearGradient>

    <!-- Flame Layers -->
    <linearGradient id="flameOuter5" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#DC2626" />
      <stop offset="50%" stop-color="#EA580C" />
      <stop offset="100%" stop-color="#F59E0B" />
    </linearGradient>

    <linearGradient id="flameMid5" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#EA580C" />
      <stop offset="60%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#FDE047" />
    </linearGradient>

    <linearGradient id="flameCore5" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B" />
      <stop offset="50%" stop-color="#FDE047" />
      <stop offset="100%" stop-color="#FEF08A" />
    </linearGradient>

    <linearGradient id="screenGradFire" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#180A0A" />
      <stop offset="100%" stop-color="#2D0C0C" />
    </linearGradient>
  </defs>

  <g id="Artwork" transform="translate(270, 290)">
    <!-- 1. White Die-Cut Contour (Encloses flames, antenna, headset, and Tixie body) -->
    <g id="WhiteBorder" fill="#FFFFFF" stroke="#FFFFFF" stroke-linejoin="round" stroke-linecap="round">
      <path d="M -120 -150 C -160 -190, -150 -265, -95 -290 C -75 -245, -55 -230, -45 -200 Z" stroke-width="26" />
      <path d="M -60 -170 C -60 -265, -15 -320, 15 -330 C 30 -275, 65 -235, 45 -180 Z" stroke-width="26" />
      <path d="M 30 -160 C 65 -215, 125 -275, 135 -225 C 140 -190, 115 -160, 100 -145 Z" stroke-width="26" />
      
      <path d="M -180 -120 C -225 -100, -235 -40, -210 -10 C -190 -30, -180 -60, -175 -85 Z" stroke-width="24" />
      <path d="M 175 -120 C 220 -100, 230 -40, 205 -10 C 185 -30, 175 -60, 170 -85 Z" stroke-width="24" />

      <circle cx="-135" cy="-210" r="14" stroke-width="20" />
      <circle cx="130" cy="-240" r="12" stroke-width="20" />
      <circle cx="155" cy="-160" r="15" stroke-width="20" />

      <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke-width="46" />
      <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
      <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke-width="26" />
      <circle cx="-70" cy="73" r="14" stroke-width="24" />
      <path d="M -190 -10 C -190 60, -160 70, -160 70 L -160 10 L -160 -10 Z" stroke-width="12" />

      <rect x="-75" y="48" width="150" height="28" rx="14" stroke-width="24" />
    </g>

    <!-- Solid White Gap Fills behind earcups -->
    <path d="M 160 -40 A 25 25 0 0 0 160 10 L 175 10 L 175 -40 Z" fill="#FFFFFF" stroke="none" />
    <path d="M -160 -40 A 25 25 0 0 1 -160 10 L -175 10 L -175 -40 Z" fill="#FFFFFF" stroke="none" />

    <!-- 2. Roaring Flames Behind Tixie -->
    <path d="
      M -125 -135
      C -165 -180, -155 -260, -100 -285
      C -85 -240, -55 -225, -45 -195
      C -30 -265, -5 -325, 15 -322
      C 28 -270, 58 -230, 42 -175
      C 72 -205, 126 -265, 134 -215
      C 138 -180, 110 -150, 95 -135
      Z
    " fill="url(#flameOuter5)" />

    <path d="
      M -105 -140
      C -135 -180, -130 -240, -92 -260
      C -78 -220, -52 -210, -40 -185
      C -24 -240, -2 -295, 14 -290
      C 24 -245, 48 -210, 35 -165
      C 58 -190, 102 -235, 112 -195
      C 116 -165, 92 -145, 82 -135
      Z
    " fill="url(#flameMid5)" />

    <path d="
      M -80 -145
      C -105 -175, -95 -220, -75 -235
      C -65 -200, -45 -190, -32 -170
      C -18 -215, 2 -260, 14 -255
      C 22 -220, 36 -190, 28 -155
      C 45 -175, 78 -205, 85 -175
      C 88 -155, 70 -145, 62 -135
      Z
    " fill="url(#flameCore5)" />

    <!-- Side Flames from Headset -->
    <path d="M -180 -115 C -220 -95, -230 -40, -205 -10 C -190 -25, -180 -55, -175 -80 Z" fill="url(#flameOuter5)" />
    <path d="M -180 -105 C -210 -85, -218 -45, -198 -20 C -188 -35, -180 -60, -175 -75 Z" fill="url(#flameMid5)" />

    <path d="M 175 -115 C 215 -95, 225 -40, 200 -10 C 185 -25, 175 -55, 170 -80 Z" fill="url(#flameOuter5)" />
    <path d="M 175 -105 C 205 -85, 213 -45, 193 -20 C 183 -35, 175 -60, 170 -75 Z" fill="url(#flameMid5)" />

    <!-- Embers -->
    <circle cx="-135" cy="-210" r="7" fill="#F59E0B" />
    <circle cx="-135" cy="-210" r="3.5" fill="#FEF08A" />
    <circle cx="130" cy="-240" r="6" fill="#F97316" />
    <circle cx="130" cy="-240" r="3" fill="#FEF08A" />
    <circle cx="155" cy="-160" r="7.5" fill="#EF4444" />
    <circle cx="155" cy="-160" r="4" fill="#FDE047" />

    <!-- 3. Antenna (Blazing spark plug / burning wick) -->
    <path d="M 0 -150 L 0 -220" stroke="#78350F" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#EF4444" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#FEF08A" />

    <!-- 4. Head Ticket Shell (Heated Crimson/Orange Gradient) -->
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#fireHeadGrad)" stroke="#991B1B" stroke-width="2.5" />

    <!-- Flame Tongues on Top Edge of Head -->
    <path d="M -90 -160 C -105 -125, -80 -115, -88 -90 C -75 -110, -70 -135, -72 -160 Z" fill="#FDE047" opacity="0.9" />
    <path d="M 70 -160 C 88 -125, 68 -115, 76 -90 C 62 -110, 58 -135, 60 -160 Z" fill="#FDE047" opacity="0.9" />

    <!-- 5. Visor Screen -->
    <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGradFire)" stroke="#F97316" stroke-width="4" />

    <!-- 6. Panicked Face: Wide Shocked Anime Eyes with Fire Reflections -->
    <g transform="translate(-55, -45)">
      <circle cx="0" cy="0" r="26" fill="#FFFFFF" />
      <circle cx="0" cy="0" r="18" fill="#0F172A" />
      <path d="M -8 10 C -12 2, -6 -6, 0 -12 C 6 -6, 12 2, 8 10 C 4 6, -4 6, -8 10 Z" fill="#F59E0B" />
      <circle cx="-5" cy="-6" r="4.5" fill="#FFFFFF" />
      <circle cx="5" cy="5" r="2.5" fill="#FFFFFF" />
    </g>

    <g transform="translate(55, -45)">
      <circle cx="0" cy="0" r="26" fill="#FFFFFF" />
      <circle cx="0" cy="0" r="18" fill="#0F172A" />
      <path d="M -8 10 C -12 2, -6 -6, 0 -12 C 6 -6, 12 2, 8 10 C 4 6, -4 6, -8 10 Z" fill="#F59E0B" />
      <circle cx="-5" cy="-6" r="4.5" fill="#FFFFFF" />
      <circle cx="5" cy="5" r="2.5" fill="#FFFFFF" />
    </g>

    <!-- Flying Sweat Droplets from Panic -->
    <path d="M -95 -85 C -105 -75, -110 -68, -110 -60 C -110 -50, -102 -44, -94 -44 C -86 -44, -78 -50, -78 -60 C -78 -68, -85 -75, -95 -85 Z" fill="#38BDF8" stroke="#FFFFFF" stroke-width="2.5" />
    <path d="M 95 -85 C 105 -75, 110 -68, 110 -60 C 110 -50, 102 -44, 94 -44 C 86 -44, 78 -50, 78 -60 C 78 -68, 85 -75, 95 -85 Z" fill="#38BDF8" stroke="#FFFFFF" stroke-width="2.5" />

    <!-- Flushed Red Hot Cheeks -->
    <ellipse cx="-75" cy="-10" rx="16" ry="9" fill="#DC2626" opacity="0.9" />
    <ellipse cx="75" cy="-10" rx="16" ry="9" fill="#DC2626" opacity="0.9" />

    <!-- Open Panicked Screaming Mouth -->
    <path d="M -14 -12 Q 0 -22 14 -12 Q 18 10 0 12 Q -18 10 -14 -12 Z" fill="#EF4444" stroke="#FEF08A" stroke-width="3" stroke-linejoin="round" />
    <ellipse cx="0" cy="4" rx="8" ry="4" fill="#7F1D1D" />

    <!-- 7. Headset -->
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#1E293B" stroke-width="22" stroke-linecap="round" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#EA580C" stroke-width="8" stroke-linecap="round" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#EA580C" stroke-width="6" />
    <rect x="-200" y="-70" width="25" height="55" rx="12" fill="#78350F" />
    <rect x="165" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#EA580C" stroke-width="6" />
    <rect x="175" y="-70" width="25" height="55" rx="12" fill="#78350F" />
    <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke="#1E293B" stroke-width="10" stroke-linecap="round" />
    <circle cx="-70" cy="73" r="14" fill="#EF4444" stroke="#FFFFFF" stroke-width="4" />

    <!-- 8. Bottom Alert Pill: "PROD ON FIRE" -->
    <g transform="translate(0, 62)">
      <rect x="-70" y="-12" width="140" height="24" rx="12" fill="#0F172A" stroke="#EF4444" stroke-width="2" />
      <text y="4.5" font-family="'Noto Sans', monospace, sans-serif" font-size="9.5" font-weight="900" fill="#FEF08A" letter-spacing="2" text-anchor="middle">🔥 PROD ON FIRE</text>
    </g>
  </g>
</svg>"""

cutline_05 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">
  {svg_05.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">', '').replace('</svg>', '')}
  <g id="CutContour" transform="translate(270, 290)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
    <path d="M -120 -150 C -160 -190, -150 -265, -95 -290 C -75 -245, -55 -230, -45 -200 Z" stroke-width="26" />
    <path d="M -60 -170 C -60 -265, -15 -320, 15 -330 C 30 -275, 65 -235, 45 -180 Z" stroke-width="26" />
    <path d="M 30 -160 C 65 -215, 125 -275, 135 -225 C 140 -190, 115 -160, 100 -145 Z" stroke-width="26" />
    <path d="M -180 -120 C -225 -100, -235 -40, -210 -10 C -190 -30, -180 -60, -175 -85 Z" stroke-width="24" />
    <path d="M 175 -120 C 220 -100, 230 -40, 205 -10 C 185 -30, 175 -60, 170 -85 Z" stroke-width="24" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" stroke-width="46" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
    <path d="M -190 -10 C -190 70, -110 95, -75 75" stroke-width="26" />
    <circle cx="-70" cy="73" r="14" stroke-width="24" />
    <rect x="-75" y="48" width="150" height="28" rx="14" stroke-width="24" />
  </g>
</svg>"""

# ==============================================================================
# 6. STICKER 06: TIXIE NEON (SOFT CYBERPUNK SYNTHWAVE MASCOT)
# ==============================================================================
svg_06 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">
  <defs>
    <!-- Dark Cyber-Slate Body Gradient -->
    <linearGradient id="neonBodyGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#090D16" />
    </linearGradient>

    <!-- Neon Glow Gradient -->
    <linearGradient id="cyanMagentaGrad6" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F0FF" />
      <stop offset="50%" stop-color="#A855F7" />
      <stop offset="100%" stop-color="#FF007F" />
    </linearGradient>

    <!-- Visor Gradient -->
    <linearGradient id="neonVisorGrad6" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#050814" />
      <stop offset="100%" stop-color="#0E172E" />
    </linearGradient>
  </defs>

  <g id="Artwork" transform="translate(260, 275)">
    <!-- 1. White Die-Cut Contour -->
    <g id="WhiteBorder" fill="#FFFFFF" stroke="#FFFFFF" stroke-linejoin="round" stroke-linecap="round">
      <circle cx="0" cy="-230" r="22" stroke-width="24" />
      <line x1="0" y1="-150" x2="0" y2="-230" stroke-width="32" />
      <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke-width="46" />
      <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
      <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke-width="26" />
      <circle cx="-70" cy="73" r="14" stroke-width="24" />
      <path d="M -190 -10 C -190 60, -160 70, -160 70 L -160 10 L -160 -10 Z" stroke-width="12" />
    </g>

    <path d="M 160 -40 A 25 25 0 0 0 160 10 L 175 10 L 175 -40 Z" fill="#FFFFFF" stroke="none" />
    <path d="M -160 -40 A 25 25 0 0 1 -160 10 L -175 10 L -175 -40 Z" fill="#FFFFFF" stroke="none" />

    <!-- 2. Neon Antenna with Pulsing Glow Ring -->
    <path d="M 0 -150 L 0 -220" stroke="#334155" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#00F0FF" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#FF007F" />
    <circle cx="0" cy="-230" r="30" fill="none" stroke="#00F0FF" stroke-width="2" stroke-dasharray="6,4" opacity="0.8" />

    <!-- 3. Head Ticket Shell (Sleek Obsidian Chassis with Neon Outline) -->
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#neonBodyGrad6)" stroke="url(#cyanMagentaGrad6)" stroke-width="3.5" />

    <!-- Subtle Soft Cyber Panel Lines on Forehead/Cheek -->
    <path d="M -145 -145 L -120 -145 L -105 -130" fill="none" stroke="#00F0FF" stroke-width="1.8" opacity="0.6" stroke-linecap="round" />
    <path d="M 145 -145 L 120 -145 L 105 -130" fill="none" stroke="#FF007F" stroke-width="1.8" opacity="0.6" stroke-linecap="round" />

    <!-- 4. Screen Visor with Soft Neon Glow -->
    <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#neonVisorGrad6)" stroke="#00F0FF" stroke-width="3" />
    
    <!-- Delicate Cyber Scanline Mesh -->
    <g stroke="#00F0FF" stroke-width="0.8" opacity="0.12">
      <line x1="-120" y1="-95" x2="120" y2="-95" />
      <line x1="-120" y1="-65" x2="120" y2="-65" />
      <line x1="-120" y1="-35" x2="120" y2="-35" />
      <line x1="-120" y1="-5" x2="120" y2="-5" />
      <line x1="-120" y1="20" x2="120" y2="20" />
    </g>

    <!-- Top Screen Header: Cyber Neon Telemetry -->
    <text x="-105" y="-105" font-family="'Noto Sans', monospace, sans-serif" font-size="7.5" font-weight="900" fill="#00F0FF" letter-spacing="1.5">TIXIE // NEON-016</text>
    <text x="105" y="-105" font-family="'Noto Sans', monospace, sans-serif" font-size="7.5" font-weight="900" fill="#FF007F" letter-spacing="1.5" text-anchor="end">SYS: NOMINAL</text>

    <!-- 5. Both Signature Cute Anime Eyes with Vibrant Neon Glow & Catchlights -->
    <!-- Left Eye -->
    <g transform="translate(-55, -45)">
      <ellipse cx="0" cy="0" rx="25" ry="31" fill="none" stroke="#00F0FF" stroke-width="2" opacity="0.6" />
      <ellipse cx="0" cy="0" rx="23" ry="29" fill="#00F0FF" />
      <ellipse cx="0" cy="0" rx="19" ry="25" fill="#0284C7" />
      <polygon points="0,-12 3,-3 12,0 3,3 0,12 -3,3 -12,0 -3,-3" fill="#FFFFFF" transform="translate(-6, -7) scale(0.65)" />
      <circle cx="-6" cy="-8" r="7" fill="#FFFFFF" />
      <circle cx="7" cy="9" r="4.5" fill="#FFFFFF" />
      <circle cx="8" cy="-5" r="2.5" fill="#FF007F" />
    </g>

    <!-- Right Eye -->
    <g transform="translate(55, -45)">
      <ellipse cx="0" cy="0" rx="25" ry="31" fill="none" stroke="#FF007F" stroke-width="2" opacity="0.6" />
      <ellipse cx="0" cy="0" rx="23" ry="29" fill="#00F0FF" />
      <ellipse cx="0" cy="0" rx="19" ry="25" fill="#0284C7" />
      <polygon points="0,-12 3,-3 12,0 3,3 0,12 -3,3 -12,0 -3,-3" fill="#FFFFFF" transform="translate(-6, -7) scale(0.65)" />
      <circle cx="-6" cy="-8" r="7" fill="#FFFFFF" />
      <circle cx="7" cy="9" r="4.5" fill="#FFFFFF" />
      <circle cx="8" cy="-5" r="2.5" fill="#FF007F" />
    </g>

    <!-- Cyber Neon Blush -->
    <g transform="translate(-75, -5)">
      <ellipse cx="0" cy="0" rx="16" ry="9" fill="#FF007F" opacity="0.85" />
      <line x1="-10" y1="0" x2="10" y2="0" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" />
    </g>
    <g transform="translate(75, -5)">
      <ellipse cx="0" cy="0" rx="16" ry="9" fill="#FF007F" opacity="0.85" />
      <line x1="-10" y1="0" x2="10" y2="0" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" />
    </g>

    <!-- Adorable Neon Smile -->
    <path d="M -16 -4 Q -8 8 0 0 Q 8 8 16 -4" fill="none" stroke="#00F0FF" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />

    <!-- 6. Cyber Headset -->
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#1E293B" stroke-width="22" stroke-linecap="round" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="url(#cyanMagentaGrad6)" stroke-width="8" stroke-linecap="round" />
    
    <!-- Left Earcup with Neon Equalizer Bands -->
    <rect x="-210" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#00F0FF" stroke-width="5" />
    <rect x="-200" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <line x1="-196" y1="-55" x2="-178" y2="-55" stroke="#FF007F" stroke-width="3" stroke-linecap="round" />
    <line x1="-196" y1="-42" x2="-178" y2="-42" stroke="#00F0FF" stroke-width="3" stroke-linecap="round" />
    <line x1="-196" y1="-30" x2="-178" y2="-30" stroke="#FF007F" stroke-width="3" stroke-linecap="round" />

    <!-- Right Earcup -->
    <rect x="165" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#FF007F" stroke-width="5" />
    <rect x="175" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <line x1="178" y1="-55" x2="196" y2="-55" stroke="#00F0FF" stroke-width="3" stroke-linecap="round" />
    <line x1="178" y1="-42" x2="196" y2="-42" stroke="#FF007F" stroke-width="3" stroke-linecap="round" />
    <line x1="178" y1="-30" x2="196" y2="-30" stroke="#00F0FF" stroke-width="3" stroke-linecap="round" />

    <!-- Boom Mic with Neon Cyan Node -->
    <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke="#1E293B" stroke-width="10" stroke-linecap="round" />
    <circle cx="-70" cy="73" r="14" fill="#00F0FF" stroke="#FFFFFF" stroke-width="4" />
    <circle cx="-70" cy="73" r="6" fill="#FF007F" />
  </g>
</svg>"""

cutline_06 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">
  {svg_06.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">', '').replace('</svg>', '')}
  <g id="CutContour" transform="translate(260, 275)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
    <circle cx="0" cy="-230" r="22" stroke-width="24" />
    <line x1="0" y1="-150" x2="0" y2="-230" stroke-width="32" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" stroke-width="46" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
    <path d="M -190 -10 C -190 70, -110 95, -75 75" stroke-width="26" />
    <circle cx="-70" cy="73" r="14" stroke-width="24" />
  </g>
</svg>"""

# ==============================================================================
# 7. STICKER 07: VINTAGE POSTAL STAMP (EMERALD 200 OK • ACCURATE MASTER MARK)
# ==============================================================================
svg_07 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 460" width="460" height="460">
  <defs>
    <!-- Midnight Navy Dispatch Canvas -->
    <linearGradient id="stampBg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="100%" stop-color="#1E293B" />
    </linearGradient>

    <!-- 24K Gold Laurel Gradient -->
    <linearGradient id="goldGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDE047" />
      <stop offset="50%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>

    <!-- Official TixDesk Master Logo Gradient (Royal Blue -> Cerulean -> Cyan) -->
    <linearGradient id="tixdeskMasterGrad7" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3877F6" />
      <stop offset="50%" stop-color="#4CA2EA" />
      <stop offset="100%" stop-color="#5AC1C4" />
    </linearGradient>

    <filter id="stampTextShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#022C22" flood-opacity="0.95" />
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="#000000" flood-opacity="0.8" />
    </filter>
  </defs>

  <g id="Artwork" transform="translate(230, 230)">
    <!-- 1. White Die-Cut Base -->
    <rect x="-150" y="-175" width="300" height="350" rx="20" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="16" stroke-linejoin="round" />

    <!-- 2. Main Postage Stamp Inner Canvas -->
    <rect x="-140" y="-165" width="280" height="330" rx="14" fill="url(#stampBg7)" stroke="#F59E0B" stroke-width="3" />

    <!-- Vintage Engraved Banknote Guilloche Double Border -->
    <rect x="-132" y="-157" width="264" height="314" rx="10" fill="none" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.8" />
    <rect x="-126" y="-151" width="252" height="302" rx="8" fill="none" stroke="#64748B" stroke-width="1" opacity="0.5" />

    <circle cx="-122" cy="-147" r="3" fill="#F59E0B" />
    <circle cx="122" cy="-147" r="3" fill="#F59E0B" />
    <circle cx="-122" cy="147" r="3" fill="#F59E0B" />
    <circle cx="122" cy="147" r="3" fill="#F59E0B" />

    <!-- Top Postal Header -->
    <text x="0" y="-128" font-family="'Noto Sans', serif, sans-serif" font-size="11" font-weight="900" fill="#F8FAFC" letter-spacing="3" text-anchor="middle">TIXDESK OFFICIAL DISPATCH</text>
    <text x="0" y="-114" font-family="'Noto Sans', sans-serif" font-size="8" font-weight="700" fill="#94A3B8" letter-spacing="2" text-anchor="middle">★ GLOBAL HELPDESK STANDARD ★</text>

    <!-- Nominal Value in Stamp Corners -->
    <text x="-105" y="-90" font-family="'Noto Sans', monospace, sans-serif" font-size="14" font-weight="900" fill="#34D399">200</text>
    <text x="-105" y="-78" font-family="'Noto Sans', monospace, sans-serif" font-size="8" font-weight="800" fill="#10B981">OK</text>
    
    <text x="105" y="-90" font-family="'Noto Sans', monospace, sans-serif" font-size="14" font-weight="900" fill="#34D399" text-anchor="end">SLA</text>
    <text x="105" y="-78" font-family="'Noto Sans', monospace, sans-serif" font-size="8" font-weight="800" fill="#10B981" text-anchor="end">MET</text>

    <!-- 3. Central Medallion: Golden Wreath & EXACT MASTER TIXDESK LOGO -->
    <g transform="translate(0, -10)">
      <g fill="none" stroke="url(#goldGrad7)" stroke-width="3" stroke-linecap="round">
        <path d="M -15 65 C -65 50, -75 -25, -20 -60" />
        <path d="M 15 65 C 65 50, 75 -25, 20 -60" />
      </g>
      <g fill="url(#goldGrad7)">
        <ellipse cx="-35" cy="-50" rx="7" ry="4" transform="rotate(35, -35, -50)" />
        <ellipse cx="-55" cy="-28" rx="8" ry="4.5" transform="rotate(15, -55, -28)" />
        <ellipse cx="-62" cy="0" rx="8" ry="4.5" transform="rotate(-5, -62, 0)" />
        <ellipse cx="-55" cy="28" rx="8" ry="4.5" transform="rotate(-25, -55, 28)" />
        <ellipse cx="-35" cy="52" rx="7" ry="4" transform="rotate(-45, -35, 52)" />

        <ellipse cx="35" cy="-50" rx="7" ry="4" transform="rotate(-35, 35, -50)" />
        <ellipse cx="55" cy="-28" rx="8" ry="4.5" transform="rotate(-15, 55, -28)" />
        <ellipse cx="62" cy="0" rx="8" ry="4.5" transform="rotate(5, 62, 0)" />
        <ellipse cx="55" cy="28" rx="8" ry="4.5" transform="rotate(25, 55, 28)" />
        <ellipse cx="35" cy="52" rx="7" ry="4" transform="rotate(45, 35, 52)" />
      </g>

      <!-- EXACT AUTHENTIC TIXDESK MASTER MARK (Identical to Sticker 01) -->
      <g transform="translate(0, -6) scale(0.38)">
        <path d="{path_01_body}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="18" stroke-linejoin="round" />
        <path d="{path_01_body}" fill="url(#tixdeskMasterGrad7)" />
        <path d="{path_01_t}" fill="#FFFFFF" />
      </g>

      <!-- 5 CSAT Stars -->
      <g transform="translate(0, 48)" fill="url(#goldGrad7)">
        <polygon points="0,-8 2,-2 8,-2 3,2 5,8 0,4 -5,8 -3,2 -8,-2 -2,-2" transform="translate(-44, 0) scale(1.1)" />
        <polygon points="0,-8 2,-2 8,-2 3,2 5,8 0,4 -5,8 -3,2 -8,-2 -2,-2" transform="translate(-22, 0) scale(1.1)" />
        <polygon points="0,-8 2,-2 8,-2 3,2 5,8 0,4 -5,8 -3,2 -8,-2 -2,-2" transform="translate(0, 0) scale(1.3)" />
        <polygon points="0,-8 2,-2 8,-2 3,2 5,8 0,4 -5,8 -3,2 -8,-2 -2,-2" transform="translate(22, 0) scale(1.1)" />
        <polygon points="0,-8 2,-2 8,-2 3,2 5,8 0,4 -5,8 -3,2 -8,-2 -2,-2" transform="translate(44, 0) scale(1.1)" />
      </g>
      <text x="0" y="68" font-family="'Noto Sans', sans-serif" font-size="8" font-weight="800" fill="#FDE047" letter-spacing="1.5" text-anchor="middle">100% CSAT SATISFACTION</text>
    </g>

    <!-- Bottom Postal Certification Strip -->
    <rect x="-115" y="95" width="230" height="35" rx="6" fill="#047857" opacity="0.25" stroke="#10B981" stroke-width="1.5" />
    <text x="0" y="110" font-family="'Noto Sans', monospace, sans-serif" font-size="9" font-weight="900" fill="#34D399" letter-spacing="2" text-anchor="middle">BUSINESS SLA • MET</text>
    <text x="0" y="122" font-family="'Noto Sans', sans-serif" font-size="7" font-weight="700" fill="#94A3B8" letter-spacing="1" text-anchor="middle">ISO/IEC 20000 SERVICE DESK COMPLIANT</text>

    <!-- 4. OFFICIAL EMERALD POSTMARK CANCELLATION STAMP (WITH CRISP DROP SHADOW & HIGH VISIBILITY) -->
    <g transform="rotate(-13) translate(-8, 5)">
      <rect x="-106" y="-27" width="212" height="54" rx="10" fill="#022C22" fill-opacity="0.85" stroke="#10B981" stroke-width="3" stroke-dasharray="14,2" />
      <rect x="-101" y="-22" width="202" height="44" rx="7" fill="none" stroke="#34D399" stroke-width="1.5" />

      <g filter="url(#stampTextShadow)">
        <text x="0" y="-4" font-family="'Noto Sans', sans-serif" font-size="14.5" font-weight="900" fill="#A7F3D0" letter-spacing="2.5" text-anchor="middle">★ TICKET RESOLVED ★</text>
        <text x="0" y="13" font-family="'Noto Sans', monospace, sans-serif" font-size="11" font-weight="900" fill="#FFFFFF" letter-spacing="3" text-anchor="middle">STATUS: 200 OK</text>
      </g>
    </g>

    <!-- Wavy Emerald Cancellation Waves -->
    <g stroke="#10B981" stroke-width="2.5" fill="none" opacity="0.85" transform="translate(50, -110) rotate(-13)">
      <path d="M 0 0 C 10 -6, 20 6, 30 0 C 40 -6, 50 6, 60 0 C 70 -6, 80 6, 90 0" />
      <path d="M 0 8 C 10 2, 20 14, 30 8 C 40 2, 50 14, 60 8 C 70 2, 80 14, 90 8" />
      <path d="M 0 16 C 10 10, 20 22, 30 16 C 40 10, 50 22, 60 16 C 70 10, 80 22, 90 16" />
    </g>
  </g>
</svg>"""

cutline_07 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 460" width="460" height="460">
  {svg_07.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 460" width="460" height="460">', '').replace('</svg>', '')}
  <g id="CutContour" transform="translate(230, 230)">
    <rect x="-150" y="-175" width="300" height="350" rx="20" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" />
  </g>
</svg>"""
# BATCH GENERATION FOR ALL 7 STICKERS
# ==============================================================================
items = [
    ("tixdesk-sticker-01-hero-mark", svg_01, cutline_01),
    ("tixdesk-sticker-02-mascot-tixie", svg_02, cutline_02),
    ("tixdesk-sticker-03-retro-pixel-arcade", svg_03, cutline_03),
    ("tixdesk-sticker-04-tixie-caffeine-nightshift", svg_04, cutline_04),
    ("tixdesk-sticker-05-tixie-sla-firefighter", svg_05, cutline_05),
    ("tixdesk-sticker-06-cyber-neon-decal", svg_06, cutline_06),
    ("tixdesk-sticker-07-vintage-postal-stamp", svg_07, cutline_07),
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

print("Generated full 7-sticker collection successfully!")
