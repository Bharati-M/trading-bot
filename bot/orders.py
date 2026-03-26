import logging


def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing order: {symbol} {side} {order_type}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol, side=side, type="MARKET", quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )
        else:
            raise ValueError("Invalid order type")

        logging.info(f"Order response: {order}")
        return order

    except Exception as e:
        print("ERROR:", str(e))  # 👈 add this
        logging.error(f"Error: {str(e)}")
        return None
