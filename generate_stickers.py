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
# 5. STICKER 05: TIXIE SLA INCIDENT FIREFIGHTER (PANIC MODE > < / ZERO DOWNTIME)
# ==============================================================================
svg_05 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">
  <defs>
    <linearGradient id="headGrad5" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3877F6" />
      <stop offset="50%" stop-color="#4CA2EA" />
      <stop offset="100%" stop-color="#5AC1C4" />
    </linearGradient>
    <linearGradient id="screenGrad5" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#080E1E" />
      <stop offset="100%" stop-color="#111C35" />
    </linearGradient>
    <linearGradient id="extGrad5" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#EF4444" />
      <stop offset="50%" stop-color="#F87171" />
      <stop offset="100%" stop-color="#DC2626" />
    </linearGradient>
    <linearGradient id="sirenGrad5" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#EF4444" />
      <stop offset="100%" stop-color="#F59E0B" />
    </linearGradient>
  </defs>

  <g id="Artwork" transform="translate(260, 265)">
    <!-- 1. White Die-Cut Contour -->
    <g id="WhiteBorder" fill="#FFFFFF" stroke="#FFFFFF" stroke-linejoin="round" stroke-linecap="round">
      <circle cx="0" cy="-230" r="26" stroke-width="24" />
      <line x1="0" y1="-150" x2="0" y2="-230" stroke-width="32" />
      <path d="M -38 -245 C -45 -230, -45 -215, -38 -200" fill="none" stroke-width="16" />
      <path d="M 38 -245 C 45 -230, 45 -215, 38 -200" fill="none" stroke-width="16" />

      <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke-width="46" />
      <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
      <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke-width="26" />
      <circle cx="-70" cy="73" r="14" stroke-width="24" />
      <path d="M -190 -10 C -190 60, -160 70, -160 70 L -160 10 L -160 -10 Z" stroke-width="12" />

      <rect x="-25" y="45" width="55" height="80" rx="16" stroke-width="24" />
      <rect x="-15" y="28" width="35" height="20" rx="6" stroke-width="20" />
      <path d="M 10 35 C 35 30, 45 45, 50 35" fill="none" stroke-width="18" />
      <circle cx="65" cy="30" r="18" stroke-width="22" />
      <circle cx="85" cy="22" r="16" stroke-width="22" />
      <circle cx="95" cy="38" r="16" stroke-width="22" />
      <circle cx="75" cy="45" r="14" stroke-width="22" />
    </g>

    <path d="M 160 -40 A 25 25 0 0 0 160 10 L 175 10 L 175 -40 Z" fill="#FFFFFF" stroke="none" />
    <path d="M -160 -40 A 25 25 0 0 1 -160 10 L -175 10 L -175 -40 Z" fill="#FFFFFF" stroke="none" />

    <!-- Emergency Siren on Antenna -->
    <path d="M 0 -150 L 0 -210" stroke="#64748B" stroke-width="12" stroke-linecap="round" />
    <rect x="-16" y="-215" width="32" height="8" rx="3" fill="#334155" />
    <path d="M -14 -215 L -10 -242 Q 0 -248, 10 -242 L 14 -215 Z" fill="url(#sirenGrad5)" stroke="#FFFFFF" stroke-width="3" />
    <line x1="-5" y1="-238" x2="-5" y2="-220" stroke="#FEF08A" stroke-width="3" stroke-linecap="round" />
    <path d="M -34 -238 C -40 -228, -40 -218, -34 -208" fill="none" stroke="#EF4444" stroke-width="4.5" stroke-linecap="round" />
    <path d="M 34 -238 C 40 -228, 40 -218, 34 -208" fill="none" stroke="#EF4444" stroke-width="4.5" stroke-linecap="round" />

    <!-- Head Ticket Shell -->
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#headGrad5)" stroke="#1D4ED8" stroke-width="2.5" />

    <!-- Visor -->
    <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGrad5)" stroke="#38BDF8" stroke-width="4" />
    <path d="M -115 -105 Q 0 -125 115 -105 L 115 -90 Q 0 -110 -115 -90 Z" fill="#FFFFFF" opacity="0.24" />

    <!-- Anime Panic (> <) Eyes -->
    <g transform="translate(-55, -45)">
      <path d="M -18 -18 L 12 0 L -18 18" fill="none" stroke="#38BDF8" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M -15 -15 L 8 0 L -15 15" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
    </g>
    <g transform="translate(55, -45)">
      <path d="M 18 -18 L -12 0 L 18 18" fill="none" stroke="#38BDF8" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M 15 -15 L -8 0 L 15 15" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
    </g>

    <!-- Sweat Drop on Visor -->
    <path d="M -90 -85 C -98 -75, -102 -68, -102 -62 C -102 -54, -96 -48, -88 -48 C -80 -48, -74 -54, -74 -62 C -74 -68, -78 -75, -86 -85 Z" fill="#38BDF8" stroke="#FFFFFF" stroke-width="2.5" />

    <ellipse cx="-70" cy="-15" rx="16" ry="9" fill="#F43F5E" opacity="0.9" />
    <ellipse cx="70" cy="-15" rx="16" ry="9" fill="#F43F5E" opacity="0.9" />

    <path d="M -14 -12 Q 0 -22 14 -12 Q 0 8 -14 -12 Z" fill="#F43F5E" stroke="#38BDF8" stroke-width="3.5" stroke-linejoin="round" />
    <path d="M -5 -15 L 0 -11 L 5 -15 Z" fill="#FFFFFF" />

    <!-- Headset -->
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#1E293B" stroke-width="22" stroke-linecap="round" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#38BDF8" stroke-width="8" stroke-linecap="round" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="-200" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <rect x="165" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="175" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke="#1E293B" stroke-width="10" stroke-linecap="round" />
    <circle cx="-70" cy="73" r="14" fill="#EF4444" stroke="#FFFFFF" stroke-width="4" />

    <!-- Fire Extinguisher & Frost Foam Puff -->
    <rect x="-22" y="48" width="48" height="75" rx="14" fill="url(#extGrad5)" stroke="#991B1B" stroke-width="3" />
    <rect x="-14" y="32" width="32" height="18" rx="5" fill="#94A3B8" stroke="#475569" stroke-width="2.5" />
    <circle cx="2" cy="41" r="6" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.5" />
    <line x1="2" y1="41" x2="4" y2="38" stroke="#10B981" stroke-width="1.5" />
    
    <!-- Clean Unobstructed ZERO DOWNTIME Label -->
    <rect x="-18" y="65" width="40" height="28" rx="4" fill="#FFFFFF" />
    <text x="2" y="76" font-family="'Noto Sans', sans-serif" font-size="8" font-weight="900" fill="#DC2626" text-anchor="middle">ZERO</text>
    <text x="2" y="88" font-family="'Noto Sans', sans-serif" font-size="7.5" font-weight="900" fill="#1E293B" text-anchor="middle">DOWNTIME</text>

    <!-- Hose & Discharge Nozzle -->
    <path d="M 14 38 C 32 35, 42 46, 48 38" fill="none" stroke="#1E293B" stroke-width="6" stroke-linecap="round" />
    <polygon points="46,34 56,38 46,42" fill="#64748B" />

    <!-- Frosty Foam Cloud Puff -->
    <g fill="#E0F2FE" stroke="#38BDF8" stroke-width="3.5">
      <circle cx="66" cy="32" r="16" />
      <circle cx="84" cy="24" r="14" />
      <circle cx="96" cy="38" r="14" />
      <circle cx="78" cy="44" r="13" />
    </g>
    <circle cx="84" cy="24" r="3.5" fill="#FFFFFF" />
    <circle cx="70" cy="32" r="4" fill="#FFFFFF" />
    <circle cx="92" cy="38" r="3" fill="#FFFFFF" />

    <!-- Cute Chibi Hands on SIDES of Extinguisher (Clean, Zero Text Obstruction!) -->
    <circle cx="-25" cy="78" r="11" fill="#3877F6" stroke="#FFFFFF" stroke-width="3" />
    <circle cx="29" cy="78" r="11" fill="#5AC1C4" stroke="#FFFFFF" stroke-width="3" />
  </g>
</svg>"""

cutline_05 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">
  {svg_05.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">', '').replace('</svg>', '')}
  <g id="CutContour" transform="translate(260, 265)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
    <circle cx="0" cy="-230" r="26" stroke-width="24" />
    <line x1="0" y1="-150" x2="0" y2="-230" stroke-width="32" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" stroke-width="46" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
    <circle cx="-70" cy="73" r="14" stroke-width="24" />
    <circle cx="85" cy="22" r="16" stroke-width="22" />
  </g>
</svg>"""

# ==============================================================================
# 6. STICKER 06: HOLOGRAPHIC CYBER NEON / SYNTHWAVE DECAL
# ==============================================================================
path_06_contour = """
  M 0 -115
  L 125 -115
  A 26 26 0 0 1 151 -89
  L 151 -35
  A 20 20 0 0 0 151 5
  L 151 55
  A 26 26 0 0 1 125 81
  L 20 81
  L -20 81
  L -70 142
  A 12 12 0 0 1 -82 136
  L -82 81
  L -125 81
  A 26 26 0 0 1 -151 55
  L -151 5
  A 20 20 0 0 0 -151 -35
  L -151 -89
  A 26 26 0 0 1 -125 -115
  Z
"""

svg_06 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 460" width="460" height="460">
  <defs>
    <linearGradient id="cyberNeon6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" />
      <stop offset="50%" stop-color="#A855F7" />
      <stop offset="100%" stop-color="#FF007F" />
    </linearGradient>

    <radialGradient id="carbonPlate6" cx="50%" cy="45%" r="65%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="70%" stop-color="#070A12" />
      <stop offset="100%" stop-color="#020408" />
    </radialGradient>
  </defs>

  <g id="Artwork" transform="translate(230, 215)">
    <!-- 1. White Die-Cut Contour -->
    <path id="WhiteBorder" d="{path_06_contour}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="22" stroke-linejoin="round" stroke-linecap="round" />

    <!-- 2. Dark Carbon Cyberplate Ticket Body -->
    <path id="CyberBody" d="{path_06_contour}" fill="url(#carbonPlate6)" stroke="url(#cyberNeon6)" stroke-width="3.5" />

    <!-- 3. Isometric Cyber Mesh Lines -->
    <g opacity="0.18" stroke="#00F0FF" stroke-width="1">
      <line x1="-130" y1="-80" x2="130" y2="-80" />
      <line x1="-130" y1="-40" x2="130" y2="-40" />
      <line x1="-130" y1="0" x2="130" y2="0" />
      <line x1="-130" y1="40" x2="130" y2="40" />
      <line x1="-90" y1="-100" x2="-90" y2="70" />
      <line x1="-45" y1="-100" x2="-45" y2="70" />
      <line x1="45" y1="-100" x2="45" y2="70" />
      <line x1="90" y1="-100" x2="90" y2="70" />
    </g>

    <!-- 4. Glowing PCB Circuit Traces -->
    <path d="M -135 -70 L -95 -70 L -75 -50 L -45 -50" fill="none" stroke="#00F0FF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
    <circle cx="-135" cy="-70" r="4" fill="#00F0FF" />
    <circle cx="-45" cy="-50" r="3.5" fill="#A855F7" />

    <path d="M -135 40 L -95 40 L -70 15 L -35 15" fill="none" stroke="#00F0FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
    <circle cx="-135" cy="40" r="3.5" fill="#00F0FF" />

    <path d="M -75 110 L -65 95 L -35 95" fill="none" stroke="#00F0FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
    <circle cx="-75" cy="110" r="3" fill="#00F0FF" />

    <path d="M 135 -70 L 95 -70 L 75 -50 L 45 -50" fill="none" stroke="#FF007F" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
    <circle cx="135" cy="-70" r="4" fill="#FF007F" />
    <circle cx="45" cy="-50" r="3.5" fill="#A855F7" />

    <path d="M 135 40 L 95 40 L 70 15 L 35 15" fill="none" stroke="#FF007F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
    <circle cx="135" cy="40" r="3.5" fill="#FF007F" />

    <!-- 5. RADIANT CENTRAL 'T' CORE -->
    <path d="M -65 -60 L 65 -60 A 18 18 0 0 1 65 -24 L 20 -24 L 20 46 L -20 46 L -20 -24 L -65 -24 A 18 18 0 0 1 -65 -60 Z" fill="none" stroke="#00F0FF" stroke-width="7" opacity="0.4" stroke-linejoin="round" />
    <path d="M -65 -60 L 65 -60 A 18 18 0 0 1 65 -24 L 20 -24 L 20 46 L -20 46 L -20 -24 L -65 -24 A 18 18 0 0 1 -65 -60 Z" fill="url(#cyberNeon6)" stroke="#FFFFFF" stroke-width="2" stroke-linejoin="round" />
    
    <line x1="-50" y1="-42" x2="50" y2="-42" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" opacity="0.9" />
    <line x1="0" y1="-42" x2="0" y2="36" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" opacity="0.9" />
    <circle cx="0" cy="-42" r="4" fill="#FFFFFF" />

    <!-- 6. Stencil Tech HUD Typography -->
    <text x="0" y="-95" font-family="'Noto Sans', monospace, sans-serif" font-size="8.5" font-weight="800" fill="#00F0FF" letter-spacing="2" text-anchor="middle">SYS: NOMINAL // SLA: 100%</text>
    <text x="0" y="68" font-family="'Noto Sans', monospace, sans-serif" font-size="8.5" font-weight="800" fill="#FF007F" letter-spacing="2" text-anchor="middle">UNIT-016 // CORE-OK</text>

    <path d="M -125 -95 L -138 -95 L -138 -82" fill="none" stroke="#00F0FF" stroke-width="2" />
    <path d="M 125 -95 L 138 -95 L 138 -82" fill="none" stroke="#FF007F" stroke-width="2" />
    <path d="M 125 65 L 138 65 L 138 52" fill="none" stroke="#FF007F" stroke-width="2" />

    <text x="-136" y="-10" font-family="monospace" font-size="6" font-weight="700" fill="#64748B">0101</text>
    <text x="122" y="-10" font-family="monospace" font-size="6" font-weight="700" fill="#64748B">1010</text>
  </g>
</svg>"""

cutline_06 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 460" width="460" height="460">
  {svg_06.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 460" width="460" height="460">', '').replace('</svg>', '')}
  <g id="CutContour" transform="translate(230, 215)">
    <path d="{path_06_contour}" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" />
  </g>
</svg>"""

# ==============================================================================
# 7. STICKER 07: "TICKET RESOLVED • 200 OK" VINTAGE POSTAL STAMP / BADGE
# ==============================================================================
svg_07 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 460" width="460" height="460">
  <defs>
    <linearGradient id="stampBg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="100%" stop-color="#1E293B" />
    </linearGradient>

    <linearGradient id="goldGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDE047" />
      <stop offset="50%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>

    <linearGradient id="cyanGold7" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
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
    <text x="-105" y="-90" font-family="'Noto Sans', monospace, sans-serif" font-size="14" font-weight="900" fill="#38BDF8">200</text>
    <text x="-105" y="-78" font-family="'Noto Sans', monospace, sans-serif" font-size="8" font-weight="800" fill="#34D399">OK</text>
    
    <text x="105" y="-90" font-family="'Noto Sans', monospace, sans-serif" font-size="14" font-weight="900" fill="#38BDF8" text-anchor="end">SLA</text>
    <text x="105" y="-78" font-family="'Noto Sans', monospace, sans-serif" font-size="8" font-weight="800" fill="#34D399" text-anchor="end">MET</text>

    <!-- 3. Central Medallion: Golden Wreath & TixDesk Ticket Emblem -->
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

      <g transform="scale(0.48) translate(0, -15)">
        <path d="
          M 0 -75
          L 80 -75
          A 20 20 0 0 1 100 -55
          L 100 -25
          A 15 15 0 0 0 100 5
          L 100 35
          A 20 20 0 0 1 80 55
          L -50 55
          L -90 95
          A 10 10 0 0 1 -100 90
          L -100 55
          A 20 20 0 0 1 -100 -55
          L -100 -25
          A 15 15 0 0 0 -100 5
          Z
        " fill="url(#cyanGold7)" stroke="#FFFFFF" stroke-width="4" />
        <path d="
          M -45 -40
          L 45 -40
          A 12 12 0 0 1 45 -16
          L 15 -16
          L 15 45
          L -15 45
          L -15 -16
          L -45 -16
          A 12 12 0 0 1 -45 -40
          Z
        " fill="#FFFFFF" />
      </g>

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
    <rect x="-115" y="95" width="230" height="35" rx="6" fill="#0284C7" opacity="0.2" stroke="#38BDF8" stroke-width="1.5" />
    <text x="0" y="110" font-family="'Noto Sans', monospace, sans-serif" font-size="9" font-weight="900" fill="#38BDF8" letter-spacing="2" text-anchor="middle">BUSINESS SLA • MET</text>
    <text x="0" y="122" font-family="'Noto Sans', sans-serif" font-size="7" font-weight="700" fill="#94A3B8" letter-spacing="1" text-anchor="middle">ISO/IEC 20000 SERVICE DESK COMPLIANT</text>

    <!-- 4. OFFICIAL RUBBER POSTMARK CANCELLATION STAMP -->
    <g transform="rotate(-13) translate(-8, 5)">
      <rect x="-105" y="-26" width="210" height="52" rx="10" fill="#EF4444" fill-opacity="0.15" stroke="#EF4444" stroke-width="3" stroke-dasharray="14,2" />
      <rect x="-100" y="-21" width="200" height="42" rx="7" fill="none" stroke="#EF4444" stroke-width="1.5" />

      <text x="0" y="-4" font-family="'Noto Sans', sans-serif" font-size="14" font-weight="900" fill="#EF4444" letter-spacing="2" text-anchor="middle">★ TICKET RESOLVED ★</text>
      <text x="0" y="12" font-family="'Noto Sans', monospace, sans-serif" font-size="10" font-weight="900" fill="#FFFFFF" letter-spacing="2.5" text-anchor="middle">STATUS: 200 OK</text>
    </g>

    <!-- Wavy Cancellation Waves -->
    <g stroke="#EF4444" stroke-width="2" fill="none" opacity="0.75" transform="translate(50, -110) rotate(-13)">
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

# ==============================================================================
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
