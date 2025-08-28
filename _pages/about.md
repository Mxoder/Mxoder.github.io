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

I am a graduate of the School of Computer Science and Engineering (SCSE) at Beihang University (北京航空航天大学计算机学院). My research is centered on **Large Language Models (LLMs)** and **Multimodal Large Language Models (MLLMs)**, with a current focus on enhancing the **coding capabilities of LLMs**. I am also passionate about exploring **Data Curation** methodologies and the potential of **Small Models**.

I am a passionate advocate for open-source and take pride in contributing to the community with a variety of projects, models, and datasets on GitHub and Hugging Face. It is also my pleasure to give back to the academic world by serving as a reviewer for international conferences and workshops.

I find great joy in connecting with others and sharing knowledge through my technical blog. If my work resonates with you or if you have any ideas to discuss, I would be delighted to hear from you. You can find my email on the left.

I am a native speaker of **Chinese**, with professional working proficiency in **English** and **German**.

<a href='https://scholar.google.com/citations?user=OpcS2vQAAAAJ'>
  <img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations">
</a>

<a href="https://github.com/Mxoder">
  <img src="https://img.shields.io/github/stars/Mxoder?affiliations=OWNER&style=flat-square&label=Total%20Stars&logo=github" alt="Total Stars"/>
</a>

[![Hugging Face Downloads](https://img.shields.io/endpoint?url=https://mxoder.github.io/hf_downloads_badge.json&logo=hugging-face)](https://huggingface.co/Mxode) [![Hugging Face Likes](https://img.shields.io/endpoint?url=https://mxoder.github.io/hf_likes_badge.json&logo=hugging-face)](https://huggingface.co/Mxode)

<!-- [![Zhihu Followers](https://img.shields.io/endpoint?url=https://mxoder.github.io/zhihu_followers_badge.json&logo=zhihu)](https://www.zhihu.com/people/mxode) [![Zhihu Upvotes](https://img.shields.io/endpoint?url=https://mxoder.github.io/zhihu_voteups_badge.json&logo=zhihu)](https://www.zhihu.com/people/mxode) [![Zhihu Bookmarks](https://img.shields.io/endpoint?url=https://mxoder.github.io/zhihu_favorites_badge.json&logo=zhihu)](https://www.zhihu.com/people/mxode) [![知乎感谢](https://img.shields.io/endpoint?url=https://mxoder.github.io/zhihu_thanks_badge.json&logo=zhihu)](https://www.zhihu.com/people/mxode) -->



# 🔥 News {#news}

- *2025.08*: &nbsp;🎉 One paper accepted to *EMNLP 2025*.
- *2025.07*: &nbsp;🎉 Two papers accepted to *ICCV 2025 Workshops*.
- *2025.06*: &nbsp;🎉 Two papers accepted to *ICML 2025 Workshops*.
- *2025.04*: &nbsp;🏅 Received **3 Great Review distinctions** in *ACL Rolling Review (Feb. cycle)*.
- *2024.12*: &nbsp;🎉 One paper accepted to *AAAI 2025*.



# 📝 Publications {#publications}

Authors marked with \* contributed equally (co-first authors).

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2025</div><img src='images/Math-PUMA-500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Math-PUMA: Progressive Upward Multimodal Alignment to Enhance Mathematical Reasoning](https://ojs.aaai.org/index.php/AAAI/article/view/34815)

Wenwen Zhuang\*, Xin Huang\*, **Xiantao Zhang\***, Jin Zeng

[**Project**](https://github.com/wwzhuang01/Math-PUMA) <a href="https://github.com/wwzhuang01/Math-PUMA"><img src="https://img.shields.io/github/stars/wwzhuang01/Math-PUMA?style=flat&logo=github" alt="GitHub stars"/></a> <strong><span class='show_paper_citations' data='OpcS2vQAAAAJ:u5HHmVD_uO8C'></span></strong>
- This paper introduces Math-PUMA, a novel training methodology that uses Progressive Upward Multimodal Alignment to significantly narrow the performance gap between textual and visual modalities in mathematical reasoning , achieving state-of-the-art results among open-source MLLMs. 
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CV4A11y@ICCV 2025</div><img src='images/The_Escalator_Problem-500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[The Escalator Problem: Identifying Implicit Motion Blindness in AI for Accessibility](https://arxiv.org/abs/2508.07989)

**Xiantao Zhang**

- This paper identifies "Implicit Motion Blindness" in MLLMs, exemplified by their failure to determine an escalator's direction , and argues this flaw—caused by the prevalent frame-sampling paradigm —necessitates a paradigm shift from semantic recognition to robust physical perception to build trustworthy assistive AI for the visually impaired. 
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">WCCA@ICCV 2025</div><img src='images/Pre_vs_Fab-500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Preservation vs. Fabrication: An Ethical Framework of Consent, Transparency, and Integrity for Posthumous AI Art](https://openreview.net/forum?id=UEHmz3m7zl)

**Xiantao Zhang**

- This paper proposes an ethical framework for posthumous AI art, demanding the artist's explicit consent, mandatory transparency, and an integrity rule that forbids AI from fabricating new works where no verifiable intent exists. 
</div>
</div>



# 📖 Educations {#educations}
- *2021.09 - 2025.06*, B.S. in Computer Science, School of Computer Science and Engineering (SCSE), Beihang University. 



# 🎖 Honors and Awards {#honors-and-awards}

- *2025.06*, Outstanding Bachelor Thesis, School of Computer Science and Engineering (SCSE), Beihang University.



# 💻 Internships {#internships}

- *2024.07 - 2024.09*, ByteDance, Beijing.



# 📝 Academic Service {#academic-service}

**Conferences:**

- **Program Committee Member**, *AAAI 2026*
- **Reviewer**, *EMNLP 2025* (ARR May. cycle)
- **Reviewer**, *ACM Multimedia 2025*
- **Reviewer**, *ACL 2025* (ARR Feb. cycle) — Received **3 Great Review distinctions**

**Workshops:**

- **Reviewer**, *NeurIPS 2025 Workshop on MATH-AI*
- **Reviewer**, *NeurIPS 2025 Workshop on COML*
- **Reviewer**, *ICML 2025 Workshop on AIW*
- **Reviewer**, *COLM 2025 Workshop on INTERPLAY*



# 🚀 Open Source Projects {#open-source-projects}

- [LLM-from-scratch](https://github.com/Mxoder/LLM-from-scratch) <a href="https://github.com/Mxoder/LLM-from-scratch"><img src="https://img.shields.io/github/stars/Mxoder/LLM-from-scratch?style=flat&logo=github" alt="GitHub stars"/></a>: A series of hands-on reproductions and technical deep-dives, including *pretraining LLaMA-3 from scratch*, *implementing LoRA from scratch*, in-depth analyses of the *Qwen Series technical reports*, and explorations of *asynchronous concurrency in LLMs*, and more.

- [Maxs-Awesome-Datasets](https://github.com/Mxoder/Maxs-Awesome-Datasets) <a href="https://github.com/Mxoder/Maxs-Awesome-Datasets"><img src="https://img.shields.io/github/stars/Mxoder/Maxs-Awesome-Datasets?style=flat&logo=github" alt="GitHub stars"/></a>: A diverse set of open-source datasets I have released, with a particular emphasis on **Chinese datasets** across various domains and topics, among others.



# ✍️ Blogs {#blogs}

*Friendly reminder: the following blog posts are written in **Chinese**.*
{: .notice--info}

- **[How Qwen3 Achieves Hybrid Thinking (Fast and Slow Thinking)?](https://zhuanlan.zhihu.com/p/1900555481715570305)** – 200+ likes, 300+ bookmarks

- **[LoRA from Scratch](https://zhuanlan.zhihu.com/p/702419731)** – 200+ likes, 400+ bookmarks

- **[Pretraining a Miniature LLaMA-3 from Scratch](https://zhuanlan.zhihu.com/p/695130168)** – 150+ likes, 400+ bookmarks

- **[A New Chinese Reasoning Distillation Dataset: Chinese-Reasoning-Distil-Data](https://zhuanlan.zhihu.com/p/1898405616860521535)** – 30+ likes, 80+ bookmarks

*Read more on my [Zhihu Homepage](https://www.zhihu.com/people/mxode).*