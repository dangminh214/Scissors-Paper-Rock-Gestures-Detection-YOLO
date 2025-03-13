from roboflow import Roboflow # type: ignore
rf = Roboflow(api_key="I9ikXnr1Edwn3gJkL18M")
project = rf.workspace("joseph-nelson").project("rock-paper-scissors")
version = project.version(1)
dataset = version.download("folder")