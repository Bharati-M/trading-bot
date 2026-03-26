import argparse
import os
import sys

# Add bot folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), "bot"))

from client import get_client
from logging_config import setup_logging
from orders import place_order
from validators import validate_inputs


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    setup_logging()

    try:
        validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)

        client = get_client()

        print("\n📌 Order Request Summary:")
        print(vars(args))

        order = place_order(
            client, args.symbol, args.side, args.type, args.quantity, args.price
        )

        if order:
            print("\n✅ Order Success!")
            print(order)
        else:
            print("\n❌ Order Failed!")

    except Exception as e:
        print(f"\n⚠️ Error: {str(e)}")


if __name__ == "__main__":
    main()
