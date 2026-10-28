# Installation

This package is prepared for the GitHub profile repository:

`saeedvarvaee/saeedvarvaee`

## Upload

Do **not** leave the ZIP as the repository's only file. Open the archive and upload its contents so the repository root looks like this:

```text
README.md
assets/
docs/
scripts/
site/
```

`README.md` must be at the repository root.

1. Open `saeedvarvaee/saeedvarvaee` on GitHub.
2. Upload `README.md` and the complete `assets/`, `docs/`, `scripts/` and `site/` directories.
3. Commit the changes to the branch used by the profile README (normally `main`).
4. Open the repository page and then your GitHub profile.
5. Hard-refresh the page if the old README is still cached.

## Why the README uses GIF/PNG instead of SVG

The editable SVG originals are included for maintainability, but the README deliberately references the files in `assets/animations/` and `assets/static/`.

GitHub supports relative image paths in Markdown and can display GIF/PNG/SVG files, but GitHub's documentation states that SVGs do not support animation. The README therefore uses GIF for the motion layer. If GIF animation is unavailable in a viewer, the first GIF frame remains a complete static composition.

## Expected README asset references

The rendered README should load:

- `assets/animations/nexus-hero.gif`
- `assets/animations/nexus-divider.gif`
- `assets/animations/financial-orbit.gif`
- `assets/animations/banking-network.gif`
- `assets/animations/skill-matrix.gif`
- `assets/animations/finovaan-network.gif`
- `assets/animations/career-trajectory.gif`
- `assets/static/financial-quote.png`
- `assets/static/profile-signature.png`

## No build step

The profile README requires no Node.js, Python runtime, API key, external database, CDN, or server.

The optional `site/` experience is independent of the README and does not need to run for the profile to display correctly.
