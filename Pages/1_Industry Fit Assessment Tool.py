import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

# Set Streamlit theme to a colorful and attractive style
st.set_page_config(
    page_title="Industry Fit Assessment Tool",
    page_icon="🌟",
    layout="wide",
)

# Customize the background color and text color
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to create radar charts with customizable size and resolution
def plot_radar_chart(categories, scores, title, figure_size=(2, 2), dpi=2000, title_fontsize=4, label_distance=0.5):
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    scores += scores[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(subplot_kw={"polar": True}, figsize=figure_size, dpi=dpi)
    ax.fill(angles, scores, color="green", alpha=0.7, linewidth=2, edgecolor="green")
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=3)  # Reduce label font size
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(["20", "40", "60", "80", "100"], fontsize=4, color="gray")  # Reduce label font size

    # Set the radial label position with label_distance
    ax.set_rlabel_position(label_distance)

    plt.ylim(0, 100)
    plt.title(title, fontsize=title_fontsize, weight="bold", color="#333333")

    # Customize grid lines
    ax.xaxis.grid(color="gray", linestyle="--", linewidth=0.5)
    ax.yaxis.grid(color="gray", linestyle="--", linewidth=0.5)

    # Customize radial labels
    ax.tick_params(axis="y", colors="gray")
    ax.spines["polar"].set_visible(False)

    # Save the figure to a high-resolution image
    img_data = io.BytesIO()
    fig.savefig(img_data, format="png", dpi=dpi, bbox_inches="tight")
    img_data.seek(0)

    # Display the high-resolution image using st.image
    st.image(img_data, width=1000)

# Function to create a bar chart with customizable size, resolution, and fontsize
def plot_bar_chart(labels, values, title, figure_size=(8, 4), dpi=1500, label_fontsize=12, title_fontsize=14):
    fig, ax = plt.subplots(figsize=figure_size, dpi=dpi)
    ax.barh(labels, values, color='green')
    ax.set_xlabel('Scores', fontsize=label_fontsize)  # Set label fontsize
    ax.set_title(title, fontsize=title_fontsize)  # Set title fontsize

    # Customize grid lines and labels
    ax.xaxis.grid(color="gray", linestyle="--", linewidth=0.5)
    ax.yaxis.grid(color="gray", linestyle="--", linewidth=0.5)

    plt.tight_layout()

    # Save the figure to a high-resolution image
    img_data = io.BytesIO()
    fig.savefig(img_data, format="png", dpi=dpi, bbox_inches="tight")
    img_data.seek(0)

    return img_data

# Function to calculate total fit percentages
def calculate_total_fit(user_personality_scores, user_skill_scores, user_work_life_balance_scores, industry_scores):
    fit_percentages = {}
    for industry, (industry_personality, industry_skills, industry_work_life_balance) in industry_scores.items():
        personality_fit = 100 - np.sqrt(np.sum((np.array(user_personality_scores) - np.array(industry_personality)) ** 2))
        skill_fit = 100 - np.sqrt(np.sum((np.array(user_skill_scores) - np.array(industry_skills)) ** 2))
        work_life_balance_fit = 100 - np.sqrt(np.sum((np.array(user_work_life_balance_scores) - np.array(industry_work_life_balance)) ** 2))
        total_fit = (personality_fit + skill_fit + work_life_balance_fit) / 3
        fit_percentages[industry] = max(0, total_fit)
    return fit_percentages

# Function to calculate Big Five scores
def calculate_big_five_scores(responses):
    mapped_responses = [(response / 100) * 100 for response in responses]
    openness_score = np.mean(mapped_responses[0:2])
    conscientiousness_score = np.mean(mapped_responses[2:4])
    extraversion_score = np.mean(mapped_responses[4:6])
    agreeableness_score = np.mean(mapped_responses[6:8])
    neuroticism_score = np.mean(mapped_responses[8:10])
    return {
        "Openness": openness_score,
        "Conscientiousness": conscientiousness_score,
        "Extraversion": extraversion_score,
        "Agreeableness": agreeableness_score,
        "Neuroticism": neuroticism_score,
    }

# Function to get responses from sliders
def get_responses_from_sliders(sliders):
    return [slider for slider in sliders]

header_image = "https://images.pexels.com/photos/277593/pexels-photo-277593.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"


# Main function
def main():
    st.image(header_image)
    st.title("Career Fit Assessment Tool\n Assessment of Industry Fit based on Big 5 Personality Traits, Skills, and Work-Life Balance")

    # Big Five Personality Questions
    personality_questions = [
        "I enjoy taking on new challenges and stepping outside my comfort zone.",
        "I often explore and appreciate new art, music, and creative works.",
        "I have a strong desire to learn new information and expand my knowledge.",
        "I am open to unconventional experiences and enjoy trying new things.",
        "I am organized and pay attention to detail in my work.",
        "I prefer planning and structure over spontaneity.",
        "I enjoy socializing and spending time with others.",
        "I feel energized when surrounded by people and social events.",
        "I tend to worry and feel anxious about various aspects of life.",
        "I find it difficult to relax and often feel tense."
    ]

    personality_sliders = []
    for index, question in enumerate(personality_questions):
        st.markdown(f"### {question}")
        st.write("Rate your agreement on a scale from 1 to 100")
        slider = st.slider("", 1, 100, 50, key=f"personality_slider_{index}")
        personality_sliders.append(slider)

    # Skill Assessment Questions
    skill_questions = [
        "I excel at problem-solving and finding innovative solutions.",
        "I am skilled at critical thinking and analyzing complex issues.",
        "I have experience in leadership roles and can effectively manage teams.",
        "I am adept at clear and persuasive communication.",
        "I am known for my creativity and ability to think outside the box.",
    ]

    skill_sliders = []
    skill_labels = [
        "Problem Solving",
        "Critical Thinking",
        "Leadership",
        "Communication",
        "Creativity",
    ]
    for index, question in enumerate(skill_questions):
        st.markdown(f"### {question}")
        st.write("Rate your proficiency on a scale from 1 to 100")
        slider = st.slider("", 1, 100, 50, key=f"skill_slider_{index}")
        skill_sliders.append(slider)

    # Work-Life Balance Questions
    work_life_balance_questions = [
        "I am able to maintain a healthy work-life balance.",
        "I regularly take breaks and vacations to recharge.",
        "I can disconnect from work-related stress during personal time.",
        "I have time for hobbies and interests outside of work.",
        "I feel content with the amount of time I spend with family and friends.",
    ]

    work_life_balance_sliders = []
    for index, question in enumerate(work_life_balance_questions):
        st.markdown(f"### {question}")
        st.write("Rate the importance of this aspect on a scale from 1 to 100")
        slider = st.slider("", 1, 100, 50, key=f"work_life_balance_slider_{index}")
        work_life_balance_sliders.append(slider)

    if st.button("Submit"):
        personality_responses = get_responses_from_sliders(personality_sliders)
        personality_scores = calculate_big_five_scores(personality_responses)

        skill_responses = get_responses_from_sliders(skill_sliders)
        work_life_balance_responses = get_responses_from_sliders(work_life_balance_sliders)

        # Define industry scores for skills and work-life balance
        industry_scores = {
            "Investment Banking": ([70, 90, 75, 65, 30], [80, 90, 50, 85, 70], [45, 25, 65, 90, 55]),
            "Corporate Job (General)": ([65, 80, 50, 90, 50], [65, 60, 50, 75, 55], [95, 90, 90, 95, 85]),
            "Self-Employed (Entrepreneurship)": ([90, 95, 95, 70, 20], [95, 80, 90, 95, 85], [50, 40, 70, 60, 60]),
            "Computer Science (Tech Industry)": ([50, 90, 55, 85, 30], [90, 90, 45, 75, 90], [70, 70, 75, 80, 70]),
            "Consulting": ([85, 90, 90, 90, 40], [95, 90, 40, 95, 85], [70, 55, 65, 60, 65]),
        }

        total_fit_percentages = calculate_total_fit(
            list(personality_scores.values()), skill_responses, work_life_balance_responses, industry_scores
        )

        # Display Radar Chart for Personality
        plot_radar_chart(
            list(personality_scores.keys()), list(personality_scores.values()), "Your Big Five Personality Traits"
        )
        # Display Skills Profile
        st.subheader("Skills Profile")
        skills_profile_img = plot_bar_chart(skill_labels, skill_responses, "Skills Profile", label_fontsize=10, title_fontsize=12)
        st.image(skills_profile_img, width=900)

        # Display Work-Life Balance Profile
        st.subheader("Work-Life Balance Profile")
        average_work_life_balance = np.mean(work_life_balance_responses)
        st.write(f"Average Importance of Work-Life Balance: {average_work_life_balance:.2f} (out of 100)")

        # Visualize Importance of Work-Life Balance
        importance_values = [average_work_life_balance]
        importance_labels = ["Work-Life Balance"]

        # Use the modified plot_bar_chart function to get the image data
        importance_img_data = plot_bar_chart(importance_labels, importance_values, "Importance of Work-Life Balance", figure_size=(5, 1), dpi=1200, label_fontsize=6, title_fontsize=8)

        # Display the high-resolution image using st.image
        st.image(importance_img_data, width=900)

        # Display Radar Chart for Industry Fit
        st.subheader("Industry Fit")
        plot_radar_chart(list(industry_scores.keys()), list(total_fit_percentages.values()), "Industry Fit")

        for industry, fit in total_fit_percentages.items():
            st.write(f"Total Fit for {industry}: {fit:.2f}%")

        recommended_industry = max(total_fit_percentages, key=total_fit_percentages.get)
        st.success(f"Recommended Industry: {recommended_industry}")

if __name__ == "__main__":
    main()

