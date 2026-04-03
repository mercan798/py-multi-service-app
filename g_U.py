import gradio as gr
from weather_api import get_weather
from currency_api import currency
from crypto_api import crypto

css = open("style.css").read()

with gr.Blocks() as demo:
    gr.Markdown("# Weather, Currency and Crypto Info App")

    with gr.Tab("Weather Info"):
        city = gr.Textbox(label="Enter City Name")
        button = gr.Button("Get Weather Info")
        output = gr.Textbox(label="Weather Information", lines=5)
        button.click(fn=get_weather, inputs=city, outputs=output)

    with gr.Tab("Currency Info"):
        button2 = gr.Button("Get Currency Info")
        output2 = gr.Textbox(label="Currency Information", lines=5)
        button2.click(fn=currency, inputs=None, outputs=output2)

    with gr.Tab("Crypto Info"):
        button3 = gr.Button("Get Crypto Info")
        output3 = gr.Textbox(label="Crypto Information", lines=5)
        button3.click(fn=crypto, inputs=None, outputs=output3)

demo.launch(css=css, share=True, footer_links=[], inbrowser=True, show_error=True)
