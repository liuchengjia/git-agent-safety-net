# Git & Version Control: an agent safety net

**Chengjia Liu & Yiyang Yan · Tutorial 02**

[Website](https://liuchengjia.github.io/git-agent-safety-net/) · [Short slides](https://liuchengjia.github.io/git-agent-safety-net/slides.pdf) · [Full handout](https://liuchengjia.github.io/git-agent-safety-net/document.pdf)

The live session is **7 minutes of explanation + 3 minutes of demonstration**. Its nine-page deck covers checkpoints, the two diffs, accepting/recovering changes, branch labels, and Git's limits. The last page is the live-demo command card. The handout and website retain the complete tutorial and references.

## Present

- [Short deck source](slides/short.md) → `output/slides.pdf`.
- [Presenter guide](docs/presenter-guide.md) → exact timings, before-class setup, and the three-minute demo.
- [Full tutorial](sections/03-content.prose.md) → `output/document.pdf` and `_site/index.html`.
- [Proposal](topic.md), [audience](metadata.yaml), and [review history](rounds/round-001/SYNTHESIS.md).

Agent edits are deterministic simulations. There is no LLM dependency and no PySR execution. The demonstration shows a broken metric producing a deceptively low score, a failing fixed check, and recovery from the committed version.

## Run and rehearse

Requirements: Git 2.28+ and Python 3.9+ (`python3` where appropriate).

```sh
python examples/create_demo.py ../git-safety-demo-live
cd ../git-safety-demo-live
git init -b main
```

Follow the [presenter guide](docs/presenter-guide.md) to prepare a tested checkpoint **before** the ten-minute slot. The helper refuses nonempty destinations.

From this tutorial's root, rehearse the full safety exercise automatically:

```sh
python examples/verify_demo.py
```

## Build

Install Pandoc, just, XeLaTeX/Metropolis, and librsvg. On Ubuntu 24.04:

```sh
sudo apt-get install just pandoc texlive-xetex texlive-latex-extra texlive-fonts-recommended texlive-pictures librsvg2-bin
just build
python3 scripts/verify_site.py
just serve
```

`just slides` builds the nine-page timed deck. `just slides-full` optionally builds the complete lecture deck. `just doc` builds the complete handout. PDFs and `_site/` are generated and ignored by Git.

For the portable Windows setup, put Pandoc, just, Tectonic, and Git's POSIX utilities on PATH, then run `just engine=tectonic build`. Tectonic downloads its TeX dependencies on first use.

## GitHub Pages

The [workflow](.github/workflows/pages.yml) tests the demo, builds the PDFs/site, and checks local links. Pull requests build without deploying. Pushes to `main` and manual runs on `main` deploy the tested artifact to Pages. Publishing permissions exist only in the deployment job.

One-time setting: **Settings → Pages → Build and deployment → Source: GitHub Actions**. Subsequent updates publish after a successful `main` build. To trigger manually: `gh workflow run pages.yml --ref main` or use the Actions tab.

## Method and provenance

The full tutorial follows the [course brief](https://github.com/EduDocs/agentic_development/blob/main/tutorials/tutorial-02-git-version-control.md) and the original [course template repository](https://github.com/AgenticDevelopmentDiscovery/nec-02-git-version-control). The original history is retained. Official technical references are in `references.bib`.

[CLAUDE.md](CLAUDE.md) records the independent-review method and the deliberate short-deck exception. Round 001 reviewed the full tutorial; the later time-limited deck has its own build, visual checks, and timed presenter plan.
