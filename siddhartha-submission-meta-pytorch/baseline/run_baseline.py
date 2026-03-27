from app.env import EmailEnv
from app.models import Action

env = EmailEnv()

obs = env.reset()

action = Action(label="normal", action="ignore")

obs, reward, done, _ = env.step(action)

print("Baseline Score:", reward.score)