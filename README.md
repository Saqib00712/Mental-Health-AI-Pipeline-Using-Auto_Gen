# Mental Health AI Pipeline
> A strict 2-step multi-agent pipeline that analyzes emotions from user input and recommends personalized therapy techniques — powered by AutoGen, Llama 3.2 (via Ollama), and a Gradio web interface. Runs completely locally with zero API costs.

---

## What This Project Does

You describe how you're feeling in plain English. Two specialized AI agents work in sequence:

```
Your feelings (text input)
        ↓
[Emotion Agent] — extracts 3-5 emotions from your message
        ↓
[Therapy Agent] — recommends relaxation techniques based on those emotions
        ↓
Final Output displayed in clean Gradio UI
```

The pipeline is **strict** — the Therapy Agent never re-analyzes emotions. It only receives the emotion output and generates targeted recommendations.

---

## Demo

**Input:**
```
I've been feeling overwhelmed at work, can't sleep properly,
and I keep snapping at people I care about.
```

**Output:**
```
🧠 EMOTION ANALYSIS
-------------------
1. Anxiety
2. Exhaustion
3. Frustration
4. Irritability
5. Stress

💡 THERAPY RECOMMENDATIONS
-------------------------
Based on these emotions, here are some relaxation techniques:

1. Box Breathing (4-4-4-4) — for anxiety and stress
2. Progressive Muscle Relaxation — for physical tension and exhaustion
3. Journaling — to process frustration before it affects relationships
4. Sleep hygiene routine — 30 min wind-down with no screens
5. Brief mindfulness walk — 10 minutes to reset irritability
```

---

## Architecture

```
User Input (Gradio Textbox)
        ↓
emotion_agent.generate_reply(user_input)
        → extracts 3-5 emotions only
        → no explanations, no questions
        ↓
therapy_agent.generate_reply(emotion_output)
        → recommends techniques based on emotions
        → does NOT re-analyze input
        ↓
Combined Output (Gradio Textbox)
```

Both agents run locally using **Llama 3.2 via Ollama** — no data is sent to external servers.

---

## Agents

| Agent | Role | System Prompt Behavior |
|-------|------|----------------------|
| **Emotion Analysis Agent** | Identifies emotions from user text | Returns ONLY 3-5 emotions, no explanations |
| **Therapy Recommendation Agent** | Suggests relaxation techniques | Uses emotion output only, never re-analyzes |

The `system_message` for each agent enforces strict behavior — preventing the common problem of agents going off-task or repeating work.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![AutoGen](https://img.shields.io/badge/AutoGen-ConversableAgent-purple?style=flat-square)
![Ollama](https://img.shields.io/badge/Ollama-Llama%203.2-black?style=flat-square)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange?style=flat-square)

- **AutoGen** — `ConversableAgent` for building specialized AI agents
- **Llama 3.2** (via Ollama) — local LLM, completely free to run
- **Gradio** — clean web UI for user interaction
- **Python 3.11** — core language

---

## Project Structure

```
Mental-Health-AI-Pipeline/
│
├── app.py                  # Main pipeline and Gradio UI
├── requirements.txt        # All dependencies
└── README.md
```

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Saqib00712/Mental-Health-AI-Pipeline.git
cd Mental-Health-AI-Pipeline
```

### 2. Install Ollama and pull Llama 3.2 (runs locally — completely free)
```bash
# Download Ollama from https://ollama.com
ollama pull llama3.2
ollama serve    # starts local server on http://localhost:11434
```

### 3. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

### 5. Open your browser
```
http://127.0.0.1:7860
```
Type how you're feeling and get instant emotion analysis + therapy recommendations.

---

## Key Concepts Covered

- **ConversableAgent** — AutoGen's core agent class with custom `system_message` and `llm_config`
- **Strict pipeline design** — enforcing agent boundaries using system prompts to prevent task overlap
- **generate_reply()** — calling each agent individually and passing outputs as inputs to the next
- **Local LLM configuration** — connecting AutoGen to Ollama's OpenAI-compatible endpoint
- **Gradio Interface** — building a simple, clean web UI with `gr.Interface`
- **Sequential multi-agent flow** — chaining agents without using a crew or graph framework
- **Zero-cost inference** — `"price": [0, 0]` config for local model with no token billing

---

## Why Local LLM?

This project uses **Llama 3.2 locally via Ollama** — which means:
- **No API costs** — completely free to run
- **Full privacy** — sensitive mental health input never leaves your machine
- **Works offline** — no internet connection required after setup

---

## Responsible AI Note

This project is for **educational and demonstration purposes only**. It is not a substitute for professional mental health support. If you are experiencing serious mental health concerns, please reach out to a qualified professional or a crisis helpline in your region.

---

## Related Certifications

Built as part of the IBM **Building AI Agents and Agentic Workflows Specialization** and **Agentic AI with LangGraph, CrewAI, AutoGen and BeeAI** on Coursera.

[![IBM Badge](https://img.shields.io/badge/IBM-AI%20Agents%20Specialization-blue?style=flat-square)](https://www.credly.com/users/muhammad-saqib.361f9b8c)
[![IBM Badge](https://img.shields.io/badge/IBM-AutoGen%20%26%20BeeAI-blue?style=flat-square)](https://www.credly.com/users/muhammad-saqib.361f9b8c)

---

## Author

**Muhammad Saqib**
- GitHub: [@Saqib00712](https://github.com/Saqib00712)
- LinkedIn: [muhammad-saqib](https://www.linkedin.com/in/muhammad-saqib-68b9b3374/)
- Email: saqibkhosa649@gmail.com
- Credly: [15x IBM Certified](https://www.credly.com/users/muhammad-saqib.361f9b8c)
