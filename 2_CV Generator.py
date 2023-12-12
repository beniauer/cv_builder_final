import streamlit as st

st.title("CV Generator 📃")

tab_titles = [
    "Consulting 🧮",
    "Finance 📈",
    "Corporate 🏢",
    "Start-Up 🚀",
    "IT 🖥",
    "Academic 📚"
]

tabs=st.tabs(tab_titles)

with tabs[0]:
    import streamlit as st

    # Streamlit-Benutzeroberfläche
    st.title("Consulting 🧮")

    # API Anbindung
    st.button("Get your input via LinkedIn", key="unique_key_0")

    # Persönliche Informationen
    st.header("Personal Information")
    name = st.text_input("Name", key="unique_key_1")
    address = st.text_input("Adresse", key="unique_key_2")
    phone = st.text_input("Telefonnummer", key="unique_key_3")
    email = st.text_input("E-Mail", key="unique_key_4")

    # Education
    st.header("Education")
    university1 = st.text_input("Universität/Schule 1", key="unique_key_5")
    locationus1 = st.text_input("Standort 1", key="unique_key_6")
    majorus1 = st.text_input("Studiengang 1", key="unique_key_7")
    timeus1 = st.text_input("Zeitraum 1", key="unique_key_8")
    courses1 = st.text_input("Kurse 1", key="unique_key_9")
    gpa1 = st.text_input("GPA 1", key="unique_key_10")
    clubs1 = st.text_input("Clubs/Aktivitäten 1", key="unique_key_11")

    university2 = st.text_input("Universität/Schule 2", "", key="unique_key_12")
    locationus2 = st.text_input("Standort 2", "", key="unique_key_13")
    majorus2 = st.text_input("Studiengang 2", "", key="unique_key_14")
    timeus2 = st.text_input("Zeitraum 2", "", key="unique_key_15")
    courses2 = st.text_input("Kurse 2", "", key="unique_key_16")
    gpa2 = st.text_input("GPA 2", "", key="unique_key_17")
    clubs2 = st.text_input("Clubs/Aktivitäten 2", "", key="unique_key_18")

    # Professional Experience
    st.header("Professional Experience")
    experience1 = st.text_input("Erfahrung 1", key="unique_key_19")
    locatione1 = st.text_input("Standort Erfahrung 1", key="unique_key_20")
    position1 = st.text_input("Position 1", key="unique_key_21!")
    timee1 = st.text_input("Zeitraum Erfahrung 1", key="unique_key_22")
    task11 = st.text_area("Aufgaben 1", key='task11_1', height=100)
    task12 = st.text_area("Aufgaben 2", key='task12_2', height=100)
    task13 = st.text_area("Aufgaben 3", key='task13_3', height=100)

    experience2 = st.text_input("Erfahrung 2", "", key="unique_key_23")
    locatione2 = st.text_input("Standort Erfahrung 2", "", key="unique_key_24")
    position2 = st.text_input("Position 2", "", key="position_2_key")
    timee2 = st.text_input("Zeitraum Erfahrung 2", "", key="unique_key_25")
    task21 = st.text_area("Aufgaben 1", key='task21_4', height=100)
    task22 = st.text_area("Aufgaben 2", key='task22_5', height=100)
    task23 = st.text_area("Aufgaben 3", key='task23_6', height=100)

    experience3 = st.text_input("Erfahrung 3", "", key="unique_key_26")
    locatione3 = st.text_input("Standort Erfahrung 3", "", key="unique_key_27")
    position3 = st.text_input("Position 3", "", key="unique_key_28")
    timee3 = st.text_input("Zeitraum Erfahrung 3", "", key="unique_key_29")
    task31 = st.text_area("Aufgaben 1", key='task31_7', height=100)
    task32 = st.text_area("Aufgaben 2", key='task32_8', height=100)
    task33 = st.text_area("Aufgaben 3", key='task33_9', height=100)

    # Extracurricular Activities / Engagement
    st.header("Extracurricular Activities / Engagement")
    extracurricular1 = st.text_input("Extrakurrikulare Aktivitäten", key="unique_key_30")
    additionaleducation1 = st.text_input("Zusätzliche Bildung", key="unique_key_31")
    certificates1 = st.text_input("Zertifikate und Errungenschaften", key="unique_key_32")

    # Skills & Interest
    st.header("Skills & Interest")
    languages1 = st.text_input("Sprachen", key="unique_key_33")
    computer1 = st.text_input("Computerkenntnisse", key="unique_key_34")
    interests1 = st.text_input("Interessen", key="unique_key_35")

    # Button zum Erstellen des CVs
    if st.button("CV Erstellen", key="unique_key_36"):
        try:
            with open('template_finance.tex', 'r', encoding='utf-8') as file:
                latex_template = file.read()

            try:
                # Formatierung des LaTeX-Templates
                latex_filled = latex_template.format(
                    name=name,
                    address=address,
                    phone=phone,
                    email=email,
                    university1=university1, 
                    locationus1=locationus1, 
                    majorus1=majorus1, 
                    timeus1=timeus1,
                    courses1=courses1, 
                    gpa1=gpa1, 
                    clubs1=clubs1,
                    university2=university2, 
                    locationus2=locationus2, 
                    majorus2=majorus2, 
                    timeus2=timeus2, 
                    courses2=courses2, 
                    gpa2=gpa2, 
                    clubs2=clubs2, 
                    experience1=experience1, 
                    locatione1=locatione1, 
                    position1=position1, 
                    timee1=timee1, 
                    task11=task11, 
                    task12=task12, 
                    task13=task13, 
                    experience2=experience2, 
                    locatione2=locatione2, 
                    position2=position2, 
                    timee2=timee2, 
                    task21=task21, 
                    task22=task22, 
                    task23=task23, 
                    experience3=experience3,
                    locatione3=locatione3, 
                    position3=position3, 
                    timee3=timee3, 
                    task31=task31, 
                    task32=task32, 
                    task33=task33, 
                    extracurricular1=extracurricular1, 
                    additionaleducation1=additionaleducation1, 
                    certificates1=certificates1, 
                    languages1=languages1,
                    computer1=computer1, 
                    interests1=interests1
                )

                # Anzeigen des gefüllten LaTeX-Codes auf der Streamlit-Oberfläche
                st.text_area("Gefüllter LaTeX-Code", latex_filled, height=300)

            except KeyError as key_err:
                st.error(f"Fehler bei der Formatierung: Unbekannter Platzhalter {key_err}")
            except Exception as format_err:
                st.error(f"Fehler bei der Formatierung: {format_err}")

        except FileNotFoundError:
            st.error("Die LaTeX-Vorlagendatei wurde nicht gefunden.")
        except Exception as e:
            st.error(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

with tabs[1]:
    import streamlit as st

    # Streamlit-Benutzeroberfläche
    st.title("Finance 📈")

    # API Anbindung
    st.button("Get your input via LinkedIn", key="unique_key_37")

    # Persönliche Informationen
    st.header("Personal Information")
    name = st.text_input("Name", key="unique_key_38")
    address = st.text_input("Adresse", key="unique_key_39")
    phone = st.text_input("Telefonnummer", key="unique_key_40")
    email = st.text_input("E-Mail", key="unique_key_41")

    # Education
    st.header("Education")
    university1 = st.text_input("Universität/Schule 1", key="unique_key_42")
    locationus1 = st.text_input("Standort 1", key="unique_key_43")
    majorus1 = st.text_input("Studiengang 1", key="unique_key_44")
    timeus1 = st.text_input("Zeitraum 1", key="unique_key_45")
    courses1 = st.text_input("Kurse 1", key="unique_key_46")
    gpa1 = st.text_input("GPA 1", key="unique_key_47")
    clubs1 = st.text_input("Clubs/Aktivitäten 1", key="unique_key_48")

    university2 = st.text_input("Universität/Schule 2", "", key="unique_key_49")
    locationus2 = st.text_input("Standort 2", "", key="unique_key_50")
    majorus2 = st.text_input("Studiengang 2", "", key="unique_key_51")
    timeus2 = st.text_input("Zeitraum 2", "", key="unique_key_52")
    courses2 = st.text_input("Kurse 2", "", key="unique_key_53")
    gpa2 = st.text_input("GPA 2", "", key="unique_key_54")
    clubs2 = st.text_input("Clubs/Aktivitäten 2", "", key="unique_key_55")

    # Professional Experience
    st.header("Professional Experience")
    experience1 = st.text_input("Erfahrung 1", key="unique_key_56")
    locatione1 = st.text_input("Standort Erfahrung 1", key="unique_key_57")
    position1 = st.text_input("Position 1", key="unique_key_21")
    timee1 = st.text_input("Zeitraum Erfahrung 1", key="unique_key_58")
    task11 = st.text_area("Aufgaben 1", key='task11_10', height=100)
    task12 = st.text_area("Aufgaben 2", key='task12_11', height=100)
    task13 = st.text_area("Aufgaben 3", key='task13_12', height=100)

    experience2 = st.text_input("Erfahrung 2", "", key="unique_key_59")
    locatione2 = st.text_input("Standort Erfahrung 2", "", key="unique_key_60")
    position2 = st.text_input("Position 2", "", key="position_3_key")
    timee2 = st.text_input("Zeitraum Erfahrung 2", "", key="unique_key_61")
    task21 = st.text_area("Aufgaben 1", key='task21_13', height=100)
    task22 = st.text_area("Aufgaben 2", key='task22_14', height=100)
    task23 = st.text_area("Aufgaben 3", key='task23_15', height=100)

    experience3 = st.text_input("Erfahrung 3", "", key="unique_key_62")
    locatione3 = st.text_input("Standort Erfahrung 3", "", key="unique_key_63")
    position3 = st.text_input("Position 3", "", key="unique_key_64")
    timee3 = st.text_input("Zeitraum Erfahrung 3", "", key="unique_key_65")
    task31 = st.text_area("Aufgaben 1", key='task31_16', height=100)
    task32 = st.text_area("Aufgaben 2", key='task32_17', height=100)
    task33 = st.text_area("Aufgaben 3", key='task33_18', height=100)

    # Extracurricular Activities / Engagement
    st.header("Extracurricular Activities / Engagement")
    extracurricular1 = st.text_input("Extrakurrikulare Aktivitäten", key="unique_key_66")
    additionaleducation1 = st.text_input("Zusätzliche Bildung", key="unique_key_67")
    certificates1 = st.text_input("Zertifikate und Errungenschaften", key="unique_key_68")

    # Skills & Interest
    st.header("Skills & Interest")
    languages1 = st.text_input("Sprachen", key="unique_key_69")
    computer1 = st.text_input("Computerkenntnisse", key="unique_key_70")
    interests1 = st.text_input("Interessen", key="unique_key_71")

    # Button zum Erstellen des CVs
    if st.button("CV Erstellen", key="unique_key_72"):
        try:
            with open('template_finance.tex', 'r', encoding='utf-8') as file:
                latex_template = file.read()

            try:
                # Formatierung des LaTeX-Templates
                latex_filled = latex_template.format(
                    name=name,
                    address=address,
                    phone=phone,
                    email=email,
                    university1=university1, 
                    locationus1=locationus1, 
                    majorus1=majorus1, 
                    timeus1=timeus1,
                    courses1=courses1, 
                    gpa1=gpa1, 
                    clubs1=clubs1,
                    university2=university2, 
                    locationus2=locationus2, 
                    majorus2=majorus2, 
                    timeus2=timeus2, 
                    courses2=courses2, 
                    gpa2=gpa2, 
                    clubs2=clubs2, 
                    experience1=experience1, 
                    locatione1=locatione1, 
                    position1=position1, 
                    timee1=timee1, 
                    task11=task11, 
                    task12=task12, 
                    task13=task13, 
                    experience2=experience2, 
                    locatione2=locatione2, 
                    position2=position2, 
                    timee2=timee2, 
                    task21=task21, 
                    task22=task22, 
                    task23=task23, 
                    experience3=experience3,
                    locatione3=locatione3, 
                    position3=position3, 
                    timee3=timee3, 
                    task31=task31, 
                    task32=task32, 
                    task33=task33, 
                    extracurricular1=extracurricular1, 
                    additionaleducation1=additionaleducation1, 
                    certificates1=certificates1, 
                    languages1=languages1,
                    computer1=computer1, 
                    interests1=interests1
                )

                # Anzeigen des gefüllten LaTeX-Codes auf der Streamlit-Oberfläche
                st.text_area("Gefüllter LaTeX-Code", latex_filled, height=300)

            except KeyError as key_err:
                st.error(f"Fehler bei der Formatierung: Unbekannter Platzhalter {key_err}")
            except Exception as format_err:
                st.error(f"Fehler bei der Formatierung: {format_err}")

        except FileNotFoundError:
            st.error("Die LaTeX-Vorlagendatei wurde nicht gefunden.")
        except Exception as e:
            st.error(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

with tabs[2]:
    import streamlit as st

    # Streamlit-Benutzeroberfläche
    st.title("Corporate 🏢")

    # API Anbindung
    st.button("Get your input via LinkedIn", key="unique_key_73")

    # Persönliche Informationen
    st.header("Personal Information")
    name = st.text_input("Name", key="unique_key_74")
    address = st.text_input("Adresse", key="unique_key_75")
    phone = st.text_input("Telefonnummer", key="unique_key_76")
    email = st.text_input("E-Mail", key="unique_key_77")

    # Education
    st.header("Education")
    university1 = st.text_input("Universität/Schule 1", key="unique_key_78")
    locationus1 = st.text_input("Standort 1", key="unique_key_79")
    majorus1 = st.text_input("Studiengang 1", key="unique_key_80")
    timeus1 = st.text_input("Zeitraum 1", key="unique_key_81")
    courses1 = st.text_input("Kurse 1", key="unique_key_82")
    gpa1 = st.text_input("GPA 1", key="unique_key_83")
    clubs1 = st.text_input("Clubs/Aktivitäten 1", key="unique_key_84")

    university2 = st.text_input("Universität/Schule 2", "", key="unique_key_85")
    locationus2 = st.text_input("Standort 2", "", key="unique_key_86")
    majorus2 = st.text_input("Studiengang 2", "", key="unique_key_87")
    timeus2 = st.text_input("Zeitraum 2", "", key="unique_key_88")
    courses2 = st.text_input("Kurse 2", "", key="unique_key_89")
    gpa2 = st.text_input("GPA 2", "", key="unique_key_90")
    clubs2 = st.text_input("Clubs/Aktivitäten 2", "", key="unique_key_91")

    # Professional Experience
    st.header("Professional Experience")
    experience1 = st.text_input("Erfahrung 1", key="unique_key_92")
    locatione1 = st.text_input("Standort Erfahrung 1", key="unique_key_93")
    position1 = st.text_input("Position 1", key="unique_key_94")
    timee1 = st.text_input("Zeitraum Erfahrung 1", key="unique_key_95")
    task11 = st.text_area("Aufgaben 1", key='task11_19', height=100)
    task12 = st.text_area("Aufgaben 2", key='task12_20', height=100)
    task13 = st.text_area("Aufgaben 3", key='task13_21', height=100)

    experience2 = st.text_input("Erfahrung 2", "", key="unique_key_96")
    locatione2 = st.text_input("Standort Erfahrung 2", "", key="unique_key_97")
    position2 = st.text_input("Position 2", "", key="position_4_key")
    timee2 = st.text_input("Zeitraum Erfahrung 2", "", key="unique_key_98")
    task21 = st.text_area("Aufgaben 1", key='task21_22', height=100)
    task22 = st.text_area("Aufgaben 2", key='task22_23', height=100)
    task23 = st.text_area("Aufgaben 3", key='task23_24', height=100)

    experience3 = st.text_input("Erfahrung 3", "", key="unique_key_99")
    locatione3 = st.text_input("Standort Erfahrung 3", "", key="unique_key_100")
    position3 = st.text_input("Position 3", "", key="unique_key_101")
    timee3 = st.text_input("Zeitraum Erfahrung 3", "", key="unique_key_102")
    task31 = st.text_area("Aufgaben 1", key='task31', height=100)
    task32 = st.text_area("Aufgaben 2", key='task32', height=100)
    task33 = st.text_area("Aufgaben 3", key='task33', height=100)

    # Extracurricular Activities / Engagement
    st.header("Extracurricular Activities / Engagement")
    extracurricular1 = st.text_input("Extrakurrikulare Aktivitäten", key="unique_key_103")
    additionaleducation1 = st.text_input("Zusätzliche Bildung", key="unique_key_104")
    certificates1 = st.text_input("Zertifikate und Errungenschaften", key="unique_key_105")

    # Skills & Interest
    st.header("Skills & Interest")
    languages1 = st.text_input("Sprachen", key="unique_key_106")
    computer1 = st.text_input("Computerkenntnisse", key="unique_key_107")
    interests1 = st.text_input("Interessen", key="unique_key_108")

    # Button zum Erstellen des CVs
    if st.button("CV Erstellen", key="unique_key_109"):
        try:
            with open('template_finance.tex', 'r', encoding='utf-8') as file:
                latex_template = file.read()

            try:
                # Formatierung des LaTeX-Templates
                latex_filled = latex_template.format(
                    name=name,
                    address=address,
                    phone=phone,
                    email=email,
                    university1=university1, 
                    locationus1=locationus1, 
                    majorus1=majorus1, 
                    timeus1=timeus1,
                    courses1=courses1, 
                    gpa1=gpa1, 
                    clubs1=clubs1,
                    university2=university2, 
                    locationus2=locationus2, 
                    majorus2=majorus2, 
                    timeus2=timeus2, 
                    courses2=courses2, 
                    gpa2=gpa2, 
                    clubs2=clubs2, 
                    experience1=experience1, 
                    locatione1=locatione1, 
                    position1=position1, 
                    timee1=timee1, 
                    task11=task11, 
                    task12=task12, 
                    task13=task13, 
                    experience2=experience2, 
                    locatione2=locatione2, 
                    position2=position2, 
                    timee2=timee2, 
                    task21=task21, 
                    task22=task22, 
                    task23=task23, 
                    experience3=experience3,
                    locatione3=locatione3, 
                    position3=position3, 
                    timee3=timee3, 
                    task31=task31, 
                    task32=task32, 
                    task33=task33, 
                    extracurricular1=extracurricular1, 
                    additionaleducation1=additionaleducation1, 
                    certificates1=certificates1, 
                    languages1=languages1,
                    computer1=computer1, 
                    interests1=interests1
                )

                # Anzeigen des gefüllten LaTeX-Codes auf der Streamlit-Oberfläche
                st.text_area("Gefüllter LaTeX-Code", latex_filled, height=300)

            except KeyError as key_err:
                st.error(f"Fehler bei der Formatierung: Unbekannter Platzhalter {key_err}")
            except Exception as format_err:
                st.error(f"Fehler bei der Formatierung: {format_err}")

        except FileNotFoundError:
            st.error("Die LaTeX-Vorlagendatei wurde nicht gefunden.")
        except Exception as e:
            st.error(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

with tabs[3]:
    import streamlit as st

    # Streamlit-Benutzeroberfläche
    st.title("Start-Up 🚀")

    # API Anbindung
    st.button("Get your input via LinkedIn", key="unique_key_110")

    # Persönliche Informationen
    st.header("Personal Information")
    name = st.text_input("Name", key="unique_key_111")
    address = st.text_input("Adresse", key="unique_key_112")
    phone = st.text_input("Telefonnummer", key="unique_key_113")
    email = st.text_input("E-Mail", key="unique_key_114")

    # Education
    st.header("Education")
    university1 = st.text_input("Universität/Schule 1", key="unique_key_115")
    locationus1 = st.text_input("Standort 1", key="unique_key_116")
    majorus1 = st.text_input("Studiengang 1", key="unique_key_117")
    timeus1 = st.text_input("Zeitraum 1", key="unique_key_118")
    courses1 = st.text_input("Kurse 1", key="unique_key_119")
    gpa1 = st.text_input("GPA 1", key="unique_key_120")
    clubs1 = st.text_input("Clubs/Aktivitäten 1", key="unique_key_123")

    university2 = st.text_input("Universität/Schule 2", "", key="unique_key_124")
    locationus2 = st.text_input("Standort 2", "", key="unique_key_125")
    majorus2 = st.text_input("Studiengang 2", "", key="unique_key_126")
    timeus2 = st.text_input("Zeitraum 2", "", key="unique_key_127")
    courses2 = st.text_input("Kurse 2", "", key="unique_key_128")
    gpa2 = st.text_input("GPA 2", "", key="unique_key_129")
    clubs2 = st.text_input("Clubs/Aktivitäten 2", "", key="unique_key_130")

    # Professional Experience
    st.header("Professional Experience")
    experience1 = st.text_input("Erfahrung 1", key="unique_key_131")
    locatione1 = st.text_input("Standort Erfahrung 1", key="unique_key_132")
    position1 = st.text_input("Position 1", key="unique_key_133")
    timee1 = st.text_input("Zeitraum Erfahrung 1", key="unique_key_134")
    task11 = st.text_area("Aufgaben 1", key='task11_19!', height=100)
    task12 = st.text_area("Aufgaben 2", key='task12_20!', height=100)
    task13 = st.text_area("Aufgaben 3", key='task13_21!', height=100)

    experience2 = st.text_input("Erfahrung 2", "", key="unique_key_135")
    locatione2 = st.text_input("Standort Erfahrung 2", "", key="unique_key_136")
    position2 = st.text_input("Position 2", "", key="position_5_key")
    timee2 = st.text_input("Zeitraum Erfahrung 2", "", key="unique_key_137")
    task21 = st.text_area("Aufgaben 1", key='task21_22!', height=100)
    task22 = st.text_area("Aufgaben 2", key='task22_23!', height=100)
    task23 = st.text_area("Aufgaben 3", key='task23_24!', height=100)

    experience3 = st.text_input("Erfahrung 3", "", key="unique_key_138")
    locatione3 = st.text_input("Standort Erfahrung 3", "", key="unique_key_139")
    position3 = st.text_input("Position 3", "", key="unique_key_140")
    timee3 = st.text_input("Zeitraum Erfahrung 3", "", key="unique_key_141")
    task31 = st.text_area("Aufgaben 1", key='task31!', height=100)
    task32 = st.text_area("Aufgaben 2", key='task32!', height=100)
    task33 = st.text_area("Aufgaben 3", key='task33!', height=100)

    # Extracurricular Activities / Engagement
    st.header("Extracurricular Activities / Engagement")
    extracurricular1 = st.text_input("Extrakurrikulare Aktivitäten", key="unique_key_142")
    additionaleducation1 = st.text_input("Zusätzliche Bildung", key="unique_key_143")
    certificates1 = st.text_input("Zertifikate und Errungenschaften", key="unique_key_144")

    # Skills & Interest
    st.header("Skills & Interest")
    languages1 = st.text_input("Sprachen", key="unique_key_145")
    computer1 = st.text_input("Computerkenntnisse", key="unique_key_146")
    interests1 = st.text_input("Interessen", key="unique_key_147")

    # Button zum Erstellen des CVs
    if st.button("CV Erstellen", key="unique_key_148"):
        try:
            with open('template_finance.tex', 'r', encoding='utf-8') as file:
                latex_template = file.read()

            try:
                # Formatierung des LaTeX-Templates
                latex_filled = latex_template.format(
                    name=name,
                    address=address,
                    phone=phone,
                    email=email,
                    university1=university1, 
                    locationus1=locationus1, 
                    majorus1=majorus1, 
                    timeus1=timeus1,
                    courses1=courses1, 
                    gpa1=gpa1, 
                    clubs1=clubs1,
                    university2=university2, 
                    locationus2=locationus2, 
                    majorus2=majorus2, 
                    timeus2=timeus2, 
                    courses2=courses2, 
                    gpa2=gpa2, 
                    clubs2=clubs2, 
                    experience1=experience1, 
                    locatione1=locatione1, 
                    position1=position1, 
                    timee1=timee1, 
                    task11=task11, 
                    task12=task12, 
                    task13=task13, 
                    experience2=experience2, 
                    locatione2=locatione2, 
                    position2=position2, 
                    timee2=timee2, 
                    task21=task21, 
                    task22=task22, 
                    task23=task23, 
                    experience3=experience3,
                    locatione3=locatione3, 
                    position3=position3, 
                    timee3=timee3, 
                    task31=task31, 
                    task32=task32, 
                    task33=task33, 
                    extracurricular1=extracurricular1, 
                    additionaleducation1=additionaleducation1, 
                    certificates1=certificates1, 
                    languages1=languages1,
                    computer1=computer1, 
                    interests1=interests1
                )

                # Anzeigen des gefüllten LaTeX-Codes auf der Streamlit-Oberfläche
                st.text_area("Gefüllter LaTeX-Code", latex_filled, height=300)

            except KeyError as key_err:
                st.error(f"Fehler bei der Formatierung: Unbekannter Platzhalter {key_err}")
            except Exception as format_err:
                st.error(f"Fehler bei der Formatierung: {format_err}")

        except FileNotFoundError:
            st.error("Die LaTeX-Vorlagendatei wurde nicht gefunden.")
        except Exception as e:
            st.error(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

with tabs[4]:
    import streamlit as st

    # Streamlit-Benutzeroberfläche
    st.title("IT 🖥️")

    # API Anbindung
    st.button("Get your input via LinkedIn", key="unique_key_110!")

    # Persönliche Informationen
    st.header("Personal Information")
    name = st.text_input("Name", key="unique_key_111!")
    address = st.text_input("Adresse", key="unique_key_112!")
    phone = st.text_input("Telefonnummer", key="unique_key_113!")
    email = st.text_input("E-Mail", key="unique_key_114!")

    # Education
    st.header("Education")
    university1 = st.text_input("Universität/Schule 1", key="unique_key_115!")
    locationus1 = st.text_input("Standort 1", key="unique_key_116!")
    majorus1 = st.text_input("Studiengang 1", key="unique_key_117!")
    timeus1 = st.text_input("Zeitraum 1", key="unique_key_118!")
    courses1 = st.text_input("Kurse 1", key="unique_key_119!")
    gpa1 = st.text_input("GPA 1", key="unique_key_120!")
    clubs1 = st.text_input("Clubs/Aktivitäten 1", key="unique_key_123!")

    university2 = st.text_input("Universität/Schule 2", "", key="unique_key_124!")
    locationus2 = st.text_input("Standort 2", "", key="unique_key_125!")
    majorus2 = st.text_input("Studiengang 2", "", key="unique_key_126!")
    timeus2 = st.text_input("Zeitraum 2", "", key="unique_key_127!")
    courses2 = st.text_input("Kurse 2", "", key="unique_key_128!")
    gpa2 = st.text_input("GPA 2", "", key="unique_key_129!")
    clubs2 = st.text_input("Clubs/Aktivitäten 2", "", key="unique_key_130!")

    # Professional Experience
    st.header("Professional Experience")
    experience1 = st.text_input("Erfahrung 1", key="unique_key_131!")
    locatione1 = st.text_input("Standort Erfahrung 1", key="unique_key_132!")
    position1 = st.text_input("Position 1", key="unique_key_133!")
    timee1 = st.text_input("Zeitraum Erfahrung 1", key="unique_key_134!")
    task11 = st.text_area("Aufgaben 1", key='task11_19!!', height=100)
    task12 = st.text_area("Aufgaben 2", key='task12_20!!', height=100)
    task13 = st.text_area("Aufgaben 3", key='task13_21!!', height=100)

    experience2 = st.text_input("Erfahrung 2", "", key="unique_key_135!")
    locatione2 = st.text_input("Standort Erfahrung 2", "", key="unique_key_136!")
    position2 = st.text_input("Position 2", "", key="position_5!_key")
    timee2 = st.text_input("Zeitraum Erfahrung 2", "", key="unique_key_137!")
    task21 = st.text_area("Aufgaben 1", key='task21_22!!', height=100)
    task22 = st.text_area("Aufgaben 2", key='task22_23!!', height=100)
    task23 = st.text_area("Aufgaben 3", key='task23_24!!', height=100)

    experience3 = st.text_input("Erfahrung 3", "", key="unique_key_138!")
    locatione3 = st.text_input("Standort Erfahrung 3", "", key="unique_key_139!")
    position3 = st.text_input("Position 3", "", key="unique_key_140!")
    timee3 = st.text_input("Zeitraum Erfahrung 3", "", key="unique_key_141!")
    task31 = st.text_area("Aufgaben 1", key='task31!!', height=100)
    task32 = st.text_area("Aufgaben 2", key='task32!!', height=100)
    task33 = st.text_area("Aufgaben 3", key='task33!!', height=100)

    # Extracurricular Activities / Engagement
    st.header("Extracurricular Activities / Engagement")
    extracurricular1 = st.text_input("Extrakurrikulare Aktivitäten", key="unique_key_142!")
    additionaleducation1 = st.text_input("Zusätzliche Bildung", key="unique_key_143!")
    certificates1 = st.text_input("Zertifikate und Errungenschaften", key="unique_key_144!")

    # Skills & Interest
    st.header("Skills & Interest")
    languages1 = st.text_input("Sprachen", key="unique_key_145!")
    computer1 = st.text_input("Computerkenntnisse", key="unique_key_146!")
    interests1 = st.text_input("Interessen", key="unique_key_147!")

    # Button zum Erstellen des CVs
    if st.button("CV Erstellen", key="unique_key_148!"):
        try:
            with open('template_finance.tex', 'r', encoding='utf-8') as file:
                latex_template = file.read()

            try:
                # Formatierung des LaTeX-Templates
                latex_filled = latex_template.format(
                    name=name,
                    address=address,
                    phone=phone,
                    email=email,
                    university1=university1, 
                    locationus1=locationus1, 
                    majorus1=majorus1, 
                    timeus1=timeus1,
                    courses1=courses1, 
                    gpa1=gpa1, 
                    clubs1=clubs1,
                    university2=university2, 
                    locationus2=locationus2, 
                    majorus2=majorus2, 
                    timeus2=timeus2, 
                    courses2=courses2, 
                    gpa2=gpa2, 
                    clubs2=clubs2, 
                    experience1=experience1, 
                    locatione1=locatione1, 
                    position1=position1, 
                    timee1=timee1, 
                    task11=task11, 
                    task12=task12, 
                    task13=task13, 
                    experience2=experience2, 
                    locatione2=locatione2, 
                    position2=position2, 
                    timee2=timee2, 
                    task21=task21, 
                    task22=task22, 
                    task23=task23, 
                    experience3=experience3,
                    locatione3=locatione3, 
                    position3=position3, 
                    timee3=timee3, 
                    task31=task31, 
                    task32=task32, 
                    task33=task33, 
                    extracurricular1=extracurricular1, 
                    additionaleducation1=additionaleducation1, 
                    certificates1=certificates1, 
                    languages1=languages1,
                    computer1=computer1, 
                    interests1=interests1
                )

                # Anzeigen des gefüllten LaTeX-Codes auf der Streamlit-Oberfläche
                st.text_area("Gefüllter LaTeX-Code", latex_filled, height=300)

            except KeyError as key_err:
                st.error(f"Fehler bei der Formatierung: Unbekannter Platzhalter {key_err}")
            except Exception as format_err:
                st.error(f"Fehler bei der Formatierung: {format_err}")

        except FileNotFoundError:
            st.error("Die LaTeX-Vorlagendatei wurde nicht gefunden.")
        except Exception as e:
            st.error(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

with tabs[5]:
    import streamlit as st

    # Streamlit-Benutzeroberfläche
    st.title("Academic 📚")

    # API Anbindung
    st.button("Get your input via LinkedIn", key="unique_key_110!§")

    # Persönliche Informationen
    st.header("Personal Information")
    name = st.text_input("Name", key="unique_key_111!§")
    address = st.text_input("Adresse", key="unique_key_112!§")
    phone = st.text_input("Telefonnummer", key="unique_key_113!§")
    email = st.text_input("E-Mail", key="unique_key_114!§")

    # Education
    st.header("Education")
    university1 = st.text_input("Universität/Schule 1", key="unique_key_115!§")
    locationus1 = st.text_input("Standort 1", key="unique_key_116!§")
    majorus1 = st.text_input("Studiengang 1", key="unique_key_117!§")
    timeus1 = st.text_input("Zeitraum 1", key="unique_key_118!§")
    courses1 = st.text_input("Kurse 1", key="unique_key_119!§")
    gpa1 = st.text_input("GPA 1", key="unique_key_120!§")
    clubs1 = st.text_input("Clubs/Aktivitäten 1", key="unique_key_123!§")

    university2 = st.text_input("Universität/Schule 2", "", key="unique_key_124!§")
    locationus2 = st.text_input("Standort 2", "", key="unique_key_125!§")
    majorus2 = st.text_input("Studiengang 2", "", key="unique_key_126!§")
    timeus2 = st.text_input("Zeitraum 2", "", key="unique_key_127!§")
    courses2 = st.text_input("Kurse 2", "", key="unique_key_128!§")
    gpa2 = st.text_input("GPA 2", "", key="unique_key_129!§")
    clubs2 = st.text_input("Clubs/Aktivitäten 2", "", key="unique_key_130!§")

    # Professional Experience
    st.header("Professional Experience")
    experience1 = st.text_input("Erfahrung 1", key="unique_key_131!§")
    locatione1 = st.text_input("Standort Erfahrung 1", key="unique_key_132!§")
    position1 = st.text_input("Position 1", key="unique_key_133!§")
    timee1 = st.text_input("Zeitraum Erfahrung 1", key="unique_key_134!§")
    task11 = st.text_area("Aufgaben 1", key='task11_19!!§', height=100)
    task12 = st.text_area("Aufgaben 2", key='task12_20!!§', height=100)
    task13 = st.text_area("Aufgaben 3", key='task13_21!!§', height=100)

    experience2 = st.text_input("Erfahrung 2", "", key="unique_key_135!§")
    locatione2 = st.text_input("Standort Erfahrung 2", "", key="unique_key_136!§")
    position2 = st.text_input("Position 2", "", key="position_5!§_key")
    timee2 = st.text_input("Zeitraum Erfahrung 2", "", key="unique_key_137!§")
    task21 = st.text_area("Aufgaben 1", key='task21_22!!§', height=100)
    task22 = st.text_area("Aufgaben 2", key='task22_23!!§', height=100)
    task23 = st.text_area("Aufgaben 3", key='task23_24!!§', height=100)

    experience3 = st.text_input("Erfahrung 3", "", key="unique_key_138!§")
    locatione3 = st.text_input("Standort Erfahrung 3", "", key="unique_key_139!§")
    position3 = st.text_input("Position 3", "", key="unique_key_140!§")
    timee3 = st.text_input("Zeitraum Erfahrung 3", "", key="unique_key_141!§")
    task31 = st.text_area("Aufgaben 1", key='task31!!§', height=100)
    task32 = st.text_area("Aufgaben 2", key='task32!!§', height=100)
    task33 = st.text_area("Aufgaben 3", key='task33!!§', height=100)

    # Extracurricular Activities / Engagement
    st.header("Extracurricular Activities / Engagement")
    extracurricular1 = st.text_input("Extrakurrikulare Aktivitäten", key="unique_key_142!§")
    additionaleducation1 = st.text_input("Zusätzliche Bildung", key="unique_key_143!§")
    certificates1 = st.text_input("Zertifikate und Errungenschaften", key="unique_key_144!§")

    # Skills & Interest
    st.header("Skills & Interest")
    languages1 = st.text_input("Sprachen", key="unique_key_145!§")
    computer1 = st.text_input("Computerkenntnisse", key="unique_key_146!§")
    interests1 = st.text_input("Interessen", key="unique_key_147!§")

    # Button zum Erstellen des CVs
    if st.button("CV Erstellen", key="unique_key_148!§"):
        try:
            with open('template_finance.tex', 'r', encoding='utf-8') as file:
                latex_template = file.read()

            try:
                # Formatierung des LaTeX-Templates
                latex_filled = latex_template.format(
                    name=name,
                    address=address,
                    phone=phone,
                    email=email,
                    university1=university1, 
                    locationus1=locationus1, 
                    majorus1=majorus1, 
                    timeus1=timeus1,
                    courses1=courses1, 
                    gpa1=gpa1, 
                    clubs1=clubs1,
                    university2=university2, 
                    locationus2=locationus2, 
                    majorus2=majorus2, 
                    timeus2=timeus2, 
                    courses2=courses2, 
                    gpa2=gpa2, 
                    clubs2=clubs2, 
                    experience1=experience1, 
                    locatione1=locatione1, 
                    position1=position1, 
                    timee1=timee1, 
                    task11=task11, 
                    task12=task12, 
                    task13=task13, 
                    experience2=experience2, 
                    locatione2=locatione2, 
                    position2=position2, 
                    timee2=timee2, 
                    task21=task21, 
                    task22=task22, 
                    task23=task23, 
                    experience3=experience3,
                    locatione3=locatione3, 
                    position3=position3, 
                    timee3=timee3, 
                    task31=task31, 
                    task32=task32, 
                    task33=task33, 
                    extracurricular1=extracurricular1, 
                    additionaleducation1=additionaleducation1, 
                    certificates1=certificates1, 
                    languages1=languages1,
                    computer1=computer1, 
                    interests1=interests1
                )

                # Anzeigen des gefüllten LaTeX-Codes auf der Streamlit-Oberfläche
                st.text_area("Gefüllter LaTeX-Code", latex_filled, height=300)

            except KeyError as key_err:
                st.error(f"Fehler bei der Formatierung: Unbekannter Platzhalter {key_err}")
            except Exception as format_err:
                st.error(f"Fehler bei der Formatierung: {format_err}")

        except FileNotFoundError:
            st.error("Die LaTeX-Vorlagendatei wurde nicht gefunden.")
        except Exception as e:
            st.error(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
