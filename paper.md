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

# Installation and Quick Start

You can install CarbonSwipe directly from GitHub:

```bash
pip install git+https://github.com/rajbudigam/CarbonSwipe.git
```
Once you have installed it, you can measure the energy, carbon, and water footprint of a single prompt with just a few lines of code:

```python
from carbonswipe import CarbonTracker

tracker = CarbonTracker(model_path="mistral7b_q4.bin", device="cuda")
energy, co2, water = tracker.measure("Hello, world!")
print(f"Energy: {energy:.4f} kWh, CO2: {co2:.2f} g, Water: {water:.2f} mL")
```

# Functionality

CarbonSwipe provides a programmatic interface to monitor and report resource usage during local AI model inference. It works with any model that runs locally, including large models optimized by quantization [@Dettmers:2022]. Its core functionality includes:
- Energy Monitoring: Monitors power draw during model inference using the CodeCarbon library [@CodeCarbon:2022]. It accounts for CPU/GPU power use and uses estimates if direct sensor data are unavailable.
- Emissions and Water: After measuring energy, the tool converts it into equivalent CO$_2$ emissions and water usage. This uses configurable conversion factors (by default around 0.709 kg CO$_2$/kWh and 1.8 L/kWh) [@Shehabi:2018].
-Reporting: After each prompt, it outputs an “AI Carbon Receipt” summarizing the energy, CO$_2$, and water used. Results can be shown in the console or saved to a file. The tool can also aggregate statistics over multiple runs for analysis.

# Implementation

CarbonSwipe is a Python tool designed for simplicity and reproducibility. It uses the CodeCarbon toolkit [@CodeCarbon:2022] to read hardware power sensors and estimate energy use. During each model inference, CarbonSwipe integrates the power measurements over time to compute total energy (E). It subtracts the system’s idle baseline to isolate the model’s actual consumption and then multiplies E by the specified conversion factors to calculate the CO$_2$ emissions and water usage. These factors are user-configurable to accommodate different grid mixes and conditions.

# Validation

For several test queries, CarbonSwipe’s reported energy use was within about 5% of external meter measurements. The tool’s power monitoring approach is reasonably accurate. The CO$_2$ and water values it calculates also align with manual computations using the same conversion factors. CarbonSwipe’s output is reliable for practical use.

# Usage Example

We used CarbonSwipe to profile a local LLM on a consumer-grade laptop. In our test, a 7B-parameter model (Mistral-7B) quantized to 4-bit was run on 150 diverse prompts. The energy per query ranged from about 0.07 Wh for the simplest prompt up to nearly 1 Wh for the most complex output. On average, a query consumed roughly 0.38 Wh (0.27 g CO$_2$ and 0.7 mL of water). Tasks such as code generation or long instructional responses used significantly more energy than short conversational answers. Notably, this per-query footprint on local hardware is comparable to reported values for large cloud models (around 0.3 to 0.4 Wh [@Jegham:2025]). This suggests that if many users run LLMs on personal devices, the aggregate energy use could approach that of a data center.

# Acknowledgements

We thank the developers of the CodeCarbon project and the creators of the Mistral-7B model and GPTQ technique for enabling this work. We also appreciate the broader open source community for their support.

# References

