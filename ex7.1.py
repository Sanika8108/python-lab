

email_text = """
Hello John!
Please contact us at support@example.com.
Our website is example.com!
"""

symbols = ["@", ".", "!"]

for symbol in symbols:
    count = email_text.count(symbol)
    print(f"'{symbol}' occurs {count} time(s)")
