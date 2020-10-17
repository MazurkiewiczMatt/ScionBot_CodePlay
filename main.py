with open("settings.txt") as f:
    settings = f.readlines()

# check whether the file is valid
if not len(settings) == 4:
    raise Exception("Invalid settings file: 4 lines expected, " + str(len(settings)) + " received.")

# remove whitespace
for i in range(len(settings)):
    settings[i] = settings[i].strip()

# convert string containing subreddit names to a list
settings[-1] = settings[-1].split()


print(settings)
