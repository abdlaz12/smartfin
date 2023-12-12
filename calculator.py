import math
import streamlit as st

data_history=[]

def penjumlahan(num1, num2):
    return num1+num2


def pengurangan(num1, num2):
    return num1-num2


def perkalian(num1, num2):
    return num1*num2


def perpangkatan(num1, num2):
    return num1**num2


def pembagian(num1, num2):
    return num1/num2


def akar_kuadrat(num):
    return math.sqrt(num)

def akar(num1, num2):
    return num1**(1/num2)



def budgeting():
    Budget=st.number_input('Put your budget')
    Count=st.button('My Budget')
    if Count:
        budget11=Budget*0.5
        st.write("This is for live", budget11)
        budget22=(Budget*0.5)-(Budget*0.2)
        st.write("This is for fun", budget22)
        budget33=(Budget*0.5)-(Budget*0.3)
        st.write("This is for my future", budget33)



def calculation():
    def calc(x):
        try:
            return eval(x)
        except:
            pass

    a=st.text_input('Hitung uang kamu di sini',placeholder='contoh 2*(5/2)')
    if a:
        result=calc(a)
        st.write('Jawaban')
        if result==None:
            st.error(result)
        else:
            st.success(result)
            data_history.append([a, result])
    else :
        st.write('Jawaban')
        st.text_input('', label_visibility='collapsed', disabled=True)



