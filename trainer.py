from src.learning.memory import store_feedback
from src.learning.reward import compute_reward
from src.learning.doctor import simulated_doctor

def learning_loop(agent, text):

    state, trace = agent(text)

    draft = state["summary"]
    edited = simulated_doctor(draft)

    score = compute_reward(draft, edited)

    store_feedback(draft, edited, score)

    return score
