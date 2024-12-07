import customtkinter as ctk
import random
import numpy as np

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

import numpy as np

fivebyfivesolver = np.array([
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
])




class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Initialize the window
        self.title("Lights Out Puzzle")
        self.geometry("800x600")
        self.resizable(False, False)

        # Initialize attributes
        self.selected_size = "3x3"  # Default size
        self.matrix = []  # Matrix will be initialized later
        self.current_mode = "Knight's Move"  # Default mode
        self.last_mode = self.current_mode  # Track the last mode

        # Modes dropdown
        self.mode_options = ["Knight's Move", "Normal Mode", "Edit Mode"]
        self.mode_dropdown = ctk.CTkOptionMenu(self,
                                               width=160,
                                               height=30,
                                               fg_color="#e32710",
                                               button_color="#af0600",
                                               values=self.mode_options,
                                               command=self.set_mode)
        self.mode_dropdown.place(x=50, y=20)
        self.mode_dropdown.set(self.current_mode)

        # Size options dropdown
        size_options = ["3x3", "4x4", "5x5", "6x6", "7x7"]
        self.size_dropdown = ctk.CTkOptionMenu(self,
                                               width=120,
                                               height=30,
                                               fg_color="#b002fb",
                                               button_color="#7000a0",
                                               values=size_options,
                                               command=self.check_and_display_matrix)
        self.size_dropdown.place(x=246, y=20)

        # Check solution button
        self.check_button = ctk.CTkButton(self,
                                          text="Check Solution",
                                          width=150,
                                          height=30,
                                          fg_color="#11b600",
                                          command=self.check_solution)
        self.check_button.place(x=400, y=20)

        self.solve_button = ctk.CTkButton(self,
                                          text="Solve",
                                          width=110,
                                          height=30,
                                          fg_color="#ee9400",
                                          command=self.solve_solution)
        self.solve_button.place(x=600, y=20)

        # Frame for the matrix display
        self.matrix_frame = ctk.CTkFrame(self, width=580, height=500, fg_color="#2a2a2a")
        self.matrix_frame.place(x=10, y=70)

        # Result label
        self.result_label = ctk.CTkLabel(self,
                                         text="",
                                         font=("Arial", 16),
                                         text_color="white")
        self.result_label.place(x=10, y=530)

        # Initialize and display the default matrix
        self.generate_matrix(3)  # Initialize a 3x3 matrix
        self.display_matrix()

    def solve_solution(self):
        # Ensure the matrix is 5x5
        if len(self.matrix) != 5 or len(self.matrix[0]) != 5:
            self.result_label.configure(text="Solving is only implemented for 5x5!", text_color="orange")
            return

        print(self.matrix)
        self.matrix = np.array(self.matrix)
        # Flatten the 5x5 matrix to a column vector

        matrix_to_column = self.matrix.flatten().reshape(-1, 1)
        #matrix_to_column = np.array(matrix_to_column).reshape(-1, 1)
        modulus = 2
        matrix_to_column_mod2 = matrix_to_column % 2
        fivebyfivesolver_mod2 = fivebyfivesolver % 2
        result_matrix = self.gaussian_elimination_mod2(fivebyfivesolver_mod2, matrix_to_column_mod2)

        # Display the result
        self.display_result_matrix(result_matrix)

    def gaussian_elimination_mod2(self, A, b):
        n = len(b)

        # Augment matrix A with column b (right-hand side)
        augmented = np.hstack([A, b])

        # Perform Gaussian elimination
        for i in range(n):
            # Make the diagonal element 1 (pivoting step, if necessary)
            if augmented[i, i] == 0:
                # Try to swap rows if necessary
                for j in range(i + 1, n):
                    if augmented[j, i] == 1:
                        augmented[[i, j]] = augmented[[j, i]]
                        break

            # Eliminate all below the pivot
            for j in range(i + 1, n):
                if augmented[j, i] == 1:
                    augmented[j] ^= augmented[i]

        # Back-substitution to find solution
        solution = np.zeros(n, dtype=int)
        for i in range(n - 1, -1, -1):
            solution[i] = augmented[i, -1] - np.dot(augmented[i, :-1], solution) % 2

        solution.reshape(5,5)
        sol = solution.reshape(5, 5).astype(int).tolist()  # Convert to Python list of lists

        return sol


    def display_result_matrix(self, result_matrix):
        """
        Display the resulting matrix of the solve function.
        """
        # Create a frame for the result matrix if it doesn't exist
        result_frame = ctk.CTkFrame(self, width=250, height=250, fg_color="#2a2a2a")
        result_frame.place(x=440, y=90)  # Adjust the x-position to place it next to the puzzle

        # Clear any existing result display (if applicable)
        for widget in result_frame.winfo_children():
            widget.destroy()

        # Display the result matrix as buttons
        button_size = 50
        col = 0
        for row in range(len(result_matrix)):
            for col in range(len(result_matrix[row])):
                btn = ctk.CTkButton(result_frame,
                                    text=str(abs(result_matrix[row][col])),
                                    text_color='white',
                                    width=button_size - 10,
                                    height=button_size - 10,
                                    fg_color=['#000000','#21f100'][result_matrix[row][col]],  # Alternate colors
                                    state="disabled")  # Disable buttons to make them just display the result
                btn.grid(row=row, column=col, padx=4, pady=4)

        # Update the layout after placing the frame
        self.update_idletasks()




    def generate_matrix(self, size):
        """
        Generate a new matrix of the given size.
        """
        self.matrix = [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]


    def display_matrix(self):
        """
        Display the current matrix without regenerating it.
        """
        # Clear the matrix display
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

        # Dynamically generate the matrix of buttons
        button_size = 50
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                btn = ctk.CTkButton(self.matrix_frame,
                                    text="",
                                    width=button_size,
                                    height=button_size,
                                    fg_color=['#eab5b5',"#1bf9fc"][self.matrix[row][col]],  # Blue or Red
                                    command=lambda r=row, c=col: self.apply_move(r, c))
                btn.grid(row=row, column=col, padx=5, pady=5)

    def set_mode(self, selected_mode):
        """
        Set the current mode and reset the matrix if switching between game modes.
        """
        # Reset the matrix only if switching between "Knight's Move" and "Normal Mode"
        if (self.current_mode in ["Knight's Move", "Normal Mode"]
                and selected_mode in ["Knight's Move", "Normal Mode"]
                and self.current_mode != selected_mode):
            self.generate_matrix(len(self.matrix))  # Reset matrix
            self.display_matrix()

        # Update the current and last modes
        self.current_mode = selected_mode

    def check_and_display_matrix(self, selected_size):
        """
        Triggered when the size dropdown changes. Regenerates the matrix only on size change.
        """
        size = int(selected_size[0])  # Extract size (e.g., "3x3" -> 3)
        if len(self.matrix) != size:
            self.generate_matrix(size)  # Regenerate matrix if size changes
        self.display_matrix()  # Always update the display

    def apply_move(self, r, c):
        """
        Apply the move logic based on the current mode.
        """
        if self.current_mode == "Knight's Move":
            self.knights_move(r, c)
        elif self.current_mode == "Normal Mode":
            self.normal_move(r, c)
        elif self.current_mode == "Edit Mode":
            self.toggle_cell(r, c)

    def toggle_cell(self, r, c):
        """
        Toggle a single cell (for Edit Mode).
        """
        self.matrix[r][c] = (self.matrix[r][c] + 1) % 2
        self.display_matrix()

    def knights_move(self, r, c):
        """
        Toggle cells using Knight's Move rules.
        """
        self.toggle_cell(r, c)
        for dr, dc in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]:
            if 0 <= r + dr < len(self.matrix) and 0 <= c + dc < len(self.matrix[0]):
                self.toggle_cell(r + dr, c + dc)

    def normal_move(self, r, c):
        """
        Toggle cells using Normal Mode rules.
        """
        self.toggle_cell(r, c)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= r + dr < len(self.matrix) and 0 <= c + dc < len(self.matrix[0]):
                self.toggle_cell(r + dr, c + dc)

    def check_solution(self):
        """
        Check if all cells are in the same state (0 or 1).
        """
        if all(cell == 0 for row in self.matrix for cell in row) or all(cell == 1 for row in self.matrix for cell in row):
            self.result_label.configure(text="🎉 Congratulations! You solved the puzzle!", text_color="green")
        else:
            self.result_label.configure(text="❌ Not yet solved. Keep trying!", text_color="red")


if __name__ == "__main__":
    app = App()
    app.mainloop()
