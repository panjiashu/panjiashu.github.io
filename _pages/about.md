---
layout: home
title: home
permalink: /
last_updated: 2026-10-06
description: Jia-Shu Pan is a Ph.D. student at Westlake University studying the interaction between data structure and model learning.
---

<nav class="home-anchor-nav" aria-label="Homepage sections">
  <a href="#about"><span data-lang="en">About Me</span><span data-lang="zh" hidden>关于我</span></a>
  <a href="#research"><span data-lang="en">Research</span><span data-lang="zh" hidden>研究</span></a>
  <a href="#publications"><span data-lang="en">Publications</span><span data-lang="zh" hidden>论文</span></a>
  <a href="{{ "/projects/" | relative_url }}"><span data-lang="en">Projects</span><span data-lang="zh" hidden>项目</span></a>
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
      I study the <strong>interplay between representation learning and generative modeling</strong>, drawing on statistical physics and information theory. Some questions that guide my research are:
    </p>
    <ul class="research-questions">
      <li><strong>How does the encoding distribution \(q(z_0\mid x)\) shape the learnability of generative models?</strong> <a href="https://arxiv.org/abs/2510.11690" target="_blank" rel="noopener noreferrer">RAE</a> · <a href="https://arxiv.org/abs/2504.10483" target="_blank" rel="noopener noreferrer">REPA-E</a></li>
      <li><strong>How does the forward process \(p_F(z_{0:T})\) shape the learnability of generative models?</strong> <a href="https://arxiv.org/abs/2506.19935" target="_blank" rel="noopener noreferrer">AO-GPT</a> · <a href="https://zhuanlan.zhihu.com/p/1989306829931557631" target="_blank" rel="noopener noreferrer">Discussion on Zhihu (Chinese)</a></li>
      <li><strong>How can representation-aware objectives enable few-step or one-step generation?</strong> <a href="https://arxiv.org/abs/2607.03524" target="_blank" rel="noopener noreferrer">Perceptual Flow Matching</a> · <a href="https://arxiv.org/abs/2602.04770" target="_blank" rel="noopener noreferrer">Drifting Models</a></li>
    </ul>
    <p>These questions guide my current focus on <strong>end-to-end (single-step) latent generative models</strong>: jointly learning representations and generators to achieve both <strong>efficient learning and few-step generation</strong>.</p>
    <p class="home-opportunity">I am actively seeking <strong>internships with leading academic and industry research groups</strong>. Please <a href="#contact">get in touch</a> if our interests overlap.</p>
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
      我主要关注<strong>表示学习与生成模型之间的相互作用</strong>，并借助统计物理和信息论研究其中的规律。具体而言，我关心：
    </p>
    <ul class="research-questions">
      <li><strong>编码分布 \(q(z_0\mid x)\) 如何影响生成模型的可学习性？</strong><a href="https://arxiv.org/abs/2510.11690" target="_blank" rel="noopener noreferrer">RAE</a> · <a href="https://arxiv.org/abs/2504.10483" target="_blank" rel="noopener noreferrer">REPA-E</a></li>
      <li><strong>前向过程 \(p_F(z_{0:T})\) 如何影响生成模型的可学习性？</strong><a href="https://arxiv.org/abs/2506.19935" target="_blank" rel="noopener noreferrer">AO-GPT</a> · <a href="https://zhuanlan.zhihu.com/p/1989306829931557631" target="_blank" rel="noopener noreferrer">知乎讨论</a></li>
      <li><strong>如何利用表示空间中的训练目标，实现少步或单步生成？</strong><a href="https://arxiv.org/abs/2607.03524" target="_blank" rel="noopener noreferrer">Perceptual Flow Matching</a> · <a href="https://arxiv.org/abs/2602.04770" target="_blank" rel="noopener noreferrer">Drifting Models</a></li>
    </ul>
    <p>这些问题共同指向我目前的研究重点：<strong>端到端（单步）隐空间生成模型</strong>。通过联合学习表示与生成器，使模型兼具<strong>高效学习与少步生成能力</strong>。</p>
    <p class="home-opportunity">我正在积极寻找<strong>顶尖学术团队与工业界研究机构的实习机会</strong>。如果研究兴趣契合，欢迎<a href="#contact">联系我</a>。</p>
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

  <div class="research-feature">
    <div class="research-feature-overview">
      <div data-lang="en">
        <span class="research-kicker">NeurIPS 2026</span>
      <h3>Feature Information Dynamics in Diffusion</h3>
        <p>Using the <strong>I-MMSE relation</strong>, we define <strong>feature information density</strong> during diffusion for <strong>any feature</strong> in <strong>any representation space</strong>, quantifying <strong>the order in which different features emerge</strong>.</p>
        <p>Across the four representation spaces we study, <strong>only RAE exhibits the class → mask → Canny order</strong>, and diffusion models converge fastest in this space. We hypothesize that <strong>these ordered feature dynamics help explain its faster convergence</strong>.</p>
      </div>
      <div data-lang="zh" hidden>
        <span class="research-kicker">NeurIPS 2026</span>
        <h3>扩散模型中的特征信息动力学</h3>
        <p>利用 <strong>I-MMSE 关系</strong>，我们定义了<strong>任意表示空间</strong>上、<strong>任意特征</strong>在扩散中的<strong>特征信息密度</strong>，以量化<strong>不同特征在扩散过程中的出现顺序</strong>。</p>
        <p>在我们研究的四种表示空间中，<strong>只有 RAE 呈现类别 → mask → Canny 的顺序</strong>，且其上的扩散模型收敛最快。我们猜测，<strong>这种有序的特征动力学可能解释其更快的训练收敛</strong>。</p>
      </div>
      <p class="publication-links"><a href="{{ '/feature-information-dynamics/' | relative_url }}"><span data-lang="en">Project page →</span><span data-lang="zh" hidden>项目主页 →</span></a></p>
    </div>
    <figure class="research-figure">
      <a href="{{ '/assets/pdf/fid-demo-pixel-curves.pdf' | relative_url }}" target="_blank" rel="noopener noreferrer">
        <img src="{{ '/assets/img/publication_preview/fid-demo-pixel-curves.png' | relative_url }}" alt="Feature information dynamics for class, mask, and Canny in pixel space" width="2401" height="1350" loading="lazy">
      </a>
      <figcaption><span data-lang="en">Feature information dynamics in pixel space.</span><span data-lang="zh" hidden>像素空间中的特征信息动力学。</span></figcaption>
    </figure>
  <details class="research-feature-details">
    <summary class="research-feature-summary">
      <span data-lang="en">
        <span class="research-expand-label">Explore the definition and compare four representation spaces</span>
        <span class="research-collapse-label">Collapse details</span>
      </span>
      <span data-lang="zh" hidden>
        <span class="research-expand-label">展开查看定义与四种表示空间的对比</span>
        <span class="research-collapse-label">收起详情</span>
      </span>
    </summary>

    <div class="research-feature-content">
      <div class="research-feature-copy" data-lang="en">
        <p>
          Diffusion models generate data through a continuum of denoising problems, and are widely observed to reveal coarse structure before fine detail. Yet, this intuition is mostly empirical and qualitative—and, crucially, <strong>it need not hold after data are mapped into a representation space</strong>.
        </p>
        <h4>Feature information density</h4>
        <p>
          Let \(X\in\mathbb{R}^d\) be clean data (e.g., an image or latent), \(Y\) a feature of \(X\) (e.g., class, mask, or Canny), and \(X_\gamma=\sqrt{\gamma}X+N\) the Gaussian-corrupted data at signal-to-noise ratio \(\gamma\), where \(N\sim\mathcal{N}(0,I)\) is independent noise. We define the <strong>feature information density</strong> as
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
          Its trajectory across noise levels describes how that feature's information is distributed over the generation process. Empirically, we find that <strong>class, mask, and Canny information exhibit markedly different dynamics across pixel, SDVAE, VAVAE, and RAE spaces</strong>. <strong>Only RAE exhibits the class → mask → Canny order.</strong> We hypothesize that <strong>these ordered feature dynamics may explain why diffusion models converge fastest in the RAE space</strong>.
        </p>
      </div>

      <div class="research-feature-copy" data-lang="zh" hidden>
        <p>
          扩散模型通过一系列连续的去噪问题生成数据，人们普遍观察到它会先呈现粗粒度结构，再补充细节。然而，这一直主要是一种经验性的定性直觉；更关键的是，<strong>当数据被映射到表示空间后，这一 coarse-to-fine 直觉未必仍然成立</strong>。
        </p>
        <h4>特征信息密度</h4>
        <p>
          设 \(X\in\mathbb{R}^d\) 是干净数据（例如图像或 latent），\(Y\) 是 \(X\) 的某个特征（例如类别、mask 或 Canny），\(X_\gamma=\sqrt{\gamma}X+N\) 是信噪比 \(\gamma\) 下经过高斯扰动的数据，其中 \(N\sim\mathcal{N}(0,I)\) 是独立噪声。我们将<strong>特征信息密度</strong>定义为
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
          它随噪声水平变化的轨迹刻画了该特征信息在生成过程中的分布。经验上，我们发现<strong>类别、mask 和 Canny 信息在像素、SDVAE、VAVAE 与 RAE 空间中呈现显著不同的动力学</strong>。其中，<strong>只有 RAE 上的特征信息动力学服从类别 → mask → Canny 的顺序</strong>。我们猜测，<strong>这种有序的特征动力学可能正是扩散模型在 RAE 空间中收敛最快的原因</strong>。
        </p>
      </div>

      <figure class="research-figure">
        <a href="{{ '/assets/img/publication_preview/fid-four-representations.png' | relative_url }}" target="_blank" title="Open the full-resolution figure" rel="noopener noreferrer">
          <img
            src="{{ '/assets/img/publication_preview/fid-four-representations.png' | relative_url }}"
            alt="Feature information densities across pixel, SDVAE, VAVAE, and RAE spaces"
            loading="lazy"
          >
        </a>
        <figcaption data-lang="en">
          Feature information dynamics across pixel, SDVAE, VAVAE, and RAE spaces. Curves show normalized information densities for successive class, mask, and Canny conditions along log-SNR. <strong>Only RAE exhibits the class → mask → Canny order.</strong>
        </figcaption>
        <figcaption data-lang="zh" hidden>
          像素、SDVAE、VAVAE 与 RAE 空间中的特征信息动力学。曲线展示依次加入类别、mask、Canny 条件时，沿 log-SNR 分布的归一化信息密度。<strong>只有 RAE 呈现类别 → mask → Canny 的顺序。</strong>
        </figcaption>
      </figure>
      <button class="research-collapse-button" type="button" data-collapse-research>
        <span data-lang="en">Collapse details ↑</span><span data-lang="zh" hidden>收起详情 ↑</span>
      </button>
    </div>
  </details>
  </div>
</section>

<section id="publications" class="home-section">
  <header class="home-section-header">
    <span class="home-section-number">03</span>
    <h2><span data-lang="en">Selected Publications</span><span data-lang="zh" hidden>代表论文</span></h2>
  </header>

  <div class="publication-list">
    <article class="publication-card">
      <p class="publication-venue">NeurIPS 2026</p>
      <h3>Feature Information Dynamics in Diffusion</h3>
      <p class="publication-authors"><strong>Jia-Shu Pan</strong>, Tao Zhang, Yufei Huang, Yanjun Sheng, Tailin Wu</p>
      <p class="publication-summary" data-lang="en">
        A quantitative framework for locating hierarchical features along diffusion trajectories and relating their temporal organization to representation-dependent convergence.
      </p>
      <p class="publication-summary" data-lang="zh" hidden>
        定量定位层次特征在扩散轨迹中的生成时刻，并研究这种时间组织方式与不同表示空间收敛速度之间的关系。
      </p>
      <div class="publication-links">
        <a href="{{ "/feature-information-dynamics/" | relative_url }}"><span data-lang="en">Project page</span><span data-lang="zh" hidden>项目主页</span></a>
        <a href="https://arxiv.org/abs/2610.08626" target="_blank" rel="noopener noreferrer">arXiv</a>
        <a href="https://github.com/AI4Science-WestlakeU/feature-information-dynamics" target="_blank" rel="noopener noreferrer">Code</a>
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
    <span>🎞️ <span data-lang="en">Anime</span><span data-lang="zh" hidden>二次元</span></span>
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
  <span class="home-last-updated"><span data-lang="en">Last updated: </span><span data-lang="zh" hidden>最后编辑：</span><time datetime="{{ page.last_updated | date: '%Y-%m-%d' }}">{{ page.last_updated | date: '%Y-%m-%d' }}</time></span>
  <span data-lang="en">© 2026 Jia-Shu Pan · Built with Jekyll and al-folio · Website design inspired by <a href="https://huanranchen.github.io/" target="_blank" rel="noopener noreferrer">Huanran Chen</a> · Milky Way photographed by the author in the Tengger Desert on the night of August 12, 2026.</span>
  <span data-lang="zh" hidden>© 2026 潘嘉书 · 使用 Jekyll 与 al-folio 构建 · 网站设计参考了<a href="https://huanranchen.github.io/" target="_blank" rel="noopener noreferrer">陈焕然</a>的个人主页 · 星空照片由本人于 2026 年 8 月 12 日晚摄于腾格里沙漠。</span>
</p>
