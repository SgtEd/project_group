import api, cash_on_hand, profit_loss, overheads

def main():
    """
    This function is to write a summary using value found in api,cash_on_hand,profit_loss,overheads.
    
    """
    exchange_data = api.getData()
    print("Exchange rate: ", exchange_data)

    cash_on_hand_data = cash_on_hand.readCSV(exchange_data)

    profit_loss_data = profit_loss.readCSV(exchange_data)

    overhead_data = overheads.readCSV(exchange_data)

    print("Writing summary report..")

    with open("summary_report.txt", "w") as f:

        f.write("[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD")
        f.write(str(exchange_data))
        f.write("\n")

        for x in cash_on_hand_data:

            f.write("[CASH DEFICIT] Day: ")
            f.write(x[0])
            f.write(", ")

            f.write("AMOUNT: SGD")
            f.write(str(x[1]))
            f.write("\n")

        for y in profit_loss_data:

            f.write("[PROFIT DEFICIT] DAY: ")
            f.write(y[0])
            f.write(", ")

            f.write("AMOUNT: SGD")
            f.write(str(y[1]))
            f.write("\n")

        

        f.write("[HIGHEST OVERHEADS] ")
        f.write(overhead_data[0])
        f.write(": SGD")
        f.write(str(overhead_data[1]))

    print("Summary report done!")


main()