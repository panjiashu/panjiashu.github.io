---
layout: home
title: home
permalink: /
description: Jia-Shu Pan is a Ph.D. student at Westlake University studying the interaction between data structure and model learning.
---

<nav class="home-anchor-nav" aria-label="Homepage sections">
  <a href="#about"><span data-lang="en">About Me</span><span data-lang="zh" hidden>关于我</span></a>
  <a href="#research"><span data-lang="en">Research</span><span data-lang="zh" hidden>研究</span></a>
  <a href="#publications"><span data-lang="en">Publications</span><span data-lang="zh" hidden>论文</span></a>
  <a href="#hobbies"><span data-lang="en">Hobbies</span><span data-lang="zh" hidden>爱好</span></a>
  <a href="#contact"><span data-lang="en">Contact</span><span data-lang="zh" hidden>联系</span></a>
</nav>

<section id="about" class="home-section">
  <header class="home-section-header">
    <span class="home-section-number">01</span>
    <h2><span data-lang="en">About Me</span><span data-lang="zh" hidden>关于我</span></h2>
  </header>

  <div data-lang="en">
    <p class="home-lead">
      I am a Ph.D. student at Westlake University
      (Fall 2025), advised by Prof. <a href="https://tailin.org/" target="_blank" rel="noopener noreferrer">Tailin Wu</a>.
      I am deeply interested in the <strong>physics of intelligence</strong>. I do research to reduce my perplexity about the world we live in.
    </p>
    <p>
      I mainly study the <strong>interplay between understanding—or representation learning—and generative models</strong>. I believe this interaction underlies many
      important phenomena in language and vision: why does changing the order of training data alter a language model's convergence speed, and why
      does the choice of representation space strongly affect the efficiency of visual generative modeling? I enjoy connecting these questions to
      statistical physics and information theory, and using <strong>scientific methods</strong> to uncover the principles behind them.
    </p>
    <p>
      Previously, I studied astronomy at Nanjing University
      and the Australian National University,
      working with Prof. <a href="https://www.mso.anu.edu.au/~yting/" target="_blank" rel="noopener noreferrer">Yuan-Sen Ting</a>.
    </p>
  </div>

  <div data-lang="zh" hidden>
    <p class="home-lead">
      我于 2025 年秋季进入西湖大学攻读博士学位，导师是<a href="https://tailin.org/" target="_blank" rel="noopener noreferrer">吴泰霖老师</a>。我对<strong>智能的物理学</strong>有浓厚兴趣。我做研究，是为了减少自己对我们所生活的世界的困惑。
    </p>
    <p>
      我目前主要关注<strong>理解（或者说表示学习）与生成模型之间的相互作用</strong>。我相信这种相互作用支配了语言和视觉建模中众多有趣且重要的现象：为什么语言模型看到训练数据的顺序不同，会产生不同的收敛速度？为什么表示空间的选择会显著改变视觉生成模型的收敛效率？我享受这些问题与统计物理、信息论等领域的联系，并希望用<strong>科学方法</strong>理解现象背后的规律。
    </p>
    <p>
      此前，我在南京大学和澳大利亚国立大学学习天文，并与<a href="https://www.mso.anu.edu.au/~yting/" target="_blank" rel="noopener noreferrer">Yuan-Sen Ting 教授</a>合作。
    </p>
  </div>
</section>

<section id="research" class="home-section">
  <header class="home-section-header">
    <span class="home-section-number">02</span>
    <h2><span data-lang="en">Research Highlight</span><span data-lang="zh" hidden>研究工作</span></h2>
  </header>

  <details class="research-feature">
    <summary class="research-feature-summary">
      <span data-lang="en">
        <span class="research-kicker">Submitted to NeurIPS 2026</span>
        <strong>Feature Information Dynamics in Diffusion</strong>
        <span class="research-expand-label">Click to expand details</span>
      </span>
      <span data-lang="zh" hidden>
        <span class="research-kicker">投稿于 NeurIPS 2026</span>
        <strong>扩散模型中的特征信息动力学</strong>
        <span class="research-expand-label">点击展开详情</span>
      </span>
    </summary>

    <div class="research-feature-content">
      <div class="research-feature-copy" data-lang="en">
        <p>
          Diffusion models generate data through a continuum of denoising problems, and are widely observed to reveal coarse structure before fine detail. Yet, this intuition is mostly empirical and qualitative.
        </p>
        <h4>Feature information density</h4>
        <p>
          Let \(X\in\mathbb{R}^d\) be clean data, \(Y\) a feature of \(X\), and \(X_\gamma=\sqrt{\gamma}X+N\) the Gaussian-corrupted data at signal-to-noise ratio \(\gamma\), where \(N\sim\mathcal{N}(0,I)\) is independent noise. We define the <strong>feature information density</strong> as
        </p>
        <div class="research-equation" aria-label="Feature information density definition">
          \[D_Y(\gamma):=\frac{\mathrm d}{\mathrm d\gamma}I(Y;X_\gamma).\]
        </div>
        <p>
          Intuitively, \(D_Y(\gamma)\) distributes the total information about \(Y\) along the SNR axis: it measures how much additional feature information becomes accessible from an infinitesimal increase in SNR. A peak therefore identifies the noise level at which that feature is revealed most rapidly during denoising.
        </p>
        <p>
          At any fixed SNR, a feature-conditional denoiser has access to \(Y\) in addition to \(X_\gamma\). Since it can always ignore this extra condition, its best achievable denoising loss \(m_Y(\gamma)\) cannot exceed the optimal unconditional loss \(m_\varnothing(\gamma)\). Using the I-MMSE identity, we show that feature information density is exactly half of this <strong>reduction in optimal denoising loss brought by feature conditioning</strong>:
        </p>
        <div class="research-equation" aria-label="Feature information density equation">
          \[D_Y(\gamma)=\frac{1}{2}\left[m_\varnothing(\gamma)-m_Y(\gamma)\right].\]
        </div>
        <p>
          Its trajectory across noise levels describes how that feature's information is distributed over the generation process. Empirically, we quantitatively confirm spectral autoregression in pixel diffusion and find that class, mask, and edge information follow markedly different dynamics across pixel, SDVAE, VAVAE, and RAE spaces—revealing how representations reshape the order in which features are generated.
        </p>
      </div>

      <div class="research-feature-copy" data-lang="zh" hidden>
        <p>
          扩散模型通过一系列连续的去噪问题生成数据，人们普遍观察到它会先呈现粗粒度结构，再补充细节。然而，这一直主要是一种经验性的定性直觉。
        </p>
        <h4>特征信息密度</h4>
        <p>
          设 \(X\in\mathbb{R}^d\) 是干净数据，\(Y\) 是 \(X\) 的某个特征，\(X_\gamma=\sqrt{\gamma}X+N\) 是信噪比 \(\gamma\) 下经过高斯扰动的数据，其中 \(N\sim\mathcal{N}(0,I)\) 是独立噪声。我们将<strong>特征信息密度</strong>定义为
        </p>
        <div class="research-equation" aria-label="特征信息密度定义">
          \[D_Y(\gamma):=\frac{\mathrm d}{\mathrm d\gamma}I(Y;X_\gamma).\]
        </div>
        <p>
          直观上，\(D_Y(\gamma)\) 将关于 \(Y\) 的总信息量分布到信噪比轴上：它衡量信噪比增加无穷小量时，我们能从数据中多获得多少关于该特征的信息。因此，曲线的峰值对应这一特征在去噪过程中显现得最快的噪声水平。
        </p>
        <p>
          在任意固定的信噪比上，特征条件去噪器除了 \(X_\gamma\) 之外还能使用 \(Y\)。由于它总可以选择忽略这一额外条件，其能够达到的最优去噪损失 \(m_Y(\gamma)\) 不会高于无条件去噪器的最优损失 \(m_\varnothing(\gamma)\)。我们利用 I-MMSE 关系证明，特征信息密度恰好等于这一<strong>特征条件带来的最优去噪损失下降</strong>的一半：
        </p>
        <div class="research-equation" aria-label="特征信息密度公式">
          \[D_Y(\gamma)=\frac{1}{2}\left[m_\varnothing(\gamma)-m_Y(\gamma)\right].\]
        </div>
        <p>
          它随噪声水平变化的轨迹刻画了该特征信息在生成过程中的分布。经验上，我们定量验证了像素扩散中的频谱自回归现象，并观察到类别、mask和边缘信息在像素、SDVAE、VAVAE 与 RAE 空间中呈现显著不同的动力学，从而揭示表示如何重塑特征的生成顺序。
        </p>
      </div>

      <figure class="research-figure">
        <a href="{{ '/assets/pdf/fid-demo-pixel-curves.pdf' | relative_url }}" target="_blank" title="Open the figure as PDF">
          <img
            src="{{ '/assets/img/publication_preview/fid-demo-pixel-curves.png' | relative_url }}"
            alt="Feature information dynamics for class, mask, and Canny features in pixel space"
            width="2401"
            height="1350"
            loading="lazy"
          >
        </a>
        <figcaption data-lang="en">
          Feature information dynamics in pixel space. Select the figure for the full-resolution PDF.
        </figcaption>
        <figcaption data-lang="zh" hidden>
          像素空间中的特征信息动力学。点击图片可查看高清 PDF。
        </figcaption>
      </figure>
    </div>
  </details>
</section>

<section id="publications" class="home-section">
  <header class="home-section-header">
    <span class="home-section-number">03</span>
    <h2><span data-lang="en">Selected Publications</span><span data-lang="zh" hidden>代表论文</span></h2>
  </header>

  <div class="publication-list">
    <article class="publication-card">
      <p class="publication-venue">NeurIPS 2026 · Under Review</p>
        <h3>Feature Information Dynamics in Diffusion</h3>
      <p class="publication-authors"><strong>Jia-Shu Pan</strong>, Tao Zhang, Yufei Huang, Yanjun Sheng, Tailin Wu</p>
      <p class="publication-summary" data-lang="en">
        A quantitative framework for locating hierarchical features along diffusion trajectories and relating their temporal organization to representation-dependent convergence.
      </p>
      <p class="publication-summary" data-lang="zh" hidden>
        定量定位层次特征在扩散轨迹中的生成时刻，并研究这种时间组织方式与不同表示空间收敛速度之间的关系。
      </p>
      <div class="publication-links">
        <a href="#research"><span data-lang="en">Overview</span><span data-lang="zh" hidden>简介</span></a>
        <span><span data-lang="en">Manuscript coming soon</span><span data-lang="zh" hidden>论文即将公开</span></span>
      </div>
    </article>

    <article class="publication-card">
      <p class="publication-venue">ICLR 2026</p>
      <h3>VFScale: Intrinsic Reasoning through Verifier-Free Test-time Scalable Diffusion Model</h3>
      <p class="publication-authors">Tao Zhang*, <strong>Jia-Shu Pan*</strong>, Ruiqi Feng, Tailin Wu</p>
      <p class="publication-note"><span data-lang="en">* Equal contribution</span><span data-lang="zh" hidden>* 共同第一作者</span></p>
      <p class="publication-summary" data-lang="en">
        VFScale trains a diffusion model's own energy to serve as a verifier and combines it with hybrid Monte Carlo Tree Search, enabling verifier-free test-time scaling on Maze and Sudoku.
      </p>
      <p class="publication-summary" data-lang="zh" hidden>
        VFScale 将扩散模型自身的能量训练为验证器，并结合混合蒙特卡洛树搜索，在迷宫与数独任务上实现无需外部验证器的测试时扩展。
      </p>
      <div class="publication-links">
        <a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/6188c02ccc16a7587716de2efd754033-Abstract-Conference.html" target="_blank" rel="noopener noreferrer">ICLR 2026</a>
        <a href="https://arxiv.org/abs/2502.01989" target="_blank" rel="noopener noreferrer">arXiv</a>
        <a href="https://github.com/AI4Science-WestlakeU/VFScale" target="_blank" rel="noopener noreferrer">Code</a>
      </div>
    </article>

  </div>
</section>

<section id="hobbies" class="home-section">
  <header class="home-section-header">
    <span class="home-section-number">04</span>
    <h2><span data-lang="en">Hobbies</span><span data-lang="zh" hidden>爱好</span></h2>
  </header>

  <div class="hobby-list" aria-label="Hobbies">
    <span>🏃 <span data-lang="en">Running</span><span data-lang="zh" hidden>跑步</span></span>
    <span>🎞️ <span data-lang="en">Anime & ACG</span><span data-lang="zh" hidden>动漫与二次元</span></span>
  </div>
</section>

<section id="contact" class="home-section">
  <header class="home-section-header">
    <span class="home-section-number">05</span>
    <h2><span data-lang="en">Contact</span><span data-lang="zh" hidden>联系我</span></h2>
  </header>

  <div class="contact-card">
    <div data-lang="en">
      <p>Interesting questions, disagreements, and half-formed ideas are always welcome. If our research interests overlap, I would be happy to talk.</p>
      <p>Email: <a href="mailto:panjiashu@westlake.edu.cn">panjiashu@westlake.edu.cn</a></p>
    </div>
    <div data-lang="zh" hidden>
      <p>有趣的问题、不同的意见和尚未成形的想法都很受欢迎。如果我们的研究兴趣有所交集，欢迎随时交流。</p>
      <p>邮箱：<a href="mailto:panjiashu@westlake.edu.cn">panjiashu@westlake.edu.cn</a></p>
    </div>
  </div>
</section>

<p class="home-colophon">
  <span data-lang="en">© 2026 Jia-Shu Pan · Built with Jekyll and al-folio · Milky Way photographed by the author in the Tengger Desert on the night of August 12, 2026.</span>
  <span data-lang="zh" hidden>© 2026 潘嘉书 · 使用 Jekyll 与 al-folio 构建 · 星空照片由本人于 2026 年 8 月 12 日晚摄于腾格里沙漠。</span>
</p>
