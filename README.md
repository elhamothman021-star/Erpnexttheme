# edt_ui - Enterprise Digital Transformation UI

Shared UI Foundation / Design System for the Enterprise Digital Transformation (EDT) program.

> **Author / Maintainer:** Anwar Taha Mohammed Al-Hitar
> Applications Developer Specialist - 2H | CEO Office · `eyaalhitar@you.com.ye`

This app is the **single source of truth** for the enterprise design system. All domain apps
(hr_transformation, finance_transformation, administration, etc.) consume this shared foundation.
No custom app should build its own visual language, components, or hardcoded styles.

## Purpose

Establish a Unified Design Language so that all applications look, feel, and behave as
**One Unified/Cohesive Enterprise Product**, preventing UI fragmentation across domains.

## Structure

```
edt_ui/
├── hooks.py                # Asset injection (app_include_css / app_include_js)
├── setup.py
├── manifest.ini
├── public/
│   ├── css/
│   │   └── edt_design_tokens.css   # CSS design tokens (colors, typography, spacing, radii, shadows)
│   └── js/
│       ├── edt_components.bundle.js # Shared Vue components (Page Header, Card, Data Table, Inputs, Toast/Modal...)
│       └── edt_utils.bundle.js      # Shared helpers (API wrapper, date formatter, error handler)
└── edt_ui/
    └── __init__.py
```

## Enforcement Rules

Once `edt_ui` is installed and confirmed, the following rules apply to **all** domain apps:

1. All apps inject `edt_ui` via `hooks.py` (`app_include_css`, `app_include_js`).
2. No inline styles — use the CSS design tokens.
3. No hardcoded colors — use CSS variables (`--edt-*`).
4. No duplicate component logic — extend `edt_ui`, do not fork it.
5. No cross-app JS imports — any shared logic goes into `edt_ui` or `api/common`.

## Deliverables (v1)

1. **Design Tokens and CSS Foundation** — `public/css/edt_design_tokens.css`
2. **edt_ui App Scaffolding** — `bench new-app edt_ui`, hooks.py asset injection
3. **Core Component Library (v1)** — 3–5 shared Vue components:
   - Page Header, Card, Breadcrumb (Layout)
   - Text, Select, Date Picker input wrappers with validation (Inputs)
   - Standard Data Table with pagination and filter bar (Data)
   - Toast notification, Modal, Confirmation Dialog, Loader (Feedback)

## Installation

```bash
# Inside the frappe bench container
bench new-app edt_ui          # (scaffolded)
bench --site erp.local install-app edt_ui
bench build
bench restart
```

## Review

The initial version is reviewed and confirmed by @Zakaria Mohammed Ali [YOU - Head Office]
before rollout to all domain developers. Anwar Al-Hitar acts as the Frontend Reviewer.

## Contact

Anwar Al-Hitar — Applications Developer Specialist - 2H | CEO Office
eyaalhitar@you.com.ye | +967 733 111 576
