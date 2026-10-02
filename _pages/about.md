---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}
<span class='anchor' id='about-me'></span>

Hi~, I'm a third-year Ph.D. student at the School of Integrated Circuits in the Nanjing University (NJU), supervised by the Associate Prof [Ningmu Zou](https://zouningmu.github.io). Previously I received my B.S. degree in 2020 and my M.S. degree in 2023, at the School of Computer Science and Technology, China University of Mining and Technology (CUMT).

My research interests is include:
* AI for Chips (Layout Hotspot Detection, Mask Optimization, Wafer Defect Detection)
* AI for Remote Sensing (Small Object Detection/Segmentation in Remote Sening Image)
* Deep Learning for Computer Vision. 

**I'm current working on AI for Chips.** I have published 20+ papers with <a href='https://scholar.google.com/citations?user=2MvuH1QAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

<span class='anchor' id='educations-and-work-experience'></span>

<span class='anchor' id='education'></span>

# 📖 Education

<ul class="experience-list">
  <li class="experience-item">
    <div class="experience-logo"><img src="{{ '/images/nju-logo.svg' | relative_url }}" alt="Nanjing University logo" width="26" height="32" loading="lazy"></div>
    <div class="experience-details">
      <div class="experience-heading"><strong>Nanjing University (NJU)</strong><span class="experience-qualifications"><span>Ph.D. · <em>2024.09 - Now</em></span></span></div>
      <p>School of Integrated Circuits, Suzhou, Jiangsu, China · Supervisor: <a href="https://zouningmu.github.io">Ningmu Zou</a>.</p>
    </div>
  </li>
  <li class="experience-item">
    <div class="experience-logo"><img src="{{ '/images/cumt-logo.png' | relative_url }}" alt="China University of Mining and Technology logo" width="32" height="32" loading="lazy"></div>
    <div class="experience-details">
      <div class="experience-heading"><strong>China University of Mining and Technology (CUMT)</strong><span class="experience-qualifications"><span>M.S. · <em>2020.09 - 2023.06</em></span><span>B.E. · <em>2016.09 - 2020.06</em></span></span></div>
      <p>School of Computer Science and Technology, Xuzhou, Jiangsu, China · Supervisors: <a href="https://cs.cumt.edu.cn/info/1016/1065.htm">Yong Zhou</a>, <a href="https://www.scholat.com/zhaojiaqi">Jiaqi Zhao</a>.</p>
    </div>
  </li>
</ul>

<span class='anchor' id='work-experience'></span>

# 💼 Work Experience

<ul class="experience-list">
  <li class="experience-item">
    <div class="experience-logo experience-logo--amedac-frame"><img src="{{ '/images/amedac-logo.png' | relative_url }}" class="experience-logo--amedac" alt="AMEDAC logo" width="32" height="32" loading="lazy"></div>
    <div class="experience-details">
      <div class="experience-heading"><strong>AMEDAC</strong><span class="experience-qualifications"><span>Engineering Intern · <em>2026.04.10 - Now</em></span></span></div>
      <p>Product Application Department I, Hefei, Anhui, China.</p>
    </div>
  </li>
  <li class="experience-item">
    <div class="experience-logo"><img src="{{ '/images/xpeng-symbol.svg' | relative_url }}" class="experience-logo--xpeng" alt="XPeng logo" width="32" height="17" loading="lazy"></div>
    <div class="experience-details">
      <div class="experience-heading"><strong>XPeng Inc.</strong><span class="experience-qualifications"><span>Engineer · <em>2023.07 - 2024.07</em></span></span></div>
      <p>Intelligent Computing Center, Shanghai, China.</p>
    </div>
  </li>
  <li class="experience-item">
    <div class="experience-logo"><img src="{{ '/images/baidu-logo.svg' | relative_url }}" alt="Baidu logo" width="32" height="32" loading="lazy"></div>
    <div class="experience-details">
      <div class="experience-heading"><strong>Baidu Research</strong><span class="experience-qualifications"><span>Research Intern · <em>2022.06 - 2023.01</em></span></span></div>
      <p>Big Data Lab, Beijing, China · Mentor: <a href="https://qingzwang.github.io">Qingzhong Wang</a>.</p>
    </div>
  </li>
</ul>

 
<span class='anchor' id='talks'></span>

# 💬 Talks 

<ul class="talks-list">
  <li class="publication-item">
    <div class="publication-venue-column"><span class="publication-venue">SPIE/COS Photonics Asia</span></div>
    <div class="publication-details">
      <div class="publication-heading"><a class="publication-title" href="https://spie.org/spie-cos-photonics-asia/presentation/OptoChat--A-large-language-model-with-retrieval-augmented-generation/13727-8">OptoChat: a large language model with retrieval augmented generation for optics.</a></div>
      <div class="publication-authors">Beijing, China · Oct. 12–14, 2025</div>
    </div>
  </li>
</ul>


<span class='anchor' id='publications'></span>

# 📝 Publications

{% include publications.html %}

# 🙏 Preprints

<ul class="publication-list">
{% for paper in site.data.preprints %}{% include publication-item.html paper=paper %}{% endfor %}
</ul>

<span class='anchor' id='honors-and-awards'></span>

# 🏅 Honors & Awards

<ul class="honors-list">
  <li><span>School Outstanding Student (NJU)</span><span class="honor-year">2026</span></li>
  <li><span>National Scholarship for Ph.D. Student (NJU)</span><span class="honor-year">2025</span></li>
  <li><span>China International College Students’ Innovation Competition, Bronze Award</span><span class="honor-year">2025</span></li>
  <li><span>The First Prize Scholarship of CUMT</span><span class="honor-year">2020–2023</span></li>
</ul>

<span class='anchor' id='services'></span>

# 🤝 Services

<ul class="services-list">
  <li>
    <h2 class="service-heading">Journal reviewer</h2>
    <ul class="service-venues">
      <li>Knowledge-Based Systems</li>
      <li>Expert Systems with Applications</li>
      <li>The Journal of Supercomputing</li>
      <li>Signal, Image and Video Processing</li>
      <li>Pattern Recognition</li>
      <li>IEEE Transactions on Semiconductor Manufacturing</li>
    </ul>
  </li>
  <li>
    <h2 class="service-heading">Conference reviewer</h2>
    <ul class="service-venues">
      <li>ICME</li>
      <li>ICASSP</li>
    </ul>
  </li>
</ul>

<span class='anchor' id='contact'></span>

# 📧 Contact

- silin.chen[at]smail[dot]nju[dot]edu[dot]cn
- silin.chen[at]cumt[dot]edu[dot]cn
- silin.sherwin.chen[at]outlook[dot]com
- silin.sherwin.chen[at]gmail[dot]com

***


<font color=gray size=3 face="KAI">问到何时葡萄先熟透 我要静候 再静候 就算失收 始终要守</font>
