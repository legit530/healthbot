import random
import re

# =======================
# KNOWLEDGE BASE
# =======================
knowledge_base = {
    "flu": {
        "symptoms": ["fever", "cough", "sore throat", "body ache"],
        "prevention": "Get vaccinated annually, wash hands regularly, and avoid close contact with sick people.",
        "treatment": "Rest, drink fluids, and take paracetamol or ibuprofen. Seek medical help if symptoms persist.",
        "doctor": {"name": "Dr. A. Mehta", "specialization": "General Physician", "education": "MBBS, MD (Internal Medicine)"}
    },
    "covid": {
        "symptoms": ["fever", "cough", "shortness of breath", "loss of taste", "loss of smell"],
        "prevention": "Wear a mask, maintain social distancing, and get vaccinated.",
        "treatment": "Rest, hydration, and paracetamol. Isolate yourself and consult a doctor if breathing issues develop.",
        "doctor": {"name": "Dr. R. Patel", "specialization": "Pulmonologist", "education": "MBBS, MD (Pulmonary Medicine)"}
    },
    "dengue": {
        "symptoms": ["fever", "joint pain", "headache", "rash", "body ache"],
        "prevention": "Avoid mosquito bites, use repellents, and remove stagnant water around your house.",
        "treatment": "Drink plenty of fluids, rest, and take paracetamol (avoid aspirin).",
        "doctor": {"name": "Dr. N. Sharma", "specialization": "Infectious Disease Specialist", "education": "MBBS, MD (Infectious Diseases)"}
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
