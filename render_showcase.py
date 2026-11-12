#!/usr/bin/env python3
import os
import subprocess

REPO_DIR = "/home/graha/tixdesk-expo-stickers"

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1800 1140" width="1800" height="1140">
  <defs>
    <radialGradient id="bgGrad" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#090D16" />
    </radialGradient>
    <filter id="stickerShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000000" flood-opacity="0.55" />
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#000000" flood-opacity="0.3" />
    </filter>
  </defs>

  <!-- Dark Expo Background -->
  <rect width="100%" height="100%" fill="url(#bgGrad)" />

  <!-- Expo Header Badge -->
  <g transform="translate(900, 58)" text-anchor="middle">
    <rect x="-360" y="-30" width="720" height="60" rx="30" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5" />
    <text y="-4" font-family="'Noto Sans', sans-serif" font-size="21" font-weight="900" letter-spacing="3" fill="#38BDF8">TIXDESK OFFICIAL EXPO STICKER COLLECTION</text>
    <text y="18" font-family="'Noto Sans', sans-serif" font-size="12" font-weight="700" fill="#94A3B8" letter-spacing="1.5">FULL 7-PIECE PREPRESS SUITE • 300 DPI • SPOT MAGENTA DIE-CUT CONTOURS</text>
  </g>

  <!-- =========================================================================
       ROW 1: CORE OFFICIAL PACK (3 Cards: width 520, height 440)
       Left margin: 60, Gap: 60 -> X = 60, 640, 1220.
       ========================================================================= -->
  <g transform="translate(60, 115)">
    <!-- Card 01 -->
    <g transform="translate(0, 0)">
      <rect width="520" height="440" rx="18" fill="#111827" stroke="#1E293B" stroke-width="1.5" />
      <!-- Top Pill Tag Centered -->
      <g transform="translate(260, 26)">
        <rect x="-55" y="-12" width="110" height="24" rx="12" fill="#3877F6" fill-opacity="0.2" stroke="#3877F6" stroke-width="1.2" />
        <text y="4" font-family="'Noto Sans', sans-serif" font-size="11" font-weight="800" fill="#60A5FA" text-anchor="middle">CORE 01</text>
      </g>
      <!-- Title & Subtitle Centered -->
      <text x="260" y="66" font-family="'Noto Sans', sans-serif" font-size="16" font-weight="900" fill="#F8FAFC" text-anchor="middle">HERO MARK (PERMANENT)</text>
      <text x="260" y="86" font-family="'Noto Sans', sans-serif" font-size="11.5" font-weight="500" fill="#64748B" text-anchor="middle">Symmetrical 40px T • Gradient Tail Hugging Die-Cut</text>
      <!-- Artwork Centered -->
      <g transform="translate(260, 270) scale(0.85)" filter="url(#stickerShadow)">
        <image href="assets/png/tixdesk-sticker-01-hero-mark-300dpi.png" x="-200" y="-200" width="400" height="400" />
      </g>
    </g>

    <!-- Card 02 -->
    <g transform="translate(580, 0)">
      <rect width="520" height="440" rx="18" fill="#111827" stroke="#1E293B" stroke-width="1.5" />
      <g transform="translate(260, 26)">
        <rect x="-55" y="-12" width="110" height="24" rx="12" fill="#10B981" fill-opacity="0.2" stroke="#10B981" stroke-width="1.2" />
        <text y="4" font-family="'Noto Sans', sans-serif" font-size="11" font-weight="800" fill="#34D399" text-anchor="middle">CORE 02</text>
      </g>
      <text x="260" y="66" font-family="'Noto Sans', sans-serif" font-size="16" font-weight="900" fill="#F8FAFC" text-anchor="middle">CHIBI TIXIE MASCOT</text>
      <text x="260" y="86" font-family="'Noto Sans', sans-serif" font-size="11.5" font-weight="500" fill="#64748B" text-anchor="middle">Preserved Notches • Solid White Gap Fills • Smooth Earcup</text>
      <g transform="translate(260, 270) scale(0.72)" filter="url(#stickerShadow)">
        <image href="assets/png/tixdesk-sticker-02-mascot-tixie-300dpi.png" x="-240" y="-240" width="480" height="480" />
      </g>
    </g>

    <!-- Card 03 -->
    <g transform="translate(1160, 0)">
      <rect width="520" height="440" rx="18" fill="#111827" stroke="#1E293B" stroke-width="1.5" />
      <g transform="translate(260, 26)">
        <rect x="-55" y="-12" width="110" height="24" rx="12" fill="#F59E0B" fill-opacity="0.2" stroke="#F59E0B" stroke-width="1.2" />
        <text y="4" font-family="'Noto Sans', sans-serif" font-size="11" font-weight="800" fill="#FBBF24" text-anchor="middle">CORE 03</text>
      </g>
      <text x="260" y="66" font-family="'Noto Sans', sans-serif" font-size="16" font-weight="900" fill="#F8FAFC" text-anchor="middle">RETRO PIXEL ARCADE</text>
      <text x="260" y="86" font-family="'Noto Sans', sans-serif" font-size="11.5" font-weight="500" fill="#64748B" text-anchor="middle">Straight Flush Side Die-Cut • Inward Notched 8-Bit Body</text>
      <g transform="translate(260, 270) scale(0.85)" filter="url(#stickerShadow)">
        <image href="assets/png/tixdesk-sticker-03-retro-pixel-arcade-300dpi.png" x="-200" y="-200" width="400" height="400" />
      </g>
    </g>
  </g>

  <!-- =========================================================================
       ROW 2: EXPO EXPANSION PACK (4 Cards: width 395, height 485)
       Left margin: 60, Gap: 48 -> X = 60, 503, 946, 1389.
       (Total span = 60 + 395*4 + 48*3 = 60 + 1580 + 144 = 1784, Right margin = 48)
       Let's balance perfectly: Left margin 45, Gap 50 -> 45 + 395*4 + 150 = 1775.
       ========================================================================= -->
  <g transform="translate(48, 595)">
    <!-- Card 04 -->
    <g transform="translate(0, 0)">
      <rect width="398" height="485" rx="18" fill="#111827" stroke="#1E293B" stroke-width="1.5" />
      <g transform="translate(199, 26)">
        <rect x="-65" y="-12" width="130" height="24" rx="12" fill="#8B5CF6" fill-opacity="0.2" stroke="#8B5CF6" stroke-width="1.2" />
        <text y="4" font-family="'Noto Sans', sans-serif" font-size="11" font-weight="800" fill="#A78BFA" text-anchor="middle">EXPANSION 04</text>
      </g>
      <text x="199" y="66" font-family="'Noto Sans', sans-serif" font-size="15" font-weight="900" fill="#F8FAFC" text-anchor="middle">POWERED BY CAFFEINE</text>
      <text x="199" y="86" font-family="'Noto Sans', sans-serif" font-size="11" font-weight="500" fill="#64748B" text-anchor="middle">Night Shift On-Call • Steaming Mug</text>
      <g transform="translate(199, 285) scale(0.72)" filter="url(#stickerShadow)">
        <image href="assets/png/tixdesk-sticker-04-tixie-caffeine-nightshift-300dpi.png" x="-240" y="-240" width="480" height="480" />
      </g>
    </g>

    <!-- Card 05 -->
    <g transform="translate(438, 0)">
      <rect width="398" height="485" rx="18" fill="#111827" stroke="#1E293B" stroke-width="1.5" />
      <g transform="translate(199, 26)">
        <rect x="-65" y="-12" width="130" height="24" rx="12" fill="#EF4444" fill-opacity="0.2" stroke="#EF4444" stroke-width="1.2" />
        <text y="4" font-family="'Noto Sans', sans-serif" font-size="11" font-weight="800" fill="#F87171" text-anchor="middle">EXPANSION 05</text>
      </g>
      <text x="199" y="66" font-family="'Noto Sans', sans-serif" font-size="15" font-weight="900" fill="#F8FAFC" text-anchor="middle">SLA INCIDENT FIREFIGHTER</text>
      <text x="199" y="86" font-family="'Noto Sans', sans-serif" font-size="11" font-weight="500" fill="#64748B" text-anchor="middle">Panic Mode &gt; &lt; • Zero Downtime Foam</text>
      <g transform="translate(199, 285) scale(0.72)" filter="url(#stickerShadow)">
        <image href="assets/png/tixdesk-sticker-05-tixie-sla-firefighter-300dpi.png" x="-240" y="-240" width="480" height="480" />
      </g>
    </g>

    <!-- Card 06 -->
    <g transform="translate(876, 0)">
      <rect width="398" height="485" rx="18" fill="#111827" stroke="#1E293B" stroke-width="1.5" />
      <g transform="translate(199, 26)">
        <rect x="-65" y="-12" width="130" height="24" rx="12" fill="#EC4899" fill-opacity="0.2" stroke="#EC4899" stroke-width="1.2" />
        <text y="4" font-family="'Noto Sans', sans-serif" font-size="11" font-weight="800" fill="#F472B6" text-anchor="middle">EXPANSION 06</text>
      </g>
      <text x="199" y="66" font-family="'Noto Sans', sans-serif" font-size="15" font-weight="900" fill="#F8FAFC" text-anchor="middle">HOLOGRAPHIC CYBER DECAL</text>
      <text x="199" y="86" font-family="'Noto Sans', sans-serif" font-size="11" font-weight="500" fill="#64748B" text-anchor="middle">Carbon Synthwave • Glowing PCB Mesh</text>
      <g transform="translate(199, 285) scale(0.78)" filter="url(#stickerShadow)">
        <image href="assets/png/tixdesk-sticker-06-cyber-neon-decal-300dpi.png" x="-210" y="-210" width="420" height="420" />
      </g>
    </g>

    <!-- Card 07 -->
    <g transform="translate(1314, 0)">
      <rect width="398" height="485" rx="18" fill="#111827" stroke="#1E293B" stroke-width="1.5" />
      <g transform="translate(199, 26)">
        <rect x="-65" y="-12" width="130" height="24" rx="12" fill="#14B8A6" fill-opacity="0.2" stroke="#14B8A6" stroke-width="1.2" />
        <text y="4" font-family="'Noto Sans', sans-serif" font-size="11" font-weight="800" fill="#2DD4BF" text-anchor="middle">EXPANSION 07</text>
      </g>
      <text x="199" y="66" font-family="'Noto Sans', sans-serif" font-size="15" font-weight="900" fill="#F8FAFC" text-anchor="middle">VINTAGE POSTAL BADGE</text>
      <text x="199" y="86" font-family="'Noto Sans', sans-serif" font-size="11" font-weight="500" fill="#64748B" text-anchor="middle">Golden Wreath • Ticket Resolved 200 OK</text>
      <g transform="translate(199, 285) scale(0.70)" filter="url(#stickerShadow)">
        <image href="assets/png/tixdesk-sticker-07-vintage-postal-stamp-300dpi.png" x="-210" y="-210" width="420" height="420" />
      </g>
    </g>
  </g>
</svg>"""

with open(f"{REPO_DIR}/showcase_composite.svg", "w") as f:
    f.write(svg_content)

subprocess.run(["rsvg-convert", "-w", "1800", f"{REPO_DIR}/showcase_composite.svg", "-o", f"{REPO_DIR}/showcase_composite.png"], check=True)
print("Updated showcase_composite.png successfully!")
