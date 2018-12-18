#!usr/bin/python
# coding: utf-8

# Very similar to a simple parser for Ook! language
# I know that this implementation was not elegant and even *suck*
# But at lesat I (seemingly?) works fine for flag-like sentences :)

import os

def ook_decode(commands):
    """
    @param commands: list of commands\n
    @return string
    """
    result = ""
    ptr = 0
    cells = [0]
    if len(commands) % 2:
        print("Commands length error.")
        return "[Errors]"

    _tmp = ""
    _ptr_commands = 0

    _ptr_parentheses_1 = -1
    _ptr_parentheses_2 = -1

    _len = len(commands)
    while _ptr_commands < _len:
        _tmp = ""
        _tmp += commands[_ptr_commands]
        _ptr_commands += 1
        _tmp += " "
        _tmp += commands[_ptr_commands]
        _ptr_commands += 1

        if _tmp == "Ook. Ook?":
            ptr += 1
            if ptr >= len(cells):
                cells.append(0)
        elif _tmp == "Ook? Ook.":
            ptr -= 1            
        elif _tmp == "Ook. Ook.":
            cells[ptr] += 1
        elif _tmp == "Ook! Ook!":
            cells[ptr] -= 1
        elif _tmp == "Ook. Ook!":
            _input = input("> ")
            cells[ptr] = hex(ord(_input[0]))
        elif _tmp == "Ook! Ook.":
            # print(chr(cells[ptr]))
            result += chr(cells[ptr])
        elif _tmp == "Ook! Ook?":
            _ptr_parentheses_1 = _ptr_commands
            _ptr_parentheses_2 = find_following_parenthese(commands, _ptr_commands)
            if cells[ptr] != 0:
                pass
            else:
                if _ptr_parentheses == -1:
                    result = "[Commands Errors]"
                    break
        elif _tmp == "Ook? Ook!":
            if cells[ptr] == 0:
                pass
            else:
                _ptr_commands = _ptr_parentheses_1
    return result


def find_following_parenthese(commands, ptr):
    _ptr = ptr
    _len = len(commands) - _ptr
    while _ptr < _len:
        _tmp = ""
        _tmp += commands[_ptr]
        _ptr += 1
        _tmp += " "
        _tmp += commands[_ptr]
        _ptr += 1
        if _tmp == "Ook? Ook!":
            return _ptr - 2
        else:
            pass
    return -1


if __name__ == "__main__":
    commands = []
    # Honestly, WTF is the inconvenience of opening relative path in Window
    with open(os.path.dirname(__file__) + '/encrypt.bin', 'r') as fp:
        for line in fp:
            commands.extend(line.strip('\n').split(' '))
    print(len(commands))
    result = ook_decode(commands)
    print(result)