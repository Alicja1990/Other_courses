import pandas as pd
import gradio as gr

def load_data():
    df = pd.read_csv("pyspark_data.csv")
    return df.to_html()  # Convert DataFrame to HTML for nicer display

def main():
    iface = gr.Interface(fn=load_data, inputs=[], outputs="html", title="Display DataFrame")
    iface.launch()

if __name__ == "__main__":
    main()
