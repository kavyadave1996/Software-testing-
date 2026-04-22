# 🧪 Software Testing Project - Summer 2025
Technische Universität Hamburg (TUHH)  Institute of Software Technology and Systems (STS)

## 📋 Project Overview

This repository contains the software testing suite. Applying various testing methodologies to a Python project with at least 10,000 lines of code and an existing `pytest` infrastructure.

## 🛠️ Environment Setup

### 1. Conda Installation
We use Conda to isolate dependencies and avoid conflicts between different Python versions.
- **Create Environment:** `conda create --name <myenv> python=3.9`
- **Activate Environment:** `conda activate <myenv>` 
-**Install Packages:** `pip install hypothesis pytest` (and other required tools)

### 2. LLM Tools (Local AI)
For AI Review tasks, we utilize Large Language Models locally.
- **Ollama:** Lightweight CLI tool (Recommended model: `deepseek-r1:7b`).
- **LM Studio:** GUI for model management on Windows/Linux/macOS].
---

## 📂 Repository Structure
The project must follow this specific directory layout to be successfully evaluated:

```text
group-xx/
├── task-1-random/        # Phase 1: Random Testing (Hypothesis)
│   ├── tests (*.py)       # Individual test implementations
│   ├── ai-assistance.pdf  # LLM test suite comparison 
│   └── documentation.pdf  # Results and screenshots 
├── task-2-isp/           # Phase 2: Input Space Partitioning
├── task-3-graph/          # Phase 3: Graph Coverage Analysis 
├── task-4-logic/          # Phase 4: Logic Coverage Criteria 
├── task-5-syntax/         # Phase 5: Mutation Testing (Uppaal) 
├── research/              # Research: ICST/ISSTA Paper Review 
├── code/                  # Project Source Code 
│   ├── original-project/  # Baseline code 
│   └── changes/           # Bug fixes/improvements
├── report.pdf             # Comprehensive project report
└── slides.pdf             # Final presentation materials 
