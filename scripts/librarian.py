import sqlite3
import sys
from typing import Tuple

db = sqlite3.connect('sqlite.db')
__commmit_token = "--commit"
__find_token = "--find"
__manual_token = "--manual"

commit_op = {"--add", "--copy", "--delete",
             "--modify", "--rename", "--type", __commmit_token}

find_op = {"--tag", "--author", "--name", "--isbn", __find_token}

manual_op = {"--tag", "--author", "--name", "--isbn", "--path",  __manual_token}

operations = set.union(commit_op, find_op, manual_op)

# The args is an dict of str to list


def __add(books: list):
    # FIXME: Complete this
    pass


def __copy(books: list):
    # FIXME: Complete this
    pass


def __delete(books: list):
    # FIXME: Complete this
    pass


def __modify(books: list):
    # FIXME: Complete this
    pass


def __rename(books: list):
    # FIXME: Complete this
    pass


def __type(books: list):
    # FIXME: Complete this
    pass


def commit(**args: list) -> None:
    def check_arg_num(args: dict[str, list]) -> bool:
        total = len(args[__commmit_token])
        __sum = sum([len(args[i]) for i in args])
        return __sum != total * 2
    if (check_arg_num(args)):
        raise ValueError('Wrong args num:', args)

    for key in args:
        if key in commit_op and key != __commmit_token:
            print(key, "books:", args[key])
            # Well, this might be some dynamic binding
            exec("__" + key[2:] + "(args[key])")

# Return list of result
def find(**args: list) -> list:
    # FIXME: complete this
    pass

def manual(**args: list) -> None:
    # FIXME: Complete this
    pass


def show_usage():
    print("""
    python3 ./scripts/librarian.py --[method] --[tags [value ...]]

    [method]: 
        commit: To update the sqlite.db of this library, 
                set all tag are empty unless it had "manual" before.
                Notice: The must have a "commit" tag, which follows all commit files.
        find: To find some books that match tags' value
        manual: To specify the tags, author, ISBN, name to the database
    
    [tags]:
        (commit) method:
            add: Book added
            copy: Book copied
            delete: Book deleted
            modify: Book modified
            rename: Book renamed
            type: Book type (i.e. regular file, symlink, submodule, …​) changed
        (find) method:
            tag: Those single tags.
                    eg: UNIX, 英文, coding
            author: The author's name
                    eg: Chih-Hsuan Yang, "Chih-Hsuan Yang" or 'Chih-Hsuan Yang' are same.
            name: The book name
                    eg: Advanced Programming in the UNIX Environment, 
                        "Advanced Programming in the UNIX Environment",
                        'Advanced Programming in the UNIX Environment'
                        are same.
            isbn: The string of isbn (will not check anything)
        (manual) method:
            Same as (find). and must
            Follows a --path tag, the path tag including the "filename", 
                                    which can be an absolute path or relative path.

    Example:
        python3 ./scripts/librarian.py --commit A.pdf B.pdf --add B.pdf A.pdf
        python3 ./scripts/librarian.py --commit # Do nothing

        python3 ./scripts/librarian.py --find --tag A B C D E --author Chih-Hsuan Yang
        python3 ./scripts/librarian.py --find --tag A B C D E --author "Chih-Hsuan Yang"

        python3 ./scripts/librarian.py --manual --tag foo bar --author 'Chih-Hsuan Yang' --path a/b/c/ed/me.pdf
        python3 ./scripts/librarian.py --manual --tag foo bar --isbn dadada --author "Chih-Hsuan Yang" --path /home/user/Desktop/me.pdf
    """)


def parse_argv() -> dict[str, list]:
    res = dict()
    files = []
    prev_op = ''
    for item in sys.argv:
        if (item not in operations) and not (item == sys.argv[0]):
            files.append(item)
        elif item in operations:
            res[prev_op] = files[:]
            prev_op = item[:]
            files = []
        else:
            pass
    res[prev_op] = files  # Push the final list
    res.pop('')  # Remove the first time's empty str of empty list
    return res


if __name__ == '__main__':
    args = parse_argv()
    if (args[__commmit_token] != None):
        commit(**args)
    elif (args[__find_token] != None):
        del args[__find_token]
        find(args)
    elif (args[__manual_token] != None):
        del args[__manual_token]
        manual(args)
    else:
        show_usage()
        sys.exit(1)
