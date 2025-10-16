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

Hi~, I'm a second-year Ph.D. student at the School of Integrated Circuits in the Nanjing University (NJU), supervised by the Associate Prof [Ningmu Zou](https://zouningmu.github.io). Previously I received my B.S. degree in 2020 and my M.S. degree in 2023, at the School of Computer Science and Technology, China University of Mining and Technology (CUMT).

My research interests is include:
* AI for Chips (Layout Hotspot Detection, Mask Optimization, Wafer Defect Detection)
* AI for Remote Sensing (Small Object Detection/Segmentation in Remote Sening Image)
* Deep Learning for Computer Vision. 

**I'm current working on AI for Chips.** I have published 10+ papers with <a href='https://scholar.google.com/citations?user=2MvuH1QAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

# 📖 Educations and Work Experience
- *2024.09 - Now*, (Ph.D.) School of Integrated Circuits, Nanjing University, Suzhou, Jiangsu, China. Supervisior: [Ningmu Zou](https://zouningmu.github.io)
- *2023.07 - 2024.07*, (Engineer) Intelligent Computing Center, Xpeng Inc., ShangHai, China. 
- *2022.06 - 2023.01*, (Research Intern) Big Data Lab, Baidu Research, Beijing, China. Mentor: [Qingzhong Wang](https://qingzwang.github.io).
- *2020.09 - 2023.06*, (M.S.) School of Computer Science and Technology, China University of Mining and Technology, Xuzhou, Jiangsu, China. Supervisor: [Yong Zhou](https://cs.cumt.edu.cn/info/1016/1065.htm), [Jiaqi Zhao](https://www.scholat.com/zhaojiaqi).
- *2016.09 - 2020.06*, (B.E.) School of Computer Science and Technology, China University of Mining and Technology, Xuzhou, Jiangsu, China.

 
<!-- # 🔥 News
- *2022.02*: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2022.02*: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->


# 📝 Publications 
- **[ACM TODAES, 2026]** [You Only Need Non-hotspot: An Unsupervised Training-Free Method for Layout Hotspot Detection](https://dl.acm.org/doi/epdf/10.1145/3771767), **Silin Chen**; Kangjian Di; Yibo Huang; Binwu Zhu; Ningmu Zou. (CCF-B, Journal) 
- **[ASP DAC, 2026]** [Understand and Detect: Lithographic Hotspot Detection by the Interpretable Graph Attention Network](https://zouningmu.github.io/images/people/Understand%20and%20Detect%20Lithographic%20Hotspot%20Detection%20by%20the%20Interpretable%20Graph%20Attention%20Network.pdf), Andy Liu\#; **Silin Chen\#**; Guohao Wang; Wenzheng Zhao, Yuxiang Fu, Ningmu Zou. (CCF-C, Conference)
- **[IEEE JEDS]** [Improved Algorithm of Dueling DQN for BSIM Parameter Extraction Task](https://ieeexplore.ieee.org/document/11197319), Wenjun Chen; Yali Zhang; Zikang Zeng; **Silin Chen**; Kangjian Di; Guohao Wang; Chia-Yen Li; Ningmu Zou.
- **[IWAPS, 2025]** SVD-based Layout Representation for Lithographic Hotspot Detection, Yibo Huang\#; **Silin Chen\#**; Hao Shu; Jiahao Wang; Wenbo Xu; Ningmu Zou.
- **[GLSVLSI, 2025]** [When Transformer Meets Layout Hotspot: An End-to-End Transformer-based Detector with Prior Lithography](https://dl.acm.org/doi/10.1145/3716368.3735160), Wenbo Xu\#; **Silin Chen\#**; Jiale Li; Kangjian Di; Yuxiang Fu; Ningmu Zou. (CCF-C, Conference)
- **[ICIC Oral, 2025]** [Adapted-MoE: Mixture of Experts with Test-Time Adaption for Anomaly Detection](https://link.springer.com/chapter/10.1007/978-981-96-9891-2_36), Tianwu Lei#; **Silin Chen#**; Bohan Wang; Zhengkai Jiang; Ningmu Zou. (CCF-C, Conference)
- **[IEEE/ACM DAC, 2025]** [Delving into Topology Representation for Layout Pattern:  A Novel Contrastive Learning Framework for Hotspot Detection](https://ieeexplore.ieee.org/document/11133380), **Silin Chen**; Kangjian Di; Guohao Wang; Wenzheng Zhao; Li Du; Ningmu Zou. (CCF-A, Conference)
- **[IEEE SPL, 2025]** [Look Twice and Closer: A Coarse-to-Fine Segmentation Network for Small Objects in Remote Sensing Images](https://ieeexplore.ieee.org/document/10878803), **Silin Chen\#**; Qingzhong Wang\#; Kangjian Di; Haoyi Xiong; Ningmu Zou. (CCF-C, Journal, *IF 3.2*)
- **[Advanced Photonics, 2025]** [Time-wavelength multiplexed photonic neural network accelerator for distributed acoustic sensing systems](https://www.spiedigitallibrary.org/journals/advanced-photonics/volume-7/issue-02/026008/Time-wavelength-multiplexed-photonic-neural-network-accelerator-for-distributed-acoustic/10.1117/1.AP.7.2.026008.pdf), Fuhao Yu; Kangjian Di; Wenjun Chen; Sen Yan; Yuanyuan Yao; **Silin Chen**; Xuping Zhang; Yixin Zhang; Ningmu Zou; Wei Jiang. (CAS 1st, Top, Journal, ***IF 20.6***)
- **[ESWA, 2023]** [Info-FPN: An informative feature pyramid network for object detection in remote sensing images](https://www.sciencedirect.com/science/article/pii/S0957417422021509), **Silin Chen**; Jiaqi Zhao; Yong Zhou; Hanzheng Wang; Rui Yao; Lixu Zhang; Yong Xue. (CCF-C, Journal, *IF 7.5*)
- **[IEEE TGRS, 2022]** [CLT-Det: Correlation learning based on transformer for detecting dense objects in remote sensing images](https://ieeexplore.ieee.org/abstract/document/9878347/), Yong Zhou; **Silin Chen**; Jiaqi Zhao; Rui Yao; Yong Xue; Abdulmotaleb El Saddik. (CCF-B, Journal, *IF 7.5*)
- **[IEEE TCSVT, 2022]** [Spatial-temporal based multihead self-attention for remote sensing image change detection](https://ieeexplore.ieee.org/abstract/document/9777690/), Yong Zhou; Fengkai Wang; Jiaqi Zhao; Rui Yao; **Silin Chen**; Heping Ma. (CCF-B, Journal, *IF 8.3*)
- **[IEEE TMM, 2022]** [Spatial-channel enhanced transformer for visible-infrared person re-identification](https://ieeexplore.ieee.org/abstract/document/9745797/), Jiaqi Zhao; Hanzheng Wang; Yong Zhou; Rui Yao; **Silin Chen**; Abdulmotaleb El Saddik. (CCF-B, Journal, *IF 8.4*)
- **[Neurocomputing, 2021]** [AMC-Net: Attentive modality-consistent network for visible-infrared person re-identification](https://www.sciencedirect.com/science/article/pii/S0925231221012376), Hanzheng Wang; Jiaqi Zhao; Yong Zhou; Rui Yao; Ying Chen; **Silin Chen**. (CCF-C, Journal, *IF 5.5*)
- **[模式识别与人工智能, 2021]** [基于深度强化学习的遥感图像可解释目标检测方法](https://kns.cnki.net/kcms2/article/abstract?v=2Z_8GvOTliWhXUiDYKrqnAIPgVc_lC1Ew6X9U5rDBYkKYAzixt42EIp65ugcuaIowLZSH_2gP6c5nPlLbdyN0Ml5JvSOTKg7F8602y-sAh1vpJ8fG_j0rDVI1TL9XD8XNNtUaciQFnhCi5tl63-L4LI84aYeo8C8ukKG3bWxsAJfhPVa3Mu23g==&uniplatform=NZKPT&language=CHS), 赵佳琦; 张迪; 周勇; **陈思霖**; 唐嘉澜; 姚睿. (CCF-T2)
- **[电子学报, 2021]** [基于弱语义注意力的遥感图像可解释目标检测](https://kns.cnki.net/kcms2/article/abstract?v=2Z_8GvOTliWJXRBpzMn5rJLaErJ_3a4jRYTL_LTQ5yIB-lw4E6oiOSC83CSnVxd-0_jO1LnpuAVLLMhVMSs2C2CCL1trIxtsV6N8xRnSrMajMzuOW2WG1oorJkzeqpB7uisWhBOJEYXxQplAxArUODG4x3DiFRpNENiuPcre8mHUABV9WyoPJw==&uniplatform=NZKPT&language=CHS), 周勇; **陈思霖**; 赵佳琦; 张迪; 王瀚正. (CCF-T1)
- **[自动化学报, 2020]** [基于可解释注意力部件模型的行人重识别方法](https://kns.cnki.net/kcms2/article/abstract?v=2Z_8GvOTliX0_Qlr2udCG_FEbYikpAPgAyKNhRBy21RPse0P_qg3kFflzU6Nzywf3zL63xZbV6jw-58XwxUwksmxiXM4SXtonDchnDVDunCJVWq6wRiPCt-e1Dq64SOKMEujSlqf-AJV-kSwx6ZqUBVfAsNK8PXnMZ92CeIPn1FFcaDrnUlEQg==&uniplatform=NZKPT&language=CHS), 周勇; 王瀚正; 赵佳琦; 陈莹; 姚睿; **陈思霖**. (CCF-T1)



# 🙏 Preprints
- [FedDyMem: Efficient Federated Learning with Dynamic Memory and Memory-Reduce for Unsupervised Image Anomaly Detection](https://arxiv.org/pdf/2502.21012), **Silin Chen**, Kangjian Di, Yichu Xu, Han-Jia Ye, Wenhan Luo, Ningmu Zou.
- [Texture-AD: An Anomaly Detection Dataset and Benchmark for Real Algorithm Development](https://arxiv.org/pdf/2409.06367), Tianwu Lei, Bohan Wang, **Silin Chen**, Shurong Cao, Ningmu Zou.


# 📧 Contact

- silin.chen[at]smail[dot]nju[dot]edu[dot]cn
- silin.chen[at]cumt[dot]edu[dot]cn
- silin.sherwin.chen[at]outlook[dot]com
- silin.sherwin.chen[at]gmail[dot]com

***


<font color=gray size=3 face="KAI">问到何时葡萄先熟透 我要静候 再静候 就算失收 始终要守</font>