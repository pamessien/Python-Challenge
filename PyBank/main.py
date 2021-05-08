import os
import csv

months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
profit_loss_change = 0


os.chdir(os.path.dirname(__file__))


budget_data_csv_path = os.path.join("Resources", "budget_data.csv")


with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")


    csv_header = next(csvfile)

  
    for row in csv_reader:

        
        count_months += 1

        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            months.append(row[0])

            profit_loss_changes.append(profit_loss_change)

            previous_month_profit_loss = current_month_profit_loss


    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")




