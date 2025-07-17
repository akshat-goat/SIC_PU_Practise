# Hackathon/data_generator_initial.py
import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker for generating realistic data
fake = Faker('en_IN') # 'en_IN' for Indian names/addresses

def generate_synthetic_delivery_data(num_records=50000):
    data = []

    # General India C-section rate for baseline
    national_csection_rate = 0.215 # NFHS-5 national average

    # State-wise C-section rates (simplified for demonstration)
    state_csection_rates = {
        'Telangana': 0.607, 'Tamil Nadu': 0.449, 'Andhra Pradesh': 0.424, 'Kerala': 0.389, 'Karnataka': 0.315,
        'Punjab': 0.385, 'Jammu and Kashmir': 0.417, 'Maharashtra': 0.254, 'Bihar': 0.097,
        'Nagaland': 0.052, 'Meghalaya': 0.082,
    }
    indian_states = list(state_csection_rates.keys()) + ['Uttar Pradesh', 'Rajasthan', 'Madhya Pradesh', 'Gujarat', 'West Bengal']
    for state in indian_states:
        if state not in state_csection_rates:
            state_csection_rates[state] = national_csection_rate

    # Simplified C-section rate multipliers for various factors
    hospital_type_multipliers = {'Public': 0.7, 'Private': 2.2}
    ses_multipliers = {'Poorest': 0.5, 'Poorer': 0.7, 'Middle': 1.0, 'Richer': 1.3, 'Richest': 1.6}
    age_group_multipliers = {'<20': 0.9, '20-29': 1.0, '30-39': 1.2, '40+': 1.5}
    education_multipliers = {'No Education': 0.7, 'Primary': 0.8, 'Secondary': 1.0, 'Higher': 1.3}
    residence_multipliers = {'Rural': 0.9, 'Urban': 1.1}
    complication_types = ['None', 'Preeclampsia', 'Breech Presentation', 'Fetal Distress', 'Previous C-section', 'Other']
    complication_probabilities = {'None': 0.85, 'Preeclampsia': 0.05, 'Breech Presentation': 0.03, 'Fetal Distress': 0.03, 'Previous C-section': 0.03, 'Other': 0.01}
    bmi_ranges = {'Underweight': (16.0, 18.4), 'Normal': (18.5, 24.9), 'Overweight': (25.0, 29.9), 'Obese': (30.0, 40.0)}
    bmi_csection_likelihood_increase = {'Underweight': 0.9, 'Normal': 1.0, 'Overweight': 1.5, 'Obese': 2.0}
    normal_delivery_stay_days = (1, 3)
    csection_delivery_stay_days = (3, 7)
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)

    # --- NEW FACTORS FOR ADVANCED ANALYSIS ---
    anc_multipliers = {'Adequate': 0.9, 'Inadequate': 1.1}
    anc_prob_adequate = 0.7

    referral_multipliers = {'Referred': 1.5, 'Direct_Admission': 0.8}
    prob_referred = 0.2

    idi_categories = {'Short (<18)': (1, 17), 'Optimal (18-59)': (18, 59), 'Long (60+)': (60, 120)}
    idi_multipliers = {'Short (<18)': 1.3, 'Optimal (18-59)': 1.0, 'Long (60+)': 1.2}
    idi_prob_dist = {'Short (<18)': 0.15, 'Optimal (18-59)': 0.70, 'Long (60+)': 0.15}

    doctor_density_ranges = {'Low': (0.1, 0.5), 'Medium': (0.5, 1.0), 'High': (1.0, 2.0)}
    midwife_density_ranges = {'Low': (1.0, 2.0), 'Medium': (2.0, 4.0), 'High': (4.0, 8.0)}
    doc_density_influence = {'Low': 0.9, 'Medium': 1.0, 'High': 1.1}
    mid_density_influence = {'Low': 1.1, 'Medium': 1.0, 'High': 0.9}

    prob_patient_prefers_csection = 0.15
    patient_preference_multiplier = 1.8

    peak_hours_multiplier = 1.2
    off_peak_hours_multiplier = 0.9
    peak_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


    for i in range(num_records):
        patient_id = i + 1
        maternal_age = random.randint(18, 45)
        maternal_education = random.choices(list(education_multipliers.keys()), weights=[0.2, 0.25, 0.3, 0.25], k=1)[0]
        residence = random.choices(list(residence_multipliers.keys()), weights=[0.6, 0.4], k=1)[0]
        hospital_type = random.choices(list(hospital_type_multipliers.keys()), weights=[0.5, 0.5], k=1)[0]
        state = random.choices(indian_states, weights=[state_csection_rates.get(s, national_csection_rate) for s in indian_states], k=1)[0]
        socio_economic_status = random.choices(list(ses_multipliers.keys()), weights=[0.2, 0.2, 0.2, 0.2, 0.2], k=1)[0]
        delivery_date_time = start_date + timedelta(days=random.randint(0, (end_date - start_date).days),
                                                    hours=random.randint(0, 23),
                                                    minutes=random.randint(0, 59))
        complication = random.choices(complication_types, weights=[complication_probabilities[c] for c in complication_types], k=1)[0]
        birth_order = random.choices([1, 2, 3, 4], weights=[0.4, 0.3, 0.2, 0.1], k=1)[0]
        if complication == 'Previous C-section' and birth_order == 1:
            birth_order = random.choices([2, 3, 4], weights=[0.5, 0.3, 0.2], k=1)[0]
        bmi_category = random.choices(list(bmi_ranges.keys()), weights=[0.05, 0.6, 0.25, 0.1], k=1)[0]
        bmi = round(random.uniform(bmi_ranges[bmi_category][0], bmi_ranges[bmi_category][1]), 1)

        # --- Generate NEW FACTOR DATA ---
        anc_adequate = random.random() < anc_prob_adequate
        referred_from_smaller_facility = random.random() < prob_referred
        inter_delivery_interval_months = np.nan
        if birth_order > 1:
            idi_category_chosen = random.choices(list(idi_multipliers.keys()), weights=list(idi_prob_dist.values()), k=1)[0]
            inter_delivery_interval_months = random.randint(idi_categories[idi_category_chosen][0], idi_categories[idi_category_chosen][1])

        doctor_density_category = random.choices(list(doctor_density_ranges.keys()), weights=[0.3, 0.4, 0.3], k=1)[0]
        doctor_density = round(random.uniform(doctor_density_ranges[doctor_density_category][0], doctor_density_ranges[doctor_density_category][1]), 2)
        
        midwife_density_category = random.choices(list(midwife_density_ranges.keys()), weights=[0.3, 0.4, 0.3], k=1)[0]
        midwife_density = round(random.uniform(midwife_density_ranges[midwife_density_category][0], midwife_density_ranges[midwife_density_category][1]), 2)

        patient_preference_csection = random.random() < prob_patient_prefers_csection
        
        delivery_time_hour = delivery_date_time.hour
        delivery_day_of_week = delivery_date_time.strftime('%A') # Full weekday name

        # Determine C-section probability based on combined factors
        base_prob = state_csection_rates.get(state, national_csection_rate)
        adjusted_prob = base_prob * hospital_type_multipliers.get(hospital_type, 1.0)
        adjusted_prob *= ses_multipliers.get(socio_economic_status, 1.0)
        adjusted_prob *= age_group_multipliers.get(
            '<20' if maternal_age < 20 else ('20-29' if 20 <= maternal_age <= 29 else ('30-39' if 30 <= maternal_age <= 39 else '40+')), 1.0
        )
        adjusted_prob *= education_multipliers.get(maternal_education, 1.0)
        adjusted_prob *= residence_multipliers.get(residence, 1.0)
        adjusted_prob *= bmi_csection_likelihood_increase.get(bmi_category, 1.0)

        # --- Apply NEW FACTOR INFLUENCES ---
        adjusted_prob *= anc_multipliers.get('Adequate' if anc_adequate else 'Inadequate', 1.0)
        adjusted_prob *= referral_multipliers.get('Referred' if referred_from_smaller_facility else 'Direct_Admission', 1.0)
        if birth_order > 1 and not np.isnan(inter_delivery_interval_months):
            idi_cat = 'Short (<18)' if inter_delivery_interval_months < 18 else ('Optimal (18-59)' if inter_delivery_interval_months <= 59 else 'Long (60+)')
            adjusted_prob *= idi_multipliers.get(idi_cat, 1.0)

        adjusted_prob *= doc_density_influence.get(doctor_density_category, 1.0)
        adjusted_prob *= mid_density_influence.get(midwife_density_category, 1.0)

        if patient_preference_csection:
            adjusted_prob *= patient_preference_multiplier

        if delivery_day_of_week in peak_days and 9 <= delivery_time_hour <= 17: # Business hours
            adjusted_prob *= peak_hours_multiplier
        else:
            adjusted_prob *= off_peak_hours_multiplier


        # Final decision on Delivery Type
        delivery_type = 'C-section'
        if complication == 'Previous C-section' or complication == 'Breech Presentation' or complication == 'Fetal Distress':
            delivery_type = 'C-section'
        elif complication == 'Preeclampsia' and random.random() < 0.8:
            delivery_type = 'C-section'
        elif random.random() >= adjusted_prob:
            delivery_type = 'Normal'


        duration_of_stay = random.randint(csection_delivery_stay_days[0], csection_delivery_stay_days[1]) if delivery_type == 'C-section' else random.randint(normal_delivery_stay_days[0], normal_delivery_stay_days[1])
        maternal_health_post_delivery = 'Good' if random.random() > (0.05 if delivery_type == 'C-section' else 0.02) else 'Minor Complication'
        child_surviving_fetal_period = True if random.random() > (0.01 if delivery_type == 'C-section' else 0.005) else False


        data.append({
            'Patient_ID': patient_id, 'Maternal_Age': maternal_age, 'Birth_Order': birth_order,
            'Residence': residence, 'Hospital_Type': hospital_type, 'State': state,
            'Socio_Economic_Status': socio_economic_status, 'Maternal_Education': maternal_education,
            'BMI': bmi, 'BMI_Category': bmi_category, 'Medical_Complication': complication,
            'Delivery_Type': delivery_type, 'Delivery_Date': delivery_date_time.strftime('%Y-%m-%d %H:%M:%S'),
            'Duration_of_Stay_Days': duration_of_stay, 'Maternal_Health_Post_Delivery': maternal_health_post_delivery,
            'Child_Surviving_Fetal_Period': child_surviving_fetal_period,
            'ANC_Adequate': anc_adequate, 'Referred_From_Smaller_Facility': referred_from_smaller_facility,
            'Inter_Delivery_Interval_Months': inter_delivery_interval_months,
            'Doctor_Density_Category': doctor_density_category,
            'Doctor_Density_Value': doctor_density,
            'Midwife_Density_Category': midwife_density_category,
            'Midwife_Density_Value': midwife_density,
            'Patient_Preference_Csection': patient_preference_csection,
            'Delivery_Time_Hour': delivery_time_hour, 'Delivery_Day_of_Week': delivery_day_of_week
        })

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    synthetic_df = generate_synthetic_delivery_data(num_records=50000)
    # This file will create synthetic_delivery_data.csv in the same directory.
    # User needs to move/rename it to data/raw_data.csv manually for the project structure.
    csv_filename = 'synthetic_delivery_data.csv'
    synthetic_df.to_csv(csv_filename, index=False)
    print(f"Synthetic data generated and saved to {csv_filename}")
    print("PLEASE MOVE/RENAME THIS FILE TO 'Hackathon/data/raw_data.csv' FOR THE PROJECT TO WORK.")
    print(synthetic_df.head())