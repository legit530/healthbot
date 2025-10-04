import random

# =======================
# KNOWLEDGE BASE
# =======================
disease_data = {
    "flu": {
        "symptoms": {"fever", "cough", "sore throat", "body ache"},
        "medicine": "Paracetamol for fever, steam inhalation, and plenty of rest.",
        "therapy": "Drink fluids, rest well, and avoid cold exposure.",
        "doctor": {"name": "Dr. A. Mehta", "specialization": "General Physician", "education": "MBBS, MD (Internal Medicine)"}
    },
    "covid": {
        "symptoms": {"fever", "cough", "shortness of breath", "loss of taste", "loss of smell"},
        "medicine": "Paracetamol for fever, multivitamins, and hydration. Consult a doctor if severe.",
        "therapy": "Isolate and monitor oxygen levels regularly.",
        "doctor": {"name": "Dr. R. Sharma", "specialization": "Pulmonologist", "education": "MBBS, MD (Pulmonary Medicine)"}
    },
    "dengue": {
        "symptoms": {"high fever", "joint pain", "rash", "headache"},
        "medicine": "Paracetamol only (avoid ibuprofen). Stay hydrated.",
        "therapy": "Drink ORS, rest, and monitor platelet count.",
        "doctor": {"name": "Dr. K. Singh", "specialization": "Infectious Disease Specialist", "education": "MBBS, MD (Infectious Diseases)"}
    },
    "malaria": {
        "symptoms": {"fever", "chills", "sweating", "headache"},
        "medicine": "Antimalarial drugs such as chloroquine or artemisinin (as prescribed).",
        "therapy": "Rest and drink fluids.",
        "doctor": {"name": "Dr. T. Verma", "specialization": "General Physician", "education": "MBBS"}
    },
    "typhoid": {
        "symptoms": {"fever", "weakness", "abdominal pain", "headache"},
        "medicine": "Antibiotics like azithromycin or ceftriaxone (as prescribed).",
        "therapy": "Eat soft food and stay hydrated.",
        "doctor": {"name": "Dr. N. Rao", "specialization": "Gastroenterologist", "education": "MBBS, MD (Gastroenterology)"}
    }
}

# =======================
# GLOBAL STATE
# =======================
user_symptoms = set()

# =======================
# CHATBOT RESPONSE LOGIC
# =======================
def chatbot_response(user_input):
    global user_symptoms
    user_input = user_input.lower().strip()

    # Reset conversation
    if user_input in ["reset", "start over", "clear"]:
        user_symptoms.clear()
        return "🔄 Conversation reset. Please enter your first symptom."

    # Greeting
    if any(greet in user_input for greet in ["hello", "hi", "hey", "namaste"]):
        return "👋 Hello! Please describe one symptom you're experiencing."

    # Extract symptom (simple version)
    for word in user_input.split():
        for disease, info in disease_data.items():
            if word in info["symptoms"]:
                user_symptoms.add(word)

    # Ask for next symptom
    if len(user_symptoms) < 2:
        if not user_symptoms:
            return "Please enter your first symptom (e.g., fever, cough, headache)."
        else:
            return "Got it. Please enter another symptom to narrow down the diagnosis."

    # Match diseases based on entered symptoms
    possible_diseases = []
    for disease, info in disease_data.items():
        match_count = len(user_symptoms.intersection(info["symptoms"]))
        if match_count >= 2:
            possible_diseases.append((disease, match_count))

    if not possible_diseases:
        return f"I couldn't find a clear match for your symptoms ({', '.join(user_symptoms)}). Please try again or type 'reset' to start over."

    # Sort by best match
    possible_diseases.sort(key=lambda x: x[1], reverse=True)
    best_match = possible_diseases[0][0]
    info = disease_data[best_match]

    # Clear after diagnosis
    user_symptoms.clear()

    return (
        f"🩺 Based on your symptoms, you might have **{best_match.title()}**.\n\n"
        f"💊 **Recommended Medicine:** {info['medicine']}\n"
        f"💆 **Therapy:** {info['therapy']}\n\n"
        f"👨‍⚕️ **Suggested Doctor:** {info['doctor']['name']} — {info['doctor']['specialization']}\n"
        f"🎓 **Education:** {info['doctor']['education']}\n\n"
        f"Type 'reset' to start again."
    )

# =======================
# TEST CHATBOT (optional)
# =======================
if __name__ == "__main__":
    print("AI Health Chatbot (Type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Take care! Goodbye!")
            break
        print(f"Chatbot: {chatbot_response(user_input)}\n")
