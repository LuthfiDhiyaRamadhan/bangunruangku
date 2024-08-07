import streamlit as st
from math import pi

st.set_page_config(page_title="Bangun Ruang", layout="wide")

st.title("Kalkulator Bangun Ruang")
st.write("Pilih bangun ruang yang ingin Anda hitung:")

bangun_ruang = st.selectbox(
    "Pilih Bangun Ruang",
    ["Kubus", "Balok", "Bola", "Kerucut", "Tabung", "Limas Segiempat", "Prisma Segitiga"]
)

def kubus(sisi):
    volume = sisi ** 3
    luas_permukaan = 6 * (sisi ** 2)
    return volume, luas_permukaan

def balok(p, l, t):
    volume = p * l * t
    luas_permukaan = 2 * (p*l + p*t + l*t)
    return volume, luas_permukaan

def bola(jari_jari):
    volume = 4/3 * pi * jari_jari ** 3
    luas_permukaan = 4 * pi * jari_jari ** 2
    return volume, luas_permukaan

def kerucut(jari_jari, tinggi):
    volume = 1/3 * pi * jari_jari ** 2 * tinggi
    luas_permukaan = pi * jari_jari * (jari_jari + (tinggi ** 2 + jari_jari ** 2) ** 0.5)
    return volume, luas_permukaan

def tabung(jari_jari, tinggi):
    volume = pi * jari_jari ** 2 * tinggi
    luas_permukaan = 2 * pi * jari_jari * (jari_jari + tinggi)
    return volume, luas_permukaan

def limas_segiempat(s, tinggi):
    volume = 1/3 * s ** 2 * tinggi
    luas_permukaan = s ** 2 + 2 * s * (s ** 2 / 4 + tinggi ** 2) ** 0.5
    return volume, luas_permukaan

def prisma_segitiga(a, t_alas, tinggi):
    volume = 1/2 * a * t_alas * tinggi
    luas_permukaan = a * t_alas + 2 * a * tinggi + 2 * t_alas * tinggi
    return volume, luas_permukaan

if bangun_ruang == "Kubus":
    sisi = st.number_input("Sisi Kubus", min_value=0.0, step=1.0)
    if st.button("Hitung"):
        volume, luas_permukaan = kubus(sisi)
        st.write(f"Volume: {volume}")
        st.write(f"Luas Permukaan: {luas_permukaan}")

elif bangun_ruang == "Balok":
    p = st.number_input("Panjang", min_value=0.0, step=1.0)
    l = st.number_input("Lebar", min_value=0.0, step=1.0)
    t = st.number_input("Tinggi", min_value=0.0, step=1.0)
    if st.button("Hitung"):
        volume, luas_permukaan = balok(p, l, t)
        st.write(f"Volume: {volume}")
        st.write(f"Luas Permukaan: {luas_permukaan}")

elif bangun_ruang == "Bola":
    jari_jari = st.number_input("Jari-jari Bola", min_value=0.0, step=1.0)
    if st.button("Hitung"):
        volume, luas_permukaan = bola(jari_jari)
        st.write(f"Volume: {volume}")
        st.write(f"Luas Permukaan: {luas_permukaan}")

elif bangun_ruang == "Kerucut":
    jari_jari = st.number_input("Jari-jari Kerucut", min_value=0.0, step=1.0)
    tinggi = st.number_input("Tinggi Kerucut", min_value=0.0, step=1.0)
    if st.button("Hitung"):
        volume, luas_permukaan = kerucut(jari_jari, tinggi)
        st.write(f"Volume: {volume}")
        st.write(f"Luas Permukaan: {luas_permukaan}")

elif bangun_ruang == "Tabung":
    jari_jari = st.number_input("Jari-jari Tabung", min_value=0.0, step=1.0)
    tinggi = st.number_input("Tinggi Tabung", min_value=0.0, step=1.0)
    if st.button("Hitung"):
        volume, luas_permukaan = tabung(jari_jari, tinggi)
        st.write(f"Volume: {volume}")
        st.write(f"Luas Permukaan: {luas_permukaan}")

elif bangun_ruang == "Limas Segiempat":
    s = st.number_input("Sisi Alas", min_value=0.0, step=1.0)
    tinggi = st.number_input("Tinggi Limas", min_value=0.0, step=1.0)
    if st.button("Hitung"):
        volume, luas_permukaan = limas_segiempat(s, tinggi)
        st.write(f"Volume: {volume}")
        st.write(f"Luas Permukaan: {luas_permukaan}")

elif bangun_ruang == "Prisma Segitiga":
    a = st.number_input("Alas Segitiga", min_value=0.0, step=1.0)
    t_alas = st.number_input("Tinggi Segitiga Alas", min_value=0.0, step=1.0)
    tinggi = st.number_input("Tinggi Prisma", min_value=0.0, step=1.0)
    if st.button("Hitung"):
        volume, luas_permukaan = prisma_segitiga(a, t_alas, tinggi)
        st.write(f"Volume: {volume}")
        st.write(f"Luas Permukaan: {luas_permukaan}")

st.sidebar.markdown("""
<style>
.sidebar .sidebar-content {
    background-color: #f8f9fa;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Tentang")
st.sidebar.info("""
Aplikasi ini dibuat untuk membantu menghitung volume dan luas permukaan berbagai bangun ruang.
Dibuat dengan menggunakan Streamlit.
""")

st.sidebar.title("Kontak")
st.sidebar.info("""
Anda dapat menghubungi pembuat aplikasi ini melalui email: [luthfidhiyar16@gmail.com](mailto:eluthfidhiyar16@gmail.com)
""")
