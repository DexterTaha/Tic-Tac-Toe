def print_board(T):
    print("\n")
    print(" {} | {} | {} ".format(T[0][0], T[0][1], T[0][2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(T[1][0], T[1][1], T[1][2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(T[2][0], T[2][1], T[2][2]))
    print("\n")

def check_winner(T, J):
    return ((T[0][0] == J and T[0][1] == J and T[0][2] == J) or
            (T[1][0] == J and T[1][1] == J and T[1][2] == J) or
            (T[2][0] == J and T[2][1] == J and T[2][2] == J) or
            (T[0][0] == J and T[1][0] == J and T[2][0] == J) or
            (T[0][1] == J and T[1][1] == J and T[2][1] == J) or
            (T[0][2] == J and T[1][2] == J and T[2][2] == J) or
            (T[0][0] == J and T[1][1] == J and T[2][2] == J) or
            (T[0][2] == J and T[1][1] == J and T[2][0] == J))

def is_board_full(T):
    for row in T:
        if ' ' in row:
            return False
    return True

def main():
    T = [[' ' for _ in range(3)] for _ in range(3)]
    J = 'X'
    G = False
    E = False

    print_board(T)

    while not G and not E:
        try:
            V, H = map(int, input("Joueur {}, enter your move (VERTIVALE ET HORIZONTALE): ".format(J)).split())
        except ValueError:
            print("Invalid input! Enter two numbers separated by a space.")
            continue
        
        if V < 0 or V >= 3 or H < 0 or H >= 3 or T[V][H] != ' ':
            print("Invalid move! Try again.")
            continue

        T[V][H] = J
        print_board(T)

        if check_winner(T, J):
            G = True
        else:
            J = 'O' if J == 'X' else 'X'
        
        E = is_board_full(T)

    if G:
        print("\nJoueur {} Vous êtes gagnez!\n".format(J))
    else:
        print("\nVous êtes en égalité!\n")

if __name__ == "__main__":
    main()
