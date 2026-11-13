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
# 01. HERO MARK
# ------------------------------------------------------------------------------
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
svg_01 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="blueCyanGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3877F6" />
      <stop offset="50%" stop-color="#4CA2EA" />
      <stop offset="100%" stop-color="#5AC1C4" />
    </linearGradient>
  </defs>
  <g id="Artwork" transform="translate(200, 195)">
    <path id="WhiteBorder" d="{path_01_body}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="28" stroke-linejoin="round" stroke-linecap="round" />
    <path id="LogoBody" d="{path_01_body}" fill="url(#blueCyanGrad)" />
    <path id="LetterT" d="{path_01_t}" fill="#FFFFFF" />
  </g>
</svg>"""

cutline_01 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  {svg_01.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">', '').replace('</svg>', '')}
  <g id="CutContour" transform="translate(200, 195)">
    <path d="{path_01_body}" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" />
  </g>
</svg>"""

# ------------------------------------------------------------------------------
# 02. CHIBI TIXIE MASCOT
# ------------------------------------------------------------------------------
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
    <path d="M 0 -150 L 0 -220" stroke="#334155" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#10B981" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#34D399" />
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#headGrad)" stroke="#1D4ED8" stroke-width="2.5" />
    <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGrad)" stroke="#38BDF8" stroke-width="4" />
    <path d="M -115 -105 Q 0 -125 115 -105 L 115 -90 Q 0 -110 -115 -90 Z" fill="#FFFFFF" opacity="0.22" />
    <g transform="translate(-55, -45)">
      <ellipse cx="0" cy="0" rx="24" ry="30" fill="#38BDF8" />
      <ellipse cx="0" cy="0" rx="19" ry="25" fill="#0284C7" />
      <circle cx="-6" cy="-8" r="7.5" fill="#FFFFFF" />
      <circle cx="7" cy="9" r="4.5" fill="#FFFFFF" />
    </g>
    <g transform="translate(55, -45)">
      <ellipse cx="0" cy="0" rx="24" ry="30" fill="#38BDF8" />
      <ellipse cx="0" cy="0" rx="19" ry="25" fill="#0284C7" />
      <circle cx="-6" cy="-8" r="7.5" fill="#FFFFFF" />
      <circle cx="7" cy="9" r="4.5" fill="#FFFFFF" />
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
    <circle cx="-70" cy="73" r="14" fill="#10B981" stroke="#1E293B" stroke-width="4" />
  </g>
</svg>"""

cutline_02 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">
  {svg_02.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">', '').replace('</svg>', '')}
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


# ------------------------------------------------------------------------------
# 03. DETECTIVE TIXIE (BUG HUNTER)
# ------------------------------------------------------------------------------
svg_03 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">
  <defs>
    <linearGradient id="headGrad3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3877F6" />
      <stop offset="50%" stop-color="#4CA2EA" />
      <stop offset="100%" stop-color="#5AC1C4" />
    </linearGradient>

    <linearGradient id="screenGrad3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#080E1E" />
      <stop offset="100%" stop-color="#111C35" />
    </linearGradient>

    <linearGradient id="capGrad3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#B45309" />
      <stop offset="40%" stop-color="#78350F" />
      <stop offset="100%" stop-color="#451A03" />
    </linearGradient>

    <linearGradient id="capBrimGrad3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#92400E" />
      <stop offset="100%" stop-color="#5B21B6" />
    </linearGradient>

    <clipPath id="capDomeClip">
      <path d="M -105 10 C -115 -75, 115 -75, 105 10 Z" />
    </clipPath>

    <linearGradient id="lensGlass3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#BAE6FD" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#38BDF8" stop-opacity="0.4" />
    </linearGradient>
  </defs>

  <g id="Artwork" transform="translate(270, 275)">
    <!-- 1. White Die-Cut Contour -->
    <g id="WhiteBorder" fill="#FFFFFF" stroke="#FFFFFF" stroke-linejoin="round" stroke-linecap="round">
      <!-- Detective Cap Outline -->
      <path d="M -115 -145 C -120 -235, 120 -235, 115 -145 Z" stroke-width="26" />
      <path d="M -135 -145 Q 0 -170 135 -145 Q 145 -135 125 -135 L -125 -135 Q -145 -135 -135 -145 Z" stroke-width="24" />
      <!-- Headset & Head Body Contour -->
      <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke-width="46" />
      <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
      <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
      <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke-width="26" />
      <circle cx="-70" cy="73" r="14" stroke-width="24" />
      <path d="M -190 -10 C -190 60, -160 70, -160 70 L -160 10 L -160 -10 Z" stroke-width="12" />

      <!-- Magnifying Glass & Handle Contour -->
      <circle cx="85" cy="40" r="58" stroke-width="24" />
      <path d="M 125 80 L 165 125" stroke-width="38" />

      <!-- Bottom Tag Pill -->
      <rect x="-85" y="52" width="170" height="26" rx="13" stroke-width="24" />
    </g>

    <!-- Solid White Gap Fills behind earcups -->
    <path d="M 160 -40 A 25 25 0 0 0 160 10 L 175 10 L 175 -40 Z" fill="#FFFFFF" stroke="none" />
    <path d="M -160 -40 A 25 25 0 0 1 -160 10 L -175 10 L -175 -40 Z" fill="#FFFFFF" stroke="none" />

    <!-- 2. Antenna (Peeking from behind the cap) -->
    <path d="M 0 -150 L 0 -225" stroke="#334155" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-225" r="16" fill="#F59E0B" stroke="#FFFFFF" stroke-width="4" />

    <!-- 3. Head Ticket Shell -->
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#headGrad3)" stroke="#1D4ED8" stroke-width="2.5" />

    <!-- 4. Screen Visor -->
    <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGrad3)" stroke="#38BDF8" stroke-width="4" />
    <path d="M -115 -105 Q 0 -125 115 -105 L 115 -90 Q 0 -110 -115 -90 Z" fill="#FFFFFF" opacity="0.22" />

    <!-- 5. Detective Expression: Left eye calculating, right eye magnified looking through glass -->
    <!-- Left Eye (Analytical Squint / Detective Focus) -->
    <g transform="translate(-55, -45)">
      <ellipse cx="0" cy="0" rx="22" ry="28" fill="#38BDF8" />
      <ellipse cx="0" cy="0" rx="18" ry="24" fill="#0284C7" />
      <circle cx="-6" cy="-8" r="7" fill="#FFFFFF" />
      <circle cx="6" cy="8" r="4" fill="#FFFFFF" />
      <path d="M -22 -22 Q 0 -26 22 -16" fill="none" stroke="#38BDF8" stroke-width="4" stroke-linecap="round" />
    </g>

    <!-- Right Eye (Peering at the bug) -->
    <g transform="translate(55, -45)">
      <ellipse cx="0" cy="0" rx="25" ry="31" fill="#38BDF8" />
      <ellipse cx="0" cy="0" rx="20" ry="26" fill="#0284C7" />
      <circle cx="-7" cy="-9" r="8" fill="#FFFFFF" />
      <circle cx="7" cy="9" r="4.5" fill="#FFFFFF" />
    </g>

    <ellipse cx="-75" cy="-5" rx="14" ry="8" fill="#F43F5E" opacity="0.75" />
    <ellipse cx="75" cy="-5" rx="14" ry="8" fill="#F43F5E" opacity="0.75" />

    <!-- Clever Detective Smirk (:3) -->
    <path d="M -16 -4 Q -8 7 0 0 Q 8 7 16 -4" fill="none" stroke="#38BDF8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />

    <!-- 6. Detective Deerstalker Cap (Sherlock Hat) with Perfectly Attached & Clipped Seams -->
    <g transform="translate(0, -155)">
      <!-- Main Cap Dome -->
      <path d="M -105 10 C -115 -75, 115 -75, 105 10 Z" fill="url(#capGrad3)" stroke="#292524" stroke-width="3" />

      <!-- Clipped Internal Seams & Stitching: 100% strictly adhering to cap shape -->
      <g clip-path="url(#capDomeClip)">
        <!-- Vertical Panel Seams -->
        <!-- Center seam -->
        <path d="M 0 -70 L 0 10" stroke="#292524" stroke-width="2.5" />
        <path d="M -2 -70 L -2 10" stroke="#FDE68A" stroke-width="1.2" stroke-dasharray="3,3" opacity="0.65" />
        <!-- Left panel curve -->
        <path d="M 0 -70 C -35 -40, -55 -10, -55 10" fill="none" stroke="#292524" stroke-width="2.5" />
        <path d="M -2 -70 C -37 -40, -57 -10, -57 10" fill="none" stroke="#FDE68A" stroke-width="1.2" stroke-dasharray="3,3" opacity="0.65" />
        <!-- Right panel curve -->
        <path d="M 0 -70 C 35 -40, 55 -10, 55 10" fill="none" stroke="#292524" stroke-width="2.5" />
        <path d="M 2 -70 C 37 -40, 57 -10, 57 10" fill="none" stroke="#FDE68A" stroke-width="1.2" stroke-dasharray="3,3" opacity="0.65" />

        <!-- Contour-hugging horizontal stitching arcs (following cap curvature) -->
        <path d="M -110 -15 Q 0 -38 110 -15" fill="none" stroke="#FDE68A" stroke-width="1.3" stroke-dasharray="4,3" opacity="0.75" />
        <path d="M -90 -40 Q 0 -58 90 -40" fill="none" stroke="#FDE68A" stroke-width="1.3" stroke-dasharray="4,3" opacity="0.7" />

        <!-- Cap Crown Shading & Highlight -->
        <path d="M -70 -50 Q 0 -72 70 -50 Q 0 -62 -70 -50 Z" fill="#FEF08A" opacity="0.18" />
      </g>

      <!-- Front Visor Brim (Curved forward brim) -->
      <path d="M -125 10 Q 0 -12 125 10 Q 135 24 115 24 L -115 24 Q -135 24 -125 10 Z" fill="#6B2F10" stroke="#292524" stroke-width="2.8" />
      <!-- Neat stitching along visor brim curve -->
      <path d="M -115 17 Q 0 -4 115 17" fill="none" stroke="#FDE68A" stroke-width="1.4" stroke-dasharray="4,3" opacity="0.8" />

      <!-- Earflap folded up on side -->
      <path d="M -75 10 C -80 -25, -45 -45, 0 -48 C 45 -45, 80 -25, 75 10 Z" fill="#58240C" stroke="#292524" stroke-width="2" opacity="0.35" />

      <!-- Top Ribbon Bow / Peak Knob -->
      <circle cx="0" cy="-68" r="8" fill="#B45309" stroke="#292524" stroke-width="2.2" />
      <path d="M -15 -64 Q 0 -76 15 -64 Q 0 -56 -15 -64 Z" fill="#F59E0B" stroke="#292524" stroke-width="1.5" />
      <!-- Hanging Ribbon Ties -->
      <path d="M -8 -60 C -12 -50, -18 -45, -15 -35" fill="none" stroke="#D97706" stroke-width="3" stroke-linecap="round" />
      <path d="M 8 -60 C 12 -50, 18 -45, 15 -35" fill="none" stroke="#D97706" stroke-width="3" stroke-linecap="round" />
    </g>

    <!-- 7. Headset (Continuous headband with dark mic joint) -->
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#1E293B" stroke-width="22" stroke-linecap="round" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#38BDF8" stroke-width="8" stroke-linecap="round" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="-200" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <rect x="165" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="175" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    

    <!-- 8. Magnifying Glass & Trapped Cute Bug -->
    <g transform="translate(85, 38)">
      <!-- Handle -->
      <path d="M 40 40 L 78 82" stroke="#78350F" stroke-width="16" stroke-linecap="round" />
      <path d="M 40 40 L 78 82" stroke="#B45309" stroke-width="10" stroke-linecap="round" />
      <circle cx="80" cy="84" r="6" fill="#F59E0B" />

      <!-- Outer Brass Lens Rim -->
      <circle cx="0" cy="0" r="48" fill="none" stroke="#F59E0B" stroke-width="9" />
      <circle cx="0" cy="0" r="44" fill="none" stroke="#78350F" stroke-width="2" />
      <!-- Glass Lens -->
      <circle cx="0" cy="0" r="43.5" fill="url(#lensGlass3)" />

      <!-- Cute Bug Trapped Under Lens -->
      <g transform="translate(0, 0)">
        <ellipse cx="-16" cy="-12" rx="10" ry="5" fill="#E0F2FE" opacity="0.7" transform="rotate(-25 -16 -12)" />
        <ellipse cx="16" cy="-12" rx="10" ry="5" fill="#E0F2FE" opacity="0.7" transform="rotate(25 16 -12)" />
        <path d="M -4 -16 Q -12 -28 -18 -26" fill="none" stroke="#14532D" stroke-width="2" stroke-linecap="round" />
        <path d="M 4 -16 Q 12 -28 18 -26" fill="none" stroke="#14532D" stroke-width="2" stroke-linecap="round" />
        <ellipse cx="0" cy="4" rx="15" ry="18" fill="#22C55E" stroke="#15803D" stroke-width="2" />
        <line x1="0" y1="-10" x2="0" y2="20" stroke="#15803D" stroke-width="1.5" />
        <circle cx="-5" cy="0" r="2.5" fill="#166534" />
        <circle cx="5" cy="0" r="2.5" fill="#166534" />
        <circle cx="-5" cy="10" r="2.5" fill="#166534" />
        <circle cx="5" cy="10" r="2.5" fill="#166534" />
        <circle cx="0" cy="-12" r="10" fill="#16A34A" stroke="#15803D" stroke-width="2" />
        <circle cx="-4" cy="-14" r="3.5" fill="#FFFFFF" />
        <circle cx="-3.5" cy="-14" r="1.8" fill="#052E16" />
        <circle cx="4" cy="-14" r="3.5" fill="#FFFFFF" />
        <circle cx="4.5" cy="-14" r="1.8" fill="#052E16" />
        <path d="M -3 -8 Q 0 -5 3 -8" fill="none" stroke="#052E16" stroke-width="1.2" stroke-linecap="round" />
      </g>

      <!-- Glass Specular Curved Glare -->
      <path d="M -30 -25 A 38 38 0 0 1 25 -30" fill="none" stroke="#FFFFFF" stroke-width="4.5" stroke-linecap="round" opacity="0.75" />
      <circle cx="30" cy="-15" r="3" fill="#FFFFFF" opacity="0.6" />
    </g>

    <!-- 9. Badge: BUG HUNTER -->
    <g transform="translate(0, 65)">
      <rect x="-85" y="-13" width="170" height="26" rx="13" fill="#0F172A" stroke="#F59E0B" stroke-width="2.5" />
      <text y="4" font-family="'Noto Sans', sans-serif" font-size="11.5" font-weight="900" letter-spacing="1.5" fill="#FBBF24" text-anchor="middle">🔍 BUG HUNTER</text>
    </g>

    <!-- Outermost Layer: Boom Mic (Nothing covers the mic!) -->
    <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke="#1E293B" stroke-width="10" stroke-linecap="round" />
    <circle cx="-70" cy="73" r="14" fill="#10B981" stroke="#1E293B" stroke-width="4" />
  </g>
</svg>"""

cutline_03 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">
  {svg_03.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">', '').replace('</svg>', '')}
  <g id="CutContour" transform="translate(270, 275)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
    <path d="M -115 -145 C -120 -235, 120 -235, 115 -145 Z" stroke-width="26" />
    <path d="M -135 -145 Q 0 -170 135 -145 Q 145 -135 125 -135 L -125 -135 Q -145 -135 -135 -145 Z" stroke-width="24" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" stroke-width="46" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
    <circle cx="85" cy="40" r="58" stroke-width="24" />
    <path d="M 125 80 L 165 125" stroke-width="38" />
    <circle cx="-70" cy="73" r="14" stroke-width="24" />
    <rect x="-85" y="52" width="170" height="26" rx="13" stroke-width="24" />
  </g>
</svg>"""

# ------------------------------------------------------------------------------
# 04. CAFFEINE NIGHT SHIFT
# ------------------------------------------------------------------------------
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

    <!-- Outermost Layer: Boom Mic (Nothing covers the mic!) -->
    <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke="#1E293B" stroke-width="10" stroke-linecap="round" />
    <circle cx="-70" cy="73" r="14" fill="#F59E0B" stroke="#1E293B" stroke-width="4" />
  </g>
</svg>"""

cutline_04 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">
  {svg_04.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" width="520" height="520">', '').replace('</svg>', '')}
  <g id="CutContour" transform="translate(260, 265)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
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

# ------------------------------------------------------------------------------
# 05. TIXIE ON FIRE
# ------------------------------------------------------------------------------
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

  <g id="Artwork" transform="translate(270, 375)">
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

    <!-- 8. Bottom Alert Pill: "PROD ON FIRE" -->
    <g transform="translate(0, 62)">
      <rect x="-70" y="-12" width="140" height="24" rx="12" fill="#0F172A" stroke="#EF4444" stroke-width="2" />
      <text y="4.5" font-family="'Noto Sans', monospace, sans-serif" font-size="9.5" font-weight="900" fill="#FEF08A" letter-spacing="2" text-anchor="middle">🔥 PROD ON FIRE</text>
    </g>

    <!-- Outermost Layer: Boom Mic (Nothing covers the mic!) -->
    <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke="#1E293B" stroke-width="10" stroke-linecap="round" />
    <circle cx="-70" cy="73" r="14" fill="#EF4444" stroke="#1E293B" stroke-width="4" />
  </g>
</svg>"""

cutline_05 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">
  {svg_05.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">', '').replace('</svg>', '')}
  <g id="CutContour" transform="translate(270, 375)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
    <path d="M -120 -150 C -160 -190, -150 -265, -95 -290 C -75 -245, -55 -230, -45 -200 Z" stroke-width="26" />
    <path d="M -60 -170 C -60 -265, -15 -320, 15 -330 C 30 -275, 65 -235, 45 -180 Z" stroke-width="26" />
    <path d="M 30 -160 C 65 -215, 125 -275, 135 -225 C 140 -190, 115 -160, 100 -145 Z" stroke-width="26" />
    <path d="M -180 -120 C -225 -100, -235 -40, -210 -10 C -190 -30, -180 -60, -175 -85 Z" stroke-width="24" />
    <path d="M 175 -120 C 220 -100, 230 -40, 205 -10 C 185 -30, 175 -60, 170 -85 Z" stroke-width="24" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" stroke-width="46" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
    <circle cx="-70" cy="73" r="14" stroke-width="24" />
  </g>
</svg>"""

# ------------------------------------------------------------------------------
# 06. TIXIE NEON (SOFT CYBER)
# ------------------------------------------------------------------------------
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
    <circle cx="-70" cy="73" r="14" fill="#00F0FF" stroke="#1E293B" stroke-width="4" />
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
    <circle cx="-70" cy="73" r="14" stroke-width="24" />
  </g>
</svg>"""

# ------------------------------------------------------------------------------
# 07. ROCKET TIXIE (LGTM // SHIP IT!)
# ------------------------------------------------------------------------------
svg_07 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">
  <defs>
    <linearGradient id="headGrad7" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3877F6" />
      <stop offset="50%" stop-color="#4CA2EA" />
      <stop offset="100%" stop-color="#5AC1C4" />
    </linearGradient>

    <linearGradient id="screenGrad7" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#080E1E" />
      <stop offset="100%" stop-color="#111C35" />
    </linearGradient>
  </defs>

  <g id="Artwork" transform="translate(270, 270)">
    <!-- 1. UNIFIED SOLID WHITE VINYL BASE CONTOUR (Completely continuous, zero disconnected islands) -->
    <g id="WhiteBorder" fill="#FFFFFF" stroke="#FFFFFF" stroke-linejoin="round" stroke-linecap="round">
      <!-- Main Core Body & Headband Fill Blob -->
      <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="36" />
      <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke-width="50" />
      <circle cx="0" cy="-215" r="32" stroke-width="32" />
      <line x1="0" y1="-140" x2="0" y2="-215" stroke-width="40" />

      <!-- Earcups & Mic -->
      <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="28" />
      <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="28" />
      <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke-width="32" />
      <circle cx="-70" cy="73" r="16" stroke-width="28" />

      <!-- Fill notches under earcups to make solid cushion -->
      <rect x="-175" y="-45" width="30" height="60" rx="10" stroke-width="10" />
      <rect x="145" y="-45" width="30" height="60" rx="10" stroke-width="10" />

      <!-- Antenna signal waves backing -->
      <path d="M -22 -232 Q 0 -248 22 -232" fill="none" stroke-width="24" stroke-linecap="round" />
      <path d="M -15 -244 Q 0 -258 15 -244" fill="none" stroke-width="20" stroke-linecap="round" />

      <!-- Confetti Outer Bridges (Overlapping seamlessly into main body) -->
      <!-- Top Left Confetti Cluster -->
      <rect x="-185" y="-170" width="26" height="15" rx="5" stroke-width="26" transform="rotate(-20 -172 -162)" />
      <rect x="-205" y="-120" width="24" height="14" rx="5" stroke-width="26" transform="rotate(15 -193 -113)" />
      <circle cx="-135" cy="-185" r="12" stroke-width="22" />
      <path d="M -165 -195 C -145 -185, -175 -175, -150 -155" fill="none" stroke-width="28" />

      <!-- Left Mid & Lower Flakes -->
      <rect x="-205" y="10" width="24" height="14" rx="5" stroke-width="26" transform="rotate(-25 -193 17)" />
      <circle cx="-205" cy="-45" r="10" stroke-width="24" />
      <rect x="-180" y="70" width="22" height="13" rx="4" stroke-width="24" transform="rotate(15 -169 76)" />
      <!-- Tail area confetti balance (lower left) -->
      <circle cx="-165" cy="115" r="10" stroke-width="24" />
      <rect x="-125" y="95" width="20" height="11" rx="4" stroke-width="22" transform="rotate(-20 -115 100)" />

      <!-- Top Right Confetti Cluster -->
      <rect x="160" y="-170" width="26" height="15" rx="5" stroke-width="26" transform="rotate(20 173 -162)" />
      <rect x="180" y="-120" width="24" height="14" rx="5" stroke-width="26" transform="rotate(-15 192 -113)" />
      <circle cx="135" cy="-185" r="12" stroke-width="22" />
      <path d="M 165 -195 C 145 -185, 175 -175, 150 -155" fill="none" stroke-width="28" />

      <!-- Right Mid & Lower Flakes -->
      <rect x="180" y="10" width="24" height="14" rx="5" stroke-width="26" transform="rotate(25 192 17)" />
      <circle cx="205" cy="-45" r="10" stroke-width="24" />
      <rect x="160" y="70" width="22" height="13" rx="4" stroke-width="24" transform="rotate(-15 171 76)" />
      <circle cx="120" cy="95" r="10" stroke-width="24" />

      <!-- Bottom Tag Pill -->
      <rect x="-105" y="65" width="210" height="30" rx="15" stroke-width="30" />
    </g>

    <!-- 2. FESTIVE CONFETTI PAPERS, STREAMERS & SPARKLES -->
    <!-- === LEFT CONFETTI === -->
    <!-- Magenta Serpentine Streamer Ribbon -->
    <path d="M -168 -198 C -145 -186, -178 -174, -152 -154" fill="none" stroke="#F43F5E" stroke-width="6.5" stroke-linecap="round" />
    <path d="M -168 -198 C -145 -186, -178 -174, -152 -154" fill="none" stroke="#FECDD3" stroke-width="2.2" stroke-linecap="round" />

    <!-- Gold Paper Strip (Top Left) -->
    <rect x="-185" y="-170" width="26" height="13" rx="3.5" fill="#FDE047" stroke="#CA8A04" stroke-width="1.8" transform="rotate(-20 -172 -163)" />
    <!-- Emerald Green Paper Strip (Upper-Mid Left) -->
    <rect x="-205" y="-120" width="24" height="12" rx="3.5" fill="#34D399" stroke="#059669" stroke-width="1.8" transform="rotate(15 -193 -114)" />
    <!-- Rose Pink Paper Strip (Mid Left) -->
    <rect x="-205" y="10" width="24" height="12" rx="3.5" fill="#F43F5E" stroke="#BE123C" stroke-width="1.8" transform="rotate(-25 -193 16)" />
    <!-- Cyan Blue Paper Strip (Lower Left) -->
    <rect x="-180" y="70" width="22" height="11" rx="3" fill="#38BDF8" stroke="#0284C7" stroke-width="1.8" transform="rotate(15 -169 75)" />
    <!-- Mint Flake near Chat Tail -->
    <rect x="-125" y="95" width="20" height="10" rx="2.5" fill="#34D399" stroke="#059669" stroke-width="1.8" transform="rotate(-20 -115 100)" />

    <!-- Confetti Dots & Stars (Left) -->
    <circle cx="-135" cy="-185" r="7" fill="#A855F7" stroke="#7E22CE" stroke-width="1.6" />
    <circle cx="-205" cy="-45" r="6" fill="#FDE047" stroke="#D97706" stroke-width="1.6" />
    <circle cx="-165" cy="115" r="5.5" fill="#F43F5E" stroke="#BE123C" stroke-width="1.5" />
    <polygon points="-160,-130 -157,-123 -150,-121 -157,-119 -160,-112 -163,-119 -170,-121 -163,-123" fill="#FDE047" stroke="#B45309" stroke-width="0.8" />

    <!-- === RIGHT CONFETTI === -->
    <!-- Cyan Serpentine Streamer Ribbon -->
    <path d="M 168 -198 C 145 -186, 178 -174, 152 -154" fill="none" stroke="#38BDF8" stroke-width="6.5" stroke-linecap="round" />
    <path d="M 168 -198 C 145 -186, 178 -174, 152 -154" fill="none" stroke="#BAE6FD" stroke-width="2.2" stroke-linecap="round" />

    <!-- Cyan Paper Strip (Top Right) -->
    <rect x="160" y="-170" width="26" height="13" rx="3.5" fill="#38BDF8" stroke="#0284C7" stroke-width="1.8" transform="rotate(20 173 -163)" />
    <!-- Rose Pink Paper Strip (Upper-Mid Right) -->
    <rect x="180" y="-120" width="24" height="12" rx="3.5" fill="#F43F5E" stroke="#BE123C" stroke-width="1.8" transform="rotate(-15 192 -114)" />
    <!-- Emerald Green Paper Strip (Mid Right) -->
    <rect x="180" y="10" width="24" height="12" rx="3.5" fill="#34D399" stroke="#059669" stroke-width="1.8" transform="rotate(25 192 16)" />
    <!-- Gold Paper Strip (Lower Right) -->
    <rect x="160" y="70" width="22" height="11" rx="3" fill="#FDE047" stroke="#CA8A04" stroke-width="1.8" transform="rotate(-15 171 75)" />
    <!-- Rose Pink Flake (Lower Right Corner) -->
    <circle cx="120" cy="95" r="6" fill="#F43F5E" stroke="#BE123C" stroke-width="1.5" />

    <!-- Confetti Dots & Stars (Right) -->
    <circle cx="135" cy="-185" r="7" fill="#FDE047" stroke="#D97706" stroke-width="1.6" />
    <circle cx="205" cy="-45" r="6" fill="#A855F7" stroke="#7E22CE" stroke-width="1.6" />
    <polygon points="160,-130 163,-123 170,-121 163,-119 160,-112 157,-119 150,-121 157,-123" fill="#FDE047" stroke="#B45309" stroke-width="0.8" />

    <!-- 3. ANTENNA (With Excitement Arcs) -->
    <path d="M 0 -150 L 0 -215" stroke="#334155" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-215" r="18" fill="#10B981" stroke="#FFFFFF" stroke-width="4.5" />
    <!-- Energetic celebration waves -->
    <path d="M -18 -232 Q 0 -246 18 -232" fill="none" stroke="#FDE047" stroke-width="4.5" stroke-linecap="round" />
    <path d="M -13 -242 Q 0 -253 13 -242" fill="none" stroke="#FDE047" stroke-width="4" stroke-linecap="round" />

    <!-- 4. HEAD TICKET SHELL -->
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#headGrad7)" stroke="#1D4ED8" stroke-width="2.5" />

    <!-- 5. SCREEN VISOR -->
    <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGrad7)" stroke="#38BDF8" stroke-width="4" />
    <path d="M -115 -105 Q 0 -125 115 -105 L 115 -90 Q 0 -110 -115 -90 Z" fill="#FFFFFF" opacity="0.22" />

    <!-- 6. SUPER HAPPY & EXCITED ANIME FACE! -->
    <!-- Left Eye -->
    <g transform="translate(-55, -45)">
      <ellipse cx="0" cy="0" rx="25" ry="31" fill="#38BDF8" />
      <ellipse cx="0" cy="0" rx="20" ry="26" fill="#0284C7" />
      <polygon points="0,-12 3,-3 12,0 3,3 0,12 -3,3 -12,0 -3,-3" fill="#FFFFFF" transform="translate(-5, -7) scale(0.75)" />
      <circle cx="-6" cy="-8" r="7.5" fill="#FFFFFF" />
      <circle cx="7" cy="8" r="4.2" fill="#FFFFFF" />
      <!-- Happy arched brow -->
      <path d="M -20 -24 Q 0 -31 20 -22" fill="none" stroke="#38BDF8" stroke-width="4" stroke-linecap="round" />
    </g>

    <!-- Right Eye -->
    <g transform="translate(55, -45)">
      <ellipse cx="0" cy="0" rx="25" ry="31" fill="#38BDF8" />
      <ellipse cx="0" cy="0" rx="20" ry="26" fill="#0284C7" />
      <polygon points="0,-12 3,-3 12,0 3,3 0,12 -3,3 -12,0 -3,-3" fill="#FFFFFF" transform="translate(-5, -7) scale(0.75)" />
      <circle cx="-6" cy="-8" r="7.5" fill="#FFFFFF" />
      <circle cx="7" cy="8" r="4.2" fill="#FFFFFF" />
      <!-- Happy arched brow -->
      <path d="M -20 -22 Q 0 -31 20 -24" fill="none" stroke="#38BDF8" stroke-width="4" stroke-linecap="round" />
    </g>

    <!-- Rosy anime blushing cheeks with gleams -->
    <ellipse cx="-75" cy="-8" rx="16" ry="10" fill="#F43F5E" opacity="0.85" />
    <line x1="-82" y1="-10" x2="-75" y2="-4" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" opacity="0.8" />
    <line x1="-75" y1="-12" x2="-68" y2="-6" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" opacity="0.8" />

    <ellipse cx="75" cy="-8" rx="16" ry="10" fill="#F43F5E" opacity="0.85" />
    <line x1="68" y1="-10" x2="75" y2="-4" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" opacity="0.8" />
    <line x1="75" y1="-12" x2="82" y2="-6" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" opacity="0.8" />

    <!-- Big Ecstatic Open Mouth (:D) with cute tongue -->
    <path d="M -22 -16 Q 0 -26 22 -16 Q 25 12 0 16 Q -25 12 -22 -16 Z" fill="#F43F5E" stroke="#38BDF8" stroke-width="3" stroke-linejoin="round" />
    <path d="M -14 3 Q 0 -4 14 3 Q 10 12 0 14 Q -10 12 -14 3 Z" fill="#FDA4AF" />

    <!-- 7. HEADSET (Continuous headband with dark mic joint) -->
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#1E293B" stroke-width="22" stroke-linecap="round" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#38BDF8" stroke-width="8" stroke-linecap="round" />
    <!-- Earcups -->
    <rect x="-210" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="-200" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <rect x="165" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="175" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    

    <!-- 8. BADGE: BALANCED (Text Centered + Rocket Glyph on Right) -->
    <g transform="translate(0, 78)">
      <rect x="-95" y="-15" width="215" height="30" rx="15" fill="#064E3B" stroke="#10B981" stroke-width="2.8" />
      <text x="12" y="4.8" font-family="'Noto Sans', sans-serif" font-size="11.5" font-weight="900" letter-spacing="1.2" fill="#34D399" text-anchor="middle">LGTM // SHIP IT!</text>
      
      <!-- Crisp Vector Rocket Glyph on Right end -->
      <g transform="translate(86, 0) scale(0.68) rotate(45)">
        <path d="M 0 -12 Q 5 0 4 8 L -4 8 Q -5 0 0 -12 Z" fill="#FFFFFF" />
        <path d="M 0 -12 Q 3 -6 3 -3 L -3 -3 Q -3 -6 0 -12 Z" fill="#EF4444" />
        <polygon points="-4,5 -9,10 -3,8" fill="#EF4444" />
        <polygon points="4,5 9,10 3,8" fill="#EF4444" />
        <path d="M -3 8 Q 0 15 3 8 Z" fill="#FDE047" />
      </g>
    </g>

    <!-- Outermost Layer: Boom Mic (Nothing covers the mic!) -->
    <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke="#1E293B" stroke-width="10" stroke-linecap="round" />
    <circle cx="-70" cy="73" r="14" fill="#10B981" stroke="#1E293B" stroke-width="4" />
  </g>
</svg>"""

cutline_07 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">
  {svg_07.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">', '').replace('</svg>', '')}
  <g id="CutContour" transform="translate(270, 270)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="36" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" stroke-width="50" />
    <circle cx="0" cy="-215" r="32" stroke-width="32" />
    <line x1="0" y1="-140" x2="0" y2="-215" stroke-width="40" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="28" />
    <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="28" />
    <path d="M -190 -10 C -190 70, -110 95, -75 75" stroke-width="32" />
    <circle cx="-70" cy="73" r="16" stroke-width="28" />
    <rect x="-175" y="-45" width="30" height="60" rx="10" stroke-width="10" />
    <rect x="145" y="-45" width="30" height="60" rx="10" stroke-width="10" />
    <path d="M -22 -232 Q 0 -248 22 -232" stroke-width="24" stroke-linecap="round" />
    <path d="M -15 -244 Q 0 -258 15 -244" stroke-width="20" stroke-linecap="round" />
    <rect x="-185" y="-170" width="26" height="15" rx="5" stroke-width="26" transform="rotate(-20 -172 -162)" />
    <rect x="-205" y="-120" width="24" height="14" rx="5" stroke-width="26" transform="rotate(15 -193 -113)" />
    <circle cx="-135" cy="-185" r="12" stroke-width="22" />
    <path d="M -165 -195 C -145 -185, -175 -175, -150 -155" stroke-width="28" />
    <rect x="-205" y="10" width="24" height="14" rx="5" stroke-width="26" transform="rotate(-25 -193 17)" />
    <circle cx="-205" cy="-45" r="10" stroke-width="24" />
    <rect x="-180" y="70" width="22" height="13" rx="4" stroke-width="24" transform="rotate(15 -169 76)" />
    <circle cx="-165" cy="115" r="10" stroke-width="24" />
    <rect x="-125" y="95" width="20" height="11" rx="4" stroke-width="22" transform="rotate(-20 -115 100)" />
    <rect x="160" y="-170" width="26" height="15" rx="5" stroke-width="26" transform="rotate(20 173 -162)" />
    <rect x="180" y="-120" width="24" height="14" rx="5" stroke-width="26" transform="rotate(-15 192 -113)" />
    <circle cx="135" cy="-185" r="12" stroke-width="22" />
    <path d="M 165 -195 C 145 -185, 175 -175, 150 -155" stroke-width="28" />
    <rect x="180" y="10" width="24" height="14" rx="5" stroke-width="26" transform="rotate(25 192 17)" />
    <circle cx="205" cy="-45" r="10" stroke-width="24" />
    <rect x="160" y="70" width="22" height="13" rx="4" stroke-width="24" transform="rotate(-15 171 76)" />
    <circle cx="120" cy="95" r="10" stroke-width="24" />
    <rect x="-105" y="65" width="210" height="30" rx="15" stroke-width="30" />
  </g>
</svg>"""

# ------------------------------------------------------------------------------
# 08. TIXIE OFF & ON
# ------------------------------------------------------------------------------
svg_08 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">
  <defs>
    <linearGradient id="headGrad8" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3877F6" />
      <stop offset="50%" stop-color="#4CA2EA" />
      <stop offset="100%" stop-color="#5AC1C4" />
    </linearGradient>

    <linearGradient id="screenGrad8" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#080E1E" />
      <stop offset="100%" stop-color="#111C35" />
    </linearGradient>
  </defs>

  <g id="Artwork" transform="translate(270, 270)">
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

      <!-- Power Plug & Cable Contour -->
      <path d="M 0 60 C 20 80, 50 110, 80 85 C 95 70, 110 50, 130 50" fill="none" stroke-width="32" />
      <rect x="125" y="32" width="45" height="36" rx="10" stroke-width="24" />
      <line x1="170" y1="40" x2="195" y2="40" stroke-width="24" />
      <line x1="170" y1="60" x2="195" y2="60" stroke-width="24" />

      <!-- Bottom Pill Tag Contour -->
      <rect x="-105" y="85" width="210" height="28" rx="14" stroke-width="24" />
    </g>

    <path d="M 160 -40 A 25 25 0 0 0 160 10 L 175 10 L 175 -40 Z" fill="#FFFFFF" stroke="none" />
    <path d="M -160 -40 A 25 25 0 0 1 -160 10 L -175 10 L -175 -40 Z" fill="#FFFFFF" stroke="none" />

    <!-- 2. Antenna with Playful Yellow Light -->
    <path d="M 0 -150 L 0 -220" stroke="#334155" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#F59E0B" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#FEF08A" />

    <!-- 3. Head Ticket Shell -->
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#headGrad8)" stroke="#1D4ED8" stroke-width="2.5" />

    <!-- 4. Visor Screen -->
    <rect x="-125" y="-125" width="250" height="160" rx="35" fill="url(#screenGrad8)" stroke="#38BDF8" stroke-width="4" />
    <path d="M -115 -105 Q 0 -125 115 -105 L 115 -90 Q 0 -110 -115 -90 Z" fill="#FFFFFF" opacity="0.22" />

    <!-- 5. Innocent "Did You Try Turning It Off & On?" Face: Winking & Cheeky Smile -->
    <!-- Left Eye (Playful Wink) -->
    <path d="M -70 -45 Q -55 -32 -40 -45" fill="none" stroke="#38BDF8" stroke-width="6.5" stroke-linecap="round" />

    <!-- Right Eye (Big Innocent Anime Eye) -->
    <g transform="translate(55, -45)">
      <ellipse cx="0" cy="0" rx="24" ry="30" fill="#38BDF8" />
      <ellipse cx="0" cy="0" rx="19" ry="25" fill="#0284C7" />
      <circle cx="-6" cy="-8" r="7.5" fill="#FFFFFF" />
      <circle cx="7" cy="9" r="4.5" fill="#FFFFFF" />
    </g>

    <!-- Cute Blush -->
    <ellipse cx="-75" cy="-5" rx="14" ry="8" fill="#F43F5E" opacity="0.8" />
    <ellipse cx="75" cy="-5" rx="14" ry="8" fill="#F43F5E" opacity="0.8" />

    <!-- Cheeky Tongue Out / Smug Smile -->
    <path d="M -16 -4 Q -8 8 0 0 Q 8 8 16 -4" fill="none" stroke="#38BDF8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />

    <!-- 6. Headset with dark mic joint ring -->
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#1E293B" stroke-width="22" stroke-linecap="round" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#38BDF8" stroke-width="8" stroke-linecap="round" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="-200" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <rect x="165" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#38BDF8" stroke-width="6" />
    <rect x="175" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    
    <!-- Boom mic with dark slate joint ring -->

    <!-- 7. Disconnected AC Power Cable & Plug (With Sparks!) -->
    <!-- Heavy Rubber Cable curving from behind Tixie -->
    <path d="M -20 65 C 10 85, 45 95, 75 75 C 95 62, 110 50, 130 50" fill="none" stroke="#0F172A" stroke-width="14" stroke-linecap="round" />

    <!-- Chibi Hand Holding Plug -->
    <circle cx="115" cy="50" r="15" fill="#3877F6" stroke="#FFFFFF" stroke-width="3.5" />

    <!-- AC Plug Head -->
    <rect x="130" y="32" width="40" height="36" rx="8" fill="#1E293B" stroke="#64748B" stroke-width="2.5" />
    <!-- Two Metallic Prongs -->
    <rect x="170" y="38" width="24" height="7" rx="2" fill="#CBD5E1" stroke="#475569" stroke-width="1.5" />
    <rect x="170" y="55" width="24" height="7" rx="2" fill="#CBD5E1" stroke="#475569" stroke-width="1.5" />
    <circle cx="186" cy="41.5" r="1.5" fill="#1E293B" />
    <circle cx="186" cy="58.5" r="1.5" fill="#1E293B" />

    <!-- Electric Sparks around plug! ⚡ -->
    <path d="M 198 32 L 208 40 L 202 44 L 214 54" fill="none" stroke="#FDE047" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
    <circle cx="206" cy="28" r="2.5" fill="#38BDF8" />
    <circle cx="218" cy="45" r="2" fill="#FEF08A" />

    <!-- 8. Tagline Banner: HAVE YOU TRIED TURNING IT OFF & ON? -->
    <g transform="translate(0, 98)">
      <rect x="-105" y="-13" width="210" height="26" rx="13" fill="#0F172A" stroke="#38BDF8" stroke-width="2.5" />
      <text y="5" font-family="'Noto Sans', monospace, sans-serif" font-size="8.8" font-weight="900" fill="#38BDF8" letter-spacing="1" text-anchor="middle">🔌 TRY TURNING IT OFF &amp; ON?</text>
    </g>

    <!-- Outermost Layer: Boom Mic (Nothing covers the mic!) -->
    <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke="#1E293B" stroke-width="10" stroke-linecap="round" />
    <circle cx="-70" cy="73" r="14" fill="#F59E0B" stroke="#1E293B" stroke-width="4" />
  </g>
</svg>"""

cutline_08 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">
  {svg_08.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">', '').replace('</svg>', '')}
  <g id="CutContour" transform="translate(270, 270)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
    <circle cx="0" cy="-230" r="22" stroke-width="24" />
    <line x1="0" y1="-150" x2="0" y2="-230" stroke-width="32" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" stroke-width="46" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
    <rect x="125" y="32" width="45" height="36" rx="10" stroke-width="24" />
    <circle cx="-70" cy="73" r="14" stroke-width="24" />
  </g>
</svg>"""

# ------------------------------------------------------------------------------
# 09. HACKER TIXIE (SUDO RESOLVE)
# ------------------------------------------------------------------------------
svg_09 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">
  <defs>
    <linearGradient id="hoodieGrad9" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>

    <linearGradient id="headGrad9" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3877F6" />
      <stop offset="50%" stop-color="#4CA2EA" />
      <stop offset="100%" stop-color="#5AC1C4" />
    </linearGradient>

    <linearGradient id="termGrad9" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#022C22" />
      <stop offset="100%" stop-color="#050C0A" />
    </linearGradient>
  </defs>

  <g id="Artwork" transform="translate(270, 270)">
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

      <!-- Keyboard & Typing Hands Contour -->
      <rect x="-115" y="25" width="230" height="60" rx="16" stroke-width="26" />

      <!-- Bottom Tag Pill -->
      <rect x="-85" y="78" width="170" height="28" rx="14" stroke-width="24" />
    </g>

    <path d="M 160 -40 A 25 25 0 0 0 160 10 L 175 10 L 175 -40 Z" fill="#FFFFFF" stroke="none" />
    <path d="M -160 -40 A 25 25 0 0 1 -160 10 L -175 10 L -175 -40 Z" fill="#FFFFFF" stroke="none" />

    <!-- 2. Antenna with Terminal Green Node -->
    <path d="M 0 -150 L 0 -220" stroke="#334155" stroke-width="12" stroke-linecap="round" />
    <circle cx="0" cy="-230" r="22" fill="#10B981" stroke="#FFFFFF" stroke-width="5" />
    <circle cx="0" cy="-230" r="11" fill="#34D399" />

    <!-- 3. Head Ticket Shell -->
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" fill="url(#headGrad9)" stroke="#1D4ED8" stroke-width="2.5" />

    <!-- 4. Linux Terminal Visor (Matrix Black/Green Theme) -->
    <rect x="-125" y="-125" width="250" height="150" rx="35" fill="url(#termGrad9)" stroke="#10B981" stroke-width="3.5" />

    <!-- Terminal Titlebar dots -->
    <circle cx="-100" cy="-105" r="4.5" fill="#EF4444" />
    <circle cx="-88" cy="-105" r="4.5" fill="#F59E0B" />
    <circle cx="-76" cy="-105" r="4.5" fill="#10B981" />
    <text x="-60" y="-101" font-family="'Noto Sans', monospace, sans-serif" font-size="7.5" font-weight="700" fill="#6EE7B7">bash - tixdesk@prod</text>

    <!-- Terminal Code / Command Prompt on Visor -->
    <g font-family="'Noto Sans', monospace, sans-serif" font-size="10.5" font-weight="900">
      <text x="-105" y="-76" fill="#34D399">$ sudo resolve --all</text>
      <text x="-105" y="-56" fill="#6EE7B7">&gt; [OK] 0 INCIDENTS</text>
      <text x="-105" y="-36" fill="#FDE047">&gt; SLA: 100% MET</text>
      <text x="-105" y="-16" fill="#34D399">&gt; STATUS: 200 OK<tspan fill="#10B981" font-weight="900">_</tspan></text>
    </g>

    <!-- Cute Hacker Anime Eyes (Glowing Green Glint Reflecting Terminal!) -->
    <g transform="translate(68, -48)">
      <!-- Cool Hacker Pixel / Matrix Sunglasses or Eyes -->
      <polygon points="0,-10 3,-2 10,0 3,2 0,10 -3,2 -10,0 -3,-2" fill="#34D399" transform="scale(0.8)" />
      <circle cx="-4" cy="-5" r="3" fill="#FFFFFF" />
    </g>

    <!-- 5. Headset with dark mic joint ring -->
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#1E293B" stroke-width="22" stroke-linecap="round" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" fill="none" stroke="#10B981" stroke-width="8" stroke-linecap="round" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#10B981" stroke-width="6" />
    <rect x="-200" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    <rect x="165" y="-85" width="45" height="85" rx="20" fill="#0F172A" stroke="#10B981" stroke-width="6" />
    <rect x="175" y="-70" width="25" height="55" rx="12" fill="#1E293B" />
    

    
    <!-- 6. Mechanical Keyboard & High-Speed Typing Action -->
    <g transform="translate(0, 48)">
      <rect x="-105" y="-18" width="210" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="3" />
      
      <!-- Keycaps Grid -->
      <g fill="#1E293B" stroke="#10B981" stroke-width="1.2" rx="3">
        <rect x="-95" y="-12" width="14" height="10" rx="2" />
        <rect x="-76" y="-12" width="14" height="10" rx="2" fill="#065F46" />
        <rect x="-57" y="-12" width="14" height="10" rx="2" />
        <rect x="-38" y="-12" width="14" height="10" rx="2" fill="#047857" />
        <rect x="-19" y="-12" width="14" height="10" rx="2" />
        <rect x="0" y="-12" width="14" height="10" rx="2" fill="#047857" />
        <rect x="19" y="-12" width="14" height="10" rx="2" />
        <rect x="38" y="-12" width="14" height="10" rx="2" fill="#065F46" />
        <rect x="57" y="-12" width="14" height="10" rx="2" />
        <rect x="76" y="-12" width="19" height="10" rx="2" fill="#047857" />

        <rect x="-95" y="2" width="18" height="10" rx="2" />
        <rect x="-72" y="2" width="14" height="10" rx="2" />
        <rect x="-53" y="2" width="14" height="10" rx="2" />
        <rect x="-34" y="2" width="30" height="10" rx="2" fill="#065F46" />
        <rect x="1" y="2" width="14" height="10" rx="2" />
        <rect x="20" y="2" width="14" height="10" rx="2" fill="#047857" />
        <rect x="39" y="2" width="14" height="10" rx="2" />
        <rect x="58" y="2" width="14" height="10" rx="2" />
        <rect x="77" y="2" width="18" height="10" rx="2" />
      </g>

      <!-- Prominent Typing Speed Lines & Motion Blur -->
      <g stroke="#34D399" stroke-width="2.5" stroke-linecap="round">
        <line x1="-58" y1="-28" x2="-45" y2="-12" />
        <line x1="-32" y1="-30" x2="-25" y2="-12" />
        <line x1="25" y1="-30" x2="32" y2="-12" />
        <line x1="45" y1="-28" x2="58" y2="-12" />
      </g>

      <!-- Fast Blurring Chibi Hands -->
      <!-- Left Hand -->
      <circle cx="-40" cy="-6" r="16" fill="#3877F6" stroke="#FFFFFF" stroke-width="3.5" />
      <circle cx="-44" cy="-10" r="4" fill="#FFFFFF" opacity="0.6" />
      <!-- Right Hand -->
      <circle cx="40" cy="-6" r="16" fill="#5AC1C4" stroke="#FFFFFF" stroke-width="3.5" />
      <circle cx="36" cy="-10" r="4" fill="#FFFFFF" opacity="0.6" />

      <!-- Spark particles of pure speed -->
      <polygon points="-62,-16 -58,-14 -60,-10 -64,-12" fill="#FDE047" />
      <polygon points="62,-16 66,-12 60,-10 58,-14" fill="#FDE047" />
    </g>
<!-- 7. Tagline Banner: SUDO RESOLVE -->
    <g transform="translate(0, 92)">
      <rect x="-80" y="-13" width="160" height="26" rx="13" fill="#022C22" stroke="#10B981" stroke-width="2.5" />
      <text y="5" font-family="'Noto Sans', monospace, sans-serif" font-size="10.5" font-weight="900" fill="#34D399" letter-spacing="2" text-anchor="middle">⚡ SUDO RESOLVE</text>
    </g>

    <!-- Outermost Layer: Boom Mic (Nothing covers the mic!) -->
    <path d="M -190 -10 C -190 70, -110 95, -75 75" fill="none" stroke="#1E293B" stroke-width="10" stroke-linecap="round" />
    <circle cx="-70" cy="73" r="14" fill="#10B981" stroke="#1E293B" stroke-width="4" />
  </g>
</svg>"""

cutline_09 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">
  {svg_09.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 540" width="540" height="540">', '').replace('</svg>', '')}
  <g id="CutContour" transform="translate(270, 270)" fill="none" stroke="#FF00FF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
    <circle cx="0" cy="-230" r="22" stroke-width="24" />
    <line x1="0" y1="-150" x2="0" y2="-230" stroke-width="32" />
    <path d="M -175 -50 C -190 -220, 190 -220, 175 -50" stroke-width="46" />
    <rect x="-210" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <rect x="165" y="-85" width="45" height="85" rx="20" stroke-width="24" />
    <path d="M -160 -150 Q -160 -160, -140 -160 L 140 -160 Q 160 -160, 160 -140 L 160 -40 A 25 25 0 0 0 160 10 L 160 50 Q 160 70, 140 70 L -90 70 L -160 120 L -160 10 A 25 25 0 0 0 -160 -40 Z" stroke-width="24" />
    <rect x="-115" y="25" width="230" height="60" rx="16" stroke-width="26" />
    <circle cx="-70" cy="73" r="14" stroke-width="24" />
  </g>
</svg>"""

# ==============================================================================
# BATCH GENERATION FOR ALL 9 STICKERS
# ==============================================================================
items = [
    ("tixdesk-sticker-01-hero-mark", svg_01, cutline_01),
    ("tixdesk-sticker-02-mascot-tixie", svg_02, cutline_02),
    ("tixdesk-sticker-03-detective-bug-hunter", svg_03, cutline_03),
    ("tixdesk-sticker-04-tixie-caffeine-nightshift", svg_04, cutline_04),
    ("tixdesk-sticker-05-tixie-on-fire", svg_05, cutline_05),
    ("tixdesk-sticker-06-tixie-neon", svg_06, cutline_06),
    ("tixdesk-sticker-07-tixie-rocket-lgtm", svg_07, cutline_07),
    ("tixdesk-sticker-08-tixie-off-and-on", svg_08, cutline_08),
    ("tixdesk-sticker-09-tixie-sudo-resolve", svg_09, cutline_09),
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

print("Generated full 9-sticker collection successfully!")
