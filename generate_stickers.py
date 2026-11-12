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
# - Symmetrical 'T' glyph: Crossbar thickness == Vertical stem width == 40px!
# - Solid pure white (#FFFFFF), zero black gaps, zero slits.
# - Contour-hugging white die-cut border that follows the curves of the tail
#   and baseline without straight diagonal shortcuts.
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
    <!-- 1. White die-cut contour that closely follows design curves & tail -->
    <path id="WhiteBorder" d="{path_01_contour}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="24" stroke-linejoin="round" stroke-linecap="round" />
    
    <!-- 2. Official Blue/Cyan Gradient body (tail is gradient) -->
    <path id="TicketBody" d="{path_01_body}" fill="url(#tixdeskGrad)" />

    <!-- 3. SOLID WHITE SYMMETRICAL 'T' GLYPH (100% solid white, stem = bar = 40px) -->
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
# 2. STICKER 02: KAWAII CHIBI MASCOT HEAD (NOTCHES PRESERVED, WHITE GAP FILL)
# - Iconic ticket-shaped head with notches preserved adjacent to headset!
# - Gap between notch and headset earcups is filled with solid white (#FFFFFF),
#   eliminating dark background show-through while retaining ticket notches.
# - Thinned-down white die-cut border closely hugging the antenna, headset,
#   earcups, mic, and speech tail (matching Sticker 01 thinness).
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
    </g>

    <!-- 2. Solid White Gap Fills inside the ticket notches (stroke=none, cleanly behind earcups) -->
    <path d="M 160 -40 A 25 25 0 0 0 160 10 L 175 10 L 175 -40 Z" fill="#FFFFFF" stroke="none" />
    <path d="M -160 -40 A 25 25 0 0 1 -160 10 L -175 10 L -175 -40 Z" fill="#FFFFFF" stroke="none" />

    <!-- 2. Antenna -->
    <path d="M 0 -150 L 0 -220" stroke="#64748B" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#10B981" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#6EE7B7" />

    <!-- 3. Head Ticket Shell (Preserves iconic ticket notches!) -->
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#headGrad)" stroke="#1D4ED8" stroke-width="2.5" />

    <!-- 4. Screen Visor -->
    <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGrad)" stroke="#38BDF8" stroke-width="4" />
    <path d="M -115 -105 Q 0 -125 115 -105 L 115 -90 Q 0 -110 -115 -90 Z" fill="#FFFFFF" opacity="0.24" />

    <!-- 5. Eyes & Expression -->
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

    <!-- 6. Headset -->
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
    </g>

    <!-- Solid White Gap Fills inside the ticket notches -->
    <path d="M 160 -40 A 25 25 0 0 0 160 10 L 175 10 L 175 -40 Z" fill="#FFFFFF" stroke="none" />
    <path d="M -160 -40 A 25 25 0 0 1 -160 10 L -175 10 L -175 -40 Z" fill="#FFFFFF" stroke="none" />

    <!-- Antenna -->
    <path d="M 0 -150 L 0 -220" stroke="#64748B" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#10B981" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#6EE7B7" />

    <!-- Head Ticket Shell -->
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#headGrad)" stroke="#1D4ED8" stroke-width="2.5" />

    <!-- Screen Visor -->
    <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGrad)" stroke="#38BDF8" stroke-width="4" />
    <path d="M -115 -105 Q 0 -125 115 -105 L 115 -90 Q 0 -110 -115 -90 Z" fill="#FFFFFF" opacity="0.24" />

    <!-- Eyes & Expression -->
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

    <!-- Headset -->
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
# 3. STICKER 03: RETRO PIXEL ART ARCADE (PURE RETRO CHARACTER EDITION)
# - Extraneous gaming overlays (hearts, SLA text banner, green HP bar) REMOVED!
# - Pure focus on the cool retro pixel arcade ticket mascot:
#   * Symmetrical 50/50 royal blue & cyan split face
#   * 8-bit black sunglasses with specular white catchlights
#   * Pixel blush, centered cat mouth, and stepped dialogue tail
#   * Sleek, contour-hugging white die-cut border with rounded corners
# ==============================================================================
path_contour_03_clean = """
  M -145 -165
  L 145 -165
  A 20 20 0 0 1 165 -145
  L 165 -45
  Q 142 -12, 165 20
  L 165 85
  A 20 20 0 0 1 145 105
  L -85 105
  L -155 165
  A 12 12 0 0 1 -175 155
  L -175 105
  L -165 20
  Q -142 -12, -165 -45
  L -165 -145
  A 20 20 0 0 1 -145 -165
  Z
"""

svg_03 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 460" width="460" height="460">
  <g id="Artwork" transform="translate(230, 220)">
    <!-- 1. White die-cut contour -->
    <path id="WhiteBorder" d="{path_contour_03_clean}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="22" stroke-linejoin="round" stroke-linecap="round" />

    <!-- 2. Ticket Body (Clean 50/50 Split) -->
    <rect x="-160" y="-145" width="160" height="250" fill="#3877F6" />
    <rect x="0" y="-145" width="160" height="250" fill="#5AC1C4" />
    
    <!-- Ticket Notches -->
    <rect x="-180" y="-35" width="30" height="45" fill="#FFFFFF" />
    <rect x="150" y="-35" width="30" height="45" fill="#FFFFFF" />

    <!-- Stepped Tail at bottom-left -->
    <polygon points="-150,105 -150,150 -95,105" fill="#3877F6" />
    <polygon points="-128,105 -150,150 -110,105" fill="#2563EB" />

    <!-- 3. Pixel Sunglasses & Face -->
    <g transform="translate(0, -25)">
      <rect x="-120" y="-20" width="100" height="45" fill="#0F172A" />
      <rect x="20" y="-20" width="100" height="45" fill="#0F172A" />
      <rect x="-20" y="-10" width="40" height="18" fill="#0F172A" />
      <rect x="-105" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="-87" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="35" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="53" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="-20" y="58" width="40" height="12" fill="#0F172A" />
      <rect x="-12" y="70" width="24" height="12" fill="#0F172A" />
      <rect x="-78" y="38" width="24" height="12" fill="#F43F5E" />
      <rect x="54" y="38" width="24" height="12" fill="#F43F5E" />
    </g>
  </g>
</svg>"""

cutline_03 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 460" width="460" height="460">
  <g id="Artwork" transform="translate(230, 220)">
    <path id="WhiteBorder" d="{path_contour_03_clean}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="22" stroke-linejoin="round" stroke-linecap="round" />

    <!-- Ticket Body -->
    <rect x="-160" y="-145" width="160" height="250" fill="#3877F6" />
    <rect x="0" y="-145" width="160" height="250" fill="#5AC1C4" />
    <rect x="-180" y="-35" width="30" height="45" fill="#FFFFFF" />
    <rect x="150" y="-35" width="30" height="45" fill="#FFFFFF" />

    <!-- Stepped Tail -->
    <polygon points="-150,105 -150,150 -95,105" fill="#3877F6" />
    <polygon points="-128,105 -150,150 -110,105" fill="#2563EB" />

    <!-- Sunglasses & Face -->
    <g transform="translate(0, -25)">
      <rect x="-120" y="-20" width="100" height="45" fill="#0F172A" />
      <rect x="20" y="-20" width="100" height="45" fill="#0F172A" />
      <rect x="-20" y="-10" width="40" height="18" fill="#0F172A" />
      <rect x="-105" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="-87" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="35" y="-10" width="18" height="14" fill="#FFFFFF" />
      <rect x="53" y="4" width="14" height="14" fill="#FFFFFF" />
      <rect x="-20" y="58" width="40" height="12" fill="#0F172A" />
      <rect x="-12" y="70" width="24" height="12" fill="#0F172A" />
      <rect x="-78" y="38" width="24" height="12" fill="#F43F5E" />
      <rect x="54" y="38" width="24" height="12" fill="#F43F5E" />
    </g>
  </g>

  <!-- Technical Die-Cut Layer: Spot Magenta 100% 0.5pt -->
  <g id="CutContour" transform="translate(230, 220)">
    <path d="{path_contour_03_clean}" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" />
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

print("Generated full pack with permanent Sticker 01, notch-preserved white-gap Mascot Sticker 02, and pure Retro Arcade Sticker 03!")
