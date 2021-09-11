# Init Variables
theMatrix = ""
system = ""
neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
fight = ""

profession = ["", "", "", ""]
adj = ["", ""]

# Get User Input
print("Welcome user!")
print("Let's play a game of madlibs!")
neo = input("Please enter your name.\n")

print(f"Hello {neo}! Let's beign.")
theMatrix = input("What is something you would like to know more about?")

print(f"So you want to know more about {theMatrix}, do you?")
print(f"First, tell me what you already know about {theMatrix}.")
system = input(f"What noun would you best use to describe {theMatrix}?")

enemy = input(f"Please provide me with another noun, in opposition to {system}.")

inside = input(f"Please tell me your favorite place to relax.")

profession[0] = input(f"What is the profession that you would most like to pursue?")
# Init Story
madlibsStory = (
    f"{theMatrix} is a {system}, {neo}. That {system} is our {enemy}. " +
    f"But when you're {inside}, you look around, what do you see? " +
    f"{profession[0]}, {profession[1]}, {profession[2]}, {profession[3]}. The very minds " +
    f"of the people we are trying to {save}. But until we do, " +
    f"these people are still a part of that {system} and that makes " +
    f"them our {enemy}. You have to understand, most of these people " +
    f"are not ready to be {unplugged}. And many of them are so {adj[0]}, " +
    f"so hopelessly {adj[1]} on the {system}, that they will {fight} to protect it."
)
# Print Story
print(madlibsStory)
