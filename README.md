Live site:

# [https://softwaretechnologyMQ.github.io](https://softwaretechnologyMQ.github.io/)

# :wave: 
Hey! This repository contains all the files the above website uses!

# Changes
If you want to make a change, follow the below steps!
<!-- - Collaborators can make changes directly.
- Others can, -->
  1. Fork this repository (top right of this page)
  2. Edit the relevant file(s) - There is a pencil icon towards top-right of the file.
  3. Commit your changes
  4. Once all file(s) are updated, go to your fork of  the repository (`<username>/SoftwareTechnologyMQ.github.io`)
  5. Click on `Contribute`
  6. Click on `Open Pull Request`
  7. Add a constructive message briefly explaining the changes made.
  8. Click on `Create Pull Request`
  9. Done!

## Slide generation
Pandoc can be used to build slides from the lesson Markdown files. To generate slides for `sorting.md` manually run:

```bash
./codex-setup.sh            # installs pandoc and LaTeX packages
pandoc sorting.md -t beamer -o sorting.pdf
pandoc sorting.md -o sorting.pptx
```

An example GitHub Actions workflow for `sorting.md` lives in `.github/workflows/sorting-slides.yml`. Duplicate this file and replace `sorting.md` with another lesson file to generate slides for other topics.
