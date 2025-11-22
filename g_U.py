import gradio as gr
from weather_api import get_weather
from currency_api import currency
from crypto_api import crypto

with gr.Blocks() as demo:
    gr.Markdown("# Weather, Currency and Crypto Info App")

    with gr.Tab("Weather Info"):
        city = gr.Textbox(label="Enter City Name")
        button = gr.Button("Get Weather Info")
        output = gr.Textbox(label="Weather Information")
        button.click(fn=get_weather, inputs=city, outputs=output)

    with gr.Tab("Currency Info"):
        button2 = gr.Button("Get Currency Info")
        output2 = gr.Textbox(label="Currency Information")
        button2.click(fn=currency, inputs=None, outputs=output2)

    with gr.Tab("Crypto Info"):
        button3 = gr.Button("Get Crypto Info")
        output3 = gr.Textbox(label="Crypto Information")
        button3.click(fn=crypto, inputs=None, outputs=output3)

demo.launch(share=True)