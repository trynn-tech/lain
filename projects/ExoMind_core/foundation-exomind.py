import json
import hashlib
import datetime


class ExoMind:
    def __init__(self, topic, version="1.0.0"):
        self.id = self.generate_id()
        self.version = version
        self.topic = topic
        self.memory_flakes = []  # Individual memory units
        self.key_points = []
        self.decisions = []
        self.open_questions = []
        self.next_steps = []
        self.references = []
        self.summary = ""
        self.changes = []
        self.resources = []
        self.constraints = []
        self.related_layers = []
        self.sub_layers = []

    def generate_id(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return f"XM{timestamp}"  # XM = ExoMind

    def add_memory_flake(self, content):
        flake_id = hashlib.sha256(content.encode()).hexdigest()[:8]
        timestamp = datetime.datetime.now().isoformat()
        self.memory_flakes.append(
            {"id": flake_id, "content": content, "timestamp": timestamp}
        )

    def add_key_point(self, point):
        self.key_points.append(point)

    def add_decision(self, decision, status="Tentative"):
        self.decisions.append(f"{status}: {decision}")

    def add_question(self, question):
        self.open_questions.append(question)

    def add_next_step(self, step):
        self.next_steps.append(step)

    def add_reference(self, reference):
        self.references.append(reference)

    def set_summary(self, summary):
        self.summary = summary

    def add_change(self, change):
        self.changes.append(change)

    def add_resource(self, resource):
        self.resources.append(resource)

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def relate_layer(self, related_id, relationship):
        self.related_layers.append({"id": related_id, "relationship": relationship})

    def add_sub_layer(self, sub_layer):
        self.sub_layers.append(sub_layer.__dict__)  # Store as a dict

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)

    def update_version(self):
        version_split = self.version.split(".")
        version_split[-1] = str(int(version_split[-1]) + 1)  # Increment patch version
        self.version = ".".join(version_split)


# Example usage:
exomind = ExoMind("Synthetic Intelligence Core")
exomind.add_memory_flake("Initial memory formation process established.")
exomind.add_key_point("ExoMind establishes a hierarchical scaffold for lossy recall.")
exomind.add_decision("Prioritize modular recall over full retention", "Confirmed")
exomind.add_question("How will multiple cognitive layers interact?")
exomind.add_next_step("Develop advanced retrieval mechanisms and decay structuring.")
exomind.set_summary(
    "ExoMind serves as the memory foundation for structured synthetic intelligence."
)

print(exomind.to_json())
