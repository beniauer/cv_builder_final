import streamlit as st
import requests

# URL of the LinkedIn logo
logo_url = 'https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png'

# Api Key and headers
api_key = 'OQfhKnmj2k9bUHmlHH9Qbg'
headers = {'Authorization': 'Bearer ' + api_key} #dictionary for HTTP headers
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin/company/job' #adress of procxycurls api endpoint

# Linkedin Country ID is filled into a dictionary
country_geo_id_mapping = {
    'Global': '92000000',
    'Austria': '103883259',
    'France': '105015875',
    'Germany': '101282230',
    'Italy': '103350119',
    'Switzerland': '106693272',
    'USA': '103644278'
}

# Initialize session state variables to make sure they all have defined values when a user uses them the first time -> hinted by chatgpt
if 'jobs' not in st.session_state:
    st.session_state['jobs'] = []
    st.session_state['next_page_url'] = None
    st.session_state['search_initiated'] = False

# Title and logo layout
header_col, logo_col = st.columns([0.85, 0.1]) #defines the columns on the st. app
with header_col:
    st.markdown("# **Job Search**")  # Make bold
with logo_col:
    st.image(logo_url, width=60)  # adjusts with

# Create search fields for user input
country = st.selectbox('Country', list(country_geo_id_mapping.keys())) #dropdownmenu for country with keys out of the dict. created above
job_type = st.selectbox('Employment type', ['Anything', 'Full Time', 'Part Time', 'Internship', 'Contract', 'Temporary', 'Volunteer']) #dropdown with available options
experience_level = st.selectbox('Experience level', ['Anything', 'Internship', 'Entry Level', 'Associate', 'Mid-Senior Level', 'Director']) #dropdown with available options
when = st.selectbox('Job posted on', ['Anytime', 'Yesterday', 'Past-Week', 'Past-Month']) #dropdown with available options
flexibility = st.selectbox('Flexibility', ['Anything', 'Remote', 'On-Site', 'Hybrid']) #dropdown with available options
keyword = st.text_input('Keywords', '') #field for user input

# Button to perform the API call
if st.button('Search Jobs'): #if button is pressed
    st.session_state['search_initiated'] = True #initiates search
    st.session_state['jobs'] = []  # resets list
    selected_geo_id = country_geo_id_mapping[country]  # Use the selected country's geo_id
    params = { #code below retrieves the parameters set above for the api call and makes text compliant with allowed text -> _ instead of " "
        'job_type': job_type.replace(' ', '_').lower(),
        'experience_level': experience_level.replace(' ', '_').lower(),
        'when': when.replace(' ', '_').lower(),
        'flexibility': flexibility.replace(' ', '_').lower(),
        'geo_id': selected_geo_id,
        'keyword': keyword
    }
    response = requests.get(api_endpoint, params=params, headers=headers) #getrequest to the proxycurl api: code below is built based on proycurl API doc: https://nubela.co/proxycurl/docs?utm_campaign=own_platforms&utm_source=medium&utm_medium=social&utm_content=post-affiliate_program#jobs-api . chatgpt was used to explain how the api works
    if response.status_code == 200:
        st.session_state['jobs'] = response.json().get('job', []) #gets the json file with the jobs, converts it into dictionary
        st.session_state['next_page_url'] = response.json().get('next_page_api_url') #sets next page for pagination
    else:
        st.error(f"Failed to retrieve jobs: {response.status_code}") #error handling if api call fails

# Container to display jobs below the button
jobs_container = st.container()

# Function to display jobs
def display_jobs(jobs, container): #defines function incl. parameters
    for job in jobs: #for loop that goes through all of the jobs
        container.write(f"**{job['job_title']}** at **{job['company']}**") #adds info about each job to the container. f string for display
        container.write(f"Location: {job['location']}")
        container.write(f"Listed on: {job['list_date']}")
        container.write(f"[Job Details]({job['job_url']})")
        container.write("---------") #seperator line for readability

# checks if there are job listings store in session state and if yes displays them
if st.session_state['jobs']:
    display_jobs(st.session_state['jobs'], jobs_container)

# basically same as above, function to load more jobs. in hindshight this was prbly not the smartest way to do it as it requires another (expensive) api call. maybe would've been possible to load more initially.
def load_more_jobs():
    next_page_url = st.session_state['next_page_url'] #fetches next page of session state
    if next_page_url:
        response = requests.get(next_page_url, headers=headers)
        if response.status_code == 200:
            new_jobs = response.json().get('job', [])
            st.session_state['jobs'].extend(new_jobs)
            st.session_state['next_page_url'] = response.json().get('next_page_api_url')
            display_jobs(st.session_state['jobs'], jobs_container)
        else:
            st.error(f"Failed to load more jobs: {response.status_code}") #errorhandling if api getrequest fails

# Show the 'Load More' button only if a search has been initiated and there's a next page URL
if st.session_state['search_initiated'] and st.session_state['next_page_url']:
    st.button('Load More', on_click=load_more_jobs)

