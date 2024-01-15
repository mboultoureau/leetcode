class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(int)
        players = set()
        for match in matches:
            players.add(match[0])
            players.add(match[1])
            scores[match[1]] += 1


        no_losses = []
        one_loss = []
        for player in players:
            if player not in scores or scores[player] == 0:
                no_losses.append(player)
            elif scores[player] == 1:
                one_loss.append(player)

        return [sorted(no_losses), sorted(one_loss)]