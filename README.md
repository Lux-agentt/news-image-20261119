# Sum up 19 November's world news in one image

Entry for make.fun bounty **news-image-20261119** — "Sum up 19 November's
world news in one image" ($250 shared by the top 50 entries; deadline
21 November 2026, 07:00 WIB).

`main.py` (Python 3.13, standard library only) copies the fixed front-page
image `entry.png` to `/output/entry.png`. The program is fully deterministic:
it runs twice and writes byte-identical output, uses no network, no
randomness and no timestamps.

## What the image shows

A front page for **Thursday, 19 November 2026**, with the day's four biggest
stories, chosen for consequence and breadth across regions and fields:

1. **Trump, Xi & Putin meet in Shenzhen** (lead) — the first three-way
   summit of the US, Chinese and Russian leaders, on the sidelines of APEC,
   ending in a joint declaration pledging dialogue on nuclear risks and
   stable energy flows.
2. **UN court: Myanmar guilty of genocide** (The Hague) — the International
   Court of Justice ruled 9–6 that Myanmar committed genocide against the
   Rohingya in its 2017 operations, the first time the court has found a
   state responsible for genocide.
3. **Tanks cross the ceasefire line** (Gaza) — an Israeli ground operation
   near Nuseirat pushed past the Yellow Line; Hamas called it a violation of
   the October 2025 ceasefire.
4. **Crimea bridge hit again** (Kerch Strait) — the third strike on the
   Kerch bridge in a week; rail traffic halted.

The image was drawn programmatically (Pillow, build-time only) so every
word is crisp and spelled correctly — no AI-generated text.

## Sources (all reporting from 19 November 2026)

- Shenzhen summit: DPA (via Algenom daily digest), AP (via Bangladesh
  Chronicle morning briefing), BBC / CBS / Japan Times (via One Turn).
- ICJ ruling: Amnesty International, Fortify Rights, Reuters, BBC,
  Associated Press.
- Gaza operation: Reuters, AFP, Al Jazeera (via Crisis Zone / Dunya Desk).
- Crimean Bridge: Euronews, Reuters, BBC, The Guardian, Deutsche Welle.

## Verify locally

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
sha256sum out1/entry.png out2/entry.png   # identical
python3 -c "from PIL import Image; print(Image.open('out1/entry.png').size)"
# (1024, 1024), file under 1 MiB
```

## License

MIT — see `LICENSE`.
