# -*- coding: UTF-8 -*-
class Dungeon:
    max_row = 32
    max_col = 32
    min_size = 10
    dungeon = [[0 for col in xrange(max_col)] for row in xrange(max_row)]

    def __init__(self):
        self.split_space()

    def to_string(self):
        for row in self.dungeon:
            print ''.join([str(col) for col in row])

    def split_space(self):
        room_size = {
            'start_row': 0,
            'start_col': 0,
            'end_row': self.max_row,
            'end_col': self.max_col
        }
        self.fill_range(room_size)

    def fill_range(self, room_size, count = 0):
        start_row = room_size.get('start_row')
        start_col = room_size.get('start_col')
        end_row = room_size.get('end_row')
        end_col = room_size.get('end_col')

        for row_index, row in enumerate(self.dungeon[start_row:end_row]):
            for col_index, col in enumerate(row[start_col:end_col]):
                new_size = self.dichotomous_split(room_size, row_index, col_index, count)

        count = count + 1
        rest_row = new_size.get('end_row') - new_size.get('start_row')
        rest_col = new_size.get('end_col') - new_size.get('end_row')

        if (rest_row < self.min_size and rest_col < self.min_size):
            return
        else:
            self.fill_range(new_size, count)

    def dichotomous_split(self, room_size, row_index, col_index, count):
        begin_row = room_size.get('start_row')
        begin_col = room_size.get('start_col')
        target_row = room_size.get('end_row')
        target_col = room_size.get('end_col')

        if (count % 2 == 0):
            target_row = (target_row - begin_row) / 2
            if (row_index == target_row):
                self.dungeon[row_index][col_index] = 1
        else :
            target_col = (target_col - begin_col) / 2
            if (col_index == target_col):
                self.dungeon[row_index][col_index] = 1

        return {
            'start_row': begin_row,
            'start_col': begin_col,
            'end_row': target_row,
            'end_col': target_col
        }


dungeon = Dungeon()
dungeon.to_string()
