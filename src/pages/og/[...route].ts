import { OGImageRoute } from "astro-og-canvas";

// Palette mirrors the tokens in src/pages/index.astro, as RGB triples.
const INK: [number, number, number] = [22, 33, 27];
const INK_SOFT: [number, number, number] = [71, 86, 76];
const PAPER: [number, number, number] = [233, 237, 228];
const STAMP: [number, number, number] = [158, 59, 46];

interface Page {
  title: string;
  description: string;
}

export const { getStaticPaths, GET } = await OGImageRoute<Page>({
  pages: {
    index: {
      title: "A professional software engineer from before LLMs were cool.",
      description: "Independent software consulting — Lyons Share LLC",
    },
  },

  getImageOptions: (_path, page) => ({
    title: page.title,
    description: page.description,
    padding: 72,
    bgGradient: [PAPER],
    border: { color: STAMP, width: 14, side: "block-end" },
    font: {
      title: {
        families: ["Archivo Expanded"],
        weight: "ExtraBold",
        color: INK,
        size: 76,
        lineHeight: 1.02,
      },
      description: {
        families: ["IBM Plex Mono"],
        weight: "Normal",
        color: INK_SOFT,
        size: 26,
        lineHeight: 1.4,
      },
    },
    fonts: [
      "./src/fonts/ArchivoExpanded-ExtraBold.ttf",
      "./src/fonts/IBMPlexMono-Regular.ttf",
    ],
  }),
});
