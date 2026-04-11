# SavingCarQuotes.com - Masterplan

## Project Overview

**SavingCarQuotes.com** is a lead-generation website for auto insurance comparison and quotes. It operates as an advertorial-style landing page that drives users toward insurance quote comparison services. Revenue is generated through lead referrals and call tracking commissions.

---

## Current State Assessment

### What Exists Today
- **Single-page static site** (`index.html`) — advertorial format, ~2,000 lines
- **Secondary landing page** (`/warranty/`) — auto security insurance offer
- **Empty placeholder** (`/insider_insurance_pro_tips/`) — unused directory
- **Static assets** in `/files/` — CSS, images, logo
- **Hosted on GitHub Pages** with custom domain via CNAME

### Tech Stack
| Layer | Technology | Version | Notes |
|-------|-----------|---------|-------|
| Markup | HTML5 | - | Single monolithic file |
| Styling | Bootstrap | 4.0.0 | Via Cloudflare CDN |
| Custom CSS | style.css | - | In `/files/` |
| JavaScript | jQuery | 2.2.4 | Inline scripts |
| Analytics | Google Analytics | gtag.js | ID: G-YTH9DR6DDK |
| Tracking | Facebook Pixel | - | Meta ID: 1182813016320048 |
| Call Routing | Ringba | - | Dynamic number replacement |
| Hosting | GitHub Pages | - | Static only |
| Geo | ipinfo.io | - | IP-based region detection |

### Strengths
- Fully functional lead generation flow
- DMS P&C regulatory compliance (as of latest commit)
- Dynamic phone number routing via Ringba
- IP-based regional personalization
- Multiple analytics/tracking integrations
- Responsive design (mobile + desktop)
- Zero hosting cost (GitHub Pages)

### Weaknesses
- Monolithic HTML file — hard to maintain and A/B test
- Outdated dependencies (jQuery 2.2.4, Bootstrap 4.0.0)
- No build pipeline or asset optimization
- No automated testing or CI/CD
- Inline CSS/JS — no separation of concerns
- Multiple backup files checked into repo (`index.html.old`, `.ori`, `.ori2`)
- No README, no documentation
- Empty directories suggest incomplete feature rollouts
- No structured data / SEO schema markup
- No page speed optimization (no minification, no image optimization)
- No A/B testing infrastructure
- French comments in code (inconsistent with English site)

---

## Strategic Goals

### Short-Term (1-3 Months)
1. **Improve conversion rate** — optimize CTAs, page speed, mobile experience
2. **SEO improvements** — structured data, meta tags, Open Graph
3. **Code quality** — clean up repo, remove dead files, organize assets
4. **Content expansion** — build out `/insider_insurance_pro_tips/`

### Medium-Term (3-6 Months)
5. **Multi-page architecture** — break monolith into reusable templates
6. **A/B testing** — test headlines, CTAs, layouts for conversion lift
7. **Performance optimization** — image compression, lazy loading, minification
8. **Additional landing pages** — target specific states/demographics

### Long-Term (6-12 Months)
9. **Static site generator** — migrate to a build-based system (e.g., 11ty, Astro)
10. **Automated compliance checks** — lint for prohibited claims
11. **Multi-vertical expansion** — home insurance, life insurance, health insurance
12. **Analytics dashboard** — centralized reporting on conversion metrics

---

## Implementation Roadmap

### Phase 1: Foundation & Cleanup

**Goal**: Clean codebase, improve maintainability, quick conversion wins.

- [ ] **Remove dead files** — delete `index.html.old`, `index.html.ori`, `index.html.ori2`, `.DS_Store`
- [ ] **Add `.gitignore`** — exclude `.DS_Store`, editor files, OS artifacts
- [ ] **Add `README.md`** — document project purpose, setup, deployment
- [ ] **Translate French comments** to English for consistency
- [ ] **Extract inline JS** into separate `files/main.js`
- [ ] **Audit and update copyright year** to 2026
- [ ] **Add Open Graph / Twitter Card meta tags** for social sharing
- [ ] **Add structured data** (JSON-LD) for Article schema and Organization schema
- [ ] **Add favicon** and Apple touch icon

### Phase 2: Conversion Optimization

**Goal**: Increase lead generation rate through UX and content improvements.

- [ ] **Optimize CTA buttons** — larger, more prominent, contrasting colors
- [ ] **Add urgency/scarcity signals** (compliant with DMS P&C)
- [ ] **Improve above-the-fold content** — clearer value proposition
- [ ] **Add trust signals** — security badges, partner logos, review counts
- [ ] **Optimize mobile tap targets** — ensure all CTAs are easily tappable
- [ ] **Implement click-to-call improvements** — bigger phone number display on mobile
- [ ] **Add exit-intent detection** — show offer before user leaves
- [ ] **Test alternative headlines** via simple JS-based split testing
- [ ] **Add testimonial/social proof section** (compliant, non-misleading)

### Phase 3: Content & SEO Expansion

**Goal**: Drive organic traffic through valuable content.

- [ ] **Build `/insider_insurance_pro_tips/`** — educational content hub
  - "How to lower your car insurance premium"
  - "Understanding coverage types: liability vs. full coverage"
  - "When to shop for new auto insurance"
  - "State-by-state insurance requirements"
  - "Discounts you might be missing"
- [ ] **Add internal linking** between content pages and main landing page
- [ ] **Implement sitemap.xml** and `robots.txt`
- [ ] **Add canonical URLs** to prevent duplicate content issues
- [ ] **State-specific landing pages** — `/insurance/california/`, `/insurance/texas/`, etc.
- [ ] **Blog/article template** — reusable layout for content marketing

### Phase 4: Technical Modernization

**Goal**: Modern tooling for faster iteration and better performance.

- [ ] **Evaluate static site generator** — 11ty or Astro (keeps GitHub Pages compatibility)
- [ ] **Upgrade Bootstrap** to v5 (drops jQuery dependency)
- [ ] **Remove jQuery** — replace with vanilla JS
- [ ] **Image optimization** — WebP format, responsive images with `srcset`
- [ ] **Implement lazy loading** for below-the-fold images
- [ ] **Add CSS minification** and critical CSS inlining
- [ ] **Set up GitHub Actions** for build, deploy, and basic checks
- [ ] **Add Lighthouse CI** — automated performance/accessibility scoring
- [ ] **Implement Content Security Policy** headers (via `_headers` file for GitHub Pages)

### Phase 5: Scaling & Multi-Vertical

**Goal**: Expand business beyond auto insurance.

- [ ] **Template system** — create reusable page components for new verticals
- [ ] **Home insurance landing page** — `/home-insurance/`
- [ ] **Life insurance landing page** — `/life-insurance/`
- [ ] **Health insurance landing page** — `/health-insurance/`
- [ ] **Shared component library** — header, footer, CTA blocks, trust signals
- [ ] **Centralized tracking config** — single place to manage all pixel/analytics IDs
- [ ] **Compliance framework** — checklist and automated checks per vertical

---

## Compliance Requirements

All content must adhere to DMS P&C and general insurance advertising regulations:

- **No prohibited claims**: Avoid "secrets", "tricks", or implying insurers are hiding information
- **No misleading testimonials**: All examples must be clearly hypothetical or disclaimed
- **Advertorial disclosure**: Must be clearly labeled on every page
- **Rate disclaimers**: All quoted rates must include "rates vary" language
- **Partner disclosure**: Must disclose compensation from insurance partners
- **Privacy policy**: Required if collecting any user data
- **Terms of service**: Required for any interactive features

---

## Key Metrics to Track

| Metric | Current Tracking | Target |
|--------|-----------------|--------|
| Page views | Google Analytics | Baseline + growth |
| Click-through rate (CTA) | GA Events | > 15% |
| Call volume | Ringba | Growth month-over-month |
| Bounce rate | Google Analytics | < 50% |
| Mobile conversion | GA + Ringba | Parity with desktop |
| Page load time | Lighthouse | < 3 seconds |
| SEO organic traffic | Google Search Console | 20% of total traffic |

---

## File Structure (Target State)

```
savingcarquotes.com/
├── .github/
│   └── workflows/
│       └── deploy.yml              # CI/CD pipeline
├── .gitignore
├── CNAME
├── MASTERPLAN.md
├── README.md
├── index.html                      # Main landing page
├── sitemap.xml
├── robots.txt
├── _headers                        # Security headers (GitHub Pages)
├── files/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── main.js                 # Core site logic
│   │   └── tracking.js             # Analytics & pixel config
│   └── img/
│       ├── logo.png
│       ├── favicon.ico
│       ├── hero.webp
│       └── ...
├── warranty/
│   └── index.html
├── insider_insurance_pro_tips/
│   ├── index.html                  # Tips hub page
│   ├── lower-premium/
│   │   └── index.html
│   └── coverage-types/
│       └── index.html
└── insurance/                      # State-specific pages (future)
    ├── california/
    │   └── index.html
    └── texas/
        └── index.html
```

---

## Risk Register

| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|------------|
| Regulatory non-compliance | High | Medium | Regular compliance audits, automated checks |
| Tracking script breakage | High | Low | Monitor Ringba/pixel health, fallback numbers |
| GitHub Pages outage | Medium | Low | CDN caching, consider backup hosting |
| Competitor copying | Low | High | Continuous optimization, brand differentiation |
| Google algorithm change | Medium | Medium | Diversify traffic sources, build email list |
| jQuery/Bootstrap EOL | Low | Certain | Plan migration in Phase 4 |

---

## Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2025-03-17 | Migrated from AWS to GitHub Pages | Cost reduction, simpler deployment |
| 2025-04-29 | Added Ringba call tracking | Better call attribution and routing |
| 2025-06-20 | Added warranty landing page | Revenue diversification |
| 2025-11-14 | Replaced phone numbers with tracking links | Improved lead attribution |
| 2026-02-26 | DMS P&C compliance overhaul | Regulatory requirement |
| 2026-04-11 | Created masterplan | Strategic planning for growth |

---

*Last updated: 2026-04-11*
