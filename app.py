import json


def json_to_text(json_data, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for intent in json_data["intents"]:
            tag = intent["tag"]
            patterns = intent["patterns"]
            responses = intent["responses"]

            file.write(f"# Tag: {tag}\n\n")
            file.write(f"Patterns: {', '.join(patterns)}\n\n")
            for response in responses:
                file.write(f"{response}\n\n")
            file.write("\n")


# Load JSON data
with open("data/anees_dataset.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)

# Convert JSON to text file
json_to_text(json_data, "output.txt")
