import utils
import argparse
from pathlib import Path
from webwriter import (
    Automator,
    COOKIES_FILE
)


def main():

    #tạo arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--sleep",
        type=int,
        default=2,
        help=f"Sleep time between posts in seconds (default is 2 second)",
    )
    parser.add_argument(
        "-c",
        "--cookies_file",
        type=str,
        default=COOKIES_FILE,
        help=f"Binary file that contains saved cookies for authentication. \
               By default -- {COOKIES_FILE}",
    )
    parser.add_argument(
        "-l",
        "--login",
        type=str,
        default=None,
        help="Login or email for authentication",)
    parser.add_argument(
        "-m",
        "--max",
        type=int,
        default=510,
        help=f"Maximum number of posts (Max is 510), there may not be  \
        able to execute all posts (default is 510)", )
    parser.add_argument(
        "-p", "--password", type=str, default=None, help="Password for authentication"
    )

    args = parser.parse_args()

    loader = Automator(
        cookies_file=args.cookies_file,
        login=args.login,
        max=args.max,
        password=args.password,
        sleep=args.sleep,
    )
    if not Path(args.cookies_file).is_file():
        print(
            f"Cookies file({args.cookies_file}) are not detected. Please, "
            + "login in next step for generate cookie for next runs."
        )
        loader.init_browser(headless=False)
    else:
        path = "./dapan"
        newExtension = ".txt"
        utils.extensionChanger(path, newExtension)
        print(f"Using cookies file: {args.cookies_file}")
        loader.init_browser(headless=True)
        loader.submit()


if __name__ == "__main__":
    main()
