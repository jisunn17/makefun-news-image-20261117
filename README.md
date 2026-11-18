[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/jisunn17/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard)
[![reward](https://make.fun/badge/news-image-20261117/jisunn17/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117)

# The world today — Tuesday 17 November 2026

One image that sums up the world's news of **Tuesday 17 November 2026**: six
stories from a single day, across regions and beats, under a masthead that names
the day. The file is `entry.png`, 1024x1024 PNG, drawn by a Pillow script and
shipped as bytes; `main.py` copies those bytes unchanged to the judge.

## The six stories, and why each was chosen

Each line below is the card as it appears in the image, with the reason it
earned a slot on the page.

| Card | Why this one |
| --- | --- |
| **MANILA SUMMIT** — Trump joins ASEAN and Quad, seals critical-minerals deals | The day's biggest diplomatic story, and the one that moved more than one region at once: the US president in Manila, at the ASEAN and Quad meetings, with critical-minerals supply deals as the concrete outcome. |
| **IRAN WARNING** — US says plot for a 'dirty bomb' in Washington; Tehran told it would pay | The sharpest security escalation reported that day. It is attributed to the US claim, not stated as fact, and it names both capitals involved. |
| **UKRAINE WAR** — Washington questions Kyiv's deep strikes; EU pressed for €70bn | The war stayed the day's largest running crisis, and 17 November had two concrete threads: Washington questioning Ukraine's long-range strikes, and pressure on the EU over the €70bn for Kyiv. |
| **ISRAEL DEADLOCK** — Election ends with no clear winner; anti-Arab hate speech reported | An election that ends without a winner is a government-level event, not a beat item: it leaves the country's direction open. Pairing it with the reported anti-Arab hate speech keeps the domestic consequence in the frame. |
| **NVIDIA CEO QUITS** — Resigns over an affair; chip-smuggling probe under way | Chosen for breadth away from war and diplomacy: the CEO of the world's most valuable chipmaker resigning, with a chip-smuggling probe running alongside it. Technology and business, in one card. |
| **DHONI RETIRES** — India's captain ends IPL career, becomes CSK mentor | The day's biggest sport story, and the one most readers worldwide would recognise instantly: M. S. Dhoni ending his IPL playing career and staying on as CSK mentor. |

Together they cover diplomacy, security, war, elections, technology and sport —
no single country's news alone, and no single beat.

Care was taken to write only what the day carried: events are attributed
("US says"), no figure appears that the reports did not give, every country is
named, and there is no "shock" or "chaos" language.

## How the image was drawn

* **Pillow, flat vector, no photographs.** Everything — the masthead, the cards,
  the icons — is drawn with `ImageDraw` primitives: rounded rectangles, lines,
  ellipses, arcs, pieslices and polygons. No sourced artwork, no stock images,
  nothing that needs a licence from anyone else.
* **Composition:** a 1024x1024 front page. Masthead band with the paper's name,
  the date in the largest type on the page, and a red rule. Then six cards in a
  2x3 grid, each 470x262, each with an accent bar, a bold headline, a
  flat vector icon and two to four lines of body text. A footer strip names the
  sourcing.
* **Colour:** one accent per card (red, amber, blue, green, purple, pink) on a
  dark page, so the six stories stay distinct when the image is scaled down.
* **Legibility at ~300 px:** large type only. The date is 52 pt, headlines 30 pt
  bold, body 23 pt. Text was wrapped to a measured pixel width using
  `ImageDraw.textlength`, and the render asserts that every glyph of a card stays
  inside that card's box, that the card grid clears the masthead and footer, and
  that no ink spills into the gaps between cards.
* **Output:** 1024x1024, a whole PNG (signature, IHDR, IDAT, IEND, all CRCs
  correct), 92,344 bytes — well under the 1 MiB cap.

## How to run the program

Python 3.13, standard library only, no network.

```
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program reads `entry.png` from beside itself and writes exactly those bytes
to `$MAKEFUN_OUTPUT_DIR/entry.png`, creating the directory if it is missing.
With `MAKEFUN_OUTPUT_DIR` unset it falls back to `/output`. It exits 0 on
success; a missing `entry.png` or an unwritable output directory prints a clear
error to stderr and exits 1. Two runs write the same bytes.

## Licence

MIT — see `LICENSE`.
