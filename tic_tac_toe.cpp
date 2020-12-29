// g++ -o program -std=c++11

#include <iostream>
#include <vector>
#include <map>
#include <math.h>

#define ROW 3
#define COL 3
#define PLAYER_X "x"
#define PLAYER_O "o"
#define E "-" // empty
#define N " " // nobody
#define MIN -100
#define MAX 100

using namespace std;
map<string,int> score;
bool finish = false;
bool play(vector<vector<string>> &board,int x,int y,string player);

vector<vector<string>> transpose(vector<vector<string>> (&board)){
    for(int i=0;i<ROW;i++){
        for(int k=i+1;k<COL;k++){
            string temp = board[k][i];
            board[k][i] = board[i][k];
            board[i][k] = temp;
        }
    }
    return board;
}

string check_winner(vector<vector<string>> board){
    // for horizontal control
    for(vector<string> row:board){
        int sum = score[row[0]] + score[row[1]] + score[row[2]];
        if(sum == 3){
            return PLAYER_O;
        }else if(sum == -3){
            return PLAYER_X;
        }
    }

    // for vertical control
    board = transpose(board);
    for(vector<string> row:board){
        int sum = score[row[0]] + score[row[1]] + score[row[2]];
        if(sum == 3){
            return PLAYER_O;
        }else if(sum == -3){
            return PLAYER_X;
        }
    }

    // for cross control
    int sum = score[board[0][0]] + score[board[1][1]] + score[board[2][2]];
    if(sum == 3){
        return PLAYER_O;
    }else if(sum == -3){
        return PLAYER_X;
    }

    sum = score[board[0][2]] + score[board[1][1]] + score[board[2][0]];
    if(sum == 3){
        return PLAYER_O;
    }else if(sum == -3){
        return PLAYER_X;
    }
    
    // tie?
    for(int i=0;i<ROW;i++){
        for(int k=0;k<COL;k++){
            if(board[i][k] == E){
                return N;
            }
        }
    }

    return E;
}

void draw_board(vector<vector<string>> board){
    for(vector<string> row:board){
        for(string col:row){
            cout<<col<<" ";
        }
        cout<<endl;
    }
}

int minmax(vector<vector<string>> board,int alpha,int beta,bool ismax){
    string winner = check_winner(board);
    if(winner != N){
        return score[winner];
    }

    if(ismax){
        int min_score = MIN;
        string temp;
        int result;

        for(int i=0;i<ROW;i++){
            for(int k=0;k<COL;k++){
                if(board[i][k] == E){
                    temp = board[i][k];
                    board[i][k] = PLAYER_O;
                    result = minmax(board,alpha,beta,false);
                    if(result>=min_score){
                        min_score = result;
                    }
                    board[i][k] = temp;

                    if(result >= beta){
                        break;
                    }else if(result > alpha){
                        alpha = result;
                    }
                    
                }
            }
        }
        return min_score;
    }else{
        int max_score = MAX;
        string temp;
        int result;

        for(int i=0;i<ROW;i++){
            for(int k=0;k<COL;k++){
                if(board[i][k] == E){
                    temp = board[i][k];
                    board[i][k] = PLAYER_X;
                    result = minmax(board,alpha,beta,true);
                    if(result<=max_score){
                        max_score = result;
                    }
                    board[i][k] = temp;

                    if(result <= alpha){
                        break;
                    }else if(result < beta){
                        beta = result;
                    }
                }
            }
        } 
        return max_score;
    }
}

void play_computer(vector<vector<string>> &board){
    struct{
        int x=0;
        int y=0;
    } best_move;

    string temp;
    int best_score = MIN;
    int result;

    for(int i=0;i<ROW;i++){
        for(int k=0;k<COL;k++){
            if(board[i][k] == E){
                temp = board[i][k];
                board[i][k] = PLAYER_O;
                result = minmax(board,MIN,MAX,false);
                if(result >= best_score){
                    best_score = result;
                    best_move.x = i;
                    best_move.y = k;
                }
                board[i][k] = temp;
            }
        }
    }
    cout<<"Computer: "<<best_move.x<<" "<<best_move.y<<endl;
    play(board,best_move.x,best_move.y,PLAYER_O);
    return;
}

bool play(vector<vector<string>> &board,int x,int y,string player){
    if(board[x][y] == E){
        board[x][y] = player;
        return true;
    }else{
        return false;
    }
}

int main(){
    score[PLAYER_X] = -1;
    score[PLAYER_O] = 1;
    score[E] = 0;

    vector<vector<string>> board = {{"-","-","-"},{"-","-","-"},{"-","-","-"}};
    int x,y;
    string winner;

    cout<<"You: X Computer: O - X and Y coordinates start from 0"<<endl;

    while(!finish){
        cout<<"X Y for move:";
        cin>>x>>y;
        if(!play(board,x,y,PLAYER_X)){
            cout<<"Wrong move. Please try again"<<endl;
            continue;
        }

        cout<<"Computer playing..."<<endl;
        play_computer(board);
        draw_board(board);
        winner = check_winner(board);
        if(winner != N){
            finish=true;
            cout<<"Game over. Winner is: "<<winner<<endl;
        }
        
    }
    return 0;
}
