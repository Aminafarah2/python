# # def find_last_round(skills):
# #     # Number of players
# #     n = len(skills)
    
# #     # Initialize a list to track the remaining players in each round
# #     remaining_players = list(range(n))
    
# #     # Initialize a list to store the last round each player participates in
# #     last_rounds = [-1] * n
    
# #     # Simulate tournament rounds
# #     round_number = 1
# #     while len(remaining_players) > 1:
# #         next_round_players = []
# #         for i in range(0, len(remaining_players), 2):
# #             # Determine winner of the match
# #             winner_index = max(remaining_players[i], remaining_players[i + 1], key=lambda x: skills[x])
# #             next_round_players.append(winner_index)
# #             # Update last round for each player
# #             last_rounds[remaining_players[i]] = round_number
# #             last_rounds[remaining_players[i + 1]] = round_number
# #         remaining_players = next_round_players
# #         round_number += 1
    
# #     return last_rounds

# # def solution(skills):
# #     return find_last_round(skills)

# # # Example usage:
# # skills = [4, 22, 7, 3, 1, 8, 6, 5]
# # print(solution(skills))  # Output: [3, 3, 2, 3, 1, 2, 2, 2]
# def find_last_round(skills):
#     # Number of players
#     n = len(skills)
    
#     # Initialize a list to track the remaining players in each round
#     remaining_players = list(range(n))
    
#     # Initialize a list to store the last round each player participates in
#     last_rounds = [-1] * n
    
#     # Simulate tournament rounds
#     round_number = 1
#     while len(remaining_players) > 1:
#         next_round_players = []
#         i = 0
#         while i < len(remaining_players):
#             # Determine winner of the match
#             player1 = remaining_players[i]
#             player2 = remaining_players[i + 1] if i + 1 < len(remaining_players) else None
#             if player2 is None or skills[player1] > skills[player2]:
#                 winner_index = player1
#             else:
#                 winner_index = player2
#             next_round_players.append(winner_index)
#             # Update last round for each player
#             last_rounds[player1] = round_number
#             if player2 is not None:
#                 last_rounds[player2] = round_number
#             i += 2
#         remaining_players = next_round_players
#         round_number += 1
    
#     return last_rounds

# def solution(skills):
#     return find_last_round(skills)

# # Example usage:
# skills = [2, 1, 3, 1, 1, 3, 2, 1]

# print(solution(skills))  # Output: [2, 1, 3, 1, 1, 3, 2, 1]


def find_last_round(skills):
    n = len(skills)
    remaining_players = list(range(n))
    last_rounds = [-1] * n
    round_number = 1
    while len(remaining_players) > 1:
        next_round_players = []
        i = 0
        while i < len(remaining_players):
            player1 = remaining_players[i]
            player2 = remaining_players[i + 1] if i + 1 < len(remaining_players) else None
            if player2 is None or skills[player1] > skills[player2]:
                winner_index = player1
            else:
                winner_index = player2
            next_round_players.append(winner_index)
            last_rounds[player1] = round_number
            if player2 is not None:
                last_rounds[player2] = round_number
            i += 2
        remaining_players = next_round_players
        round_number += 1
    return last_rounds

def solution(skills):
    return find_last_round(skills)

