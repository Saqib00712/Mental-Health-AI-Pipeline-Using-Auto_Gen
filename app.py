import gradio as gr
from autogen import ConversableAgent

# =========================
# OLLAMA CONFIG
# =========================

llm_config = {
    "config_list": [
        {
            "model": "llama3.2",
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama",
            "price": [0, 0]
        }
    ],
    "temperature": 0.7,
}

# =========================
# AGENTS
# =========================

emotion_agent = ConversableAgent(
    name="emotion_analysis",
    system_message=(
        "You are an emotion analysis agent.\n"
        "Extract ONLY 3–5 emotions.\n"
        "No explanations.\n"
        "No questions."
    ),
    llm_config=llm_config
)

therapy_agent = ConversableAgent(
    name="therapy_recommendation",
    system_message=(
        "You are a therapy agent.\n"
        "Give relaxation techniques based on emotions.\n"
        "Do NOT re-analyze emotions."
    ),
    llm_config=llm_config
)

# =========================
# 🔥 STRICT PIPELINE (KEY FIX)
# =========================

def run_pipeline(user_input):

    print("\n🧠 Running FULL AI Pipeline...\n")

    # STEP 1: Emotion Analysis
    emotion_output = emotion_agent.generate_reply(
        messages=[{"role": "user", "content": user_input}]
    )

    # STEP 2: Therapy Recommendation
    therapy_output = therapy_agent.generate_reply(
        messages=[{"role": "user", "content": emotion_output}]
    )

    # FINAL OUTPUT
    return f"""
🧠 EMOTION ANALYSIS
-------------------
{emotion_output}

💡 THERAPY RECOMMENDATIONS
-------------------------
{therapy_output}
"""

# =========================
# GRADIO UI
# =========================

ui = gr.Interface(
    fn=run_pipeline,
    inputs=gr.Textbox(lines=3, placeholder="How are you feeling?"),
    outputs=gr.Textbox(lines=20),
    title="🧠 Mental Health AI Pipeline (Ollama + Agents)",
    description="Strict 2-step AI pipeline: Emotion → Therapy"
)

ui.launch()
