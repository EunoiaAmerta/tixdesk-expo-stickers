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
# 2. STICKER 02: KAWAII CHIBI MASCOT HEAD (PURE ICONIC FACE EDITION)
# - Floating robot body removed for iconic focus on the character face!
# - Thinned-down white die-cut border closely hugging the antenna, headset,
#   earcups, mic, ticket notches, and speech tail (matching Sticker 01 thinness).
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
    <!-- 1. Tight White Die-Cut Contour matching Sticker 01 thinness (stroke-width=24) -->
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

    <!-- 2. Antenna -->
    <path d="M 0 -150 L 0 -220" stroke="#64748B" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#10B981" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#6EE7B7" />

    <!-- 3. Head Ticket Shell -->
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
# 3. STICKER 03: RETRO PIXEL ART ARCADE (TOP BANNER & ATTACHED HEART CROWN)
# - Top floating achievement banner: "★ SLA SAVED: 100% ★"
# - 3-Heart Crown physically attached directly ON TOP of the head line (Y = -160)
# - Clean 50/50 royal blue & cyan split face
# - Distinct chin baseline & stepped dialogue tail at bottom
# - Symmetrical, thin, uniform white die-cut contour matching Sticker 01
# ==============================================================================
path_contour_03 = """
  M -160 -256
  L 160 -256
  A 18 18 0 0 1 178 -238
  L 178 -212
  A 18 18 0 0 1 160 -194
  L 125 -194
  Q 185 -172, 192 -130
  L 192 -48
  Q 165 -15, 192 18
  L 192 110
  A 18 18 0 0 1 174 128
  L -85 128
  L -155 188
  A 12 12 0 0 1 -175 180
  L -175 110
  L -192 110
  L -192 18
  Q -165 -15, -192 -48
  L -192 -130
  Q -185 -172, -125 -194
  L -160 -194
  A 18 18 0 0 1 -178 -212
  L -178 -238
  A 18 18 0 0 1 -160 -256
  Z
"""

svg_03 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 540" width="520" height="540">
  <g id="Artwork" transform="translate(260, 295)">
    <!-- 1. White die-cut contour -->
    <path id="WhiteBorder" d="{path_contour_03}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" />

    <!-- 2. Floating SLA SAVED Banner at Top -->
    <g transform="translate(0, -225)">
      <rect x="-155" y="-19" width="310" height="38" rx="8" fill="#0F172A" stroke="#38BDF8" stroke-width="3" />
      <text x="0" y="8" font-family="'Noto Sans Mono', monospace" font-size="18" font-weight="900" letter-spacing="2.5" fill="#38BDF8" text-anchor="middle">★ SLA SAVED: 100% ★</text>
    </g>

    <!-- 3. Ticket Body (Crisp 50/50 Blue/Cyan Split) -->
    <rect x="-175" y="-160" width="175" height="270" fill="#3877F6" />
    <rect x="0" y="-160" width="175" height="270" fill="#5AC1C4" />
    
    <!-- Ticket Notches -->
    <rect x="-195" y="-35" width="35" height="45" fill="#FFFFFF" />
    <rect x="160" y="-35" width="35" height="45" fill="#FFFFFF" />

    <!-- Stepped Tail at bottom-left -->
    <polygon points="-160,110 -160,165 -100,110" fill="#3877F6" />
    <polygon points="-135,110 -160,165 -115,110" fill="#2563EB" />

    <!-- 4. Heart Crown Attached directly ON TOP of the head line (Y = -160) -->
    <!-- Left Heart -->
    <g transform="translate(-80, -170) scale(4.0)">
      <path d="M -4 -2 H -1 V 1 H -4 Z M 1 -2 H 4 V 1 H 1 Z M -3 1 H 3 V 3 H -3 Z M -2 3 H 2 V 4 H -2 Z M -1 4 H 1 V 5 H -1 Z" fill="#EF4444" />
      <rect x="-3" y="-1" width="1" height="1" fill="#FECACA" />
    </g>
    <!-- Center Heart (Taller Crown Jewel) -->
    <g transform="translate(0, -173) scale(4.8)">
      <path d="M -4 -2 H -1 V 1 H -4 Z M 1 -2 H 4 V 1 H 1 Z M -3 1 H 3 V 3 H -3 Z M -2 3 H 2 V 4 H -2 Z M -1 4 H 1 V 5 H -1 Z" fill="#EF4444" />
      <rect x="-3" y="-1" width="1" height="1" fill="#FECACA" />
    </g>
    <!-- Right Heart -->
    <g transform="translate(80, -170) scale(4.0)">
      <path d="M -4 -2 H -1 V 1 H -4 Z M 1 -2 H 4 V 1 H 1 Z M -3 1 H 3 V 3 H -3 Z M -2 3 H 2 V 4 H -2 Z M -1 4 H 1 V 5 H -1 Z" fill="#EF4444" />
      <rect x="-3" y="-1" width="1" height="1" fill="#FECACA" />
    </g>

    <!-- 5. Pixel Sunglasses & Face -->
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

    <!-- 6. XP Bar -->
    <g transform="translate(0, 80)">
      <rect x="-85" y="0" width="170" height="12" fill="#0F172A" />
      <rect x="-82" y="2" width="164" height="8" fill="#22C55E" />
    </g>
  </g>
</svg>"""

cutline_03 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 540" width="520" height="540">
  <g id="Artwork" transform="translate(260, 295)">
    <path id="WhiteBorder" d="{path_contour_03}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" />

    <!-- Floating SLA SAVED Banner at Top -->
    <g transform="translate(0, -225)">
      <rect x="-155" y="-19" width="310" height="38" rx="8" fill="#0F172A" stroke="#38BDF8" stroke-width="3" />
      <text x="0" y="8" font-family="'Noto Sans Mono', monospace" font-size="18" font-weight="900" letter-spacing="2.5" fill="#38BDF8" text-anchor="middle">★ SLA SAVED: 100% ★</text>
    </g>

    <!-- Ticket Body -->
    <rect x="-175" y="-160" width="175" height="270" fill="#3877F6" />
    <rect x="0" y="-160" width="175" height="270" fill="#5AC1C4" />
    <rect x="-195" y="-35" width="35" height="45" fill="#FFFFFF" />
    <rect x="160" y="-35" width="35" height="45" fill="#FFFFFF" />
    <polygon points="-160,110 -160,165 -100,110" fill="#3877F6" />
    <polygon points="-135,110 -160,165 -115,110" fill="#2563EB" />

    <!-- Heart Crown -->
    <g transform="translate(-80, -170) scale(4.0)">
      <path d="M -4 -2 H -1 V 1 H -4 Z M 1 -2 H 4 V 1 H 1 Z M -3 1 H 3 V 3 H -3 Z M -2 3 H 2 V 4 H -2 Z M -1 4 H 1 V 5 H -1 Z" fill="#EF4444" />
      <rect x="-3" y="-1" width="1" height="1" fill="#FECACA" />
    </g>
    <g transform="translate(0, -173) scale(4.8)">
      <path d="M -4 -2 H -1 V 1 H -4 Z M 1 -2 H 4 V 1 H 1 Z M -3 1 H 3 V 3 H -3 Z M -2 3 H 2 V 4 H -2 Z M -1 4 H 1 V 5 H -1 Z" fill="#EF4444" />
      <rect x="-3" y="-1" width="1" height="1" fill="#FECACA" />
    </g>
    <g transform="translate(80, -170) scale(4.0)">
      <path d="M -4 -2 H -1 V 1 H -4 Z M 1 -2 H 4 V 1 H 1 Z M -3 1 H 3 V 3 H -3 Z M -2 3 H 2 V 4 H -2 Z M -1 4 H 1 V 5 H -1 Z" fill="#EF4444" />
      <rect x="-3" y="-1" width="1" height="1" fill="#FECACA" />
    </g>

    <!-- Sunglasses & XP Bar -->
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
    <g transform="translate(0, 80)">
      <rect x="-85" y="0" width="170" height="12" fill="#0F172A" />
      <rect x="-82" y="2" width="164" height="8" fill="#22C55E" />
    </g>
  </g>

  <!-- Technical Die-Cut Layer: Spot Magenta 100% 0.5pt -->
  <g id="CutContour" transform="translate(260, 295)">
    <path d="{path_contour_03}" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" />
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

print("Official 3-sticker pack generated successfully with permanent Sticker 01, Mascot Head Sticker 02, and Top-Banner Crown Sticker 03!")
