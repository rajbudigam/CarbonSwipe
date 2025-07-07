---
title: "A Lightweight Pipeline for Measuring Energy, Carbon, and Water Costs of Large Language Models"
tags:
  - Python
  - AI
  - sustainability
  - energy
  - LLM
authors:
  - name: "Jasraj Budigam"
affiliation: 1
affiliations:
  - name: "Indus International School, Hyderabad"
    index: 1
date: 6 July 2025
bibliography: paper.bib

---

# Summary

Large language model (LLM) queries consume electricity. A single prompt to a state-of-the-art model can use a few watt-hours of energy, roughly an order of magnitude more than a typical web search [@deVries:2023; @Jegham:2025]. While the carbon cost of training large models has been studied [@Strubell:2019], the energy used during everyday model use is now a major concern [@Jegham:2025].

We present **CarbonSwipe**, an open source pipeline to measure the energy, CO$_2$, and water used by LLM inference on consumer hardware. CarbonSwipe monitors power usage during each model query and converts it into equivalent carbon emissions and water usage. We demonstrate it on a 7B model running on a laptop. In our tests, each query consumed about 0.38 Wh of energy (0.27 g CO$_2$ and 0.7 mL of water). We found that output length and complexity had a much greater effect on energy use than input length; for example, code-generation or instruction prompts used about 2 to 3 times more energy than casual chat. Our results suggest that widespread on-device AI use could produce carbon emissions comparable to those from large data centers. To encourage transparency, we propose an “AI Carbon Receipt” that reports the footprint of each query to users. CarbonSwipe provides a way to generate per-query environmental impact reports.

# Statement of Need

AI models are being integrated into everyday applications, but their environmental costs are largely invisible to users and policymakers. The inference phase can dominate the total carbon footprint of AI services as usage scales up [@Jegham:2025]. Yet AI providers rarely disclose energy or emissions metrics [@Laranjeira:2024]. This lack of information makes it difficult for users or regulators to gauge the environmental impact of AI services.

Despite the importance of usage-phase emissions, accessible tools for measuring them are lacking. Existing trackers like *CarbonTracker* [@Anthony:2020] focus on estimating the carbon footprint of model training or large-scale cloud operations. They do not provide a simple way for an end-user or researcher to measure the energy of a single AI query on local hardware. **CarbonSwipe** addresses this gap. It enables researchers, developers, and even end-users to quantify the per-query energy, carbon, and water footprint of running an LLM on a personal device. This can support greener model development by highlighting inefficiencies. By making inference costs visible, CarbonSwipe can help promote more sustainable and accountable AI usage.

#Acknowledgements

We thank the developers of the CodeCarbon project and the creators of the Mistral-7B model and GPTQ technique for enabling this work. We also appreciate the broader open source community for their support.

#References

<!-- Trigger workflow -->
 

