from serpapi.google_search import GoogleSearch
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def compare (med_name):
    params = {
        "engine": "google_shopping",
        "q": med_name,
        "api_key": "ea52d20ff6cc5f0cd2707b2a58485304d8de2f4f076a871a682c898d654b2baf",
        "gl": "in"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    shopping_results = results["shopping_results"]
    return shopping_results

col1, col2, col3 = st.columns(3)
col1.image("e_pharmacy.png", width=500)
col2.header("E-pharmacy price comparison system")

# """------------------------------------------"""

st.title("Enter Name Of Medicine")
med_name= st.sidebar.text_input("Enter Name Here")
number= st.sidebar.text_input("Enter Number of option here")


medicine_cmp = []
med_price = []
if med_name is not None and number is not None:
    if st.sidebar.button("price compare"):
        shopping_results= compare(med_name)
        lowest_price = float(shopping_results[0].get('price')[1:].replace(',', ''))
        print(lowest_price)
        lowest_price_index = 0
        st.sidebar.image(shopping_results[0].get('thumbnail'))


        for i in range(int(number)):
            current_price = float((shopping_results[i].get('price'))[1:].replace(',', ''))
            medicine_cmp.append(shopping_results[i].get('source'))
            med_price.append(float((shopping_results[i].get('price'))[1:].replace(',', '')))

            # ------------------------------------------------------------------------------

            st.title(f" option {i+1}")

            col1, col2, = st.columns(2)
            col1.write("Company:")
            col2.write(shopping_results[i].get('source'))

            col1.write("Title:")
            col2.write(shopping_results[i].get('title'))

            col1.write("Price:")
            col2.write(shopping_results[i].get('price'))

            url = shopping_results[i].get('product_link')
            col1.write = ('Buy Link')
            col2.write = ('[Link] (%s)' %url)

        if (current_price < lowest_price):
            lowest_price = current_price
            lowest_price_index = i

            # this is the best option

            st.title("best option")

            col1, col2, = st.columns(2)
            col1.write("Company:")
            col2.write(shopping_results[lowest_price_index].get('source'))

            col1.write("Title:")
            col2.write(shopping_results[lowest_price_index].get('title'))

            col1.write("Price:")
            col2.write(shopping_results[lowest_price_index].get('price'))

            url = shopping_results[lowest_price_index].get('product_link')
            col1.write = ('Buy Link')
            col2.write = ('[Link] (%s)' % url)

#-------------------------------------------------------------------------------------------
# graphs Comparison

            df = pd.DataFrame(med_price,medicine_cmp)
            st.title("Chart Comparison")
            st.bar_chart(df)

        fig, ax = plt.subplots()
        ax.pie(med_price, labels= medicine_cmp, shadow=True)
        ax.axis("equal")
        st.pyplot(fig)




