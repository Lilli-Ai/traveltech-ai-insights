import gradio as gr
import requests
import re
import os

AIRTABLE_TOKEN = os.environ.get("AIRTABLE_TOKEN")
BASE_ID = "appSA71cqcQenZHHY"
TABLE_NAME = "Insights"

def load_data():
    url = "https://api.airtable.com/v0/" + BASE_ID + "/" + TABLE_NAME
    headers = {"Authorization": "Bearer " + AIRTABLE_TOKEN}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        records = response.json().get("records", [])
        return [r.get("fields", {}) for r in records]
    return []

def clean_text(text):
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'[#!*\[\]]', '', text)
    text = ' '.join(text.split())
    return text[:300]

def show_dashboard():
    data = load_data()
    if not data:
        return "No insights yet. Awaiting data from n8n."
    output = ""
    for item in data:
        output += "📰 **" + str(item.get('Title', 'N/A')) + "**\n\n"
        output += "🔗 " + str(item.get('URL ', 'N/A')) + "\n\n"
        output += "📝 " + clean_text(str(item.get('Summary ', ''))) + "\n\n"
        output += "📅 " + str(item.get('Date ', 'N/A'))[:10] + "\n\n"
        output += "---\n\n"
    return output

css = """
    .gradio-container {
        background: linear-gradient(135deg, #f0f8ff 0%, #c8e6f5 50%, #a8d8f0 100%) !important;
        min-height: 100vh;
        min-width: 100% !important;
    }
    .gradio-container h2 {
        text-align: center !important;
        color: #0d4f8a !important;
        font-size: 1.5rem !important;
    }
    .tab-wrapper {
        width: 100% !important;
        justify-content: center !important;
        display: flex !important;
    }
    .tab-container {
        width: 100% !important;
        justify-content: center !important;
        display: flex !important;
    }
"""

with gr.Blocks(title="TravelTech AI Insights", css=css) as app:
    gr.Markdown("## 🌐 Automated Industry Intelligence Dashboard")

    with gr.Tabs():
        with gr.Tab("🤖 AI Assistant"):
            gr.HTML("""
            <iframe
              title="Typebot"
              src="https://typebot.co/travel-tech-ai-assistant-m9ce9ut"
              style="border: none; width: 100%; height: 600px"
            ></iframe>
            """)
        with gr.Tab("📊 Insights Dashboard"):
            output = gr.Markdown()
            refresh_btn = gr.Button("🔄 Refresh")
            refresh_btn.click(show_dashboard, outputs=output)

app.launch(server_name="0.0.0.0", server_port=7860)
