#!/usr/bin/env python3
"""
TixDesk Expo Sticker Generator
Generates:
  - 3x High-Fidelity SVG Stickers
  - 3x Print-Ready Cutline SVGs (Magenta 100% Spot CutContour)
  - 3x 300 DPI High-Resolution Transparent PNGs
  - 3x Vector Print-Ready PDFs
  - 1x Interactive HTML & PNG Preview Sheet
"""

import os
import subprocess

OUTPUT_DIR = "/home/graha/tixdesk-expo-stickers"
SVG_DIR = os.path.join(OUTPUT_DIR, "assets/svg")
PNG_DIR = os.path.join(OUTPUT_DIR, "assets/png")
CUTLINE_DIR = os.path.join(OUTPUT_DIR, "assets/print-ready-cutlines")

os.makedirs(SVG_DIR, exist_ok=True)
os.makedirs(PNG_DIR, exist_ok=True)
os.makedirs(CUTLINE_DIR, exist_ok=True)

# Official TixDesk Logo Path (Normalized to 0,0 center)
# Original bounding box: X [103.0 .. 286.69] (W=183.69, CX=194.845)
#                        Y [250.82 .. 406.87] (H=156.05, CY=328.845)
LOGO_PATH = (
    "M106.07 258.81 L104.23 262.5 L103.61 264.65 L103.61 265.87 L103.31 266.18 "
    "L103.31 293.52 L103 293.83 L103 296.29 L103.31 297.21 L106.69 298.13 L109.76 299.66 "
    "L110.99 300.59 L114.98 304.89 L117.13 309.8 L117.13 311.03 L117.44 311.34 "
    "L117.44 315.64 L117.13 315.94 L117.13 317.48 L116.52 319.32 L114.06 323.62 "
    "L110.68 327 L109.76 327.31 L108.22 328.54 L105.46 329.46 L104.54 329.46 "
    "L103.31 330.08 L103.31 360.49 L103.61 360.79 L103.92 363.25 L105.76 367.55 "
    "L107.61 370.01 L110.68 372.77 L116.21 375.54 L119.59 375.84 L119.89 376.15 "
    "L144.78 376.15 L145.39 376.46 L146.01 377.38 L146.01 405.03 L147.23 406.56 "
    "L149.08 406.87 L150.92 405.95 L177.34 379.22 L180.1 376.15 L180.72 374.92 "
    "L180.72 301.81 L179.79 300.28 L144.78 300.28 L143.24 299.66 L142.63 299.05 "
    "L142.01 297.51 L142.01 279.7 L142.63 278.16 L143.55 277.24 L144.47 277.24 "
    "L144.78 276.93 L245.22 276.93 L245.53 277.24 L246.45 277.24 L247.68 278.47 "
    "L247.68 279.39 L247.99 279.7 L247.99 297.82 L247.68 298.74 L246.15 299.97 "
    "L244.61 299.97 L244.3 300.28 L209.9 300.28 L208.98 301.51 L208.98 374.92 "
    "L209.59 375.84 L210.51 376.15 L270.72 376.15 L271.03 375.84 L272.87 375.84 "
    "L277.48 374 L280.55 371.85 L283.62 368.47 L285.46 365.09 L286.69 360.79 "
    "L286.69 330.08 L286.08 329.46 L282.09 328.54 L278.4 326.08 L275.63 323.32 "
    "L274.1 320.86 L272.87 317.79 L272.87 316.25 L272.56 315.94 L272.56 311.03 "
    "L272.87 310.72 L272.87 309.8 L274.1 306.42 L275.63 303.96 L280.24 299.66 "
    "L283.31 298.13 L286.08 297.51 L286.69 296.9 L286.69 265.57 L285.46 261.57 "
    "L283.62 258.2 L282.39 256.66 L279.32 253.89 L275.02 251.74 L274.1 251.74 "
    "L272.87 251.13 L271.03 251.13 L270.72 250.82 L120.51 250.82 L120.2 251.13 "
    "L117.74 251.13 L113.14 252.67 L109.76 254.82 Z"
)

# -------------------------------------------------------------
# 1. STICKER 01: THE HERO DIE-CUT MARK
# -------------------------------------------------------------
def build_sticker_01():
    # Width 800, Height 700 (Scale approx 3.2x)
    # Centered at (400, 350)
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 700" width="800" height="700">
  <defs>
    <!-- Primary Brand Gradient -->
    <linearGradient id="tixdeskGrad01" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6" />
      <stop offset="50%" stop-color="#1D9BF0" />
      <stop offset="100%" stop-color="#06B6D4" />
    </linearGradient>

    <!-- Subtle White Sheen Overlay -->
    <linearGradient id="tixdeskSheen01" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.22" />
      <stop offset="45%" stop-color="#FFFFFF" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.0" />
    </linearGradient>

    <!-- Ambient Shadow for Screen Presentation -->
    <filter id="stickerShadow01" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#0B1B3D" flood-opacity="0.28" />
    </filter>
  </defs>

  <g filter="url(#stickerShadow01)">
    <!-- LAYER 1: Die-Cut White Base Contour (Thickness = 48px) -->
    <g transform="translate(400, 350) scale(3.2) translate(-194.845, -328.845)">
      <path d="{LOGO_PATH}"
            fill="#FFFFFF"
            stroke="#FFFFFF"
            stroke-width="36"
            stroke-linejoin="round"
            stroke-linecap="round" />
    </g>

    <!-- LAYER 2: Colored Gradient Ticket Mark -->
    <g transform="translate(400, 350) scale(3.2) translate(-194.845, -328.845)">
      <!-- Ambient Drop Inside Shadow -->
      <path d="{LOGO_PATH}"
            fill="#2563EB"
            opacity="0.12"
            transform="translate(0, 4)" />

      <!-- Main Gradient Fill -->
      <path d="{LOGO_PATH}" fill="url(#tixdeskGrad01)" />

      <!-- Inner Top Edge Highlights -->
      <path d="{LOGO_PATH}" fill="url(#tixdeskSheen01)" />

      <!-- Delicate Crisp Inner Stroke -->
      <path d="{LOGO_PATH}"
            fill="none"
            stroke="#FFFFFF"
            stroke-width="0.75"
            stroke-opacity="0.45"
            stroke-linejoin="round" />
    </g>
  </g>
</svg>'''

    # Cutline file for sticker 01
    svg_cutline = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 700" width="800" height="700">
  <!-- CutContour Path in 100% Magenta Spot Color for Roland / Mimaki / Summa Plotters -->
  <g transform="translate(400, 350) scale(3.2) translate(-194.845, -328.845)">
    <path id="CutContour"
          d="{LOGO_PATH}"
          fill="none"
          stroke="#FF00FF"
          stroke-width="1.5"
          stroke-linejoin="round"
          stroke-linecap="round" />
  </g>
</svg>'''

    return svg_content, svg_cutline


# -------------------------------------------------------------
# 2. STICKER 02: THE TECH BADGE ("SUPPORT HERO / ZERO OVERDUE SLAs")
# -------------------------------------------------------------
def build_sticker_02():
    # Hexagon Badge, 800 x 920 px (~6.8 cm x 7.8 cm at 300 DPI)
    # Hexagon Points: (400, 40), (740, 240), (740, 680), (400, 880), (60, 680), (60, 240)
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 920" width="800" height="920">
  <defs>
    <!-- Background Gradient for Badge -->
    <linearGradient id="badgeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#0B132B" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>

    <!-- Glowing Rim Gradient -->
    <linearGradient id="rimGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="50%" stop-color="#3B82F6" />
      <stop offset="100%" stop-color="#06B6D4" />
    </linearGradient>

    <!-- Logo Gradient -->
    <linearGradient id="tixdeskGrad02" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6" />
      <stop offset="50%" stop-color="#1D9BF0" />
      <stop offset="100%" stop-color="#06B6D4" />
    </linearGradient>

    <!-- Shadow -->
    <filter id="badgeShadow" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#020617" flood-opacity="0.38" />
    </filter>

    <filter id="cyanGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="12" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <g filter="url(#badgeShadow)">
    <!-- White Die-Cut Background Contour (Outer border) -->
    <path d="M 400 30
             Q 412 30, 420 35
             L 750 225
             Q 760 231, 760 245
             L 760 675
             Q 760 689, 750 695
             L 420 885
             Q 412 890, 400 890
             Q 388 890, 380 885
             L 50 695
             Q 40 689, 40 675
             L 40 245
             Q 40 231, 50 225
             L 380 35
             Q 388 30, 400 30 Z"
          fill="#FFFFFF" />

    <!-- Hexagon Main Dark Surface -->
    <path d="M 400 52
             Q 410 52, 417 56
             L 730 236
             Q 738 241, 738 252
             L 738 668
             Q 738 679, 730 684
             L 417 864
             Q 410 868, 400 868
             Q 390 868, 383 864
             L 70 684
             Q 62 679, 62 668
             L 62 252
             Q 62 241, 70 236
             L 383 56
             Q 390 52, 400 52 Z"
          fill="url(#badgeBg)"
          stroke="url(#rimGrad)"
          stroke-width="4.5" />

    <!-- Inner Subtle Tech Pattern Lines -->
    <line x1="120" y1="200" x2="680" y2="200" stroke="#1E293B" stroke-width="1.5" stroke-dasharray="6,8" />
    <line x1="120" y1="720" x2="680" y2="720" stroke="#1E293B" stroke-width="1.5" stroke-dasharray="6,8" />

    <!-- TOP PILL: "ZERO OVERDUE SLAs" -->
    <g transform="translate(400, 140)">
      <rect x="-170" y="-22" width="340" height="44" rx="22"
            fill="#1E293B" stroke="#06B6D4" stroke-width="2" />
      <!-- Pulsing Dot -->
      <circle cx="-135" cy="0" r="7" fill="#10B981" />
      <circle cx="-135" cy="0" r="11" fill="#10B981" opacity="0.35" />
      <text x="-115" y="6"
            font-family="'Noto Sans', 'Segoe UI', system-ui, sans-serif"
            font-size="18" font-weight="900"
            letter-spacing="3"
            fill="#FFFFFF">ZERO OVERDUE SLAs</text>
    </g>

    <!-- CENTER LOGO ICON -->
    <g transform="translate(400, 360)">
      <!-- Soft Cyan Glow Behind Icon -->
      <circle cx="0" cy="0" r="120" fill="#0284C7" opacity="0.22" filter="blur(20px)" />
      
      <!-- Scaled TixDesk Logo Mark -->
      <g transform="scale(2.2) translate(-194.845, -328.845)">
        <path d="{LOGO_PATH}" fill="url(#tixdeskGrad02)" />
        <path d="{LOGO_PATH}" fill="none" stroke="#FFFFFF" stroke-width="0.6" stroke-opacity="0.5" />
      </g>
    </g>

    <!-- BRAND WORDMARK "TixDesk" -->
    <text x="400" y="555"
          font-family="'Noto Sans', 'Segoe UI', system-ui, sans-serif"
          font-size="52" font-weight="900"
          letter-spacing="2"
          text-anchor="middle"
          fill="#FFFFFF">TixDesk</text>

    <!-- 3 PILL MODULES: TICKET • SLA • KB -->
    <g transform="translate(400, 620)">
      <!-- Ticket Pill -->
      <g transform="translate(-155, 0)">
        <rect x="-55" y="-18" width="110" height="36" rx="18" fill="#1E293B" stroke="#3B82F6" stroke-width="1.8" />
        <circle cx="-32" cy="0" r="5" fill="#3B82F6" />
        <text x="-16" y="6" font-family="'Noto Sans', sans-serif" font-size="16" font-weight="800" fill="#BFDBFE">Ticket</text>
      </g>

      <!-- SLA Pill -->
      <g transform="translate(0, 0)">
        <rect x="-50" y="-18" width="100" height="36" rx="18" fill="#1E293B" stroke="#06B6D4" stroke-width="1.8" />
        <circle cx="-28" cy="0" r="5" fill="#06B6D4" />
        <text x="-14" y="6" font-family="'Noto Sans', sans-serif" font-size="16" font-weight="900" fill="#A5F3FC">SLA</text>
      </g>

      <!-- KB Pill -->
      <g transform="translate(155, 0)">
        <rect x="-48" y="-18" width="96" height="36" rx="18" fill="#1E293B" stroke="#10B981" stroke-width="1.8" />
        <circle cx="-26" cy="0" r="5" fill="#10B981" />
        <text x="-12" y="6" font-family="'Noto Sans', sans-serif" font-size="16" font-weight="900" fill="#BBF7D0">KB</text>
      </g>
    </g>

    <!-- BOTTOM SUBTEXT: MISSION-CRITICAL SUPPORT -->
    <text x="400" y="780"
          font-family="'Noto Sans', 'Segoe UI', system-ui, sans-serif"
          font-size="21" font-weight="900"
          letter-spacing="4"
          text-anchor="middle"
          fill="#38BDF8">SUPPORT HERO • EXPO 2026</text>

    <!-- Small Tech Stamp -->
    <text x="400" y="822"
          font-family="'Noto Sans', monospace, sans-serif"
          font-size="16" font-weight="800"
          letter-spacing="2.5"
          text-anchor="middle"
          fill="#94A3B8">200 OK — TICKET RESOLVED</text>
  </g>
</svg>'''

    # Cutline file for sticker 02
    svg_cutline = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 920" width="800" height="920">
  <path id="CutContour"
        d="M 400 30
           Q 412 30, 420 35
           L 750 225
           Q 760 231, 760 245
           L 760 675
           Q 760 689, 750 695
           L 420 885
           Q 412 890, 400 890
           Q 388 890, 380 885
           L 50 695
           Q 40 689, 40 675
           L 40 245
           Q 40 231, 50 225
           L 380 35
           Q 388 30, 400 30 Z"
        fill="none"
        stroke="#FF00FF"
        stroke-width="1.5" />
</svg>'''

    return svg_content, svg_cutline


# -------------------------------------------------------------
# 3. STICKER 03: THE EXECUTIVE BRAND LOCKUP (HORIZONTAL)
# -------------------------------------------------------------
def build_sticker_03():
    # Width 1140, Height 460 (~9.6 cm x 3.9 cm at 300 DPI)
    # Stadium/Capsule contour with rounded edges
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1140 460" width="1140" height="460">
  <defs>
    <!-- Brand Gradient -->
    <linearGradient id="tixdeskGrad03" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6" />
      <stop offset="50%" stop-color="#1D9BF0" />
      <stop offset="100%" stop-color="#06B6D4" />
    </linearGradient>

    <!-- Text Gradient for Accent -->
    <linearGradient id="textGrad03" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="70%" stop-color="#0B1B3D" />
      <stop offset="100%" stop-color="#0284C7" />
    </linearGradient>

    <!-- Subtle Container Background -->
    <linearGradient id="containerBg03" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#F8FAFC" />
    </linearGradient>

    <!-- Shadow -->
    <filter id="lockupShadow" x="-10%" y="-15%" width="120%" height="130%">
      <feDropShadow dx="0" dy="16" stdDeviation="20" flood-color="#0F172A" flood-opacity="0.22" />
    </filter>
  </defs>

  <g filter="url(#lockupShadow)">
    <!-- LAYER 1: White Die-Cut Outer Padding -->
    <rect x="25" y="25" width="1090" height="410" rx="90"
          fill="#FFFFFF" />

    <!-- LAYER 2: Inner Subtle Card Border -->
    <rect x="37" y="37" width="1066" height="386" rx="78"
          fill="url(#containerBg03)"
          stroke="#E2E8F0"
          stroke-width="3" />

    <!-- LEFT SIDE: TixDesk Logo Mark -->
    <g transform="translate(185, 230) scale(1.65) translate(-194.845, -328.845)">
      <!-- Ambient Drop Inside Shadow -->
      <path d="{LOGO_PATH}" fill="#2563EB" opacity="0.12" transform="translate(0, 5)" />
      <!-- Logo Body -->
      <path d="{LOGO_PATH}" fill="url(#tixdeskGrad03)" />
      <!-- Top Highlight -->
      <path d="{LOGO_PATH}" fill="none" stroke="#FFFFFF" stroke-width="0.8" stroke-opacity="0.5" />
    </g>

    <!-- RIGHT SIDE: Typography & Details -->
    <g transform="translate(370, 0)">
      <!-- Main Brand Name -->
      <text x="0" y="190"
            font-family="'Noto Sans', 'Segoe UI', system-ui, sans-serif"
            font-size="88" font-weight="900"
            letter-spacing="-1.5"
            fill="url(#textGrad03)">TixDesk</text>

      <!-- Subtitle Tagline -->
      <text x="4" y="248"
            font-family="'Noto Sans', 'Segoe UI', system-ui, sans-serif"
            font-size="24" font-weight="700"
            letter-spacing="2"
            fill="#475569">Helpdesk &amp; Ticketing Platform</text>

      <!-- Horizontal Divider Accent -->
      <rect x="4" y="275" width="670" height="4" rx="2" fill="url(#tixdeskGrad03)" />

      <!-- Feature Pill Chips -->
      <g transform="translate(4, 335)">
        <!-- Pill 1: Ticket Engine -->
        <g transform="translate(0, 0)">
          <rect x="0" y="-22" width="190" height="44" rx="22" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.8" />
          <circle cx="28" cy="0" r="6" fill="#3B82F6" />
          <text x="46" y="7" font-family="'Noto Sans', sans-serif" font-size="16" font-weight="700" fill="#1E40AF">Ticket System</text>
        </g>

        <!-- Pill 2: Business SLA -->
        <g transform="translate(210, 0)">
          <rect x="0" y="-22" width="180" height="44" rx="22" fill="#ECFEFF" stroke="#A5F3FC" stroke-width="1.8" />
          <circle cx="28" cy="0" r="6" fill="#06B6D4" />
          <text x="46" y="7" font-family="'Noto Sans', sans-serif" font-size="16" font-weight="800" fill="#0E7490">Business SLA</text>
        </g>

        <!-- Pill 3: Knowledge Base -->
        <g transform="translate(410, 0)">
          <rect x="0" y="-22" width="190" height="44" rx="22" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.8" />
          <circle cx="28" cy="0" r="6" fill="#10B981" />
          <text x="46" y="7" font-family="'Noto Sans', sans-serif" font-size="16" font-weight="800" fill="#166534">Knowledge Base</text>
        </g>
      </g>
    </g>
  </g>
</svg>'''

    # Cutline file for sticker 03
    svg_cutline = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1140 460" width="1140" height="460">
  <rect id="CutContour"
        x="25" y="25" width="1090" height="410" rx="90"
        fill="none"
        stroke="#FF00FF"
        stroke-width="1.5" />
</svg>'''

    return svg_content, svg_cutline


# -------------------------------------------------------------
# MAIN BUILD SCRIPT
# -------------------------------------------------------------
def main():
    print("Generating TixDesk Expo Stickers...")

    stickers = [
        ("tixdesk-sticker-01-hero-mark", build_sticker_01()),
        ("tixdesk-sticker-02-support-hero-badge", build_sticker_02()),
        ("tixdesk-sticker-03-brand-lockup", build_sticker_03()),
    ]

    for name, (svg_art, svg_cut) in stickers:
        svg_art_path = os.path.join(SVG_DIR, f"{name}.svg")
        svg_cut_path = os.path.join(CUTLINE_DIR, f"{name}-cutline.svg")
        png_path = os.path.join(PNG_DIR, f"{name}-300dpi.png")
        pdf_path = os.path.join(OUTPUT_DIR, f"{name}-print.pdf")

        # Write SVG Artwork
        with open(svg_art_path, "w") as f:
            f.write(svg_art)
        print(f"Saved: {svg_art_path}")

        # Write Cutline SVG
        with open(svg_cut_path, "w") as f:
            f.write(svg_cut)
        print(f"Saved: {svg_cut_path}")

        # Render 300 DPI Transparent PNG via rsvg-convert
        cmd_png = ["rsvg-convert", "-d", "300", "-p", "300", svg_art_path, "-o", png_path]
        subprocess.run(cmd_png, check=True)
        print(f"Rendered PNG: {png_path}")

        # Render Vector PDF via rsvg-convert
        cmd_pdf = ["rsvg-convert", "-f", "pdf", svg_art_path, "-o", pdf_path]
        subprocess.run(cmd_pdf, check=True)
        print(f"Rendered PDF: {pdf_path}")

    # Build Interactive HTML Preview Sheet
    html_preview_path = os.path.join(OUTPUT_DIR, "preview.html")
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TixDesk Expo Stickers — Presentation &amp; Quality Check</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: #0b0f19;
      color: #f8fafc;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      padding: 40px 20px;
      line-height: 1.6;
    }
    .header {
      text-align: center;
      margin-bottom: 50px;
    }
    .header h1 {
      font-size: 38px;
      font-weight: 900;
      background: linear-gradient(135deg, #38bdf8, #818cf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 10px;
    }
    .header p {
      color: #94a3b8;
      font-size: 18px;
    }
    .badge-bar {
      display: inline-flex;
      gap: 12px;
      margin-top: 15px;
    }
    .badge {
      background: #1e293b;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 600;
      color: #38bdf8;
      border: 1px solid #334155;
    }
    .container {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 50px;
    }
    .card {
      background: #131b2e;
      border: 1px solid #1e293b;
      border-radius: 24px;
      padding: 36px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }
    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 16px;
    }
    .card-title h2 {
      font-size: 24px;
      font-weight: 800;
      color: #ffffff;
    }
    .card-title span {
      font-size: 14px;
      color: #64748b;
    }
    .specs {
      font-size: 14px;
      color: #38bdf8;
      background: #0f172a;
      padding: 8px 16px;
      border-radius: 8px;
      border: 1px solid #1e293b;
      font-family: monospace;
    }
    .preview-stage {
      background: radial-gradient(circle at center, #1e293b 0%, #0f172a 100%);
      border-radius: 16px;
      padding: 40px;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 420px;
      position: relative;
      overflow: hidden;
      border: 1px dashed #334155;
    }
    /* Grid background to preview transparency */
    .preview-stage::before {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background-image: 
        linear-gradient(45deg, #182234 25%, transparent 25%), 
        linear-gradient(-45deg, #182234 25%, transparent 25%), 
        linear-gradient(45deg, transparent 75%, #182234 75%), 
        linear-gradient(-45deg, transparent 75%, #182234 75%);
      background-size: 24px 24px;
      background-position: 0 0, 0 12px, 12px -12px, -12px 0px;
      opacity: 0.35;
      pointer-events: none;
    }
    .preview-stage img {
      max-width: 100%;
      height: auto;
      max-height: 380px;
      position: relative;
      z-index: 1;
      filter: drop-shadow(0 15px 25px rgba(0,0,0,0.5));
      transition: transform 0.3s ease;
    }
    .preview-stage img:hover {
      transform: scale(1.03);
    }
    .card-desc {
      margin-top: 20px;
      color: #94a3b8;
      font-size: 15px;
    }
    .download-links {
      margin-top: 20px;
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #2563eb;
      color: white;
      text-decoration: none;
      padding: 10px 18px;
      border-radius: 10px;
      font-size: 14px;
      font-weight: 700;
      transition: background 0.2s;
    }
    .btn:hover { background: #1d4ed8; }
    .btn-secondary {
      background: #1e293b;
      color: #cbd5e1;
      border: 1px solid #334155;
    }
    .btn-secondary:hover { background: #334155; color: white; }
    .btn-magenta {
      background: #be185d;
      border: 1px solid #f43f5e;
    }
    .btn-magenta:hover { background: #9d174d; }
  </style>
</head>
<body>

  <div class="header">
    <h1>TixDesk Expo Sticker Collection</h1>
    <p>Official High-Craft Merchandise for Tech Expo (November 17–18, 2026)</p>
    <div class="badge-bar">
      <span class="badge">Target Size: ~6.5–7 cm</span>
      <span class="badge">300 DPI CMYK-Ready</span>
      <span class="badge">Full Die-Cut Cutline Included</span>
      <span class="badge">Zero AI-Slop Design</span>
    </div>
  </div>

  <div class="container">

    <!-- STICKER 1 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title">
          <h2>Sticker 01: The Pure Hero Die-Cut</h2>
          <span>Universal brand icon for phone cases, laptops, and gadget lids</span>
        </div>
        <div class="specs">Format: ~7.0 × 6.1 cm • Die-Cut Contour</div>
      </div>
      <div class="preview-stage">
        <img src="assets/png/tixdesk-sticker-01-hero-mark-300dpi.png" alt="Sticker 01 Hero Mark">
      </div>
      <div class="card-desc">
        Focuses on the pure iconic silhouette of TixDesk: a support ticket combined with a speech bubble and negative space 'T'. Features the signature Royal Blue to Cyan gradient, subtle light sheen, and a 2.5mm solid white contour for effortless die-cutting.
      </div>
      <div class="download-links">
        <a class="btn" href="assets/svg/tixdesk-sticker-01-hero-mark.svg" target="_blank">📄 SVG Vector</a>
        <a class="btn btn-secondary" href="tixdesk-sticker-01-hero-mark-print.pdf" target="_blank">🖨️ Print PDF</a>
        <a class="btn btn-secondary" href="assets/png/tixdesk-sticker-01-hero-mark-300dpi.png" target="_blank">🖼️ 300 DPI PNG</a>
        <a class="btn btn-magenta" href="assets/print-ready-cutlines/tixdesk-sticker-01-hero-mark-cutline.svg" target="_blank">✂️ Magenta Cutline</a>
      </div>
    </div>

    <!-- STICKER 2 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title">
          <h2>Sticker 02: Support Hero / SLA Guard (Dev Badge)</h2>
          <span>High-tech hexagonal badge crafted for students, engineers, and ops enthusiasts</span>
        </div>
        <div class="specs">Format: ~6.8 × 7.8 cm • Hexagonal Badge</div>
      </div>
      <div class="preview-stage">
        <img src="assets/png/tixdesk-sticker-02-support-hero-badge-300dpi.png" alt="Sticker 02 Tech Badge">
      </div>
      <div class="card-desc">
        Inspired by modern developer badges (Docker, Kubernetes, Rust). Features dark slate cyber aesthetic, cyan glowing accents, glowing central TixDesk mark, the 3 feature pills (Ticket, SLA, KB), and proud slogans: "ZERO OVERDUE SLAs" and "200 OK — TICKET RESOLVED". Highly attractive for laptop stickers.
      </div>
      <div class="download-links">
        <a class="btn" href="assets/svg/tixdesk-sticker-02-support-hero-badge.svg" target="_blank">📄 SVG Vector</a>
        <a class="btn btn-secondary" href="tixdesk-sticker-02-support-hero-badge-print.pdf" target="_blank">🖨️ Print PDF</a>
        <a class="btn btn-secondary" href="assets/png/tixdesk-sticker-02-support-hero-badge-300dpi.png" target="_blank">🖼️ 300 DPI PNG</a>
        <a class="btn btn-magenta" href="assets/print-ready-cutlines/tixdesk-sticker-02-support-hero-badge-cutline.svg" target="_blank">✂️ Magenta Cutline</a>
      </div>
    </div>

    <!-- STICKER 3 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title">
          <h2>Sticker 03: Executive Brand Lockup</h2>
          <span>Clean horizontal capsule for enterprise attendees, notebooks, and B2B booths</span>
        </div>
        <div class="specs">Format: ~9.6 × 3.9 cm • Capsule Pill Contour</div>
      </div>
      <div class="preview-stage">
        <img src="assets/png/tixdesk-sticker-03-brand-lockup-300dpi.png" alt="Sticker 03 Brand Lockup">
      </div>
      <div class="card-desc">
        Presents the complete official lockup: the TixDesk mark alongside the bold PascalCase wordmark, tagline "Helpdesk &amp; Ticketing Platform", and 3 soft-tinted status chips. Clean, credible, and trustworthy.
      </div>
      <div class="download-links">
        <a class="btn" href="assets/svg/tixdesk-sticker-03-brand-lockup.svg" target="_blank">📄 SVG Vector</a>
        <a class="btn btn-secondary" href="tixdesk-sticker-03-brand-lockup-print.pdf" target="_blank">🖨️ Print PDF</a>
        <a class="btn btn-secondary" href="assets/png/tixdesk-sticker-03-brand-lockup-300dpi.png" target="_blank">🖼️ 300 DPI PNG</a>
        <a class="btn btn-magenta" href="assets/print-ready-cutlines/tixdesk-sticker-03-brand-lockup-cutline.svg" target="_blank">✂️ Magenta Cutline</a>
      </div>
    </div>

  </div>

</body>
</html>'''

    with open(html_preview_path, "w") as f:
        f.write(html_content)
    print(f"Generated Interactive Preview Sheet: {html_preview_path}")

    # Generate a composite showcase image (MacBook / Desk Mockup Style)
    showcase_svg = '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1600 1000" width="1600" height="1000">
  <defs>
    <linearGradient id="lidGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E2430" />
      <stop offset="50%" stop-color="#111622" />
      <stop offset="100%" stop-color="#0B0E17" />
    </linearGradient>

    <radialGradient id="stageGlow" cx="50%" cy="45%" r="65%">
      <stop offset="0%" stop-color="#1E3A8A" stop-opacity="0.35" />
      <stop offset="60%" stop-color="#0B0E17" stop-opacity="0.1" />
      <stop offset="100%" stop-color="#0B0E17" stop-opacity="0" />
    </radialGradient>

    <filter id="drop" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="20" stdDeviation="25" flood-color="#000000" flood-opacity="0.6" />
    </filter>
  </defs>

  <rect width="100%" height="100%" fill="url(#lidGrad)" />
  <rect width="100%" height="100%" fill="url(#stageGlow)" />

  <g opacity="0.06" stroke="#38BDF8" stroke-width="1">
    <line x1="0" y1="160" x2="1600" y2="160" />
    <line x1="0" y1="500" x2="1600" y2="500" />
    <line x1="0" y1="840" x2="1600" y2="840" />
    <line x1="300" y1="0" x2="300" y2="1000" />
    <line x1="800" y1="0" x2="800" y2="1000" />
    <line x1="1300" y1="0" x2="1300" y2="1000" />
  </g>

  <text x="800" y="85"
        font-family="'Noto Sans', 'Segoe UI', system-ui, sans-serif"
        font-size="34" font-weight="900"
        letter-spacing="5"
        text-anchor="middle"
        fill="#F8FAFC">TIXDESK EXPO STICKER TRIO</text>
  <text x="800" y="125"
        font-family="'Noto Sans', sans-serif"
        font-size="16" font-weight="700"
        letter-spacing="2"
        text-anchor="middle"
        fill="#38BDF8">OFFICIAL PHYSICAL MERCHANDISE PACK • NOVEMBER 17–18, 2026</text>

  <g transform="translate(80, 200) rotate(-3 250 250)" filter="url(#drop)">
    <image href="assets/png/tixdesk-sticker-01-hero-mark-300dpi.png" x="0" y="0" width="480" height="420" />
    <text x="240" y="470" font-family="'Noto Sans', sans-serif" font-size="20" font-weight="800" fill="#94A3B8" text-anchor="middle">01 • THE PURE HERO MARK</text>
    <text x="240" y="495" font-family="'Noto Sans', sans-serif" font-size="14" font-weight="600" fill="#64748B" text-anchor="middle">~7.0 × 6.1 cm | Universal Die-Cut</text>
  </g>

  <g transform="translate(560, 170) rotate(2 250 280)" filter="url(#drop)">
    <image href="assets/png/tixdesk-sticker-02-support-hero-badge-300dpi.png" x="0" y="0" width="480" height="550" />
    <text x="240" y="600" font-family="'Noto Sans', sans-serif" font-size="20" font-weight="800" fill="#38BDF8" text-anchor="middle">02 • SUPPORT HERO DEV BADGE</text>
    <text x="240" y="625" font-family="'Noto Sans', sans-serif" font-size="14" font-weight="600" fill="#64748B" text-anchor="middle">~6.8 × 7.8 cm | Hexagonal Shield</text>
  </g>

  <g transform="translate(1030, 230) rotate(-2 250 200)" filter="url(#drop)">
    <image href="assets/png/tixdesk-sticker-03-brand-lockup-300dpi.png" x="0" y="0" width="520" height="210" />
    <text x="260" y="260" font-family="'Noto Sans', sans-serif" font-size="20" font-weight="800" fill="#94A3B8" text-anchor="middle">03 • EXECUTIVE LOCKUP</text>
    <text x="260" y="285" font-family="'Noto Sans', sans-serif" font-size="14" font-weight="600" fill="#64748B" text-anchor="middle">~9.6 × 3.9 cm | Pill Contour</text>
  </g>

  <g transform="translate(800, 930)">
    <rect x="-400" y="-25" width="800" height="50" rx="25" fill="#131B2E" stroke="#1E293B" stroke-width="1.5" />
    <text x="0" y="6" font-family="'Noto Sans', sans-serif" font-size="15" font-weight="700" fill="#94A3B8" text-anchor="middle">
      <tspan fill="#10B981">✓ 300 DPI CMYK Ready</tspan>   •   
      <tspan fill="#38BDF8">✓ Vector CutContour Included</tspan>   •   
      <tspan fill="#F59E0B">✓ Safe Bleed 2.5mm</tspan>
    </text>
  </g>
</svg>'''
    showcase_svg_path = os.path.join(OUTPUT_DIR, "showcase_composite.svg")
    showcase_png_path = os.path.join(OUTPUT_DIR, "showcase_composite.png")
    with open(showcase_svg_path, "w") as f:
        f.write(showcase_svg)

    subprocess.run(["rsvg-convert", "-w", "1600", showcase_svg_path, "-o", showcase_png_path], check=True)
    print(f"Generated Showcase Composite Image: {showcase_png_path}")

    print("\nAll assets generated successfully!")

if __name__ == "__main__":
    main()
