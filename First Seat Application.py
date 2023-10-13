import tkinter as tk
from tkinter import PhotoImage

# Define the Model class to store the selected movie, seat, and price
class Model:
    def __init__(self):
        self.selected_movie = ""
        self.selected_seat = ""
        self.selected_price = 0.0

# MovieSelectionView module
class MovieSelectionView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.movie_buttons = []

        # Display a welcome message
        label1 = tk.Label(root, text="Welcome to First Seat")
        label1.pack()

        # Label to instruct the user to select a movie
        label2 = tk.Label(root, text="Select a Movie:")
        label2.pack()

        # Load and display an image
        movie_select_image = PhotoImage(file="C:\\Users\\bjame\\Downloads\\machs_project.png")
        image_label = tk.Label(root, image=movie_select_image)
        image_label.image = movie_select_image
        image_label.pack()

        # List of available movies with buttons
        movies = [
            "Guardians of the Galaxy 3",
            "Five Nights at Freddy's",
            "The Hunger Games: The Ballad of Songbirds and Snakes",
            "LoL Esports 2023 Worlds Finals",
            "Deadpool 3",
            "Disney's Wish",
            "Kung Fu Panda 4",
            "Legend of the White Dragon",
            "Spider-Man: Beyond the Spider-Verse",
            "Spy x Family Code: White",
        ]

        # Create buttons for each movie
        for movie in movies:
            movie_button = tk.Button(root, text=movie, command=lambda m=movie: controller.select_movie(m))
            movie_button.pack()
            self.movie_buttons.append(movie_button)

        # Button to exit the application
        exit_button = tk.Button(root, text="Exit", command=root.quit)
        exit_button.pack()

# SeatSelectionView module
class SeatSelectionView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.row_buttons = []

        # Create a new window for seat selection
        self.seat_window = tk.Toplevel(root)
        self.seat_window.title("Seat Selection")

        # Label to instruct the user to select a row
        label3 = tk.Label(self.seat_window, text="Select a Row:")
        label3.pack()

        # Dictionary of row prices
        row_prices = {
            "Front Row": 100.00,
            "Row 2": 85.00,
            "Row 3": 75.00,
            "Row 4": 50.00,
            "Row 5": 40.00,
            "Row 6": 30.00,
            "Row 7": 20.00,
        }

        # Create buttons for each row with price information
        for row, price in row_prices.items():
            row_button = tk.Button(self.seat_window, text=f"{row} (${price:.2f}", command=lambda r=row, p=price: controller.select_seat(r, p))
            row_button.pack()
            self.row_buttons.append(row_button)

# ConfirmationView module
class ConfirmationView:
    def __init__(self, root, controller, selected_movie, selected_seat, selected_price):
        self.root = root
        self.controller = controller

        # Create a new window for confirmation
        self.confirmation_window = tk.Toplevel(root)
        self.confirmation_window.title("Confirmation")

        # Display the selected movie
        label4 = tk.Label(self.confirmation_window, text=f"Selected Movie: {selected_movie}")
        label4.pack()

        # Display the selected seat and price
        label5 = tk.Label(self.confirmation_window, text=f"Selected Seat: {selected_seat} (${selected_price:.2f}")
        label5.pack()

        # Button to confirm the purchase
        confirm_button = tk.Button(self.confirmation_window, text="Confirm Purchase", command=controller.confirm_purchase)
        confirm_button.pack()

        # Button to cancel the purchase
        cancel_button = tk.Button(self.confirmation_window, text="Cancel Purchase", command=controller.cancel_purchase)
        cancel_button.pack()

# ThankYouView module
class ThankYouView:
    def __init__(self, root):
        self.root = root

    def show_thank_you(self):
        # Create a new window to display a thank you message
        thank_you_window = tk.Toplevel(self.root)
        thank_you_window.title("Thank You!")

        # Load and display a thank you image
        thank_you_image = PhotoImage(file="C:\\Users\\bjame\\Downloads\\machs_project_2.png")
        image_label = tk.Label(thank_you_window, image=thank_you_image)
        image_label.image = thank_you_image
        image_label.pack()

        # Display a thank you message
        label6 = tk.Label(thank_you_window, text="Thank you for shopping at First Seat!")
        label6.pack()

# Controller module
class Controller:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.movie_selection_view = MovieSelectionView(root, self)
        self.seat_selection_view = None
        self.confirmation_view = None
        self.thank_you_view = ThankYouView(root)

    # Handle movie selection
    def select_movie(self, movie):
        self.model.selected_movie = movie
        self.movie_selection_view.root.withdraw()
        self.open_seat_selection()

    # Handle seat selection
    def select_seat(self, seat, price):
        self.model.selected_seat, self.model.selected_price = seat, price
        self.open_confirmation()

    # Confirm the purchase
    def confirm_purchase(self):
        if self.confirmation_view:
            self.confirmation_view.confirmation_window.destroy()
            self.open_thank_you(purchase_confirmed=True)

    # Cancel the purchase and return to seat selection
    def cancel_purchase(self):
        if self.confirmation_view:
            self.confirmation_view.confirmation_window.destroy()
        self.model.selected_movie = ""
        self.return_to_movie_selection()

    # Open the seat selection view
    def open_seat_selection(self):
        self.seat_selection_view = SeatSelectionView(self.root, self)

    # Open the confirmation view
    def open_confirmation(self):
        self.confirmation_view = ConfirmationView(self.root, self, self.model.selected_movie, self.model.selected_seat, self.model.selected_price)

    # Open the movie selection view
    def open_movie_selection(self):
        self.model.selected_movie = ""
        self.seat_selection_view = None
        self.confirmation_view = None
        self.movie_selection_view.root.deiconify()

    # Open the thank you view and close the seat selection window
    def open_thank_you(self, purchase_confirmed=False):
        if self.seat_selection_view:
            self.seat_selection_view.seat_window.destroy()
        if purchase_confirmed:
            self.thank_you_view.show_thank_you()

    # Return to the movie selection view
    def return_to_movie_selection(self):
        if self.seat_selection_view:
            self.seat_selection_view.seat_window.destroy()
        self.movie_selection_view.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("First Seat - Choose a Movie")

    model = Model()
    controller = Controller(root, model)

    root.mainloop()