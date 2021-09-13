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

# Get theMatrix variable from user
print(f"Hello {neo}! Let's beign.")
theMatrix = input("What is something you would like to know more about?")

# Get system variable from user
print(f"So you want to know more about {theMatrix}, do you?")
print(f"First, tell me what you already know about {theMatrix}.")
system = input(f"What noun would you best use to describe {theMatrix}?")

# Get enemy variable from user
enemy = input(f"Please provide me with another noun, in opposition to {system}.")

# Get inside variable from user
inside = input(f"Please tell me your favorite place to relax.")

# Get profession list from user
print(f"What are the top 4 jobs that you would most like to have?")

for i in range(len(profession)):
    profession[i] = input(f"Profession {i + 1} / {len(profession)}: ")

# Get save variable from user
save = input(f"Now, please provide me with a verb to provide action for our story.")

# Get unplugged variable from user
unplugged = input(f"We're nearing the end now. Please give me another verb.")

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
