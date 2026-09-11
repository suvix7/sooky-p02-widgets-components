import streamlit as st
import pandas as pd
import datetime
import time
from PIL import Image
import matplotlib.pyplot as plt

st.write(
    "# 🤯 1. Nadpis (Title)"
)

st.title("Moja aplikacia s Widgetmi a komponentami")

st.write(
    "# 🔠 2. Text (Text)"
)

st.write("Toto je klasicky test")


st.write(
    "# ▶️ 3. Tlačidlo (Button)"
)

if st.button("Klikni na mna"):
    st.write("Si klikol na tlacidlo")

st.write(
    "# 🛝 4. Posuvník (slider)"
)

cislo = st.slider("Vyber cislo", 0, 100, 50)
st.write(f"Vybrali ste cislo {cislo}")


st.write(
    "# ✍ 5. Textový vstup (Text Input)"
)

meno = st.text_input("Zadajte svoje meno: ")
st.write(f"Ahoj, {meno}")

st.write(
    "# ☑️ 6. Zaškrtávacie políčko. (Checkbox)"
)

akcia = st.checkbox("Zobrazit text")
if akcia:
    st.write("Text je zobrazeny")

st.write(
    "# 🔽 8. Rozbaľovací zoznam s možnosťami. (Selectbox)"
)

volba = st.selectbox("Vyberte moznost: ", ["Moznost 1", "Moznost 2", "Moznost 3"])
st.write(f"Vybrali ste: {volba}")

st.write(
    "# 📁 9. Upload súborov. (File uploader)"
)

subor = st.file_uploader("Nahrajte subor")
if subor is not None:
    st.write("Subor nahrany!")

st.write(
    "# 🔥 10. Upload CSV súborov. (File CSV uploader)"
)

upload_subor = st.file_uploader("Nahrajte CVS subor: ", type="csv")
if upload_subor is not None:
    df = pd.read_csv(upload_subor)    
    st.write("Subor nahrany!")
    st.dataframe(df)

st.write(
    "# 🏁 11. Upload obrázkov. (File image uploader)"
)

upload_obr = st.file_uploader("Nahrajte obrazok: ", type=["jpg", "png"])
if upload_obr is not None:
    obrazok = Image.open(upload_obr)
    st.image(obrazok, caption = "Nahrany obrazok", use_container_width=True)

st.write(
    "# 📥 12. Tlačidlo na stiahnutie. (Download button)"
)

# Konvertovanie pandas dataframe do CSV
try:
    csv = df.to_csv(index=False)
    st.download_button(
        label="Stiahnut CSV", 
        data=csv, 
        file_name="filmy.csv", 
        mime="text/csv"
        )
except:
    st.write("Nic na stiahnutie!")

st.write(
    "# 📻 13. Výber jednej možnosti. (Radio)"
)

volba = st.radio("Valaszd ki a kedvenc gyikodat: ", ("Fürge gyík","Hidasgyík","Baziliszkusz gyík"))
if volba == "Fürge gyík":
    obr1 = Image.open("data/furgegyik.jpg")
    st.image(obr1, caption = "Fürge gyík", use_container_width=True)
elif volba == "Hidasgyík":
    obr1 = Image.open("data/Hidasgyik.jpg")
    st.image(obr1, caption = "Hidasgyík", use_container_width=True)
else:
    obr1 = Image.open("data/Baziliszkuszgyik.jpg")
    st.image(obr1, caption = "Baziliszkusz gyík", use_container_width=True)

vybrane_moznosti = st.multiselect(
    "Vyberte svoje oblubene filmy",
    ["Matrix","Pan prstenov","Star Wars","Inception"],
    placeholder="Vyberte film, ktory sa vam paci"
)

st.write(f"Vybrali ste: {', '.join(vybrane_moznosti)}")

st.write(
    "# 📅 14. Výber dátumu. (Date input)"
)

datum = st.date_input(
    "Vyberte datum",
    datetime.datetime.now()
    #datetime.date(2026,5,31)
)
st.write("Vybrali ste datum: ", datum)

st.write(
    "# 🕔 15. Výber času. (Time input)"
)

cas = st.time_input(
    "Zadajte cas",
    datetime.time(10,30,30)
)
st.write("Vybrali ste cas: ", cas)


st.write(
    "# 🅰 16. Vstup dlhšieho textu. (Text area)"
)

text = st.text_area(
    "Napiste svoj nazor na film",
    "Zadajte text sem"
)
st.write("Vas nazor je: ", text)


st.write(
    "# 🔢 17. Vstup číselnej hodnoty. (Number Input)"
)
hodnotenie = st.number_input(
    "Zadajte hodnotenie filmy (od 1 do  10)",
    min_value=1,
    max_value=10,
    value=5,
)
st.write(f"Vase hodnotenie {hodnotenie}/10")


st.write(
    "# 🎚️ 18. Posuvník s výberom. (Select Slider)"
)
stupnica = st.select_slider(
    "Ako velmi sa vam pacil film?",
    options=["Hrozne","Slabe","Priemerne","Dobre","Vyborne"],
    value="Dobre"
)
st.write(f"Vase hodnotenie {stupnica}")

st.write(
    "# 🔴 19. Výber farby (Color picker)"
)
farba= st.color_picker(
    "Vyberte farbu pozadia",
    "#00F900"
)
st.write(f"Vasa farba {farba}")


st.write(
    "# ⏳ 20. Indikátor progresu (Progress)"
)
progress = st.progress(0)

# for i in range(100):
#     time.sleep(0.05)
#     progress.progress(i+1)


st.write(
    "# 📐 21. Zobrazenie LaTeXu (matematické výrazy) (latex)"
)
st.latex(r'''
    a^2 + b^2 = c^2
''')


st.write(
    "# 🌍 22. Zobrazenie kódu s formátovaním (code)"
)
st.code('''
def ahoj():
    print("Ahoj, Streamlit!")
''', language='python')


st.write(
    "# 🌐 23. Zobrazenie JSON dát (json)"
)
data = {
    'meno': 'Peter',
    'vek': 30,
    'zamestnanie': 'programator'
}
st.json(data)


st.write(
    "# ➡️ 24. Dynamický widget (všestranný) (write)"
)
st.write("Text")
st.write(123)
st.write({'kluc':'hodnota'})


st.write(
    "# 📏 25. Zobrazenie kľúčových metrik (metric)"
)
st.metric(label="Teplota", value="24℃", delta="-2℃")


st.write(
    "# ❌ 26. Zobrazenie chybovej správy (error)"
)
st.error("Chybove hlasenie!")


st.write(
    "# ✅ 27. Zobrazenie úspešnej správy (success)"
)
st.success("Uspech!")


st.write(
    "# ⚠️ 28. Zobrazenie varovnej správy (warning)"
)
st.warning("Varovanie!")


st.write(
    "# 🆗 29. Zobrazenie informatívnej správy (info)"
)
st.info("Informacia.")



st.write(
    "# ❗ 30. Zobrazenie výnimky (chyby v kóde) (exception)"
)
try:
    1/0
except ZeroDivisionError as e:
    st.exception(e)


st.write(
    "# 🌀 31. Zobrazenie spinneru počas načítavania (spinner)"
)
with st.spinner('Cakajte prosim...'):
    time.sleep(5)
st.success('Hotovo')


st.write(
    "# 📝 32. Zobrazenie textovej poznámky (caption)"
)
st.caption("Toto je vysvetlenie")


st.write(
    "# 🖼️ 33. Zobrazenie obrázkov (image)"
)
st.image("https://ng.24.hu/uploads/2018/11/6669f569c5a49865541630331527608-1058x705.jpg")


st.write(
    "# 🎞️ 34. Zobrazenie videa/audio (video/audio)"
)
st.video("https://www.youtube.com/watch?v=5Aep2ZFLSIo&t=51s")


st.write(
    "# 🏛️ 35. Rozdelenie obrazovky do stĺpcov (columns)"
)
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Stlpec 1")
with col2:
    st.write("Stlpec 2")
with col3:
    st.write("Stlpec 3")


st.write(
    "# 📑 36. Vytváranie záložiek/tabov (tabs)"
)
tab1, tab2, tab3 = st.tabs(["Tab 1","Tab 2","Tab 3"])
with tab1:
    st.write("Obsah pre zalozku 1")
with tab2:
    st.write("Obsah pre zalozku 2")
with tab3:
    st.write("Obsah pre zalozku 3")

st.write(
    "# 🚀 37. Rozbalovací blok (expander)"
)
with st.expander("Kliknite sem pre viac info"):
    st.write("Toto je rozbaleny obsah.")


st.write(
    "# 📈 38. Zobrazenie grafov v Matplotlib (pyplot)"
)
fig, ax = plt.subplots()
ax.plot([1,2,3,4],[1,4,9,16])

st.pyplot(fig)
