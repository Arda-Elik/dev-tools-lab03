#!/usr/bin/env python3
"""Main entry point for legacy-service."""
from utils import format_response
from database import connect_db


def main():
    print("Starting legacy-service...")
    connect_db()
    print(format_response("OK"))


if __name__ == "__main__":
    main()
