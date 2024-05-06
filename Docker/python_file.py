import pandas as pd
import gradio as gr

def load_data():
    df = pd.read_csv("pyspark_data.csv")
    return df.to_html()  # Convert DataFrame to HTML for nicer display

def main():
    iface = gr.Interface(fn=load_data, inputs=[], outputs="html", title="Display DataFrame")
    # Launch with explicit settings to listen on all interfaces and use port 7860
    iface.launch(server_name='0.0.0.0', server_port=7860)

if __name__ == "__main__":
    main()
