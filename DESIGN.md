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
| Gradient Start | Royal Electric Blue | `#3B82F6` | `59, 130, 246` | `C:75 M:48 Y:0 K:0` |
| Gradient Mid | Cerulean Sky | `#1D9BF0` | `29, 155, 240` | `C:78 M:30 Y:0 K:0` |
| Gradient End | Vivid Cyan / Teal | `#06B6D4` | `6, 182, 212` | `C:72 M:2 Y:12 K:0` |

* **Gradient Vector:** Linear gradient from top-left ($0\%, 0\%$) to bottom-right ($100\%, 100\%$).
* **Subtle Sheen Overlay:** Linear gradient pure white (`#FFFFFF`) with stops at $0\%$ (opacity $0.22$), $45\%$ (opacity $0.08$), and $100\%$ (opacity $0.00$).

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

## 6. Official Expo Sticker Quartet (4 Distinct Art Styles)

### Sticker 01: "The Pure Hero Die-Cut" (Approved Master Mark)
* **File:** `assets/svg/tixdesk-sticker-01-hero-mark.svg`
* **Target Size:** $\approx 7.0 \times 6.1\text{ cm}$
* **Style:** Pure Minimalist Geometric Die-Cut
* **Target Audience:** Universal (laptops, phones, tumblers). High contrast, iconic brand identity.

### Sticker 02: "Tixie • The Cyber-Bot" (Official Mascot Edition)
* **File:** `assets/svg/tixdesk-sticker-02-mascot-tixie.svg`
* **Target Size:** $\approx 7.2 \times 7.2\text{ cm}$
* **Style:** Kawaii Chibi Vector Mascot
* **Anatomy:**
  * **Head:** TixDesk ticket/speech-bubble silhouette with deep navy curved OLED visor screen.
  * **Expression:** Sparkling anime eyes, cat-smile (`ω`), soft coral blush, and signal status antenna (`#10B981`).
  * **Accessories:** Integrated support agent headset with boom microphone.
  * **Prop:** Holding the Golden Resolved Ticket with a green checkmark (`✓`).
* **Target Audience:** Designers, students, customer support teams, and anyone who loves cute tech companions.

### Sticker 03: "Cyber Mecha Decal // Unit-016" (Anime Tactical HUD)
* **File:** `assets/svg/tixdesk-sticker-03-cyber-mecha-decal.svg`
* **Target Size:** $\approx 7.5 \times 7.5\text{ cm}$
* **Style:** High-Tech Sci-Fi / Mecha Decal (Gundam & Evangelion aesthetic)
* **Anatomy:**
  * **Plate:** Chamfered heavy octagonal tactical plate in dark carbon navy.
  * **Emblem:** TixDesk ticket emblem inside optical targeting reticles and circuit nodes.
  * **Telemetry:** `UNIT-016 // TIM-A3`, `PROTOCOL: RESOLVED [200 OK]`, `SLA: ZERO OVERDUE`, hazard caution stripes.
* **Target Audience:** DevOps, backend engineers, Linux users, mechanical keyboard enthusiasts, and anime fans.

### Sticker 04: "Retro 16-Bit Arcade Gamer" (Pixel Art Quest)
* **File:** `assets/svg/tixdesk-sticker-04-retro-pixel-arcade.svg`
* **Target Size:** $\approx 7.0 \times 7.0\text{ cm}$
* **Style:** Nostalgic 8-Bit / 16-Bit Arcade Pixel Art
* **Anatomy:**
  * **Sprite:** Pixel-block TixDesk ticket character with split-tone blue/cyan shading.
  * **Attitude:** Pixel sunglasses ("Deal With It" vibe), retro blush, and green status smile.
  * **HUD Elements:** 3 floating red 8-bit hearts (100% full health) and retro banner: `★ SLA SAVED: 100% ★`.
* **Target Audience:** Gamers, indie hackers, CS students, and retro tech nostalgia collectors.

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
