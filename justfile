# Git safety net — full handout/site and a timed presentation.
#
# The handout/site use `sections/*.prose.md`; the timed deck uses `slides/short.md`.
# Everything is built by pandoc. There is no engine
# and no generator: the file list is a shell glob, so the numeric prefixes on the
# section filenames ARE the document order. Add a section by adding a numbered
# pair; nothing needs to be registered anywhere.
#
# CI runs these same recipes (see .github/workflows/pages.yml), so there is one
# definition of how each output is built and no second copy to drift.

outdir := "output"
site   := "_site"
pandoc := "pandoc"
engine := "xelatex"

# `open` is macOS. On Linux:  just open=xdg-open view-doc
open   := "open"

# Shared across all three outputs.
common := "--metadata-file=metadata.yaml --resource-path=.:figures --citeproc --bibliography=references.bib"

# Print available recipes (default).
default:
    @just --list

# Build all three outputs.
build: doc slides site

# --- Document ---------------------------------------------------------------

# output/document.pdf — the long-form read.
doc:
    mkdir -p {{outdir}}
    {{pandoc}} sections/*.prose.md {{common}} \
        --pdf-engine={{engine}} \
        --toc --toc-depth=2 --number-sections --include-in-header=site/document-header.tex \
        -V documentclass=article -V fontsize=11pt -V geometry:margin=1in \
        -o {{outdir}}/document.pdf

# --- Presentation -----------------------------------------------------------

# output/slides.pdf — 7-minute talk plus a 3-minute demo card (9 pages).
slides:
    mkdir -p {{outdir}}
    {{pandoc}} slides/short.md {{common}} \
        --pdf-engine={{engine}} \
        -t beamer --slide-level=2 --include-in-header=site/slides-header.tex \
        -o {{outdir}}/slides.pdf

# Optional full lecture deck; not the version used in the 10-minute slot.
slides-full:
    mkdir -p {{outdir}}
    {{pandoc}} sections/*.prose.md {{common}} \
        --pdf-engine={{engine}} \
        -t beamer --slide-level=2 --include-in-header=site/slides-header.tex \
        -o {{outdir}}/slides-full.pdf

# Overflowing slides are not a build problem to work around. They are the
# clearest signal you have that a `##` unit is carrying more than one idea, and
# the `visual` reviewer is briefed to report them as writing findings. Fix the
# prose, not the font size.
#
# Nothing here checks for you: pandoc hides the TeX log unless the build fails.
# Look at the deck, or ask the agent to.

# --- Website ----------------------------------------------------------------

# The page links to both PDFs, so this depends on them; without that, a local
# preview has two dead links that only show up after deploying.

# _site/ — one page, sidebar table of contents, both PDFs linked.
site: doc slides
    mkdir -p {{site}}
    {{pandoc}} sections/*.prose.md {{common}} \
        --standalone --toc --toc-depth=2 \
        --template=site/template.html \
        --css=style.css \
        -o {{site}}/index.html
    cp site/style.css {{site}}/
    cp {{outdir}}/document.pdf {{outdir}}/slides.pdf {{site}}/
    mkdir -p {{site}}/figures
    cp -R figures/. {{site}}/figures/
    rm -f {{site}}/figures/README.md

# Serve the site locally at http://localhost:8000.
serve: site
    python3 -m http.server 8000 --directory {{site}}

# --- Viewing ----------------------------------------------------------------

# Open the document PDF.
view-doc: doc
    {{open}} {{outdir}}/document.pdf

# Open the presentation PDF.
view-slides: slides
    {{open}} {{outdir}}/slides.pdf

# --- Publishing -------------------------------------------------------------

# Builds in CI from whatever is on `main` — so commit and push first.
# Requires `gh auth login`, and Pages set to "GitHub Actions" in the
# repository settings.

# Publish the site and both PDFs to GitHub Pages, on demand.
deploy:
    gh workflow run pages.yml
    @echo "Deploy started. Watch it with:  gh run watch"

# --- Housekeeping -----------------------------------------------------------

# Remove all build outputs.
clean:
    rm -rf {{outdir}} {{site}}
