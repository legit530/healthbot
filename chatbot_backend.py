import random
import re

# =======================
# KNOWLEDGE BASE
# =======================
knowledge_base = {
    "flu": {
        "symptoms": ["fever", "cough", "sore throat", "body ache", "fatigue"],
        "prevention": "Get vaccinated annually, wash hands regularly, and avoid close contact with sick people.",
        "treatment": "Rest, stay hydrated, and take paracetamol or ibuprofen. Seek medical help if symptoms worsen.",
        "doctor": {"name": "Dr. A. Mehta", "specialization": "General Physician", "education": "MBBS, MD (Internal Medicine)"}
    },
    "covid": {
        "symptoms": ["fever", "cough", "shortness of breath", "loss of taste", "loss of smell", "fatigue"],
        "prevention": "Wear a mask, maintain social distance, and get vaccinated.",
        "treatment": "Rest, hydrate, and isolate yourself. Seek medical attention if breathing difficulties develop.",
        "doctor": {"name": "Dr. R. Patel", "specialization": "Pulmonologist", "education": "MBBS, MD (Pulmonary Medicine)"}
    },
    "dengue": {
        "symptoms": ["fever", "joint pain", "headache", "rash", "body ache", "nausea"],
        "prevention": "Avoid mosquito bites, use repellents, and remove stagnant water.",
        "treatment": "Drink plenty of fluids, rest, and take paracetamol (avoid aspirin).",
        "doctor": {"name": "Dr. N. Sharma", "specialization": "Infectious Disease Specialist", "education": "MBBS, MD (Infectious Diseases)"}
    },
    "malaria": {
        "symptoms": ["fever", "chills", "sweating", "headache", "nausea", "vomiting"],
        "prevention": "Use mosquito nets, insect repellents, and avoid stagnant water.",
        "treatment": "Antimalarial medications as prescribed by a doctor. Rest and hydration.",
        "doctor": {"name": "Dr. S. Khanna", "specialization": "Tropical Medicine Expert", "education": "MBBS, MD (Tropical Medicine)"}
    },
    "typhoid": {
        "symptoms": ["fever", "headache", "abdominal pain", "fatigue", "constipation", "rash"],
        "prevention": "Drink clean water, maintain hygiene, and get vaccinated for typhoid.",
        "treatment": "Antibiotics prescribed by a doctor. Drink fluids and rest.",
        "doctor": {"name": "Dr. M. Verma", "specialization": "Gastroenterologist", "education": "MBBS, MD (Gastroenterology)"}
    },
    "common cold": {
        "symptoms": ["runny nose", "sneezing", "sore throat", "cough", "mild fever"],
        "prevention": "Wash hands often and avoid close contact with infected people.",
        "treatment": "Rest, drink warm fluids, and use over-the-counter cold medicines.",
        "doctor": {"name": "Dr. L. Rao", "specialization": "General Practitioner", "education": "MBBS, MD (Family Medicine)"}
    },
    "chickenpox": {
        "symptoms": ["rash", "itching", "fever", "fatigue", "loss of appetite"],
        "prevention": "Get vaccinated and avoid contact with infected individuals.",
        "treatment": "Rest, stay hydrated, and use calamine lotion to relieve itching.",
        "doctor": {"name": "Dr. P. Iyer", "specialization": "Dermatologist", "education": "MBBS, MD (Dermatology)"}
    },
    "asthma": {
        "symptoms": ["shortness of breath", "wheezing", "chest tightness", "cough"],
        "prevention": "Avoid triggers like dust, smoke, and pollution. Follow your inhaler routine.",
        "treatment": "Use prescribed inhalers and medications. Avoid known allergens.",
        "doctor": {"name": "Dr. V. Gupta", "specialization": "Respiratory Specialist", "education": "MBBS, MD (Respiratory Medicine)"}
    },
    "tuberculosis": {
        "symptoms": ["persistent cough", "chest pain", "weight loss", "night sweats", "fatigue"],
        "prevention": "Get the BCG vaccine and ensure good ventilation in living areas.",
        "treatment": "Long-term antibiotic treatment under medical supervision.",
        "doctor": {"name": "Dr. T. Roy", "specialization": "Pulmonologist", "education": "MBBS, MD (Chest Medicine)"}
    },
    "migraine": {
        "symptoms": ["headache", "nausea", "vomiting", "sensitivity to light", "sensitivity to sound"],
        "prevention": "Manage stress, get enough sleep, and avoid known triggers like caffeine or loud noise.",
        "treatment": "Take prescribed migraine medication, rest in a dark room, and stay hydrated.",
        "doctor": {"name": "Dr. R. Nair", "specialization": "Neurologist", "education": "MBBS, DM (Neurology)"}
    }
}

# =======================
# GREETINGS & FALLBACKS
# =======================
greetings = ["hello", "hi", "hey", "namaste", "hola"]

greet_responses = [
    "Hello! How can I help with your health query?",
    "Hi there! Tell me your symptoms, and I’ll suggest possible diseases.",
    "Namaste! Describe your symptoms — I’ll help you find possible causes."
]

fallbacks = [
    "Sorry, I couldn't identify the disease. Try mentioning common symptoms like fever, cough, or body ache.",
    "Hmm, I didn’t understand that. Please describe what symptoms you have.",
    "I can help with symptoms like fever, cough, rash, or headache. What are you feeling?"
]

# =======================
# CHATBOT LOGIC
# =======================
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Greeting
    if any(word in user_input for word in greetings):
        return random.choice(greet_responses)

    # Find matching diseases by symptoms
    matched_diseases = []
    for disease, info in knowledge_base.items():
        for symptom in info["symptoms"]:
            if symptom in user_input:
                matched_diseases.append(disease)
                break

    if matched_diseases:
        # If only one disease matches
        if len(matched_diseases) == 1:
            disease = matched_diseases[0]
            info = knowledge_base[disease]
            response = (
                f"🩺 It seems you may have **{disease.title()}**.\n\n"
                f"**Symptoms:** {', '.join(info['symptoms'])}\n"
                f"**Prevention:** {info['prevention']}\n"
                f"**Treatment:** {info['treatment']}\n\n"
                f"👨‍⚕️ Recommended Doctor: {info['doctor']['name']}\n"
                f"**Specialization:** {info['doctor']['specialization']}\n"
                f"**Education:** {info['doctor']['education']}"
            )
            return response

        # If multiple diseases match
        else:
            return f"Based on your symptoms, possible diseases could be: {', '.join(matched_diseases)}. Please describe another symptom to narrow it down."

    # Vaccine info
    if re.search(r'vaccine|vaccination', user_input):
        return "Vaccination schedules vary by age and disease. Visit your nearest health center for the latest schedule."

    # Fallback
    return random.choice(fallbacks)
