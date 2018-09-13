from random import randint, choice


class Player(object):

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.tiles = {x: 'black' if x % 2 == 0 else 'white' for x in range(9)}
        self.not_played = self.tiles.copy()
        self.is_first_player = choice([True,False])

    def play_tile(self, tile):
        if tile in self.not_played:
            del self.not_played[tile]
            return tile
        else:
            raise KeyError

    def game_turn(self):
        while True:
            prompt = raw_input('%s, select a tile to play.\n' % self.name)
            try:
                tile = int(prompt)
                self.play_tile(tile)
                print '{} has played a {} tile'.format(self.name,self.tiles[tile])
                return tile
            except (TypeError, ValueError, KeyError) as e:
                print 'That isn\'t an acceptable tile.'

    def check_tiles(self):
        return self.not_played

    def check_score(self):
        return self.score

    def check_other(self, other):
        return '{} has {} wins and has yet to play the following tiles: {}'\
            .format(other.name, other.score)


class Robot(Player):

    def __init__(self, name, player):
        Player.__init__(self, name)
        self.player = player

    def ai_routine(self):
        return randint(0,8)

    def play_tile(self, tile):
        if tile in self.not_played:
            del self.not_played[tile]
            return tile

    def game_turn(self):
        tile = self.ai_routine()
        print '{} has played a {} tile'.format(self.name,self.tiles[tile])
        return tile


def game_round(first_player, second_player):
    first_tile = first_player.game_turn()
    second_tile = second_player.game_turn()
    if first_tile > second_tile:
        print '{} wins'.format(first_player.name)
        first_player.score += 1
    elif first_tile == second_tile:
        print 'Draw.'
    else:
        print '{} wins'.format(second_player.name)
        first_player.is_first_player = False
        second_player.is_first_player = True
        second_player.score += 1


def winner_check(player, robot):
    if player.score < robot.score:
        print '{} with {} points to {}'.format(robot.name, robot.score, player.score)
    elif player.score > robot.score:
        print '{} with {} points to {}'.format(player.name, player.score, robot.score)
    else:
        print 'The result is a draw: {} - {}'.format(player.score, robot.score)


def black_and_white(player, robot):
    round_no = 1
    while round_no <= 9 and player.score < 5 and robot.score < 5:
        print 'You have the following tiles remaining: {}'.format(player.not_played.keys())
        if player.is_first_player:
            game_round(player, robot)
        else:
            game_round(robot, player)
        round_no += 1
    return winner_check(player, robot)


if __name__ == "__main__":
    player = Player('Eddy')
    player2 = Player('Hugh')
    ai_player = Robot('AI', player)
    black_and_white(player, player2)