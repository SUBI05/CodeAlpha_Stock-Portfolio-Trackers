import yfinance as yf

class StockPortfolio:
    def __init__(self):  
        
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        """Add or update stock in the portfolio."""
        if ticker in self.portfolio:
            self.portfolio[ticker]['shares'] += shares
        else:
            self.portfolio[ticker] = {'shares': shares}
        print(f"Added {shares} shares of {ticker} to the portfolio.")

    def remove_stock(self, ticker, shares):
        """Remove shares from the portfolio."""
        if ticker in self.portfolio:
            if self.portfolio[ticker]['shares'] >= shares:
                self.portfolio[ticker]['shares'] -= shares
                
                if self.portfolio[ticker]['shares'] == 0:
                    del self.portfolio[ticker]
                print(f"Removed {shares} shares of {ticker} from the portfolio.")
            else:
                print("Not enough shares to remove.")
        else:
            print(f"{ticker} is not in the portfolio.")

    def track_performance(self):
        """Track the current value of the portfolio."""
        total_value = 0
        print("\nStock Portfolio Performance:")
        for ticker, data in self.portfolio.items():
            stock_data = yf.Ticker(ticker)
            current_price = stock_data.history(period="1d")["Close"].iloc[0]  # Get current price
            stock_value = current_price * data['shares']
            total_value += stock_value
            print(f"{ticker}: {data['shares']} shares, Current Price: ${current_price:.2f}, Total: ${stock_value:.2f}")
        
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")


def main():
    portfolio = StockPortfolio()

    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio Performance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter the stock ticker (e.g., AAPL, TSLA): ").upper()
            shares = int(input("Enter the number of shares: "))
            portfolio.add_stock(ticker, shares)

        elif choice == '2':
            ticker = input("Enter the stock ticker to remove (e.g., AAPL, TSLA): ").upper()
            shares = int(input("Enter the number of shares to remove: "))
            portfolio.remove_stock(ticker, shares)

        elif choice == '3':
            portfolio.track_performance()

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":  
    main()