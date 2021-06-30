var containsDuplicate = nums => {
    const tracker = new Set()
    let result = false;
    nums.map((num) => {
        if (tracker.has(num)) {
            result = true
        } else {
            tracker.add(num)
        }
    })
    return result;
};