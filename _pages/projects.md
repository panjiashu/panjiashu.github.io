---
layout: page
permalink: /projects/
title: Projects
description: Research projects and interactive introductions.
nav: true
nav_order: 3
---

<style>
.project-card{border:1px solid var(--global-divider-color);border-radius:8px;overflow:hidden;background:var(--global-bg-color)}
.project-card img{display:block;width:100%;height:240px;object-fit:contain;background:#fff;padding:16px}
.project-card-body{padding:24px}.project-card h2{font-size:25px;font-weight:500;margin:0 0 16px}
.project-card p{font-size:16px;line-height:1.65;margin-bottom:16px}.project-card .project-venue{color:var(--global-text-color-light);font-size:14px}
.project-card a{color:#315f8c}html[data-theme="dark"] .project-card a{color:#91b9df}
</style>
<article class="project-card">
  <a href="{{ '/feature-information-dynamics/' | relative_url }}" aria-label="Explore Feature Information Dynamics in Diffusion">
    <img src="{{ '/feature-information-dynamics/assets/spectral-mnist.png' | relative_url }}" alt="Independent and chained feature information densities across frequency bands" width="2200" height="1781">
  </a>
  <div class="project-card-body">
    <p class="project-venue">NeurIPS 2026</p>
    <h2><a href="{{ '/feature-information-dynamics/' | relative_url }}">Feature Information Dynamics in Diffusion</a></h2>
    <p>When does diffusion generate each feature in an arbitrary representation space? Explore feature information density, chained decomposition, and how representations change generation order.</p>
    <a href="{{ '/feature-information-dynamics/' | relative_url }}">Explore the project →</a>
  </div>
</article>
