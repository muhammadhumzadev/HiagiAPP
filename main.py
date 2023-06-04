from Agents.execution_agent import ExecutionAgent
from Agents.task_creation_agent import TaskCreationAgent
from Agents.prioritization_agent import PrioritizationAgent
from Utilities.function_utils import Functions
from Utilities.storage_interface import StorageInterface
import json

#To enter & update the objective


# Load the JSON file
with open('Personas/default.json', 'r') as f:
    data = json.load(f)

# Ask the user for a new objective
new_objective = input("Enter a new objective: ")

# Update the "Objective" field with the new objective
data["Objective"] = new_objective

# Save the modified JSON to file
with open('Personas/default.json', 'w') as f:
    json.dump(data, f, indent=2)

# Load Relevant Agents
storage = StorageInterface()
taskCreationAgent = TaskCreationAgent()
prioritizationAgent = PrioritizationAgent()
executionAgent = ExecutionAgent()

# Add a variable to set the mode
functions = Functions()
functions.set_auto_mode()

# Main loop
while True:
    # Create task list
    taskCreationAgent.run_task_creation_agent()

    # Prioritize task list
    tasklist = prioritizationAgent.run_prioritization_agent()

    # Allow for feedback if auto mode is disabled
    feedback = functions.check_auto_mode()

    # Run Execution Agent
    executionAgent.run_execution_agent(context = tasklist ,feedback = feedback)


