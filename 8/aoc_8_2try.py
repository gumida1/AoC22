import numpy as np
rows, cols, index_c, index_r, right, bot, left, top, result = 0, 0, -1, -1, 0, 0, 0, 0, 0 
end = False
with open('input_1.txt') as f:
    lines = f.readlines()
    for line in lines:
        rows += 1
        cols = 0
        for c in line:
            cols += 1        
    tree_grid = np.zeros((rows, cols), dtype='object')        
    
    for line in lines:
        index_r += 1
        for sym in line:
            index_c += 1
            if not sym == '\n': tree_grid[index_r][index_c] = sym
        index_c = -1        
            
    for row in range(rows):
        for col in range(cols):
            tree_height = tree_grid[row][col]
            saved_row, saved_col = row, col
            while not end:  #doprava
                col += 1
                cur_col = col   
                if cur_col > len(tree_grid[0])-1:
                    end = True
                else:   
                    cur_tree = tree_grid[row][cur_col]
                    right += 1
                    if cur_tree >= tree_height:
                        end = True
            row, col = saved_row, saved_col
            end = False
            while not end:  #doleva
                col += -1
                cur_col = col            
                cur_tree = tree_grid[row][cur_col]
                left += 1
                if cur_col < 0:
                    end = True
                    left += -1
                if cur_tree >= tree_height:
                    end = True
            end = False
            row, col = saved_row, saved_col
            while not end:  #dolu
                row += 1
                cur_row = row   
                if cur_row > len(tree_grid)-1:
                    end = True
                else:   
                    cur_tree = tree_grid[cur_row][col]
                    bot += 1
                    if cur_tree >= tree_height:
                        end = True
            end = False
            row, col = saved_row, saved_col
            while not end:  #nahoru
                row += -1
                cur_row = row   
                if cur_row < 0:
                    end = True
                else:   
                    cur_tree = tree_grid[cur_row][col]
                    top += 1
                    if cur_tree >= tree_height:
                        end = True
            end = False
            row, col = saved_row, saved_col
            if (right * left * top * bot > result):
                result = right * left * top * bot
            right, left, bot, top = 0, 0, 0, 0
    
print(result)