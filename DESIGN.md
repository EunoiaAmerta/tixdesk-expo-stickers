# TixDesk Design System & Brand Identity Guide (DESIGN.md)

> **Document Version:** 1.0.0  
> **Status:** Active / Production Standard  
> **Target Release:** Physical Swag, Tech Expo (Nov 17–18, 2026), Web & Mobile Applications  
> **Maintainers:** Hiro (Product Owner & Tech Lead) & Zero Two (Design & Architecture Partner)

---

## 1. Brand Mission & Core Identity

**TixDesk** is a modern, high-performance, multi-tenant helpdesk and ticketing platform built for mission-critical operations. It bridges the gap between end-users, support agents, and engineering teams with real-time incident resolution, strict SLA tracking, and integrated knowledge management.

* **Exact Brand Casing:** `TixDesk` (PascalCase / UpperCamelCase — never *TIXDESK* in body text, never *tixdesk*).
* **Official Tagline:** `Helpdesk & Ticketing Platform`
* **Brand Voice & Personality:**
  * **Reliable & Disciplined:** Zero tolerance for overdue SLAs, zero-trust lifecycle transitions.
  * **Approachable & Human:** Empathetic customer communication, friendly modern interfaces.
  * **Fast & Lightweight:** Snappy real-time interactions, clean scannable layouts.

---

## 2. Logo Mark Anatomy & Geometry

The official TixDesk logo mark is a single vector glyph that synthesizes **three distinct metaphors** without cognitive clutter:

```
           ┌──────────────────────────────────────┐
           │     Continuous Rounded Top Edge      │
     ╭─────┴──────────────────────────────────────┴─────╮
     │                                                  │
   凹│ (Notch)             ┌──────────────┐      (Notch)│凹  <-- 1. Ticket Stub Metaphor
     │                     │   Negative   │             │
     │                     │  Space "T"   │             │
     │                     └──────┬───────┘             │
     │   ╭─────────╮              │              ┌──────┘
     │  ╱  Speech  │              │ (Open Stem)  │
     ╰─┤   Bubble  ├──────────────┘              └──────╮    <-- 2. Chat / Helpdesk Metaphor
       │    Tail   │                                    │
       ╰───────────╯                             3. 'T' │
                                                 Symbol │
```

1. **The Event / Support Ticket:** Semicircular concave notches carved into the left and right flanks.
2. **The Helpdesk Speech Bubble:** A downward-pointing tail on the lower-left corner indicating live customer conversations.
3. **The Letter "T":** An inner cutout in negative space forming a crisp, bold uppercase "T" whose central stem cuts openly through the bottom baseline.

### Geometric Rules
* **Aspect Ratio:** $1.177 : 1$ (Width: 183.69 units, Height: 156.05 units).
* **Inner vs. Outer Tension:** The outer perimeter uses soft, rounded curves ($R \approx 16\text{–}20\text{ px}$) conveying friendliness, while the inner "T" cutout retains strict $90^\circ$ right angles conveying operational precision.
* **Minimum Legibility Scale:** The mark must remain fully recognizable down to $16 \times 16\text{ px}$ (favicon) and up to building signage.

---

## 3. Color Tokens & Palette

### 3.1 Primary Brand Gradient
| Role | Color Name | Hex Code | RGB | CMYK (Print Target) |
|---|---|---|---|---|
| Gradient Start | Deep Royal Electric Blue | `#3877F6` | `56, 119, 246` | `C:77 M:52 Y:0 K:0` |
| Gradient Mid | Cerulean Sky | `#4CA2EA` | `76, 162, 234` | `C:68 M:31 Y:0 K:0` |
| Gradient End | Vibrant Aqua / Cyan | `#5AC1C4` | `90, 193, 196` | `C:54 M:2 Y:0 K:23` |

* **Gradient Direction:** Exact horizontal transition from left ($0\%$) to right ($100\%$), matching the official master mark.

### 3.2 Semantic Status Tokens (Three Pillars)
| Feature Pillar | Semantic Meaning | Foreground / Dot | Surface Tint | Border / Accent |
|---|---|---|---|---|
| **Ticket** | Core ticketing lifecycle | `#2563EB` | `#EFF6FF` | `#BFDBFE` |
| **SLA** | SLA monitoring & business timers | `#06B6D4` / `#F59E0B` | `#ECFEFF` / `#FEF3C7` | `#A5F3FC` / `#FDE68A` |
| **KB** | Knowledge base & resolution | `#10B981` | `#F0FDF4` | `#BBF7D0` |
| **High Priority** | Critical urgent tickets | `#EF4444` | `#FDE8E8` | `#FECACA` |

### 3.3 Neutrals & Typography
* **Deep Navy / Slate:** `#0B1B3D` / `#0F172A` (Primary titles, high-contrast dark surfaces).
* **Muted Slate:** `#475569` / `#64748B` (Subtitles, borders, secondary metadata).
* **Surface White:** `#FFFFFF` / `#F8FAFC` (Canvas, light cards, die-cut contours).

---

## 4. Typography System

* **Primary Brand Display:** Geometric Grotesque Sans (`Inter`, `Poppins`, `Noto Sans`, or `Gilroy`).
  * Weight: `Black (900)` or `Bold (800)` for brand titles.
  * Tracking / Letter-spacing: Tight for headlines ($-1.5\text{px}$), comfortable for sub-headers ($+1.5\text{px}$ to $+2.5\text{px}$).
* **Secondary / Body Copy:** Clean Sans (`Inter`, system-ui).
  * Weights: `Medium (500)` and `SemiBold (600)`.
* **Technical / Log Badges:** Monospace (`JetBrains Mono`, `Fira Code`, system mono).
  * Use case: Status badges, HTTP responses (`200 OK — RESOLVED`), SLA counts.

---

## 5. Physical Merchandise & Sticker Production Guide

For the upcoming **Tech Expo (November 17–18, 2026)**, TixDesk merchandise adheres to the following prepress standards:

### 5.1 Physical Specifications
* **Standard Form Factor:** $6.5\text{ cm} \text{ to } 7.5\text{ cm}$ (Ideal for laptops, tablets, and smartphone cases).
* **Target Resolution:** Vector format (infinite resolution) or minimum **300 DPI raster**.
* **Die-Cut Contour (White Border):** Minimum $2.0\text{ mm} \text{ to } 2.5\text{ mm}$ ($24\text{–}36\text{ px}$ at 300 DPI) surrounding the graphic.
* **Safety Margin (Inner Bleed):** All critical text must sit at least $2.0\text{ mm}$ inside the cutline.
* **Plotter Cutline Layer:** Dedicated vector path stroked with **$100\%$ Magenta (`#FF00FF`)**, stroke width $1.0\text{ pt}$, labeled as `CutContour` (compatible with Roland VersaWorks, Mimaki FineCut, and Graphtec).

### 5.2 Material Recommendations
* **Substrate:** Premium white vinyl (PVC) film ($100\text{–}120\text{ gsm}$).
* **Adhesive:** Removable, bubble-free acrylic adhesive (leaves no sticky residue on MacBook/ThinkPad anodized aluminum).
* **Lamination:** **Matte Soft-Touch (Velvet)** or **Satin UV Protection** (scratch-resistant, waterproof, UV-proof).

---

## 6. Official Expo Sticker Suite (Complete 7-Piece Collection)

### Section 6A: Core Official Pack (Stickers 01–03)

### Sticker 01: "The Pure Hero Die-Cut" (Official Master Mark)
* **File:** `assets/svg/tixdesk-sticker-01-hero-mark.svg`
* **Target Size:** $\approx 7.0 \times 6.1\text{ cm}$
* **Style:** Pure Minimalist Geometric Die-Cut
* **Refined Anatomy:**
  * **Gradient Accuracy:** Horizontal spectrum transitioning from Deep Royal Blue (`#3877F6`) to Vibrant Cyan (`#5AC1C4`), sampled directly from the official logo asset.
  * **Symmetrical Solid White "T" Glyph:** 100% solid pure white (`#FFFFFF`) lettermark with perfectly equalized stroke weight on both axes: horizontal crossbar thickness ($40\text{px}$) == vertical stem width ($40\text{px}$). Zero dark gaps, slits, or hollow voids.
  * **Contour-Hugging Die-Cut Base:** The white outer die-cut border strictly follows the natural anatomy of the design—dipping down to follow the speech bubble tail apex, ascending into the bottom crevice, and running along the baseline horizontally without crude diagonal shortcuts.
* **Target Audience:** Universal (MacBook lids, iPads, phones, tumblers).

### Sticker 02: "Tixie • The Cyber-Bot" (Pure Iconic Head Edition)
* **File:** `assets/svg/tixdesk-sticker-02-mascot-tixie.svg`
* **Target Size:** $\approx 7.0 \times 7.0\text{ cm}$
* **Style:** Kawaii Chibi 2D Vector IP Mascot Head
* **Refined Anatomy:**
  * **Iconic Head-Only Focus:** The floating robot body, limbs, and thruster have been completely removed to provide an ultra-clean, high-recognition portrait of Tixie.
  * **Preserved Ticket Notches & Zero Negative Gaps:** The characteristic ticket notches on both flanks are fully preserved, and all negative cavities (including the area behind the earcups and between the microphone boom wire and speech bubble tail) are solidly filled with pure white (`#FFFFFF`), leaving zero dark voids or hollow holes.
  * **Ticket Head:** Seamless ticket-shaped head with curved dark OLED screen visor.
  * **Expressive Anime Face:** Sparkling eyes with multi-layer glint highlights, coral blush, and cheerful cat-smile (`ω`).
  * **Hardware:** Helpdesk customer support headset with glowing mint-green boom mic and connectivity antenna.
  * **Thinned Uniform Die-Cut Contour:** Precision white outer border engineered with an offset identical to Sticker 01 ($\approx 2.5\text{ mm}$ / $24\text{ px}$ stroke). Tightly hugs the antenna, arched headset band, earcups, boom mic, and bottom-left speech tail with organic, continuous curves and zero stair-step artifacts.
* **Target Audience:** Designers, students, support teams, community members, and kawaii tech collectors.

### Sticker 03: "Retro 16-Bit Arcade Gamer" (Pure Retro Ticket Edition)
* **File:** `assets/svg/tixdesk-sticker-03-retro-pixel-arcade.svg`
* **Target Size:** $\approx 7.0 \times 7.0\text{ cm}$
* **Style:** Nostalgic 8-Bit / 16-Bit Arcade Pixel Art
* **Refined Anatomy:**
  * **Pure Character Focus:** All extraneous gaming HUD/overlays (floating hearts, SLA text banner, and bottom green HP bar) have been eliminated for a clean, bold retro arcade character.
  * **Preserved Inward Punch Notches:** Symmetrical rectangular ticket punch cutouts directly carved into the royal blue and bright cyan body fields, filled with clean solid white backing.
  * **Smooth, Flush Die-Cut Outer Perimeter:** The outer white cutline contour runs straight and vertical along the lateral edges without indenting or dipping into the ticket notches, providing an ultra-smooth, sturdy, and peel-resistant border.
  * **Soft, Slim Die-Cut Margins:** Uniform slim margins ($\approx 10\text{–}12\text{ px}$) on top, bottom, and both flanks, with pillowy rounded corners perfectly harmonizing with Sticker 01.
  * **Pixel Sprite:** Split-tone blue/cyan pixel ticket, cool 8-bit black sunglasses with specular white gleams, coral blush, and centered pixel snout.
  * **Clean Baseline & Stepped Tail:** Retro ticket chin and stepped dialogue tail on the bottom-left with dimensional shadow accent.
* **Target Audience:** Gamers, CS students, indie hackers, and retro computing collectors.

---

### Section 6B: Expo Expansion Pack (Stickers 04–07)

### Sticker 04: "Powered by Caffeine" (Night Shift On-Call Mascot)
* **File:** `assets/svg/tixdesk-sticker-04-tixie-caffeine-nightshift.svg`
* **Target Size:** $\approx 7.0 \times 7.0\text{ cm}$
* **Style:** Cute Chibi Narrative Mascot
* **Refined Anatomy:**
  * **Sleepy-Sweet Expression:** Curved restful closed eyes with delicate fatigue accent lines and a peaceful smile, capturing the relatable developer night shift mood.
  * **Amber Beacon & Ceramic Coffee Mug:** Warm amber glowing antenna light, paired with a dark slate mug featuring a golden TixDesk "T" badge and aromatic rising steam waves.
  * **Die-Cut Integration:** White contour smoothly encloses the steam wisps, coffee mug handle, and headset without micro-slits.
* **Target Audience:** SREs, DevOps engineers, nocturnal hackers, and coffee enthusiasts.

### Sticker 05: "Tixie on Fire" (Panicked Mascot Burning // PROD ON FIRE)
* **File:** `assets/svg/tixdesk-sticker-05-tixie-sla-firefighter.svg`
* **Target Size:** $\approx 7.2 \times 7.2\text{ cm}$
* **Style:** Dynamic Anime Chibi Mascot Emergency
* **Refined Anatomy:**
  * **Panicked Facial Expression:** Wide cartoon eyes with warm golden fire highlights and reflection catchlights, screaming mouth, flying cyan sweat droplets, and glowing red blush.
  * **Roaring Vector Flames:** Dynamic multi-layered flame tongues erupting behind and around Tixie's chassis (crimson `#DC2626` $\rightarrow$ blaze orange `#EA580C` $\rightarrow$ lemon core `#FDE047`), complete with floating sparks and embers.
  * **Antenna Spark Wick:** Antenna beacon glowing cherry red with a sparking core like a lit fuse.
  * **Bottom Alert Banner:** High-contrast dark pill banner with bold yellow lettering: `🔥 PROD ON FIRE`.
  * **Die-Cut Integration:** Continuous, smooth white die-cut border surrounding the flame peaks, headset, and chassis.
* **Target Audience:** SREs, incident commanders, on-call developers, and sysadmins who know the feeling of production on fire.

### Sticker 06: "Tixie Neon (Soft Cyber)" (Cyberpunk Synthwave Mascot)
* **File:** `assets/svg/tixdesk-sticker-06-cyber-neon-decal.svg`
* **Target Size:** $\approx 7.0 \times 7.0\text{ cm}$
* **Style:** Soft Cyberpunk / Synthwave Glowing Mascot
* **Refined Anatomy:**
  * **Cute Charismatic Mascot:** Preserves Tixie's signature adorable face rather than heavy mechanical armor, featuring matching sparkling anime eyes with 4-point star glints, bright hot-pink cheek blushes, and a cute cat smile.
  * **Glowing Synthwave Lines:** Vibrant `#00F0FF` electric cyan and `#FF007F` neon magenta dual-stroke accents along the chassis edges and headset band.
  * **Audio Equalizer Earcups:** Sleek dark slate earcups with pulsing horizontal neon level meter lights.
  * **Screen HUD Telemetry:** Inset translucent visor featuring subtle scanline mesh and crisp monospaced status headers (`TIXIE // NEON-016` and `SYS: NOMINAL`).
  * **Material Optimization:** Ideal for printing on holographic rainbow vinyl or glossy UV spot coating.
* **Target Audience:** Cyberpunk lovers, mechanical keyboard builders, synthwave fans, and frontend developers.

### Sticker 07: "Vintage Postal Stamp" (Emerald 200 OK Dispatch & Master Mark)
* **File:** `assets/svg/tixdesk-sticker-07-vintage-postal-stamp.svg`
* **Target Size:** $\approx 6.8 \times 7.8\text{ cm}$
* **Style:** Vintage Banknote Security Engraving & Postmark
* **Refined Anatomy:**
  * **Perforated Stamp Border:** Scalloped postage perforation teeth framing a deep midnight navy dispatch canvas with guilloche border filigree.
  * **Authentic Master Mark:** Houses the exact official TixDesk brand mark (`path_01_body` + `path_01_t`) with the genuine Royal Blue to Cyan gradient and symmetrical 40px "T", flanked by 24K gold laurel leaves and 5 CSAT rating stars.
  * **High-Visibility Emerald Postmark Stamp:** Tilted ($-13^\circ$) emerald green (`#10B981`) cancellation stamp with dark contrast backing and dual drop-shadows, ensuring `★ TICKET RESOLVED ★` and `STATUS: 200 OK` are 100% legible against dark backgrounds.
  * **Compliance Footer:** `BUSINESS SLA • MET / ISO/IEC 20000 SERVICE DESK COMPLIANT`.
* **Target Audience:** ITIL/ISO managers, enterprise support leads, quality assurance teams, and philatelic tech collectors.

---

## 7. Quality Gates (Do's & Don'ts)

### ✅ Do
* Always maintain the $1:1$ negative space proportions of the central "T".
* Always pair the logo with the exact blue-to-cyan gradient when shown on dark or white surfaces.
* Keep the white die-cut border uniform with rounded corner joints to prevent peeling.
* Provide vector SVG/PDF cutline files with 100% Magenta `#FF00FF` to commercial print vendors.

### ❌ Don't
* **Never** use generic AI-slop elements (e.g., random floating purple orbs, clip-art headset icons, stock call-center silhouettes).
* **Never** skew, distort, or flip the logo mark horizontally (the speech bubble tail must always sit on the bottom-left).
* **Never** replace the negative space "T" with a solid shape or alter its $90^\circ$ internal angles.
* **Never** print with less than 300 DPI on physical swag.
