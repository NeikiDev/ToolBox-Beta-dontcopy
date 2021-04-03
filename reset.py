import json

with open('installation.json') as json_file:
    config = json.load(json_file)

hard_reset = config["install"]

if hard_reset == "false":
    with open('installation.json', "w+") as reset_installation:
        reset_installation.write("{ \n")
        reset_installation.write('"install": "true" \n')
        reset_installation.write("}")
    with open('Logs/latest_log.log', "w+") as reset_logs:
        reset_logs.write('You Reseted all! Pls start "Password Manager.py" Again to Install all Files!')
else:
    print("You Cant Reset all! Pls Install first the Password Manager!")
    input("Press any Key to Continue...")