import requests
import json 

api_key = '_EIqMpWEbOnJLoQvNFz1CQ'
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'linkedin_profile_url': 'https://www.linkedin.com/in/benjamin-david-auer/',
    'use_cache': 'if-recent'  # Added the use_cache parameter
}
#comment next three lines when testing
response = requests.get(api_endpoint,
                       params=params,
                       headers=headers)

def extract_info(jsondata):

    # Set default values to Not available
    extracted_info = {
        'full_name': 'Not available',
        'city':'Not available',
        'state': 'Not available',
        'country': 'Not Available',
        'education': [],
        'occupation': 'Not Available',
        'experiences': [],
        'volunteer_work': 'Not Available',
        'certifications': 'Not Available',
        'languages': 'Not Available',
        'interests': 'Not Available'
    }

    # Replace values if found in response
    if "full_name" in jsondata:
        extracted_info["full_name"] = jsondata["full_name"]
    
    if "city" in jsondata:
        extracted_info["city"]  = jsondata["city"]

    if "state" in jsondata:
        extracted_info["state"]  = jsondata["state"]

    if "country" in jsondata:
        extracted_info["country"]  = jsondata["country"]

    if "education" in jsondata:
        for educations in jsondata ["education"]:
            extracted_info['education'].append({
                'school': educations ["school"],
                'degree_name': educations ["degree_name"],
                'field_of_study': educations["field_of_study"],
                'grade': educations["grade"]
             })
    if "occupation" in jsondata:
        extracted_info["occupation"]  = jsondata["occupation"]

    if "experiences" in jsondata:
        for experience in jsondata["experiences"]:
            extracted_info['experiences'].append({
                'title': experience["title"],
                'company': experience["company"],
                'location': experience["location"]
            })
    if "volunteer_work" in jsondata:
        extracted_info["volunteer_work"]  = jsondata["volunteer_work"]

    if "certifications" in jsondata:
        extracted_info["certifications"]  = jsondata["certifications"]

    if "languages" in jsondata:
        extracted_info["languages"]  = jsondata["languages"]

    if "interests" in jsondata:
        extracted_info["interests"]  = jsondata["interests"]

    return extracted_info 
# Check if the response was successful
if response.status_code == 200:
    jsondata = response.json()
    # Call the extract_info function with the JSON data
    extracted_info = extract_info(jsondata)
    # Print the extracted information - Correct place to put the print function
    print(extracted_info)
else:
    print("Error: Unable to fetch data. Status code:", response.status_code)
