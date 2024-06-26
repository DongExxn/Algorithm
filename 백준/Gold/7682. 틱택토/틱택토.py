# import sys; input = sys.stdin.readline
def check_line(string, player):
    ret = False
    if player == string[0] == string[1] == string[2]\
            or player == string[3] == string[4] == string[5]\
            or player == string[6] == string[7] == string[8]\
            or player == string[0] == string[3] == string[6]\
            or player == string[1] == string[4] == string[7]\
            or player == string[2] == string[5] == string[8]\
            or player == string[0] == string[4] == string[8]\
            or player == string[2] == string[4] == string[6]:
        ret = True
    return ret

def check_string(string):
    win_x, win_o = check_line(string, 'X'), check_line(string, 'O')
    num_x, num_o, num_dot = string.count('X'), string.count('O'), string.count('.')
    if (win_x and not win_o and num_x == num_o + 1)\
            or (not win_x and win_o and num_x == num_o)\
            or (not win_x and not win_o and num_x == 5 and num_o == 4):
        return "valid"
    return "invalid"


def main():
    answer = []
    while True:
        string = input().rstrip()
        if string == "end":
            break
        answer.append(check_string(string))
    print(*answer, sep='\n')


if __name__ == "__main__":
    main()