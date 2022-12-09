import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
from kafka import KafkaConsumer
import json
consumer = KafkaConsumer('Systemx', bootstrap_servers='localhost:29092')
last_rows =  np.array([[0]])
chart = st.line_chart(last_rows)

print('ready!!')
while True:
    for message in consumer:
        consumed_message = json.loads(message.value.decode())
        data = pd.DataFrame.from_dict(consumed_message)
        data = data.to_numpy(dtype=np.int32)
        chart.add_rows(data)
        last_rows = data

