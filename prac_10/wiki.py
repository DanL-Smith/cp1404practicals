"""
CP1404/CP5632 Practical
Wikipedia search program using wikipedia api
"""

import wikipedia


def main():
    search_phrase = input("Enter a page title or search phrase: ")
    while search_phrase != '':
        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(f"Title: {page.title}")
            print(f"Summary: {page.summary}")
            print(f"URL: {page.url}")
        except wikipedia.PageError:
            print("That search did not match any pages.")
        search_phrase = input("Enter a page title or search phrase: ")


if __name__ == "__main__":
    main()
