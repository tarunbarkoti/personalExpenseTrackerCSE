# Personal Expense Tracker

This is a simple Python-based command-line application that helps you track your personal expenses. You can record expenses, view past expenses, see a summary of monthly expenses, and visualize your data through charts. This project is submitted as part of the CCE IIT Mandi Minor in CSE program, under the subject code CSE101.


## Features

1. **Add Expense**
   - Record your expenses by entering the date, category, description, and amount.
   - Supports both current and custom dates.

2. **View Expenses**
   - Display all recorded expenses in a paginated format.
   - Organized and easy-to-read tabular layout.

3. **Monthly Summary**
   - View a summary of expenses for the last 6 months, categorized by month.

4. **Data Visualization**
   - Generate and view:
     - Bar charts for monthly expenses.
     - Line plots for weekly expenses.
     - Pie charts for category-wise expense distribution.

5. **File Storage**
   - All data is saved to a CSV file (`expenses.csv`) for persistence.

---

## How to Use

1. **Clone the Repository**
   ```bash
   git clone https://github.com/tarunbarkoti/personalExpenseTrackerCSE.git
   cd personalExpenseTrackerCSE
   ```

2. **Install Requirements**
   Install the required Python libraries using the provided `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Run the main script to start the expense tracker:
   ```bash
   python expense_tracker.py
   ```

4. **Choose an Option**
   Select from the menu options to:
   - Add a new expense.
   - View or summarize expenses.
   - Visualize data.

---

## File Structure

- **`expense_tracker.py`**: Main script containing all application logic.
- **`expenses.csv`**: File where all expense data is stored.
- **`requirements.txt`**: List of required Python libraries.
- **`youtubeLink.txt`**: youtube video link with details for the project.
- **`README.md`**: Documentation for the project.

---

## Requirements

The application requires the following Python libraries:

- `matplotlib`: For data visualization.
- `python-dateutil`: For working with flexible date formats.

To install these libraries, run:
```bash
pip install -r requirements.txt
```

---

## Example Usage

### Adding an Expense
```
Do you confirm the current date and time? (yes/no): yes
Enter the category (e.g., Food, Transport, Bills): Food
Enter a description: Lunch with friends
Enter the amount: 15.75
Expense added successfully.
```

### Viewing Expenses
```
Date           Category        Description              Amount    
-------------------------------------------------------------
28-12-2025     Food           Lunch with friends       15.75     
27-12-2025     Transport      Uber Ride                12.50     
```

### Monthly Summary
```
--- Monthly Expenses (Last 6 Months) ---
Dec-2025: 250.00
Nov-2025: 180.50
```

---

## License
This project is licensed under the MIT License.

---

## Contributing
If you would like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request. Make sure to include tests for any new features or bug fixes.

---

## Author
Tarun Barkoti

