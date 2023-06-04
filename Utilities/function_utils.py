import os
import keyboard
import threading
from datetime import datetime


class Functions:
    mode = None

    def __init__(self):
        self.mode = None

        # Start a separate thread to listen for 'Esc' key press
        self.listen_for_esc_lock = threading.Lock()
        self.listen_for_esc_thread = threading.Thread(target=self.listen_for_esc, daemon=True)
        self.listen_for_esc_thread.start()

    def listen_for_esc(self):
        while True:
            with self.listen_for_esc_lock:
                if keyboard.is_pressed('esc') and self.mode == 'auto':
                    print("\nSwitching to Manual Mode...")
                    self.mode = 'manual'
                    keyboard.read_event(suppress=True)  # Clear the event buffer

    def set_auto_mode(self):
        # print("\nEnter Auto or Manual Mode? (a/m)")
        while True:
            user_input = input("\nEnter Auto or Manual Mode? (a/m):")
            if user_input.lower() == 'a':
                self.mode = 'auto'
                print(f"\nAuto Mode Set - Press 'Esc' to return to Manual Mode!\n")
                break

            elif user_input.lower() == 'm':
                print(f"\nManual Mode Set.\n")
                self.mode = 'manual'
                break

            else:
                print("\nPlease select a valid option!\n")

    def check_auto_mode(self):
        context = None

        # Acquire the lock while this function is running
        with self.listen_for_esc_lock:
            # Check if the mode is manual
            if self.mode == 'manual':
                user_input = input("\nAllow AI to continue? (y/n/auto) or provide feedback: ")
                if user_input.lower() == 'y':
                    pass
                elif user_input.lower() == 'n':
                    quit()
                elif user_input.lower() == 'auto':
                    self.mode = 'auto'
                    print(f"\nAuto Mode Set - Press 'Esc' to return to Manual Mode!\n")
                    keyboard.read_event(suppress=True)  # Clear the event buffer
                else:
                    context = user_input

        return context

    def print_task_list(self, task_list):
        # Print the task list
        print("\033[95m\033[1m" + "\n*****TASK LIST*****\n" + "\033[0m\033[0m")
        for t in task_list:
            print(str(t["task_order"]) + ": " + t["task_desc"])

    def print_next_task(self, task):
        # Print the next task
        print("\033[92m\033[1m" + "\n*****NEXT TASK*****\n" + "\033[0m\033[0m")
        print(str(task["task_order"]) + ": " + task["task_desc"])

    def print_result(self, result):
        # Print the task result
        print("\033[92m\033[1m" + "\n*****RESULT*****\n" + "\033[0m\033[0m")
        print(result)

        # Save the result to a log.txt file in the /Logs/ folder
        log_folder = "Logs"
        log_file = "log.txt"

        # Create the Logs folder if it doesn't exist
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        # Save the result to the log file
        self.write_file(log_folder, log_file, result)

    def write_file(self, folder, file, result):
        with open(os.path.join(folder, file), "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - TASK RESULT:\n{result}\n\n")
            
    def read_file(file_path):
        with open(file_path, 'r') as file:
            text = file.read()
        return text
