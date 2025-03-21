
import streamlit as st
import random

quiz_data = {
    "Kapittel 1: Universet og Naturvitenskapen": [
        ("Hva er en hypotese?", "En antakelse som kan testes med eksperimenter."),
        ("Hva er en hypotese?\n\n1. Salting av veier gjør at is og snø smelter.\n\n2. En brusflaske med skrukork som blir lagt i fryseren, vil sprekke.\n\n3. Svarte klær kjennes varmere på kroppen enn hvite klær når du er ute i sola.",
         "1. Salt senker frysepunktet\n2. Vann utvider seg når det fryser\n3. Svart absorberer mer sollys"),
    ],
    "Kapittel 2: Kjemi": [
        ("Hva er det kjemiske symbolet for gull?", "Au"),
        ("Hva er symbolet for vann?", "H2O"),
    ],
    "Alle Spørsmål": [
        ("Hva heter planeten nærmest solen?", "Merkur"),
        ("Hva er fotosyntese?", "Prosessen der planter lager energi ved hjelp av lys."),
    ],
}

if 'kategori' not in st.session_state:
    st.session_state.kategori = None
    st.session_state.sporsmal = []
    st.session_state.svar = None
    st.session_state.feil_teller = 0
    st.session_state.navaerende_sporsmal = None

st.title("Quiz App")

if st.button("← Tilbake til kategori"):
    st.session_state.kategori = None
    st.session_state.feil_teller = 0
    st.session_state.navaerende_sporsmal = None

if not st.session_state.kategori:
    st.subheader("Velg en kategori")
    for kategori in quiz_data.keys():
        if st.button(kategori):
            st.session_state.kategori = kategori
            st.session_state.feil_teller = 0
            st.session_state.sporsmal_liste = quiz_data[kategori][:]
            st.session_state.navaerende_sporsmal = random.choice(st.session_state.sporsmal_liste)
            st.session_state.sporsmal_liste.remove(st.session_state.navaerende_sporsmal)

if st.session_state.kategori:
    st.subheader(f"Kategori: {st.session_state.kategori}")
    sporsmal, svar = st.session_state.navaerende_sporsmal

    st.markdown("### Spørsmål")
    st.write(sporsmal)

    if st.button("Vis svar"):
        st.session_state.svar = st.session_state.navaerende_sporsmal[1]

    if st.session_state.svar:
        st.markdown("### Svar")
        st.write(st.session_state.svar)

        svar = st.radio("Klarte du spørsmålet?", ["Ja", "Nei"])
        if st.button("Bekreft svar"):
            if svar == "Nei":
                st.session_state.feil_teller += 1

            st.session_state.sporsmal_liste.remove(st.session_state.navaerende_sporsmal)
            st.session_state.svar = None

            if st.session_state.sporsmal_liste:
                st.session_state.navaerende_sporsmal = random.choice(st.session_state.sporsmal_liste)
            else:
                st.markdown(f"## Alle spørsmål er besvart! Du hadde {st.session_state.feil_teller} feil.")
                st.session_state.navaerende_sporsmal = None
