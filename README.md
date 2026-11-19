# Software Tech Demo — Project Overview

Welcome to the **Software Tech Demo** repository! This project is a **redesign mockup** of the original Software Technology stream lecture notes portal, which can be found at [softwaretechnologymq.github.io](https://softwaretechnologymq.github.io/). 

The live mockup site is hosted at [ccheung96.github.io/software-tech-demo/](https://ccheung96.github.io/software-tech-demo/).

---

## 🚀 What the Project is About

This site is a modernized renovation attempt of the original MQ Software Technology learning portal. It aims to provide first-year and introductory computer science students (enrolled in COMP1000, COMP1010, COMP2160, COMP6010, and related units at Macquarie University) with a clean, highly readable, responsive, and visual study resource. 

The site is built with:
*   **Highly structured learning modules** containing assumed knowledge and clear learning outcomes.
*   **Embedded instructional videos** (primarily YouTube tutorials).
*   **Interactive exercise blocks** with expandable code solutions.
*   **Typeset mathematical equations** for computer science theory.
*   **Rich diagrams and visualizations** (such as SVG and D3.js scripts) to help students grasp programming concepts visually.
*   **Site-wide Search**: An auto-complete search bar at the top of the page indexing all learning modules, topic headings, and code references.

---

## 🛠️ Tech Stack & Architecture

This is a static website built on **Jekyll** (Ruby's static site generator) and themed with **Just the Docs**.

*   **Static Site Generator:** Jekyll
*   **Theme:** `just-the-docs/just-the-docs` (managed as a remote theme for ease of updates).
*   **Math Rendering:** **KaTeX** (loaded dynamically for performance, only on pages that request it).
*   **Diagram Rendering:** **Mermaid.js** (configured to render flowcharts, sequence diagrams, and structures directly from markdown text).
*   **Visualizations:** **D3.js v7** (custom code is hooked in to create responsive and interactive vector graphics).
*   **Styling Engine:** Custom **SASS/SCSS** overrides located in `_sass/custom/custom.scss` to handle layout adjustments, mobile responsiveness, exercise panels, and code block formatting.

---

## 💡 New to Jekyll & Just the Docs? (A Quick Crash Course)

If you come from a JavaScript/Node.js or Python background, Ruby-based tools like Jekyll might feel a bit different at first. Here is a quick conceptual map to help you get started:

*   **Jekyll is a Static Site Generator:** You write content in Markdown (`.md`) files (inside `docs/`), and Jekyll compiles them into standard, fast-loading HTML pages.
*   **Gemfile & Gemfile.lock:** These are the Ruby equivalents of `package.json` and `package-lock.json`. They define all the project's dependencies (plugins, themes, etc.).
*   **Bundler (`bundle`):** This is the Ruby package manager, similar to `npm`. Running `bundle install` is just like running `npm install`, and `bundle exec jekyll serve` is like running `npm run dev`.
*   **Just the Docs (JTD):** This is our theme. It reads metadata at the top of your Markdown files (called YAML Front Matter) and automatically generates the page templates, the sidebar navigation, and the search indexing. You don't need to manually link pages to the sidebar!
*   **⚠️ The Compiled Site (`_site/`):** When you run the local server, Jekyll outputs the generated site to the `_site/` directory. **Never edit files inside `_site/` directly!** Any changes there will be overwritten the next time Jekyll compiles. Always edit files in `docs/`, `_includes/`, or `_sass/`.

---

## 💻 Local Setup & Development

To run this project on your local machine for testing or content editing, follow these steps:

### Prerequisites
Make sure you have Ruby, Bundler, and Git installed on your system.

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CCheung96/software-tech-demo.git
    cd software-tech-demo
    ```
2.  **Install Ruby dependencies:**
    ```bash
    bundle install
    ```
3.  *(Optional)* **Install Pandoc/LaTeX tools** (if you need to compile slides or PDFs offline):
    ```bash
    chmod +x codex-setup.sh
    ./codex-setup.sh
    ```

### Running Locally
To launch the Jekyll development server, run:
```bash
bundle exec jekyll serve
```
After building, the site will be available locally at:
👉 **[http://localhost:4000/software-tech-demo](http://localhost:4000/software-tech-demo)**

*(Note: Jekyll will watch files and automatically rebuild the site as you make edits to your markdown files).*

---

## 📁 Repository Structure

Here is a guide to the key folders in this project:

```text
├── docs/                     # Markdown files containing all the lecture notes/content
│   ├── comp1000/             # COMP1000: Introduction to Computer Programming
│   ├── comp1010/             # COMP1010: Fundamentals of Computer Science
│   ├── comp2160/             # COMP2160: Game Development
│   ├── comp6010/             # COMP6010: Foundations of Computer Programming
│   ├── common/               # Shared guides, setup instructions, and resources
│   └── index.md              # Landing page content
├── _includes/                # Reusable HTML snippets (YouTube embeds, exercise layouts, back-to-top)
├── _layouts/                 # Custom page layouts (e.g., custom-page.html)
├── _sass/                    # Styling overrides (e.g., custom.scss for KaTeX, task boxes, chats)
├── assets/                   # Images, diagrams, favicons, and custom D3 scripts
├── _config.yml               # Jekyll configuration (Remote theme, search, callouts, and plugin settings)
├── Gemfile                   # Ruby gem dependencies
└── codex-setup.sh            # Installs LaTeX/Pandoc dependencies
```

---

## 🧪 Demonstration & Test Pages

The project includes two hidden utility pages that are excluded from the main sidebar navigation (`nav_exclude: true`). They are incredibly useful for course developers to reference and test layout features:

*   **Demonstration Page (`/demo`):** Located at [docs/demo.md](file:///wsl.localhost/Ubuntu-24.04/home/crystal/softwareTechDemo/docs/demo.md). It showcases rendered examples of all standard components—headings, styled callouts, exercise blocks, YouTube videos, KaTeX equations, and D3.js visual scripts—so developers can see how elements look when published.
*   **Test Page (`/test`):** Located at [docs/test.md](file:///wsl.localhost/Ubuntu-24.04/home/crystal/softwareTechDemo/docs/test.md). It serves as a staging/sandbox area for developers to test grid structures, embed scripts, layout rendering, and Mermaid.js diagrams before pushing changes live.

---

## ✍️ Content Authoring & Contribution Guidelines

Writing new content or editing existing pages is straightforward. All files in the `docs/` folder are written in **Markdown** with custom Jekyll helpers.

### 1. Folder-to-URL Path Matching

To keep the project clean and maintainable, the physical folder path of every Markdown file must exactly mirror its website URL path (permalink).

*   **Rule:** If a page is meant to live at the URL `/comp1000/loops`, the source file **must** be created at `docs/comp1000/loops.md`.
*   **Assets:** Any assets (images, codes, scripts) for that page must similarly live inside a matching subfolder under assets: `assets/comp1000/loops/{images/ ,code/ ,js/}`.
*   **Why this matters:** This 1-to-1 mapping ensures that the browser URL navigation doubles as a file explorer map for developers. It also makes it possible to remove manual `permalink` Front Matter tags in the future, as Jekyll can auto-generate routes directly from directory locations.

### 2. Front Matter Settings
Every page must start with a YAML block at the very top. To make this easy for developers, the keys are grouped logically:

```yaml
---
# Core Page Metadata
layout: custom-page                           # (Optional) Layout template (defaults to custom-page)
title: "Primitive Operations"                 # Page display title in the sidebar navigation
custom-title: "Primitive Operations of Processing" # (Optional) Header title at top of page (defaults to title)
permalink: /comp1000/primitive-operations     # The URL path of the page
author: "Gaurav Gupta"                       # (Optional) Page author(s) (defaults to Gaurav Gupta)

# Navigation & Sidebar Hierarchy
parent: COMP1000                              # (Optional) Parent page title (for Level 2 child pages)
grand_parent: "Optional Grandparent Title"    # (Optional) Grandparent page title (for Level 3 grandchild pages)
has_children: true                            # (Optional) Set to true if this page has subpages (like indices)
nav_order: 2                                  # (Optional) Numeric sorting position in the sidebar menu
nav_exclude: true                             # (Optional) Set to true to hide this page from the sidebar navigation

# Optional Feature Toggles
use_katex: true                               # (Optional) Set to true if the page uses LaTeX math formulas ($ or $$)
has_toc: false                                # (Optional) Set to false to disable Jekyll's default in-page TOC
---
```

#### Key Explanations:

##### 📁 Core Page Metadata
*   **`layout`**: *(Optional)* The layout template to use from the `_layouts/` directory. All pages default to `custom-page` globally, but index or landing layouts can override this (e.g., `home` or `default`).
*   **`title`**: The display name of the page in the sidebar navigation menu.
*   **`custom-title`**: *(Optional)* The main header title displayed at the top of the page. If omitted, it defaults to `title`. This is useful if you want a short name in the sidebar but a longer, descriptive header on the page itself.
*   **`permalink`**: The absolute URL path of the page (e.g., `/comp1000/primitive-operations`).
*   **`author`**: *(Optional)* Specifies the page author. Defaults to "Gaurav Gupta" if omitted.

##### 🗺️ Navigation & Sidebar Hierarchy
*   **`parent`**: *(Optional)* The `title` of the parent page (e.g., `COMP1000` or `Recursion`) under which this page will be grouped as a child in the sidebar. Set this on second-level and third-level pages.
*   **`grand_parent`**: *(Optional)* The `title` of the top-level grandparent page (e.g., `COMP1010` or `Research Skills`). Set this on third-level pages (grandchild pages) to complete the three-level navigation.
*   **`has_children`**: *(Optional)* Set to `true` on index pages (like `/comp1000`) to mark it as a parent category that other pages can target in their `parent` field.
*   **`nav_order`**: *(Optional)* A number defining the sorting order of the page relative to other pages in the same sidebar level.
*   **`nav_exclude`**: *(Optional)* Set to `true` to hide the page entirely from the sidebar navigation (used for hidden utility pages like `/demo` and `/test`).

##### ⚙️ Optional Feature Toggles
*   **`use_katex`**: *(Optional)* Set to `true` to dynamically load KaTeX CSS and JS assets to render LaTeX math formulas.
*   **`has_toc`**: *(Optional)* Set to `false` on pages where you want to disable Jekyll's default in-page table of contents generator.


### 3. Auto-Generating Table of Contents
To generate an in-page table of contents automatically, place the following code right below your Front Matter:
```markdown
- TOC
{:toc}
```

### 4. Adding Course Pre-requisites & Learning Outcomes
To keep courses structured, use the `prereq_outcomes.html` helper:
```markdown
{% capture topic_prereq %}
* [Transition to Processing]({{ site.baseurl }}/comp1000/transition-to-processing)
{% endcapture %}

{% capture topic_outcomes %}
* Understand static sketches.
* Understand categories of values and types.
{% endcapture %}

{% include prereq_outcomes.html prereq=topic_prereq outcomes=topic_outcomes %}
```

### 5. Creating Standard Exercises
Exercises should be formatted using the `exercise.html` include. This keeps the look consistent and nests the solution inside an expandable button:
```markdown
{% capture my_problem %}
Identify the output of the following statement:
```java
println(17 / 5);
```
{% endcapture %}

{% capture my_solution %}
The output is `3` due to integer division (the decimal part is discarded).
{% endcapture %}

{% include exercise.html
  title="Exercise: Integer Division"
  problem=my_problem
  solution=my_solution
%}
```

### 6. Applying Stylized Callouts
You can format blockquotes and warning callouts using the predefined Jekyll CSS helper classes:
```markdown
{: .note}
> **Note:** Here is some helpful background information.

{: .warning}
> **Warning!** Watch out for integer division!

{: .readings}
> **Reading(s):** Daniel Shiffman, Chapter 1 & 2.
```
*(Predefined classes include: `.note`, `.warning`, `.highlight`, `.keynote`, `.readings`).*

### 7. Math Equations (KaTeX)
To enable math rendering:
1.  Ensure `use_katex: true` is in the page's YAML Front Matter.
2.  Use standard LaTeX syntax:
    *   Inline math: Wrap in single dollar signs (e.g., `$E = mc^2$`).
    *   Block/Display math: Wrap in double dollar signs (e.g., `$$a^2 + b^2 = c^2$$`).

---

## 🛠️ Maintenance & Roadmap (Future Tasks)

If you are a developer looking to contribute to the codebase or improve the platform, here are our current priorities:

### Top Priorities
*   **Reorganise the `assets` folder (Hybrid Course-Topic-Type model):** 
    *   Separate global site-wide assets (theme CSS, general JS libraries, logos) into `assets/{css,js,images}`.
    *   Reorganise course content assets into a **Course -> Topic -> Asset-Type** hierarchy (e.g., `assets/comp1000/loops/images/`, `assets/comp1000/loops/code/`). Clean up the flat structures inside the current `comp1000` and `comp1010` folders, and update all corresponding image/code source links in the markdown files.
*   **KaTeX mobile responsiveness:** 
    *   Ensure complex block equations adjust correctly to smaller screens without breaking layout wrappers.
*   **Perform site-wide quality checks:**
    *   Verify page functionality to ensure all content is loading and working as intended.
    *   Check for broken paths, missing image attachments, or broken external links.
    *   Test mobile responsiveness and functionality to verify layout files, images, and embedded widgets adjust correctly on narrow screens.
    *   Audit style consistency to make sure page titles, headings, and custom templates match guidelines.

### Nice-to-Have Improvements
*   **Convert Legacy Tasks:** 
    *   Find any legacy `<div class="task">` blocks and convert them to the modern `{% include exercise.html ... %}` layout format.
*   **Remove `docs/` from URLs:** 
    *   Configure Jekyll settings to avoid needing manual permalinks for directory structures.
*   **Replace static diagrams:** 
    *   Convert static images into dynamic, maintainable **Mermaid.js** diagrams, SVGs, or interactive **D3.js** charts.
*   **Implement Automated Testing & Validation Suites:**
    *   **Link & Asset Checking:** Set up automated link checking to continuously audit internal paths, external links, and verify that local image files and embedded YouTube video players load successfully.
    *   **Mobile Layout Overflow Audits:** Write automated checks to scan page renderings and verify that code blocks, tables, and custom exercise widgets fit correctly on mobile viewports without causing horizontal scroll overflows.
*   **Establish Consistent Linting & Project Formatting:**
    *   **Markdown & Stylesheet Linter:** Set up linters/formatters (e.g., `Prettier` or `markdownlint`) to enforce consistent spacing, formatting, and file structures across all Markdown and SCSS source files.
    *   **Student Code Snippet Validator:** Create a utility script to extract, validate, and lint the Java/Processing code blocks featured in the documentation. The script should verify that all standard examples are syntactically correct, while ignoring or expecting failures for intentionally "bad" code examples (e.g., by checking for a special tag like `{: .bad-code}`).

### Potential & Known Issues
*   **Exercise Block TOC Exclusion:** 
    *   Because exercise blocks (`{% include exercise.html ... %}`) are rendered dynamically via Jekyll includes after the markdown parser builds the in-page Table of Contents (TOC), their titles (e.g., `### Exercise Title`) are not included in the auto-generated TOC block.

---

## 🤝 How to Submit Changes (Pull Requests)
1.  **Fork** the repository on GitHub.
2.  Create a feature branch (`git checkout -b feature/cool-new-lesson`).
3.  **Commit** your changes (`git commit -m 'Add lesson on 2D arrays'`).
4.  **Push** to the branch (`git push origin feature/cool-new-lesson`).
5.  Open a **Pull Request** explaining your changes!

For any direct suggestions or course inquiries, please contact **Gaurav Gupta** at `gaurav.gupta@mq.edu.au`.
