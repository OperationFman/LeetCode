var moveZeroes = nums => {
    let zeroes = 0;
    let indexes = [];
    nums.map((v, i) => {
        if (v === 0) {
            indexes.push(i);
            zeroes = zeroes++;
        } 
    })
    let reversed = indexes.reverse();
    reversed.forEach((item) => {
        nums.splice(item, 1);
        nums.push(0);
    });
    return nums;
};