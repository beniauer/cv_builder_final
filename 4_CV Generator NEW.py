import streamlit as st
import requests

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

    # Function to extract information from API response
    def extract_info(jsondata):
        # Initialize default values for all fields
        extracted_info = {
            'full_name': jsondata.get('full_name', ''),
            'city': jsondata.get('city', ''),
            'state': jsondata.get('state', ''),
            'country': jsondata.get('country', ''),
            'education': jsondata.get('education', []),
            'experiences': jsondata.get('experiences', []),
            'volunteer_work': jsondata.get('volunteer_work', []),
            'certifications': jsondata.get('certifications', []),
            'languages': jsondata.get('languages', []),
            'interests': jsondata.get('interests', [])
        }
        return extracted_info

    # Function to retrieve information
    def retrieve_info(linkedin_profile_url):
        api_key = '_EIqMpWEbOnJLoQvNFz1CQ'
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {'linkedin_profile_url': linkedin_profile_url}
        response = requests.get(api_endpoint, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return extract_info(data)
        else:
            st.error(f"Failed to retrieve profile information: HTTP {response.status_code}")
            return {}

    # Initialize linkedin_data as an empty dictionary to avoid NameError
    linkedin_data = {}

    # Streamlit app layout
    linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url_key')

    if st.button('Retrieve LinkedIn Data', key='retrieve_data_button'):
        linkedin_data = retrieve_info(linkedin_profile_url) or {}

    # Personal Information Section
    st.header('Your CV, Your Story: Complete the Chapters')
    with st.expander("Personal Information", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve individual address components, defaulting to an empty string if not found
        city = linkedin_data.get('city', '')
        state = linkedin_data.get('state', '')
        country = linkedin_data.get('country', '')

        # Construct the address string, only including components that are present
        address_components = [comp for comp in [city, state, country] if comp]  # List comprehension to filter out empty components
        formatted_address = ', '.join(address_components)  # Join the components with a comma only if they are present

        # Streamlit text input fields
        name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key='name_key')
        address = st.text_input("Address", value=formatted_address, key='address_key')
        phone = st.text_input("Phone Number", key='phone_key')
        email = st.text_input("E-Mail", key='email_key')


    # Education Section
    # Assuming the first two education entries in LinkedIn data (if they exist) are to be used
    education_entries = linkedin_data.get('education', [{} for _ in range(2)])

    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # If there are education entries from LinkedIn, use them as default values, otherwise use empty strings
    university1 = education_entries[0].get('school', '') if education_entries else ''
    locationus1 = education_entries[0].get('location', '') if education_entries else ''
    majorus1 = education_entries[0].get('field_of_study', '') if education_entries else ''
    gpa1 = education_entries[0].get('grade', '') if education_entries else ''
    starts_at1 = format_date(education_entries[0].get('starts_at')) if education_entries else ''
    ends_at1 = format_date(education_entries[0].get('ends_at')) if education_entries else ''
    timeus1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    university2 = education_entries[1].get('school', '') if len(education_entries) > 1 else ''
    locationus2 = education_entries[1].get('location', '') if len(education_entries) > 1 else ''
    majorus2 = education_entries[1].get('field_of_study', '') if len(education_entries) > 1 else ''
    gpa2 = education_entries[1].get('grade', '') if len(education_entries) > 1 else ''
    starts_at2 = format_date(education_entries[1].get('starts_at')) if len(education_entries) > 1 else ''
    ends_at2 = format_date(education_entries[1].get('ends_at')) if len(education_entries) > 1 else ''
    timeus2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    with st.expander("Education", expanded=False):  # 'expanded=True' means the section will be expanded by default
        university1 = st.text_input("University/School 1", value=university1, key="unique_key_5")
        locationus1 = st.text_input("Location 1", value=locationus1, key="unique_key_6")
        majorus1 = st.text_input("Study Program 1", value=majorus1, key="unique_key_7")
        timeus1 = st.text_input("Time Frame 1", value=timeus1, key="unique_key_8")
        courses1 = st.text_input("Courses 1", key="unique_key_9")
        gpa1 = st.text_input("GPA 1", value=gpa1, key="unique_key_10")
        clubs1 = st.text_input("Clubs/Activities 1", key="unique_key_11")

        university2 = st.text_input("University/School 2", value=university2, key="unique_key_12")
        locationus2 = st.text_input("Location 2", value=locationus2, key="unique_key_13")
        majorus2 = st.text_input("Study Program 2", value=majorus2, key="unique_key_14")
        timeus2 = st.text_input("Time Frame 2", value=timeus2, key="unique_key_15")
        courses2 = st.text_input("Courses 2", key="unique_key_16")
        gpa2 = st.text_input("GPA 2", value=gpa2, key="unique_key_17")
        clubs2 = st.text_input("Clubs/Activities 2", key="unique_key_18")

    # Professional Experience Section
    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # Retrieve up to three experience entries from LinkedIn data if they exist
    experience_entries = linkedin_data.get('experiences', [{} for _ in range(3)])

    # If there are experience entries from LinkedIn, use them as default values, otherwise use empty strings
    experience1 = experience_entries[0].get('company', '') if experience_entries else ''
    locatione1 = experience_entries[0].get('location', '') if experience_entries else ''
    position1 = experience_entries[0].get('title', '') if experience_entries else ''
    starts_at1 = format_date(experience_entries[0].get('starts_at')) if experience_entries else ''
    ends_at1 = format_date(experience_entries[0].get('ends_at')) if experience_entries else ''
    timee1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    experience2 = experience_entries[1].get('company', '') if len(experience_entries) > 1 else ''
    locatione2 = experience_entries[1].get('location', '') if len(experience_entries) > 1 else ''
    position2 = experience_entries[1].get('title', '') if len(experience_entries) > 1 else ''
    starts_at2 = format_date(experience_entries[1].get('starts_at')) if len(experience_entries) > 1 else ''
    ends_at2 = format_date(experience_entries[1].get('ends_at')) if len(experience_entries) > 1 else ''
    timee2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    experience3 = experience_entries[2].get('company', '') if len(experience_entries) > 2 else ''
    locatione3 = experience_entries[2].get('location', '') if len(experience_entries) > 2 else ''
    position3 = experience_entries[2].get('title', '') if len(experience_entries) > 2 else ''
    starts_at3 = format_date(experience_entries[2].get('starts_at')) if len(experience_entries) > 2 else ''
    ends_at3 = format_date(experience_entries[2].get('ends_at')) if len(experience_entries) > 2 else ''
    timee3 = f"{starts_at3} - {ends_at3}" if ends_at3 else starts_at3

    with st.expander("Professional Experience", expanded=False):  # 'expanded=True' means the section will be expanded by default
        experience1 = st.text_input("Company 1", value=experience1, key="unique_key_131")
        locatione1 = st.text_input("Location 1", value=locatione1, key="unique_key_132")
        position1 = st.text_input("Position 1", value=position1, key="unique_key_133")
        timee1 = st.text_input("Time Frame 1", value=timee1, key="unique_key_134")
        task11 = st.text_area("Tasks 1", key='task11_19', height=100)
        task12 = st.text_area("Tasks 2", key='task12_20', height=100)
        task13 = st.text_area("Tasks 3", key='task13_21', height=100)

        experience2 = st.text_input("Company 2", value=experience2, key="unique_key_135")
        locatione2 = st.text_input("Location 2", value=locatione2, key="unique_key_136")
        position2 = st.text_input("Position 2", value=position2, key="unique_key_137")
        timee2 = st.text_input("Time Frame 2", value=timee2, key="unique_key_138")
        task21 = st.text_area("Tasks 1", key='task21_22', height=100)
        task22 = st.text_area("Tasks 2", key='task22_23', height=100)
        task23 = st.text_area("Tasks 3", key='task23_24', height=100)

        experience3 = st.text_input("Company 3", value=experience3, key="unique_key_139")
        locatione3 = st.text_input("Location 3", value=locatione3, key="unique_key_140")
        position3 = st.text_input("Position 3", value=position3, key="unique_key_141")
        timee3 = st.text_input("Time Frame 3", value=timee3, key="unique_key_142")
        task31 = st.text_area("Tasks 1", key='task31_25', height=100)
        task32 = st.text_area("Tasks 2", key='task32_26', height=100)
        task33 = st.text_area("Tasks 3", key='task33_27', height=100)

    # Extracurricular Activities / Engagement Section
    with st.expander("Extracurricular Activities", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the volunteer work, certifications, languages, and interests from LinkedIn data if they exist
        volunteer_work_entries = linkedin_data.get('volunteer_work', [])  # Assuming it's a list of dictionaries
        certifications_entries = linkedin_data.get('certifications', [])  # Assuming it's a list of dictionaries
        languages_entries = linkedin_data.get('languages', [''])  # Assuming it's a list of titles
        interests_entries = linkedin_data.get('interests', [''])  # Assuming it's a list of titles

        # Extract titles from volunteer work and certifications
        volunteer_work_titles = [entry.get('title', '') for entry in volunteer_work_entries]
        certifications_titles = [entry.get('name', '') for entry in certifications_entries]

        # Combine the first three titles with a comma
        volunteer_work_combined = ', '.join(volunteer_work_titles[0:3])
        certifications_combined = ', '.join(certifications_titles[0:3])

        extracurricular1 = st.text_input("Extracurricular Activities", value=volunteer_work_combined, key="extracurricular_1_key")
        additionaleducation1 = st.text_input("Additional Education", key="additional_education_1_key")  # No specific API data, so left for manual input
        certificates1 = st.text_input("Certificates and Awards", value=certifications_combined, key="certificates_1_key")

    # Skills & Interest Section
    # Wrap the Skills & Interest section in an expander
    with st.expander("Skills & Interest", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the computer skills entries from LinkedIn data if they exist
        computer_skills_entries = linkedin_data.get('computer_skills', [''])  # Assuming it's a list of titles

        # Join the first three entries for languages, interests, and computer skills with a comma
        languages_combined = ', '.join(languages_entries[0:3])
        interests_combined = ', '.join(interests_entries[0:3])
        computer_skills_combined = ', '.join(computer_skills_entries[0:3])

        languages1 = st.text_input("Languages", value=languages_combined, key="languages_1_key")
        computer1 = st.text_input("Computer Skills", value=computer_skills_combined, key="computer_skills_key")
        interests1 = st.text_input("Interests", value=interests_combined, key="interests_1_key")

    # Button zum Erstellen des CVs
    if st.button("Generate CV", key="unique_key_143"):
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

    # Function to extract information from API response
    def extract_info(jsondata):
        # Initialize default values for all fields
        extracted_info = {
            'full_name': jsondata.get('full_name', ''),
            'city': jsondata.get('city', ''),
            'state': jsondata.get('state', ''),
            'country': jsondata.get('country', ''),
            'education': jsondata.get('education', []),
            'experiences': jsondata.get('experiences', []),
            'volunteer_work': jsondata.get('volunteer_work', []),
            'certifications': jsondata.get('certifications', []),
            'languages': jsondata.get('languages', []),
            'interests': jsondata.get('interests', [])
        }
        return extracted_info

    # Function to retrieve information
    def retrieve_info(linkedin_profile_url):
        api_key = '_EIqMpWEbOnJLoQvNFz1CQ'
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {'linkedin_profile_url': linkedin_profile_url}
        response = requests.get(api_endpoint, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return extract_info(data)
        else:
            st.error(f"Failed to retrieve profile information: HTTP {response.status_code}")
            return {}

    # Initialize linkedin_data as an empty dictionary to avoid NameError
    linkedin_data = {}

    # Streamlit app layout
    linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url_key_2')

    if st.button('Retrieve LinkedIn Data', key='retrieve_data_button_2'):
        linkedin_data = retrieve_info(linkedin_profile_url) or {}

    # Personal Information Section
    st.header("Your CV, Your Story: Complete the Chapters")

    # Retrieve individual address components, defaulting to an empty string if not found
    with st.expander("Personal Information", expanded=False):  # 'expanded=True' means the section will be expanded by default
        city = linkedin_data.get('city', '')
        state = linkedin_data.get('state', '')
        country = linkedin_data.get('country', '')

        # Construct the address string, only including components that are present
        address_components = [comp for comp in [city, state, country] if comp]  # List comprehension to filter out empty components
        formatted_address = ', '.join(address_components)  # Join the components with a comma only if they are present

        # Streamlit text input fields
        name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key='name_key_2')
        address = st.text_input("Address", value=formatted_address, key='address_key_2')
        phone = st.text_input("Phone Number", key='phone_key_2')
        email = st.text_input("E-Mail", key='email_key_2')


    # Education Section
    # Assuming the first two education entries in LinkedIn data (if they exist) are to be used
    education_entries = linkedin_data.get('education', [{} for _ in range(2)])

    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # If there are education entries from LinkedIn, use them as default values, otherwise use empty strings
    university1 = education_entries[0].get('school', '') if education_entries else ''
    locationus1 = education_entries[0].get('location', '') if education_entries else ''
    majorus1 = education_entries[0].get('field_of_study', '') if education_entries else ''
    gpa1 = education_entries[0].get('grade', '') if education_entries else ''
    starts_at1 = format_date(education_entries[0].get('starts_at')) if education_entries else ''
    ends_at1 = format_date(education_entries[0].get('ends_at')) if education_entries else ''
    timeus1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    university2 = education_entries[1].get('school', '') if len(education_entries) > 1 else ''
    locationus2 = education_entries[1].get('location', '') if len(education_entries) > 1 else ''
    majorus2 = education_entries[1].get('field_of_study', '') if len(education_entries) > 1 else ''
    gpa2 = education_entries[1].get('grade', '') if len(education_entries) > 1 else ''
    starts_at2 = format_date(education_entries[1].get('starts_at')) if len(education_entries) > 1 else ''
    ends_at2 = format_date(education_entries[1].get('ends_at')) if len(education_entries) > 1 else ''
    timeus2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    with st.expander("Education", expanded=False):  # 'expanded=True' means the section will be expanded by default
        university1 = st.text_input("University/School 1", value=university1, key="unique_key_144")
        locationus1 = st.text_input("Location 1", value=locationus1, key="unique_key_145")
        majorus1 = st.text_input("Study Program 1", value=majorus1, key="unique_key_146")
        timeus1 = st.text_input("Time Frame 1", value=timeus1, key="unique_key_147")
        courses1 = st.text_input("Courses 1", key="unique_key_148")
        gpa1 = st.text_input("GPA 1", value=gpa1, key="unique_key_149")
        clubs1 = st.text_input("Clubs/Activities 1", key="unique_key_150")

        university2 = st.text_input("University/School 2", value=university2, key="unique_key_151")
        locationus2 = st.text_input("Location 2", value=locationus2, key="unique_key_152")
        majorus2 = st.text_input("Study Program 2", value=majorus2, key="unique_key_153")
        timeus2 = st.text_input("Time Frame 2", value=timeus2, key="unique_key_154")
        courses2 = st.text_input("Courses 2", key="unique_key_155")
        gpa2 = st.text_input("GPA 2", value=gpa2, key="unique_key_156")
        clubs2 = st.text_input("Clubs/Activities 2", key="unique_key_157")

    # Professional Experience Section
    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # Retrieve up to three experience entries from LinkedIn data if they exist
    experience_entries = linkedin_data.get('experiences', [{} for _ in range(3)])

    # If there are experience entries from LinkedIn, use them as default values, otherwise use empty strings
    experience1 = experience_entries[0].get('company', '') if experience_entries else ''
    locatione1 = experience_entries[0].get('location', '') if experience_entries else ''
    position1 = experience_entries[0].get('title', '') if experience_entries else ''
    starts_at1 = format_date(experience_entries[0].get('starts_at')) if experience_entries else ''
    ends_at1 = format_date(experience_entries[0].get('ends_at')) if experience_entries else ''
    timee1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    experience2 = experience_entries[1].get('company', '') if len(experience_entries) > 1 else ''
    locatione2 = experience_entries[1].get('location', '') if len(experience_entries) > 1 else ''
    position2 = experience_entries[1].get('title', '') if len(experience_entries) > 1 else ''
    starts_at2 = format_date(experience_entries[1].get('starts_at')) if len(experience_entries) > 1 else ''
    ends_at2 = format_date(experience_entries[1].get('ends_at')) if len(experience_entries) > 1 else ''
    timee2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    experience3 = experience_entries[2].get('company', '') if len(experience_entries) > 2 else ''
    locatione3 = experience_entries[2].get('location', '') if len(experience_entries) > 2 else ''
    position3 = experience_entries[2].get('title', '') if len(experience_entries) > 2 else ''
    starts_at3 = format_date(experience_entries[2].get('starts_at')) if len(experience_entries) > 2 else ''
    ends_at3 = format_date(experience_entries[2].get('ends_at')) if len(experience_entries) > 2 else ''
    timee3 = f"{starts_at3} - {ends_at3}" if ends_at3 else starts_at3

    with st.expander("Professional Experience", expanded=False):  # 'expanded=True' means the section will be expanded by default
        experience1 = st.text_input("Company 1", value=experience1, key="unique_key_158")
        locatione1 = st.text_input("Location 1", value=locatione1, key="unique_key_159")
        position1 = st.text_input("Position 1", value=position1, key="unique_key_160")
        timee1 = st.text_input("Time Frame 1", value=timee1, key="unique_key_161")
        task11 = st.text_area("Tasks 1", key='task11_28', height=100)
        task12 = st.text_area("Tasks 2", key='task12_29', height=100)
        task13 = st.text_area("Tasks 3", key='task13_30', height=100)

        experience2 = st.text_input("Company 2", value=experience2, key="unique_key_162")
        locatione2 = st.text_input("Location 2", value=locatione2, key="unique_key_163")
        position2 = st.text_input("Position 2", value=position2, key="unique_key_164")
        timee2 = st.text_input("Time Frame 2", value=timee2, key="unique_key_165")
        task21 = st.text_area("Tasks 1", key='task21_31', height=100)
        task22 = st.text_area("Tasks 2", key='task22_32', height=100)
        task23 = st.text_area("Tasks 3", key='task23_33', height=100)

        experience3 = st.text_input("Company 3", value=experience3, key="unique_key_166")
        locatione3 = st.text_input("Location 3", value=locatione3, key="unique_key_167")
        position3 = st.text_input("Position 3", value=position3, key="unique_key_168")
        timee3 = st.text_input("Time Frame 3", value=timee3, key="unique_key_169")
        task31 = st.text_area("Tasks 1", key='task31_34', height=100)
        task32 = st.text_area("Tasks 2", key='task32_35', height=100)
        task33 = st.text_area("Tasks 3", key='task33_36', height=100)

    # Extracurricular Activities / Engagement Section
    with st.expander("Extracurricular Activities", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the volunteer work, certifications, languages, and interests from LinkedIn data if they exist
        volunteer_work_entries = linkedin_data.get('volunteer_work', [])  # Assuming it's a list of dictionaries
        certifications_entries = linkedin_data.get('certifications', [])  # Assuming it's a list of dictionaries
        languages_entries = linkedin_data.get('languages', [''])  # Assuming it's a list of titles
        interests_entries = linkedin_data.get('interests', [''])  # Assuming it's a list of titles

        # Extract titles from volunteer work and certifications
        volunteer_work_titles = [entry.get('title', '') for entry in volunteer_work_entries]
        certifications_titles = [entry.get('name', '') for entry in certifications_entries]

        # Combine the first three titles with a comma
        volunteer_work_combined = ', '.join(volunteer_work_titles[0:3])
        certifications_combined = ', '.join(certifications_titles[0:3])

        extracurricular1 = st.text_input("Extracurricular Activities", value=volunteer_work_combined, key="extracurricular_2_key")
        additionaleducation1 = st.text_input("Additional Education", key="additional_education_2_key")  # No specific API data, so left for manual input
        certificates1 = st.text_input("Certificates and Awards", value=certifications_combined, key="certificates_2_key")

    # Skills & Interest Section
    # Wrap the Skills & Interest section in an expander
    with st.expander("Skills & Interest", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the computer skills entries from LinkedIn data if they exist
        computer_skills_entries = linkedin_data.get('computer_skills', [''])  # Assuming it's a list of titles

        # Join the first three entries for languages, interests, and computer skills with a comma
        languages_combined = ', '.join(languages_entries[0:3])
        interests_combined = ', '.join(interests_entries[0:3])
        computer_skills_combined = ', '.join(computer_skills_entries[0:3])

        languages1 = st.text_input("Languages", value=languages_combined, key="languages_2_key")
        computer1 = st.text_input("Computer Skills", value=computer_skills_combined, key="computer_skills_key_2")
        interests1 = st.text_input("Interests", value=interests_combined, key="interests_2_key")

    # Button zum Erstellen des CVs
    if st.button("Generate CV", key="unique_key_170"):
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

    # Function to extract information from API response
    def extract_info(jsondata):
        # Initialize default values for all fields
        extracted_info = {
            'full_name': jsondata.get('full_name', ''),
            'city': jsondata.get('city', ''),
            'state': jsondata.get('state', ''),
            'country': jsondata.get('country', ''),
            'education': jsondata.get('education', []),
            'experiences': jsondata.get('experiences', []),
            'volunteer_work': jsondata.get('volunteer_work', []),
            'certifications': jsondata.get('certifications', []),
            'languages': jsondata.get('languages', []),
            'interests': jsondata.get('interests', [])
        }
        return extracted_info

    # Function to retrieve information
    def retrieve_info(linkedin_profile_url):
        api_key = '_EIqMpWEbOnJLoQvNFz1CQ'
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {'linkedin_profile_url': linkedin_profile_url}
        response = requests.get(api_endpoint, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return extract_info(data)
        else:
            st.error(f"Failed to retrieve profile information: HTTP {response.status_code}")
            return {}

    # Initialize linkedin_data as an empty dictionary to avoid NameError
    linkedin_data = {}

    # Streamlit app layout
    linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url_key_3')

    if st.button('Retrieve LinkedIn Data', key='retrieve_data_button_3'):
        linkedin_data = retrieve_info(linkedin_profile_url) or {}

    # Personal Information Section
    st.header("Your CV, Your Story: Complete the Chapters")

    # Retrieve individual address components, defaulting to an empty string if not found
    with st.expander("Personal Information", expanded=False):  # 'expanded=True' means the section will be expanded by default
        city = linkedin_data.get('city', '')
        state = linkedin_data.get('state', '')
        country = linkedin_data.get('country', '')

        # Construct the address string, only including components that are present
        address_components = [comp for comp in [city, state, country] if comp]  # List comprehension to filter out empty components
        formatted_address = ', '.join(address_components)  # Join the components with a comma only if they are present

        # Streamlit text input fields
        name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key='name_key_3')
        address = st.text_input("Address", value=formatted_address, key='address_key_3')
        phone = st.text_input("Phone Number", key='phone_key_3')
        email = st.text_input("E-Mail", key='email_key_3')


    # Education Section
    # Assuming the first two education entries in LinkedIn data (if they exist) are to be used
    education_entries = linkedin_data.get('education', [{} for _ in range(2)])

    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # If there are education entries from LinkedIn, use them as default values, otherwise use empty strings
    university1 = education_entries[0].get('school', '') if education_entries else ''
    locationus1 = education_entries[0].get('location', '') if education_entries else ''
    majorus1 = education_entries[0].get('field_of_study', '') if education_entries else ''
    gpa1 = education_entries[0].get('grade', '') if education_entries else ''
    starts_at1 = format_date(education_entries[0].get('starts_at')) if education_entries else ''
    ends_at1 = format_date(education_entries[0].get('ends_at')) if education_entries else ''
    timeus1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    university2 = education_entries[1].get('school', '') if len(education_entries) > 1 else ''
    locationus2 = education_entries[1].get('location', '') if len(education_entries) > 1 else ''
    majorus2 = education_entries[1].get('field_of_study', '') if len(education_entries) > 1 else ''
    gpa2 = education_entries[1].get('grade', '') if len(education_entries) > 1 else ''
    starts_at2 = format_date(education_entries[1].get('starts_at')) if len(education_entries) > 1 else ''
    ends_at2 = format_date(education_entries[1].get('ends_at')) if len(education_entries) > 1 else ''
    timeus2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    with st.expander("Education", expanded=False):  # 'expanded=True' means the section will be expanded by default
        university1 = st.text_input("University/School 1", value=university1, key="unique_key_171")
        locationus1 = st.text_input("Location 1", value=locationus1, key="unique_key_172")
        majorus1 = st.text_input("Study Program 1", value=majorus1, key="unique_key_173")
        timeus1 = st.text_input("Time Frame 1", value=timeus1, key="unique_key_224")
        courses1 = st.text_input("Courses 1", key="unique_key_174")
        gpa1 = st.text_input("GPA 1", value=gpa1, key="unique_key_175")
        clubs1 = st.text_input("Clubs/Activities 1", key="unique_key_176")

        university2 = st.text_input("University/School 2", value=university2, key="unique_key_177")
        locationus2 = st.text_input("Location 2", value=locationus2, key="unique_key_178")
        majorus2 = st.text_input("Study Program 2", value=majorus2, key="unique_key_179")
        timeus2 = st.text_input("Time Frame 2", value=timeus2, key="unique_key_180")
        courses2 = st.text_input("Courses 2", key="unique_key_181")
        gpa2 = st.text_input("GPA 2", value=gpa2, key="unique_key_182")
        clubs2 = st.text_input("Clubs/Activities 2", key="unique_key_183")

    # Professional Experience Section
    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # Retrieve up to three experience entries from LinkedIn data if they exist
    experience_entries = linkedin_data.get('experiences', [{} for _ in range(3)])

    # If there are experience entries from LinkedIn, use them as default values, otherwise use empty strings
    experience1 = experience_entries[0].get('company', '') if experience_entries else ''
    locatione1 = experience_entries[0].get('location', '') if experience_entries else ''
    position1 = experience_entries[0].get('title', '') if experience_entries else ''
    starts_at1 = format_date(experience_entries[0].get('starts_at')) if experience_entries else ''
    ends_at1 = format_date(experience_entries[0].get('ends_at')) if experience_entries else ''
    timee1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    experience2 = experience_entries[1].get('company', '') if len(experience_entries) > 1 else ''
    locatione2 = experience_entries[1].get('location', '') if len(experience_entries) > 1 else ''
    position2 = experience_entries[1].get('title', '') if len(experience_entries) > 1 else ''
    starts_at2 = format_date(experience_entries[1].get('starts_at')) if len(experience_entries) > 1 else ''
    ends_at2 = format_date(experience_entries[1].get('ends_at')) if len(experience_entries) > 1 else ''
    timee2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    experience3 = experience_entries[2].get('company', '') if len(experience_entries) > 2 else ''
    locatione3 = experience_entries[2].get('location', '') if len(experience_entries) > 2 else ''
    position3 = experience_entries[2].get('title', '') if len(experience_entries) > 2 else ''
    starts_at3 = format_date(experience_entries[2].get('starts_at')) if len(experience_entries) > 2 else ''
    ends_at3 = format_date(experience_entries[2].get('ends_at')) if len(experience_entries) > 2 else ''
    timee3 = f"{starts_at3} - {ends_at3}" if ends_at3 else starts_at3

    with st.expander("Professional Experience", expanded=False):  # 'expanded=True' means the section will be expanded by default
        experience1 = st.text_input("Company 1", value=experience1, key="unique_key_184")
        locatione1 = st.text_input("Location 1", value=locatione1, key="unique_key_185")
        position1 = st.text_input("Position 1", value=position1, key="unique_key_186")
        timee1 = st.text_input("Time Frame 1", value=timee1, key="unique_key_187")
        task11 = st.text_area("Taks 1", key='task11_37', height=100)
        task12 = st.text_area("Taks 2", key='task12_38', height=100)
        task13 = st.text_area("Taks 3", key='task13_39', height=100)

        experience2 = st.text_input("Company 2", value=experience2, key="unique_key_188")
        locatione2 = st.text_input("Location 2", value=locatione2, key="unique_key_189")
        position2 = st.text_input("Position 2", value=position2, key="unique_key_190")
        timee2 = st.text_input("Time Frame 2", value=timee2, key="unique_key_191")
        task21 = st.text_area("Taks 1", key='task21_40', height=100)
        task22 = st.text_area("Taks 2", key='task22_41', height=100)
        task23 = st.text_area("Taks 3", key='task23_42', height=100)

        experience3 = st.text_input("Company 3", value=experience3, key="unique_key_192")
        locatione3 = st.text_input("Location 3", value=locatione3, key="unique_key_193")
        position3 = st.text_input("Position 3", value=position3, key="unique_key_194")
        timee3 = st.text_input("Time Frame 3", value=timee3, key="unique_key_195")
        task31 = st.text_area("Taks 1", key='task31_43', height=100)
        task32 = st.text_area("Taks 2", key='task32_44', height=100)
        task33 = st.text_area("Taks 3", key='task33_45', height=100)

    # Extracurricular Activities / Engagement Section
    with st.expander("Extracurricular Activities", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the volunteer work, certifications, languages, and interests from LinkedIn data if they exist
        volunteer_work_entries = linkedin_data.get('volunteer_work', [])  # Assuming it's a list of dictionaries
        certifications_entries = linkedin_data.get('certifications', [])  # Assuming it's a list of dictionaries
        languages_entries = linkedin_data.get('languages', [''])  # Assuming it's a list of titles
        interests_entries = linkedin_data.get('interests', [''])  # Assuming it's a list of titles

        # Extract titles from volunteer work and certifications
        volunteer_work_titles = [entry.get('title', '') for entry in volunteer_work_entries]
        certifications_titles = [entry.get('name', '') for entry in certifications_entries]

        # Combine the first three titles with a comma
        volunteer_work_combined = ', '.join(volunteer_work_titles[0:3])
        certifications_combined = ', '.join(certifications_titles[0:3])

        extracurricular1 = st.text_input("Extracurricular Activities", value=volunteer_work_combined, key="extracurricular_3_key")
        additionaleducation1 = st.text_input("Additional Education", key="additional_education_3_key")  # No specific API data, so left for manual input
        certificates1 = st.text_input("Certificates and Awards", value=certifications_combined, key="certificates_3_key")

    # Skills & Interest Section
    # Wrap the Skills & Interest section in an expander
    with st.expander("Skills & Interest", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the computer skills entries from LinkedIn data if they exist
        computer_skills_entries = linkedin_data.get('computer_skills', [''])  # Assuming it's a list of titles

        # Join the first three entries for languages, interests, and computer skills with a comma
        languages_combined = ', '.join(languages_entries[0:3])
        interests_combined = ', '.join(interests_entries[0:3])
        computer_skills_combined = ', '.join(computer_skills_entries[0:3])

        languages1 = st.text_input("Languages", value=languages_combined, key="languages_3_key")
        computer1 = st.text_input("Computer Skills", value=computer_skills_combined, key="computer_skills_key_3")
        interests1 = st.text_input("Interests", value=interests_combined, key="interests_3_key")

    # Button zum Erstellen des CVs
    if st.button("Generate CV", key="unique_key_196"):
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

    # Function to extract information from API response
    def extract_info(jsondata):
        # Initialize default values for all fields
        extracted_info = {
            'full_name': jsondata.get('full_name', ''),
            'city': jsondata.get('city', ''),
            'state': jsondata.get('state', ''),
            'country': jsondata.get('country', ''),
            'education': jsondata.get('education', []),
            'experiences': jsondata.get('experiences', []),
            'volunteer_work': jsondata.get('volunteer_work', []),
            'certifications': jsondata.get('certifications', []),
            'languages': jsondata.get('languages', []),
            'interests': jsondata.get('interests', [])
        }
        return extracted_info

    # Function to retrieve information
    def retrieve_info(linkedin_profile_url):
        api_key = '_EIqMpWEbOnJLoQvNFz1CQ'
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {'linkedin_profile_url': linkedin_profile_url}
        response = requests.get(api_endpoint, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return extract_info(data)
        else:
            st.error(f"Failed to retrieve profile information: HTTP {response.status_code}")
            return {}

    # Initialize linkedin_data as an empty dictionary to avoid NameError
    linkedin_data = {}

    # Streamlit app layout
    linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url_key_4')

    if st.button('Retrieve LinkedIn Data', key='retrieve_data_button_4'):
        linkedin_data = retrieve_info(linkedin_profile_url) or {}

    # Personal Information Section
    st.header("Your CV, Your Story: Complete the Chapters")

    # Retrieve individual address components, defaulting to an empty string if not found
    with st.expander("Personal Information", expanded=False):  # 'expanded=True' means the section will be expanded by default
        city = linkedin_data.get('city', '')
        state = linkedin_data.get('state', '')
        country = linkedin_data.get('country', '')

        # Construct the address string, only including components that are present
        address_components = [comp for comp in [city, state, country] if comp]  # List comprehension to filter out empty components
        formatted_address = ', '.join(address_components)  # Join the components with a comma only if they are present

        # Streamlit text input fields
        name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key='name_key_4')
        address = st.text_input("Address", value=formatted_address, key='address_key_4')
        phone = st.text_input("Phone Number", key='phone_key_4')
        email = st.text_input("E-Mail", key='email_key_4')

    # Education Section
    # Assuming the first two education entries in LinkedIn data (if they exist) are to be used
    education_entries = linkedin_data.get('education', [{} for _ in range(2)])

    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # If there are education entries from LinkedIn, use them as default values, otherwise use empty strings
    university1 = education_entries[0].get('school', '') if education_entries else ''
    locationus1 = education_entries[0].get('location', '') if education_entries else ''
    majorus1 = education_entries[0].get('field_of_study', '') if education_entries else ''
    gpa1 = education_entries[0].get('grade', '') if education_entries else ''
    starts_at1 = format_date(education_entries[0].get('starts_at')) if education_entries else ''
    ends_at1 = format_date(education_entries[0].get('ends_at')) if education_entries else ''
    timeus1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    university2 = education_entries[1].get('school', '') if len(education_entries) > 1 else ''
    locationus2 = education_entries[1].get('location', '') if len(education_entries) > 1 else ''
    majorus2 = education_entries[1].get('field_of_study', '') if len(education_entries) > 1 else ''
    gpa2 = education_entries[1].get('grade', '') if len(education_entries) > 1 else ''
    starts_at2 = format_date(education_entries[1].get('starts_at')) if len(education_entries) > 1 else ''
    ends_at2 = format_date(education_entries[1].get('ends_at')) if len(education_entries) > 1 else ''
    timeus2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    with st.expander("Education", expanded=False):  # 'expanded=True' means the section will be expanded by default
        university1 = st.text_input("University/School 1", value=university1, key="unique_key_197")
        locationus1 = st.text_input("Location 1", value=locationus1, key="unique_key_198")
        majorus1 = st.text_input("Study Program 1", value=majorus1, key="unique_key_199")
        timeus1 = st.text_input("Time Frame 1", value=timeus1, key="unique_key_200")
        courses1 = st.text_input("Courses 1", key="unique_key_201")
        gpa1 = st.text_input("GPA 1", value=gpa1, key="unique_key_202")
        clubs1 = st.text_input("Clubs/Activities 1", key="unique_key_203")

        university2 = st.text_input("University/School 2", value=university2, key="unique_key_204")
        locationus2 = st.text_input("Location 2", value=locationus2, key="unique_key_205")
        majorus2 = st.text_input("Study Program 2", value=majorus2, key="unique_key_206")
        timeus2 = st.text_input("Time Frame 2", value=timeus2, key="unique_key_207")
        courses2 = st.text_input("Courses 2", key="unique_key_208")
        gpa2 = st.text_input("GPA 2", value=gpa2, key="unique_key_209")
        clubs2 = st.text_input("Clubs/Activities 2", key="unique_key_210")

    # Professional Experience Section
    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # Retrieve up to three experience entries from LinkedIn data if they exist
    experience_entries = linkedin_data.get('experiences', [{} for _ in range(3)])

    # If there are experience entries from LinkedIn, use them as default values, otherwise use empty strings
    experience1 = experience_entries[0].get('company', '') if experience_entries else ''
    locatione1 = experience_entries[0].get('location', '') if experience_entries else ''
    position1 = experience_entries[0].get('title', '') if experience_entries else ''
    starts_at1 = format_date(experience_entries[0].get('starts_at')) if experience_entries else ''
    ends_at1 = format_date(experience_entries[0].get('ends_at')) if experience_entries else ''
    timee1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    experience2 = experience_entries[1].get('company', '') if len(experience_entries) > 1 else ''
    locatione2 = experience_entries[1].get('location', '') if len(experience_entries) > 1 else ''
    position2 = experience_entries[1].get('title', '') if len(experience_entries) > 1 else ''
    starts_at2 = format_date(experience_entries[1].get('starts_at')) if len(experience_entries) > 1 else ''
    ends_at2 = format_date(experience_entries[1].get('ends_at')) if len(experience_entries) > 1 else ''
    timee2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    experience3 = experience_entries[2].get('company', '') if len(experience_entries) > 2 else ''
    locatione3 = experience_entries[2].get('location', '') if len(experience_entries) > 2 else ''
    position3 = experience_entries[2].get('title', '') if len(experience_entries) > 2 else ''
    starts_at3 = format_date(experience_entries[2].get('starts_at')) if len(experience_entries) > 2 else ''
    ends_at3 = format_date(experience_entries[2].get('ends_at')) if len(experience_entries) > 2 else ''
    timee3 = f"{starts_at3} - {ends_at3}" if ends_at3 else starts_at3

    with st.expander("Professional Experience", expanded=False):  # 'expanded=True' means the section will be expanded by default
        experience1 = st.text_input("Company 1", value=experience1, key="unique_key_211")
        locatione1 = st.text_input("Location 1", value=locatione1, key="unique_key_212")
        position1 = st.text_input("Position 1", value=position1, key="unique_key_213")
        timee1 = st.text_input("Time Frame 1", value=timee1, key="unique_key_214")
        task11 = st.text_area("Tasks 1", key='task11_46', height=100)
        task12 = st.text_area("Tasks 2", key='task12_47', height=100)
        task13 = st.text_area("Tasks 3", key='task13_48', height=100)

        experience2 = st.text_input("Company 2", value=experience2, key="unique_key_215")
        locatione2 = st.text_input("Location 2", value=locatione2, key="unique_key_216")
        position2 = st.text_input("Position 2", value=position2, key="unique_key_217")
        timee2 = st.text_input("Time Frame 2", value=timee2, key="unique_key_218")
        task21 = st.text_area("Tasks 1", key='task21_49', height=100)
        task22 = st.text_area("Tasks 2", key='task22_50', height=100)
        task23 = st.text_area("Tasks 3", key='task23_51', height=100)

        experience3 = st.text_input("Company 3", value=experience3, key="unique_key_219")
        locatione3 = st.text_input("Location 3", value=locatione3, key="unique_key_220")
        position3 = st.text_input("Position 3", value=position3, key="unique_key_221")
        timee3 = st.text_input("Time Frame 3", value=timee3, key="unique_key_222")
        task31 = st.text_area("Tasks 1", key='task31_52', height=100)
        task32 = st.text_area("Tasks 2", key='task32_53', height=100)
        task33 = st.text_area("Tasks 3", key='task33_54', height=100)

    # Extracurricular Activities / Engagement Section
    with st.expander("Extracurricular Activities", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the volunteer work, certifications, languages, and interests from LinkedIn data if they exist
        volunteer_work_entries = linkedin_data.get('volunteer_work', [])  # Assuming it's a list of dictionaries
        certifications_entries = linkedin_data.get('certifications', [])  # Assuming it's a list of dictionaries
        languages_entries = linkedin_data.get('languages', [''])  # Assuming it's a list of titles
        interests_entries = linkedin_data.get('interests', [''])  # Assuming it's a list of titles

        # Extract titles from volunteer work and certifications
        volunteer_work_titles = [entry.get('title', '') for entry in volunteer_work_entries]
        certifications_titles = [entry.get('name', '') for entry in certifications_entries]

        # Combine the first three titles with a comma
        volunteer_work_combined = ', '.join(volunteer_work_titles[0:3])
        certifications_combined = ', '.join(certifications_titles[0:3])

        extracurricular1 = st.text_input("Extracurricular Activities", value=volunteer_work_combined, key="extracurricular_4_key")
        additionaleducation1 = st.text_input("Additional Education", key="additional_education_4_key")  # No specific API data, so left for manual input
        certificates1 = st.text_input("Certificates und Awards", value=certifications_combined, key="certificates_4_key")

    # Skills & Interest Section
    # Wrap the Skills & Interest section in an expander
    with st.expander("Skills & Interest", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the computer skills entries from LinkedIn data if they exist
        computer_skills_entries = linkedin_data.get('computer_skills', [''])  # Assuming it's a list of titles

        # Join the first three entries for languages, interests, and computer skills with a comma
        languages_combined = ', '.join(languages_entries[0:3])
        interests_combined = ', '.join(interests_entries[0:3])
        computer_skills_combined = ', '.join(computer_skills_entries[0:3])

        languages1 = st.text_input("Languages", value=languages_combined, key="languages_4_key")
        computer1 = st.text_input("Computer Skills", value=computer_skills_combined, key="computer_skills_key_4")
        interests1 = st.text_input("Interests", value=interests_combined, key="interests_4_key")

    # Button zum Erstellen des CVs
    if st.button("Generate CV", key="unique_key_223"):
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

    # Function to extract information from API response
    def extract_info(jsondata):
        # Initialize default values for all fields
        extracted_info = {
            'full_name': jsondata.get('full_name', ''),
            'city': jsondata.get('city', ''),
            'state': jsondata.get('state', ''),
            'country': jsondata.get('country', ''),
            'education': jsondata.get('education', []),
            'experiences': jsondata.get('experiences', []),
            'volunteer_work': jsondata.get('volunteer_work', []),
            'certifications': jsondata.get('certifications', []),
            'languages': jsondata.get('languages', []),
            'interests': jsondata.get('interests', [])
        }
        return extracted_info

    # Function to retrieve information
    def retrieve_info(linkedin_profile_url):
        api_key = '_EIqMpWEbOnJLoQvNFz1CQ'
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {'linkedin_profile_url': linkedin_profile_url}
        response = requests.get(api_endpoint, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return extract_info(data)
        else:
            st.error(f"Failed to retrieve profile information: HTTP {response.status_code}")
            return {}

    # Initialize linkedin_data as an empty dictionary to avoid NameError
    linkedin_data = {}

    # Streamlit app layout
    linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url_key_5')

    if st.button('Retrieve LinkedIn Data', key='retrieve_data_button_5'):
        linkedin_data = retrieve_info(linkedin_profile_url) or {}

    # Personal Information Section
    st.header("Your CV, Your Story: Complete the Chapters")

    # Retrieve individual address components, defaulting to an empty string if not found
    with st.expander("Personal Information", expanded=False):  # 'expanded=True' means the section will be expanded by default
        city = linkedin_data.get('city', '')
        state = linkedin_data.get('state', '')
        country = linkedin_data.get('country', '')

        # Construct the address string, only including components that are present
        address_components = [comp for comp in [city, state, country] if comp]  # List comprehension to filter out empty components
        formatted_address = ', '.join(address_components)  # Join the components with a comma only if they are present

        # Streamlit text input fields
        name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key='name_key_5')
        address = st.text_input("Address", value=formatted_address, key='address_key_5')
        phone = st.text_input("Phone Number", key='phone_key_5')
        email = st.text_input("E-Mail", key='email_key_5')

    # Education Section
    # Assuming the first two education entries in LinkedIn data (if they exist) are to be used
    education_entries = linkedin_data.get('education', [{} for _ in range(2)])

    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # If there are education entries from LinkedIn, use them as default values, otherwise use empty strings
    university1 = education_entries[0].get('school', '') if education_entries else ''
    locationus1 = education_entries[0].get('location', '') if education_entries else ''
    majorus1 = education_entries[0].get('field_of_study', '') if education_entries else ''
    gpa1 = education_entries[0].get('grade', '') if education_entries else ''
    starts_at1 = format_date(education_entries[0].get('starts_at')) if education_entries else ''
    ends_at1 = format_date(education_entries[0].get('ends_at')) if education_entries else ''
    timeus1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    university2 = education_entries[1].get('school', '') if len(education_entries) > 1 else ''
    locationus2 = education_entries[1].get('location', '') if len(education_entries) > 1 else ''
    majorus2 = education_entries[1].get('field_of_study', '') if len(education_entries) > 1 else ''
    gpa2 = education_entries[1].get('grade', '') if len(education_entries) > 1 else ''
    starts_at2 = format_date(education_entries[1].get('starts_at')) if len(education_entries) > 1 else ''
    ends_at2 = format_date(education_entries[1].get('ends_at')) if len(education_entries) > 1 else ''
    timeus2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    with st.expander("Education", expanded=False):  # 'expanded=True' means the section will be expanded by default
        university1 = st.text_input("University/School 1", value=university1, key="unique_key_225")
        locationus1 = st.text_input("Location 1", value=locationus1, key="unique_key_226")
        majorus1 = st.text_input("Study Program 1", value=majorus1, key="unique_key_227")
        timeus1 = st.text_input("Time Frame 1", value=timeus1, key="unique_key_228")
        courses1 = st.text_input("Courses 1", key="unique_key_229")
        gpa1 = st.text_input("GPA 1", value=gpa1, key="unique_key_230")
        clubs1 = st.text_input("Clubs/Activities 1", key="unique_key_231")

        university2 = st.text_input("University/School 2", value=university2, key="unique_key_232")
        locationus2 = st.text_input("Location 2", value=locationus2, key="unique_key_233")
        majorus2 = st.text_input("Study Program 2", value=majorus2, key="unique_key_234")
        timeus2 = st.text_input("Time Frame 2", value=timeus2, key="unique_key_235")
        courses2 = st.text_input("Courses 2", key="unique_key_236")
        gpa2 = st.text_input("GPA 2", value=gpa2, key="unique_key_237")
        clubs2 = st.text_input("Clubs/Activities 2", key="unique_key_238")

    # Professional Experience Section
    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # Retrieve up to three experience entries from LinkedIn data if they exist
    experience_entries = linkedin_data.get('experiences', [{} for _ in range(3)])

    # If there are experience entries from LinkedIn, use them as default values, otherwise use empty strings
    experience1 = experience_entries[0].get('company', '') if experience_entries else ''
    locatione1 = experience_entries[0].get('location', '') if experience_entries else ''
    position1 = experience_entries[0].get('title', '') if experience_entries else ''
    starts_at1 = format_date(experience_entries[0].get('starts_at')) if experience_entries else ''
    ends_at1 = format_date(experience_entries[0].get('ends_at')) if experience_entries else ''
    timee1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    experience2 = experience_entries[1].get('company', '') if len(experience_entries) > 1 else ''
    locatione2 = experience_entries[1].get('location', '') if len(experience_entries) > 1 else ''
    position2 = experience_entries[1].get('title', '') if len(experience_entries) > 1 else ''
    starts_at2 = format_date(experience_entries[1].get('starts_at')) if len(experience_entries) > 1 else ''
    ends_at2 = format_date(experience_entries[1].get('ends_at')) if len(experience_entries) > 1 else ''
    timee2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    experience3 = experience_entries[2].get('company', '') if len(experience_entries) > 2 else ''
    locatione3 = experience_entries[2].get('location', '') if len(experience_entries) > 2 else ''
    position3 = experience_entries[2].get('title', '') if len(experience_entries) > 2 else ''
    starts_at3 = format_date(experience_entries[2].get('starts_at')) if len(experience_entries) > 2 else ''
    ends_at3 = format_date(experience_entries[2].get('ends_at')) if len(experience_entries) > 2 else ''
    timee3 = f"{starts_at3} - {ends_at3}" if ends_at3 else starts_at3

    with st.expander("Professional Experience", expanded=False):  # 'expanded=True' means the section will be expanded by default
        experience1 = st.text_input("Company 1", value=experience1, key="unique_key_239")
        locatione1 = st.text_input("Location 1", value=locatione1, key="unique_key_240")
        position1 = st.text_input("Position 1", value=position1, key="unique_key_241")
        timee1 = st.text_input("Time Frame 1", value=timee1, key="unique_key_242")
        task11 = st.text_area("Tasks 1", key='task11_55', height=100)
        task12 = st.text_area("Tasks 2", key='task12_56', height=100)
        task13 = st.text_area("Tasks 3", key='task13_57', height=100)

        experience2 = st.text_input("Company 2", value=experience2, key="unique_key_243")
        locatione2 = st.text_input("Location 2", value=locatione2, key="unique_key_244")
        position2 = st.text_input("Position 2", value=position2, key="unique_key_245")
        timee2 = st.text_input("Time Frame 2", value=timee2, key="unique_key_255")
        task21 = st.text_area("Tasks 1", key='task21_58', height=100)
        task22 = st.text_area("Tasks 2", key='task22_59', height=100)
        task23 = st.text_area("Tasks 3", key='task23_60', height=100)

        experience3 = st.text_input("Company 3", value=experience3, key="unique_key_256")
        locatione3 = st.text_input("Location 3", value=locatione3, key="unique_key_257")
        position3 = st.text_input("Position 3", value=position3, key="unique_key_258")
        timee3 = st.text_input("Time Frame 3", value=timee3, key="unique_key_259")
        task31 = st.text_area("Tasks 1", key='task31_61', height=100)
        task32 = st.text_area("Tasks 2", key='task32_62', height=100)
        task33 = st.text_area("Tasks 3", key='task33_63', height=100)

    # Extracurricular Activities / Engagement Section
    with st.expander("Extracurricular Activities", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the volunteer work, certifications, languages, and interests from LinkedIn data if they exist
        volunteer_work_entries = linkedin_data.get('volunteer_work', [])  # Assuming it's a list of dictionaries
        certifications_entries = linkedin_data.get('certifications', [])  # Assuming it's a list of dictionaries
        languages_entries = linkedin_data.get('languages', [''])  # Assuming it's a list of titles
        interests_entries = linkedin_data.get('interests', [''])  # Assuming it's a list of titles

        # Extract titles from volunteer work and certifications
        volunteer_work_titles = [entry.get('title', '') for entry in volunteer_work_entries]
        certifications_titles = [entry.get('name', '') for entry in certifications_entries]

        # Combine the first three titles with a comma
        volunteer_work_combined = ', '.join(volunteer_work_titles[0:3])
        certifications_combined = ', '.join(certifications_titles[0:3])

        extracurricular1 = st.text_input("Extracurricular Activities", value=volunteer_work_combined, key="extracurricular_5_key")
        additionaleducation1 = st.text_input("Additional Education", key="additional_education_5_key")  # No specific API data, so left for manual input
        certificates1 = st.text_input("Certificates and Awards", value=certifications_combined, key="certificates_5_key")

    # Skills & Interest Section
    # Wrap the Skills & Interest section in an expander
    with st.expander("Skills & Interest", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the computer skills entries from LinkedIn data if they exist
        computer_skills_entries = linkedin_data.get('computer_skills', [''])  # Assuming it's a list of titles

        # Join the first three entries for languages, interests, and computer skills with a comma
        languages_combined = ', '.join(languages_entries[0:3])
        interests_combined = ', '.join(interests_entries[0:3])
        computer_skills_combined = ', '.join(computer_skills_entries[0:3])

        languages1 = st.text_input("Languages", value=languages_combined, key="languages_5_key")
        computer1 = st.text_input("Computer Skills", value=computer_skills_combined, key="computer_skills_key_5")
        interests1 = st.text_input("Interests", value=interests_combined, key="interests_5_key")

    # Button zum Erstellen des CVs
    if st.button("Generate CV", key="unique_key_260"):
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

    # Function to extract information from API response
    def extract_info(jsondata):
        # Initialize default values for all fields
        extracted_info = {
            'full_name': jsondata.get('full_name', ''),
            'city': jsondata.get('city', ''),
            'state': jsondata.get('state', ''),
            'country': jsondata.get('country', ''),
            'education': jsondata.get('education', []),
            'experiences': jsondata.get('experiences', []),
            'volunteer_work': jsondata.get('volunteer_work', []),
            'certifications': jsondata.get('certifications', []),
            'languages': jsondata.get('languages', []),
            'interests': jsondata.get('interests', [])
        }
        return extracted_info

    # Function to retrieve information
    def retrieve_info(linkedin_profile_url):
        api_key = '_EIqMpWEbOnJLoQvNFz1CQ'
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {'linkedin_profile_url': linkedin_profile_url}
        response = requests.get(api_endpoint, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return extract_info(data)
        else:
            st.error(f"Failed to retrieve profile information: HTTP {response.status_code}")
            return {}

    # Initialize linkedin_data as an empty dictionary to avoid NameError
    linkedin_data = {}

    # Streamlit app layout
    linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url_key_6')

    if st.button('Retrieve LinkedIn Data', key='retrieve_data_button_6'):
        linkedin_data = retrieve_info(linkedin_profile_url) or {}

    # Personal Information Section
    st.header("Your CV, Your Story: Complete the Chapters")

    # Retrieve individual address components, defaulting to an empty string if not found
    with st.expander("Personal Information", expanded=False):  # 'expanded=True' means the section will be expanded by default
        city = linkedin_data.get('city', '')
        state = linkedin_data.get('state', '')
        country = linkedin_data.get('country', '')

        # Construct the address string, only including components that are present
        address_components = [comp for comp in [city, state, country] if comp]  # List comprehension to filter out empty components
        formatted_address = ', '.join(address_components)  # Join the components with a comma only if they are present

        # Streamlit text input fields
        name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key='name_key_6')
        address = st.text_input("Address", value=formatted_address, key='address_key_6')
        phone = st.text_input("Phone Number", key='phone_key_6')
        email = st.text_input("E-Mail", key='email_key_6')


    # Education Section
    # Assuming the first two education entries in LinkedIn data (if they exist) are to be used
    education_entries = linkedin_data.get('education', [{} for _ in range(2)])

    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # If there are education entries from LinkedIn, use them as default values, otherwise use empty strings
    university1 = education_entries[0].get('school', '') if education_entries else ''
    locationus1 = education_entries[0].get('location', '') if education_entries else ''
    majorus1 = education_entries[0].get('field_of_study', '') if education_entries else ''
    gpa1 = education_entries[0].get('grade', '') if education_entries else ''
    starts_at1 = format_date(education_entries[0].get('starts_at')) if education_entries else ''
    ends_at1 = format_date(education_entries[0].get('ends_at')) if education_entries else ''
    timeus1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    university2 = education_entries[1].get('school', '') if len(education_entries) > 1 else ''
    locationus2 = education_entries[1].get('location', '') if len(education_entries) > 1 else ''
    majorus2 = education_entries[1].get('field_of_study', '') if len(education_entries) > 1 else ''
    gpa2 = education_entries[1].get('grade', '') if len(education_entries) > 1 else ''
    starts_at2 = format_date(education_entries[1].get('starts_at')) if len(education_entries) > 1 else ''
    ends_at2 = format_date(education_entries[1].get('ends_at')) if len(education_entries) > 1 else ''
    timeus2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    with st.expander("Education", expanded=False):  # 'expanded=True' means the section will be expanded by default
        university1 = st.text_input("University/School 1", value=university1, key="unique_key_261")
        locationus1 = st.text_input("Location 1", value=locationus1, key="unique_key_262")
        majorus1 = st.text_input("Study Program 1", value=majorus1, key="unique_key_263")
        timeus1 = st.text_input("Time Frame 1", value=timeus1, key="unique_key_264")
        courses1 = st.text_input("Courses 1", key="unique_key_265")
        gpa1 = st.text_input("GPA 1", value=gpa1, key="unique_key_266")
        clubs1 = st.text_input("Clubs/Activities 1", key="unique_key_267")

        university2 = st.text_input("University/School 2", value=university2, key="unique_key_268")
        locationus2 = st.text_input("Location 2", value=locationus2, key="unique_key_269")
        majorus2 = st.text_input("Study Program 2", value=majorus2, key="unique_key_270")
        timeus2 = st.text_input("Time Frame 2", value=timeus2, key="unique_key_271")
        courses2 = st.text_input("Courses 2", key="unique_key_272")
        gpa2 = st.text_input("GPA 2", value=gpa2, key="unique_key_273")
        clubs2 = st.text_input("Clubs/Activities 2", key="unique_key_274")

    # Professional Experience Section
    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # Retrieve up to three experience entries from LinkedIn data if they exist
    experience_entries = linkedin_data.get('experiences', [{} for _ in range(3)])

    # If there are experience entries from LinkedIn, use them as default values, otherwise use empty strings
    experience1 = experience_entries[0].get('company', '') if experience_entries else ''
    locatione1 = experience_entries[0].get('location', '') if experience_entries else ''
    position1 = experience_entries[0].get('title', '') if experience_entries else ''
    starts_at1 = format_date(experience_entries[0].get('starts_at')) if experience_entries else ''
    ends_at1 = format_date(experience_entries[0].get('ends_at')) if experience_entries else ''
    timee1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    experience2 = experience_entries[1].get('company', '') if len(experience_entries) > 1 else ''
    locatione2 = experience_entries[1].get('location', '') if len(experience_entries) > 1 else ''
    position2 = experience_entries[1].get('title', '') if len(experience_entries) > 1 else ''
    starts_at2 = format_date(experience_entries[1].get('starts_at')) if len(experience_entries) > 1 else ''
    ends_at2 = format_date(experience_entries[1].get('ends_at')) if len(experience_entries) > 1 else ''
    timee2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    experience3 = experience_entries[2].get('company', '') if len(experience_entries) > 2 else ''
    locatione3 = experience_entries[2].get('location', '') if len(experience_entries) > 2 else ''
    position3 = experience_entries[2].get('title', '') if len(experience_entries) > 2 else ''
    starts_at3 = format_date(experience_entries[2].get('starts_at')) if len(experience_entries) > 2 else ''
    ends_at3 = format_date(experience_entries[2].get('ends_at')) if len(experience_entries) > 2 else ''
    timee3 = f"{starts_at3} - {ends_at3}" if ends_at3 else starts_at3

    with st.expander("Professional Experience", expanded=False):  # 'expanded=True' means the section will be expanded by default
        experience1 = st.text_input("Company 1", value=experience1, key="unique_key_275")
        locatione1 = st.text_input("Location 1", value=locatione1, key="unique_key_276")
        position1 = st.text_input("Position 1", value=position1, key="unique_key_277")
        timee1 = st.text_input("Time Frame 1", value=timee1, key="unique_key_278")
        task11 = st.text_area("Tasks 1", key='task11_89', height=100)
        task12 = st.text_area("Tasks 2", key='task12_90', height=100)
        task13 = st.text_area("Tasks 3", key='task13_91', height=100)

        experience2 = st.text_input("Company 2", value=experience2, key="unique_key_279")
        locatione2 = st.text_input("Location 2", value=locatione2, key="unique_key_280")
        position2 = st.text_input("Position 2", value=position2, key="unique_key_281")
        timee2 = st.text_input("Time Frame 2", value=timee2, key="unique_key_282")
        task21 = st.text_area("Tasks 1", key='task21_92', height=100)
        task22 = st.text_area("Tasks 2", key='task22_93', height=100)
        task23 = st.text_area("Tasks 3", key='task23_94', height=100)

        experience3 = st.text_input("Company 3", value=experience3, key="unique_key_283")
        locatione3 = st.text_input("Location 3", value=locatione3, key="unique_key_284")
        position3 = st.text_input("Position 3", value=position3, key="unique_key_285")
        timee3 = st.text_input("Time Frame 3", value=timee3, key="unique_key_286")
        task31 = st.text_area("Tasks 1", key='task31_95', height=100)
        task32 = st.text_area("Tasks 2", key='task32_96', height=100)
        task33 = st.text_area("Tasks 3", key='task33_97', height=100)

    # Extracurricular Activities / Engagement Section
    with st.expander("Extracurricular Activities", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the volunteer work, certifications, languages, and interests from LinkedIn data if they exist
        volunteer_work_entries = linkedin_data.get('volunteer_work', [])  # Assuming it's a list of dictionaries
        certifications_entries = linkedin_data.get('certifications', [])  # Assuming it's a list of dictionaries
        languages_entries = linkedin_data.get('languages', [''])  # Assuming it's a list of titles
        interests_entries = linkedin_data.get('interests', [''])  # Assuming it's a list of titles

        # Extract titles from volunteer work and certifications
        volunteer_work_titles = [entry.get('title', '') for entry in volunteer_work_entries]
        certifications_titles = [entry.get('name', '') for entry in certifications_entries]

        # Combine the first three titles with a comma
        volunteer_work_combined = ', '.join(volunteer_work_titles[0:3])
        certifications_combined = ', '.join(certifications_titles[0:3])

        extracurricular1 = st.text_input("Extracurricular Activities", value=volunteer_work_combined, key="extracurricular_6_key")
        additionaleducation1 = st.text_input("Additional Education", key="additional_education_6_key")  # No specific API data, so left for manual input
        certificates1 = st.text_input("Certificates and Awards", value=certifications_combined, key="certificates_6_key")

    # Skills & Interest Section
    # Wrap the Skills & Interest section in an expander
    with st.expander("Skills & Interest", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the computer skills entries from LinkedIn data if they exist
        computer_skills_entries = linkedin_data.get('computer_skills', [''])  # Assuming it's a list of titles

        # Join the first three entries for languages, interests, and computer skills with a comma
        languages_combined = ', '.join(languages_entries[0:3])
        interests_combined = ', '.join(interests_entries[0:3])
        computer_skills_combined = ', '.join(computer_skills_entries[0:3])

        languages1 = st.text_input("Languages", value=languages_combined, key="languages_6_key")
        computer1 = st.text_input("Computer Skills", value=computer_skills_combined, key="computer_skills_key_6")
        interests1 = st.text_input("Interests", value=interests_combined, key="interests_6_key")

    # Button zum Erstellen des CVs
    if st.button("Generate CV", key="unique_key_287"):
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
