'''Global vars'''
seed = 70
m = 4
n = 4
start = (m-1,0)
end = (0,0)

def matrixMaze():
    '''A function.'''
    
    def _starterMatrix():
        np.random.seed(seed)
        dim_matrix = (m, n)
        starter_matrix = np.random.randint(1, 100, (dim_matrix))
        starter_matrix = starter_matrix % 2
        return starter_matrix, dim_matrix
    starter_matrix, dim_matrix = _starterMatrix()
    
    def _gameMatrix(starter_matrix):
        
        if len(starter_matrix) == 0:
            return 'Null. Empty matrix'
        
        game_matrix = []
        for i in range(m):
            game_matrix.append(['T' if x != 1 else 'F' for x in starter_matrix[i]])
        game_matrix = np.array(game_matrix)
        
        if game_matrix[start][0]  == 'T' or game_matrix[end][0] == 'T':
            return 'Null. Start: {}, End: {}'.format(game_matrix[start][0][0], game_matrix[end][0][0])
        else:
            print('Ready to play! Start: {}, End: {}'.format(game_matrix[start][0][0], game_matrix[end][0][0]))
            print(game_matrix)
        return game_matrix
    game_matrix = _gameMatrix(starter_matrix)
    
    def _movePawn():
        now_on = start
        now_on = np.array(now_on)
        count = 0
        move_row = 1
        while move_row <= 4:
            print(start)
            for i in range(n-now_on[1]):
                print('---{}----'.format(i))
                print(now_on)
                print('rows moved ={}'.format(move_row))
                if game_matrix[now_on[0], i] == 'F' and game_matrix[now_on[0], i+1] == 'T':
                    now_on = (now_on[0]-move_row, i)
                    count += 1
                    print('Count ={}'.format(count))
                    print('Now on {}'.format(now_on))
                    print('Right is {}. Its value is {}'.format((now_on[0], now_on[1]+1), game_matrix[now_on[0], now_on[1]+1]))
                    print('Left is {}. Its value is {}'.format((now_on[0], now_on[1]-1), game_matrix[now_on[0], now_on[1]-1]))
                    print('---------------------')
                if game_matrix[now_on[0], i] == 'F' and game_matrix[now_on[0], i-1] == 'T':
                    now_on = (now_on[0]-move_row, i-1)
                    count += 2
                    print('Count ={}'.format(count))
                    print('Now on {}'.format(now_on))
                    print('Right is {}. Its value is {}'.format((now_on[0], now_on[1]+1), game_matrix[now_on[0], now_on[1]+1]))
                    print('Left is {}. Its value is {}'.format((now_on[0], now_on[1]-1), game_matrix[now_on[0], now_on[1]-1]))
                if now_on == end:
                    return count
            move_row += 1

    count =_movePawn()
    return count

count = matrixMaze()
print(count)