    # -*- coding: utf-8 -*-
    """
    Created on Sat Dec 28 12:19:45 2025

    @author: tarunbarkoti
    """

    import csv
    import os
    import matplotlib.pyplot as plt
    from datetime import datetime, timedelta
    from collections import defaultdict
    from dateutil.relativedelta import relativedelta


    # File where expenses will be saved
    EXPENSES_FILE = 'expenses.csv'


    def ensure_expenses_file_exists():
        """Ensure the expenses file exists, create if not."""
        if not os.path.exists(EXPENSES_FILE):
            with open(EXPENSES_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Category', 'Description', 'Amount'])


    def record_expense():
        """Prompt the user to add an expense record."""
        while True:
            confirmation = input("Do you confirm the current date and time? (yes/no): ").strip().lower()
            if confirmation == 'yes':
                date = datetime.now().strftime("%d-%m-%Y")
                print(f"Date confirmed: {date}")
                break
            elif confirmation == 'no':
                while True:
                    entered_date = input("Enter the date (DD-MM-YYYY): ").strip()
                    try:
                        valid_date = datetime.strptime(entered_date, "%d-%m-%Y")
                        date = valid_date.strftime('%d-%m-%Y')
                        print(f"Date entered: {date}")
                        break
                    except ValueError:
                        print("Invalid date format. Please use the format DD-MM-YYYY.")
                break
            else:
                print("Invalid input. Please respond with 'yes' or 'no'.")

        category = input("Enter the category (e.g., Food, Transport, Bills): ")
        description = input("Enter a description: ")
        try:
            amount = round(float(input("Enter the amount: ")), 2)
        except ValueError:
            print("Invalid amount entered. Please enter a number.")
            return

        with open(EXPENSES_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, f"{amount:.2f}"])

        print("Expense added successfully.")


    def display_expenses():
        """Show a paginated view of all expenses."""
        try:
            with open(EXPENSES_FILE, mode='r', newline='') as file:
                reader = list(csv.reader(file))
                header = reader[0]
                rows = reader[1:]

                total_entries = len(rows)
                index = total_entries
                while index > 0:
                    start = max(0, index - 25)
                    batch = rows[start:index]

                    print(f"\n{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':<10}")
                    print("-" * 65)
                    for row in reversed(batch):
                        print(f"{row[0]:<15}{row[1]:<15}{row[2]:<25}{row[3]:<10}")
                    print("-" * 65)

                    if start == 0:
                        print("No more entries to display.")
                        break
                    more = input("Do you want to see more entries? (yes/no): ").strip().lower()
                    if more != 'yes':
                        break

                    index = start

        except FileNotFoundError:
            print("No expenses recorded yet.")


    def show_expenses_by_month():
        """Show the monthly summary of expenses."""
        try:
            with open(EXPENSES_FILE, mode='r', newline='') as file:
                reader = list(csv.reader(file))
                rows = reader[1:]

                today = datetime.now()
                last_6_months = today - relativedelta(months=6)

                monthly_expenses = defaultdict(float)

                for row in rows:
                    date = datetime.strptime(row[0], "%d-%m-%Y")
                    if date < last_6_months:
                        continue

                    month_key = date.strftime("%b-%Y")  # e.g., Jan-2024
                    monthly_expenses[month_key] += float(row[3])

                print("\n--- Monthly Expenses (Last 6 Months) ---")
                sorted_months = sorted(monthly_expenses.items())
                filtered_months = [month for month in sorted_months if datetime.strptime(month[0], "%b-%Y") >= last_6_months]
                for month, total in filtered_months:
                    print(f"{month}: {total:.2f}")

        except FileNotFoundError:
            print("No expenses recorded yet.")


    def plot_expenses():
        """Generate and display plots based on the expense data."""
        try:
            with open(EXPENSES_FILE, mode='r', newline='') as file:
                reader = list(csv.reader(file))
                rows = reader[1:]

                monthly_expenses = defaultdict(float)
                weekly_expenses = defaultdict(float)
                category_expenses = defaultdict(float)

                for row in rows:
                    date = datetime.strptime(row[0], "%d-%m-%Y")
                    month_key = date.strftime("%b-%Y")
                    week_number = date.strftime("%U")
                    week_start = (date - timedelta(days=date.weekday())).strftime("%d %b %Y")
                    week_end = (date + timedelta(days=(6 - date.weekday()))).strftime("%d %b %Y")
                    week_key = f"Week {week_number} ({week_start} - {week_end})"

                    category = row[1]

                    monthly_expenses[month_key] += float(row[3])
                    weekly_expenses[week_key] += float(row[3])
                    category_expenses[category] += float(row[3])

                # Plot Monthly Expenses
                months = list(monthly_expenses.keys())
                monthly_totals = list(monthly_expenses.values())
                plt.figure(figsize=(10, 6))
                plt.bar(months, monthly_totals, color='blue')
                plt.title("Monthly Expenses")
                plt.xlabel("Month")
                plt.ylabel("Total Amount")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

                # Plot Weekly Expenses
                weeks = list(weekly_expenses.keys())
                weekly_totals = list(weekly_expenses.values())
                plt.figure(figsize=(10, 6))
                plt.plot(weeks, weekly_totals, marker='o', color='orange')
                plt.title("Weekly Expenses")
                plt.xlabel("Week")
                plt.ylabel("Total Amount")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

                # Plot Category-Wise Distribution
                categories = list(category_expenses.keys())
                category_totals = list(category_expenses.values())
                plt.figure(figsize=(8, 8))
                plt.pie(category_totals, labels=categories, autopct='%1.1f%%', startangle=140)
                plt.title("Category-wise Expense Distribution")
                plt.show()

        except FileNotFoundError:
            print("No expenses recorded yet.")


    def show_main_menu():
        """Display the main menu and handle user input."""
        while True:
            print("\nPersonal Expense Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Show Monthly Summary")
            print("4. Visualize Data")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                record_expense()
            elif choice == '2':
                display_expenses()
            elif choice == '3':
                show_expenses_by_month()
            elif choice == '4':
                plot_expenses()
            elif choice == '5':
                print("See you next time.. Bye!")
                break
            else:
                print("Invalid option. Please try again.")


    if __name__ == '__main__':
        ensure_expenses_file_exists()
        show_main_menu()
