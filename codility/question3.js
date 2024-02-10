function solution(S) {
    let n = S.length;
    let prev_moved_player = -1; //track the last player who moved
    let successful_moves = 0;

    for (let i = 0; i < n; i++) {
        if (S[i] === '>') {
            // Check if the player is at the end of the line
            if (i === n - 1) {
                successful_moves += 1;
                prev_moved_player = i;
            }
        } else if (S[i] === '<') {
            // Check if the previous player has moved from his position
            if (prev_moved_player === i - 1) {
                successful_moves += 1;
                prev_moved_player = i;
            }
        } else if (S[i] === '^') {
            // Up move is always successful
            successful_moves += 1;
            prev_moved_player = i;
        } else {
            // Down move is always successful
            successful_moves += 1;
            prev_moved_player = i;
        }
    }

    return successful_moves;
}