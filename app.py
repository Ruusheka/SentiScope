import gradio as gr
from transformers import pipeline

# Load sentiment analysis model
sentiment = pipeline("sentiment-analysis")

def analyze(text):
    if not text.strip():
        return {"display": "", "percentage": "", "color": "#FFFFFF", "icon": ""}
    
    result = sentiment(text)[0]
    label = result['label']
    score = round(result['score'] * 100, 2)
    
    if label == "POSITIVE":
        return {
            "display": "Positive",
            "percentage": f"{score}%",
            "color": "#ffeaa7",  # Changed to golden yellow
            "icon": "😊"
        }
    else:
        return {
            "display": "Negative",
            "percentage": f"{score}%",
            "color": "#ffeaa7",  # Changed to golden yellow
            "icon": "😞"
        }

custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Playfair+Display:wght@700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&display=swap');
:root, body, .gradio-container {
    overflow: hidden !important;
    font-family: 'Poppins', sans-serif;
}
.rose-card {
    width: 550px;
    height: 650px;
    margin: auto;
    padding: 25px;
    border-radius: 20px;
    background: linear-gradient(145deg, #3a1a2f, #5a2a3f);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    color: #fff1f2;
    transition: all 0.3s ease;
    overflow: hidden;
    border: 1px solid #ff6b8b55;
    display: flex;
    flex-direction: column;
    position: relative;
}
.rose-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
}
.title-container {
    text-align: center;
    margin-bottom: 15px;
    flex-shrink: 0;
    position: relative;
}
.title {
    font-size: 36px;
    font-weight: 900;
    color: #ffeaa7;  /* Changed to golden yellow */
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    animation: fadeIn 0.8s ease-out;
    font-family: 'Dancing Script', cursive;
    margin: 10px 0;
    visibility: visible !important;
}
.clear-icon {
    position: absolute;
    top: 2px;
    right: 5px;
    background: rgba(255, 255, 255, 0.1);
    border: none;
    color: #ffeaa7;  /* Changed to golden yellow */
    font-size: 18px;
    cursor: pointer;
    transition: all 0.3s ease;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transform: scale(0.8);
}
.clear-icon:hover {
    background: rgba(255, 255, 255, 0.2);
    color: #ffb7c5;
    transform: scale(1);
}
.clear-icon.visible {
    opacity: 1;
    transform: scale(1);
}
.content {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}
.percentage-container {
    perspective: 1000px;
    margin: 10px 0;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.percentage-display {
    font-size: 64px;
    font-weight: 600;
    text-align: center;
    padding: 15px;
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.08);
    transform-style: preserve-3d;
    animation: flipIn 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
    margin: 10px 0;
    font-family: 'Poppins', sans-serif;
    letter-spacing: 2px;
    color: #ffeaa7;  /* Changed to golden yellow */
}
.sentiment-label {
    font-size: 22px;
    text-align: center;
    margin-top: 8px;
    animation: slideUp 0.5s ease-out 0.3s both;
    font-weight: 400;
    font-family: 'Playfair Display', serif;
    letter-spacing: 0.5px;
    color: #ffeaa7;  /* Changed to golden yellow */
}
.emoji {
    font-size: 40px;
    display: inline-block;
    animation: bounce 0.8s ease infinite alternate;
    margin-right: 10px;
    vertical-align: middle;
}
.button-row {
    flex-shrink: 0;
    margin-top: auto;
    padding-top: 15px;
    justify-content: center;
}
.animated-button {
    background: linear-gradient(45deg, #ff6b8b, #d23369);
    color: white;
    border: none;
    padding: 12px 28px;
    border-radius: 50px;
    font-size: 15px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(210, 51, 105, 0.3);
    margin: 8px;
    animation: pulse 2s infinite;
    font-family: 'Poppins', sans-serif;
    letter-spacing: 0.5px;
}
.animated-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(210, 51, 105, 0.4);
    animation: none;
}
.textbox {
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid #ff6b8b55;
    color: #fff1f2;
    width: 100%;
    box-sizing: border-box;
    transition: all 0.3s ease;
    border-radius: 12px;
    padding: 14px;
    margin-bottom: 15px;
    font-family: 'Poppins', sans-serif;
    font-size: 15px;
    font-weight: 300;
}
.textbox:focus {
    border-color: #ff6b8b;
    transform: scale(1.02);
    box-shadow: 0 0 10px rgba(255, 107, 139, 0.5);
}
/* Animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes flipIn {
    0% { transform: rotateX(90deg); opacity: 0; }
    100% { transform: rotateX(0); opacity: 1; }
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes bounce {
    from { transform: translateY(0); }
    to { transform: translateY(-8px); }
}
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.03); }
    100% { transform: scale(1); }
}
@keyframes colorPulse {
    0% { text-shadow: 0 0 5px currentColor; }
    50% { text-shadow: 0 0 15px currentColor; }
    100% { text-shadow: 0 0 5px currentColor; }
}
.result-shown .percentage-display {
    animation: colorPulse 2s infinite;
}
"""

with gr.Blocks(css=custom_css) as demo:
    with gr.Column(elem_classes=["rose-card"]) as card:
        # Title container with clear icon
        with gr.Column(elem_classes=["title-container"]):
            title = gr.HTML("""<div class="title">--SentiScope--</div>""", visible=True)
            clear_icon = gr.Button("✕", elem_classes=["clear-icon"])
        
        # Main content area
        with gr.Column(elem_classes=["content"]):
            input_box = gr.Textbox(
                label="Enter your text", 
                lines=1, 
                placeholder="How are you feeling today?",
                elem_classes=["textbox"]
            )
            
            # Result container
            with gr.Column(elem_classes=["percentage-container"]):
                percentage_display = gr.HTML(visible=False)
                sentiment_label = gr.HTML(visible=False)
            
            # Buttons row
            with gr.Row(elem_classes=["button-row"]):
                analyze_btn = gr.Button("Analyze Sentiment", elem_classes=["animated-button"])
        
        def show_results(text):
            if not text.strip():
                return (
                    gr.HTML(visible=False),
                    gr.HTML(visible=False),
                    {"__type__": "update", "visible": False}
                )
            
            result = analyze(text)
            
            percentage_html = f"""
            <div class='percentage-display' style='color: {result['color']}'>
                <span class='emoji'>{result['icon']}</span>{result['percentage']}
            </div>
            """
            
            label_html = f"""
            <div class='sentiment-label' style='color: {result['color']}'>
                {result['display']} Sentiment
            </div>
            """
            
            return (
                gr.HTML(percentage_html, visible=True),
                gr.HTML(label_html, visible=True),
                {"__type__": "update", "visible": True}
            )
        
        def clear_all():
            return (
                "",
                gr.HTML(visible=False),
                gr.HTML(visible=False),
                {"__type__": "update", "visible": False}
            )
        
        analyze_btn.click(
            fn=show_results,
            inputs=input_box,
            outputs=[percentage_display, sentiment_label, clear_icon]
        )
        
        clear_icon.click(
            fn=clear_all,
            inputs=None,
            outputs=[input_box, percentage_display, sentiment_label, clear_icon]
        )

demo.launch()
