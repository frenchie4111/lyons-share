# lyons-share

The one-page site for **Lyons Share LLC** — Mike Lyons' independent software
consulting practice.

> A professional software engineer from before LLMs were cool.

Live at **[lyonsshare.mikelyons.org](https://lyonsshare.mikelyons.org)**
(also served at `lyonshare.mikelyons.org`).

## What's here

The whole site is one screen, no scroll: a statement, a tagline, and an email
address. `src/pages/index.astro` holds the markup, the design tokens, and the
styles — there is no component layer because there is nothing to reuse yet.

```
src/
  pages/
    index.astro          the entire site
    og/[...route].ts     generates the social share card
  fonts/                 static TTFs, used only for the share card
```

## Design notes

The palette is ledger stock — the banded green paper financial printouts ran
on — with a single oxidized registration-stamp red used once, on the email
underline. Display face is **Archivo** at width axis 125 (expanded) and weight
800; body and utility text are **IBM Plex Mono**. Tokens live in `:root` at the
top of the `<style>` block in `index.astro`; change them there and the share
card constants in `src/pages/og/[...route].ts` to match.

## Social share card

`/og/index.png` is generated at build time by
[`astro-og-canvas`](https://github.com/delucis/astro-og-canvas) from the fonts
in `src/fonts/`. Those TTFs are committed deliberately: CanvasKit rasterizes
without a browser, so it needs a static Archivo Expanded instance rather than
the variable font the page loads from Google Fonts.

To change the card, edit the `title`/`description` in
`src/pages/og/[...route].ts` and rebuild. Keep them in sync with the `og:` meta
tags in `index.astro`.

## Favicon

The `LS` monogram is rendered from the same Archivo Expanded TTF as the share
card, as an ink tile with paper letters — the site's palette inverted, so the
mark holds up at 16px against a light browser tab. Regenerate with:

```sh
python3 scripts/build-favicon.py   # needs Pillow
```

That writes `favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, and
`icon-512.png` into `public/`. The outputs are committed, so the build doesn't
depend on Python.

## Develop

Requires Node 22 (see `.nvmrc`).

```sh
nvm use
npm install
npm run dev      # http://localhost:4321
npm run build    # static output in dist/
npm run preview  # serve the build
```

## Deploy

Hosted on Vercel under the `mike-personal` scope, connected to this repo —
pushes to `main` deploy automatically. DNS for both subdomains is managed in
the `mike-aws` Terraform config, not in the Vercel dashboard.
