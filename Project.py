import streamlit as st
import pandas as pd
import calculator 
import plotly.express as px


#streamlit web-link
st.set_page_config(page_title='SmartFin : Manage Your Finance', page_icon="money", layout='wide')
st.title('SmartFin  : Manage Your Finance Monthly')


#streamlit web-page
option=st.sidebar.selectbox("Needs",('Analysis', 'Budgeting',))

st.header(option)

# Analys function
if option == "Analysis":
    
    st.subheader('This is your Expense')
    uploaded_file= st.file_uploader('Choose a XLSX file', type='xlsx',)
    if uploaded_file:
        st.markdown('---')
        df=pd.read_excel(uploaded_file, 
                         engine='openpyxl',
                        )
        st.dataframe(df)
        groupby_column=st.selectbox(
            'WHAT DO YOU WANT TO ANALYIS',
            ('CATEGORY', ), 
                                     )

        # Grouping
        output_columns=['EXPANSES']
        df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()
        st.dataframe(df_grouped)

        fig=px.bar(
            df_grouped,
            x=groupby_column,
            y='EXPANSES',
            template='plotly_white'
        )
        st.plotly_chart(fig)
        


##calculator and budgeting##
#budgeting function
if option == "Budgeting":
    st.subheader('Manage your money with 50,30,20 methode')
    st.markdown('''
                Aturan 50/30/20 adalah metode budgeting pribadi bulanan yang membagi dana ke dalam tiga kategori, yaitu kebutuhan, keinginan,
                dan masa depan atau utang. Angka 50, 30, dan 20 mewakili persentase dana yang harus dialokasikan ke tiga kategori tersebut:\n
                1. 50% untuk kebutuhan, meliputi sewa atau cicilan rumah, belanja bahan masakan, utility, dan lain-lain.\n
                2. 30% untuk keinginan, mulai dari yang besar seperti travelling, hangout, sampai 
                yang kecil seperti biaya langganan streaming.\n 
                3. 20% untuk masa depan atau utang, yaitu tabungan dan investasi atau kartu kredit.\n
                '''
                )
    
#budgeting function
    st.subheader('Lets divide your money')
    calculator.budgeting()
#budgeting done


#calculator function
    st.subheader('Lets count how much money you have')
    calculator.calculation()
    df=pd.DataFrame(
            {"  Operasi Hitungan  ": ['Penjumlahan', 'Pengurangan', 'Perkalian', 'Pembagian','Perpangatan', 'Akar kuadrat', 'Akar'],
            "  Simbol Operasi  ": ['+', '-', '*','/', '**', 'math.sqrt(num)', 'akar(num1,num2)' ],
            "  Contoh Operasi  ":['1+1', '3-2', '3*7','6/2', '8**2', 'math.sqrt(81)', 'akar(7, 9)'],
            "  Hasil  ":['2','1', '21', '3', '64', '9','1.2413658170152087']
            
            }
    )
    st.dataframe(df)
#calculator done
    

    






