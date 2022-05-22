import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
import yfinance as yf


ticker_info = yf.Ticker("9984.T")
print('ticker_info')



st.title('streamlit 超入門')

st.write('プログレスバー表示')
'start'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
     latest_interation.text(f'interation {i+1}')
     bar.progress(i + 1)
     time.sleep(0.1)


'Done!!!!!!'








con = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', con

st.write('intaractive Widgets')
left_column, right_column = st.columns(2)
button =left_column.button('右カラムに文字表示')
if button:
    right_column.write('右カラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせを3')






# text = st.sidebar.text_input('あなたの趣味は？')
# 'あなたの趣味は' , text, 'です'


# option = st.selectbox('あなたの好きな数値を選んでください', 
# list(range(1, 10)))
# 'あなたの好きな数値は' , option, "です" 

#st.write('Display Image')

# if st.checkbox('Show Image'):
#    img = Image.open('IMG_0215.JPG')
#    st.image(img, caption='test' , use_column_width=True)


#
st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
    columns=['lat', 'lon']

)
st.map(df)

# st.dataframe(df.style.highlight_max(axis=0) )

st.table(df)

"""

# 翔
## test
### 父

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""
