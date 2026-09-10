import streamlit as st
import pandas as pd
import datetime
import time
from PIL import Image

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
    obr1 = Image.open("data\\furgegyik.jpg")
    st.image(obr1, caption = "Fürge gyík", use_container_width=True)
elif volba == "Hidasgyík":
    obr1 = Image.open("data\\Hidasgyik.jpg")
    st.image(obr1, caption = "Hidasgyík", use_container_width=True)
else:
    obr1 = Image.open("data\\Baziliszkuszgyik.jpg")
    st.image(obr1, caption = "Baziliszkusz gyík", use_container_width=True)

st.write(
    "# 📅 14. Výber dátumu. (Date input)"
)


st.write(
    "# 🕔 15. Výber času. (Time input)"
)



st.write(
    "# 🅰 16. Vstup dlhšieho textu. (Text area)"
)



st.write(
    "# 🔢 17. Vstup číselnej hodnoty. (Number Input)"
)



st.write(
    "# 🎚️ 18. Posuvník s výberom. (Select Slider)"
)



st.write(
    "# 🔴 19. Výber farby (Color picker)"
)



st.write(
    "# ⏳ 20. Indikátor progresu (Progress)"
)



st.write(
    "# 📐 21. Zobrazenie LaTeXu (matematické výrazy) (latex)"
)



st.write(
    "# 🌍 22. Zobrazenie kódu s formátovaním (code)"
)



st.write(
    "# 🌐 23. Zobrazenie JSON dát (json)"
)



st.write(
    "# ➡️ 24. Dynamický widget (všestranný) (write)"
)



st.write(
    "# 📏 25. Zobrazenie kľúčových metrik (metric)"
)



st.write(
    "# ❌ 26. Zobrazenie chybovej správy (error)"
)



st.write(
    "# ✅ 27. Zobrazenie úspešnej správy (success)"
)



st.write(
    "# ⚠️ 28. Zobrazenie varovnej správy (warning)"
)



st.write(
    "# 🆗 29. Zobrazenie informatívnej správy (info)"
)




st.write(
    "# ❗ 30. Zobrazenie výnimky (chyby v kóde) (exception)"
)



st.write(
    "# 🌀 31. Zobrazenie spinneru počas načítavania (spinner)"
)



st.write(
    "# 📝 32. Zobrazenie textovej poznámky (caption)"
)



st.write(
    "# 🖼️ 33. Zobrazenie obrázkov (image)"
)



st.write(
    "# 🎞️ 34. Zobrazenie videa/audio (video/audio)"
)



st.write(
    "# 🏛️ 35. Rozdelenie obrazovky do stĺpcov (columns)"
)


st.write(
    "# 📑 36. Vytváranie záložiek/tabov (tabs)"
)


st.write(
    "# 🚀 37. Rozbalovací blok (expander)"
)



st.write(
    "# 📈 38. Zobrazenie grafov v Matplotlib (pyplot)"
)

